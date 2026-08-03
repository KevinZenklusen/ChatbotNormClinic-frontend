# Frontend para Chatbot de normativa clínica hecho con Streamlit

Este proyecto proporciona una interfaz web desarrollada con **Streamlit** para interactuar con el chatbot de normativa clínica.

A través de esta aplicación, los usuarios pueden realizar consultas de normativa de ingeniería clínica en lenguaje natural y obtener respuestas generadas a partir de documentación previamente indexada. Además, cada respuesta incluye las **fuentes utilizadas para generar la información**, permitiendo verificar el origen del contenido mostrado por el chatbot.

Este frontend se conecta directamente con la API REST provista por el siguiente proyecto:

- https://github.com/KevinZenklusen/ChatbotNormClinic-platform

> ⚠️ Este frontend fue diseñado específicamente para funcionar junto con ese backend y no es compatible con otras APIs sin realizar modificaciones adicionales.

---

## Requisitos

Para ejecutar este proyecto necesitarás:

- **Python 3.8+**
- Tener clonado y configurado el proyecto backend:
  - https://github.com/KevinZenklusen/ChatbotNormClinic-platform

---

## Configuración del Proyecto

Sigue estos pasos para ejecutar el frontend en tu entorno local.

### 1. Clonar el Repositorio

```bash
git clone git@github.com:KevinZenklusen/ChatbotNormClinic-frontend.git
cd ChatbotNormClinic-frontend
```

### 2. Crear y Activar un Entorno Virtual

#### Windows

```bash
python3 -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

Con el entorno virtual activado, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

---

### 4. Configurar las variables de entorno

Las siguentes variables de entorno son requeridas para el correcto funcionamiento del código:

# En caso de querer utilizar Supabase bucket online (se puede setear path local en app.py)
- SUPABASE_PROJECT_URL: URL del proyecto de supabase

# ID de usuario
- USER_ID

# Acceso al backend
- API_BASE_URL = URL del backend


### 5. Ejecutar la Aplicación

El proyecto incluye distintas interfaces de prueba para diferentes funcionalidades:

```bash
streamlit run app.py --server.port 8501
```

Una vez iniciada la aplicación, Streamlit abrirá automáticamente el navegador. Si esto no ocurre, puede acceder manualmente desde:

```text
http://localhost:8501
```

---

### 6. Funcionalidades

- Interfaz web simple e interactiva desarrollada con Streamlit.
- Integración con un motor de búsqueda semántica y léxica.
- Chatbot conversacional basado en RAG.
- Visualización de las fuentes utilizadas para generar cada respuesta.
- Soporte para distintos modos de interacción y pruebas experimentales.

---

## Notas

- Este proyecto actúa únicamente como frontend.
- Toda la lógica de procesamiento, embeddings, recuperación de documentos y generación de respuestas se encuentra en el backend:
  - https://github.com/KevinZenklusen/ChatbotNormClinic-platform
- Antes de ejecutar este frontend, asegurese de que el backend se encuentre correctamente configurado y en ejecución.