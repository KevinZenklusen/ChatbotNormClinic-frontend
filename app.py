import requests
import streamlit as st
import uuid
from urllib.parse import urlparse
import os

from dotenv import load_dotenv
load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
BUSQUEDA_URL = f"{API_BASE_URL}/agent/"

# Proyecto de Supabase
SUPABASE_PROJECT_URL = os.getenv("SUPABASE_PROJECT_URL")

st.set_page_config(
    page_title="Asistente de normativa de ingeniería clínica",
    page_icon=":hospital:"
)

st.markdown("""
    <style>
    [data-testid="stStatusWidget"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Asistente de normativa de ingeniería clínica de FIUNER")


if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []


def convert_blob_name(path):
    """
    Convierte file://.../files/... a URL servida por FastAPI
    """
    if not path:
        return None

    if path.startswith("file://"):
        idx = path.lower().find("files")
        if idx != -1:
            relative = path[idx:].replace("\\", "/")
            return f"{API_BASE_URL}/{relative}"

    return path


def normalize_url(url):
    """
    Convierte URLs especiales a URLs navegables
    """
    if not url:
        return None

    parsed = urlparse(url)

    # ---- Supabase ----
    if parsed.scheme == "supabase":
        bucket = parsed.netloc
        path = parsed.path.lstrip("/")

        return f"{SUPABASE_PROJECT_URL}/storage/v1/object/public/{bucket}/{path}"

    # ---- HTTP normales ----
    if parsed.scheme in ("http", "https"):
        return url

    return url


def remote_pdf_available(url):
    """
    Verifica si el PDF remoto existe
    """
    if not url:
        return False

    try:
        r = requests.head(url, timeout=3)
        return r.status_code < 400
    except requests.RequestException:
        return False


def extract_text(respuesta):
    """
    Normaliza la respuesta del backend (Groq o Gemini)
    """
    if isinstance(respuesta, str):
        return respuesta

    if isinstance(respuesta, list):
        texts = []
        for item in respuesta:
            if isinstance(item, dict):
                if item.get("type") == "text":
                    texts.append(item.get("text", ""))
                elif item.get("type") == "code":
                    code = item.get("text", "")
                    lang = item.get("language", "")
                    texts.append(f"```{lang}\n{code}\n```")
        return "\n\n".join(texts)

    return str(respuesta)


# Render historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Input usuario
if prompt := st.chat_input("Hola ¿En qué puedo ayudarte?"):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        payload = {
            "session_id": st.session_state.session_id,
            "consulta": prompt,
            "top_k": 20
        }

        try:

            with st.spinner("Buscando en normativa..."):

                response = requests.post(BUSQUEDA_URL, json=payload)
                response.raise_for_status()
                data = response.json()

                raw_response = data.get("respuesta", "No se recibió respuesta.")
                full_response = extract_text(raw_response)

                sources = data.get("sources", [])

                message_placeholder.markdown(full_response)

                if sources:

                    st.markdown("---")
                    st.markdown("**Fuentes**")

                    for src in sources:

                        source_url = normalize_url(src.get("source_url"))
                        blob_name = normalize_url(src.get("blob_name"))
                        page_number = src.get("page_number", 1)

                        blob_url = convert_blob_name(blob_name)

                        # prioridad: source_url -> blob_url
                        pdf_url = source_url or blob_url

                        if pdf_url:

                            pdf_link = f"{pdf_url}#page={page_number}"

                            st.markdown(
                                f'- <a href="{pdf_link}" target="_blank">{pdf_link} (página {page_number})</a>',
                                unsafe_allow_html=True
                            )

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response
                })

        except requests.exceptions.RequestException as e:
            st.error(f"Error al contactar la API: {e}")