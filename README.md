# Frontend para Chatbot y Motor de Búsqueda Semántica con Streamlit

Este proyecto proporciona una interfaz web desarrollada con **Streamlit** para interactuar con un chatbot basado en búsqueda semántica y generación aumentada por recuperación (**RAG**).

A través de esta aplicación, los usuarios pueden realizar consultas en lenguaje natural y obtener respuestas generadas a partir de documentación previamente indexada. Además, cada respuesta incluye las **fuentes utilizadas para generar la información**, permitiendo verificar el origen del contenido mostrado por el chatbot.

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
git clone git@github.com:codigoarqui/front_buscador_semantico.git
cd front_buscador_semantico
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

## Ejecutar la Aplicación

El proyecto incluye distintas interfaces de prueba para diferentes funcionalidades:

```bash
streamlit run frontend.py --server.port 8501
streamlit run frontend_rag.py --server.port 8502
streamlit run frontend_rag_conversacional.py --server.port 8503
streamlit run frontend_vision.py --server.port 8504
```

Una vez iniciada la aplicación, Streamlit abrirá automáticamente el navegador. Si esto no ocurre, podés acceder manualmente desde:

```text
http://localhost:8501
```

---

## Funcionalidades

- Interfaz web simple e interactiva desarrollada con Streamlit.
- Integración con un motor de búsqueda semántica.
- Chatbot conversacional basado en RAG.
- Visualización de las fuentes utilizadas para generar cada respuesta.
- Soporte para distintos modos de interacción y pruebas experimentales.

---

## Notas

- Este proyecto actúa únicamente como frontend.
- Toda la lógica de procesamiento, embeddings, recuperación de documentos y generación de respuestas se encuentra en el backend:
  - https://github.com/KevinZenklusen/ChatbotNormClinic-platform
- Antes de ejecutar este frontend, asegurate de que el backend se encuentre correctamente configurado y en ejecución.