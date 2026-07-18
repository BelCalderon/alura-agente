import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Cargar variables de entorno locales (si existen)
load_dotenv()

def obtener_cliente_groq():
    """
    Inicializa y retorna el cliente oficial de Groq Cloud SDK.
    Busca la API Key de forma segura en las variables de entorno locales
    o en los secretos de Streamlit Cloud si se encuentra en producción.
    """
    # 1. Intenta leer del entorno local (.env)
    api_key = os.getenv("GROQ_API_KEY")
    
    # 2. Si no la encuentra localmente, intenta leerla de los secretos de Streamlit Cloud
    if not api_key:
        api_key = st.secrets.get("GROQ_API_KEY")
        
    # 3. Si no aparece en ningún lado, lanza la excepción
    if not api_key:
        raise ValueError(
            "⚠️ ERROR DE CONFIGURACIÓN: No se encontró la variable GROQ_API_KEY en el archivo .env "
            "ni en los secretos de la plataforma. Por favor, asegúrate de definir tu clave de acceso de Groq."
        )
    
    # Retorna el cliente de Groq listo para operar utilizando la llave obtenida
    return Groq(api_key=api_key)