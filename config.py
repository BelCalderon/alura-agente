import os
from dotenv import load_dotenv
from groq import Groq

# Cargar variables de entorno
load_dotenv()

def obtener_cliente_groq():
    """
    Inicializa y retorna el cliente oficial de Groq Cloud SDK.
    Utiliza la API Key almacenada de forma segura en las variables de entorno.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "⚠️ ERROR DE CONFIGURACIÓN: No se encontró la variable GROQ_API_KEY en el archivo .env.\n"
            "Por favor, asegúrate de definir tu clave de acceso de Groq."
        )
    
    # Retorna el cliente de Groq listo para operar
    return Groq(api_key=api_key)