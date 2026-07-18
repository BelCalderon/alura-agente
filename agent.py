import os
import sys
import streamlit as st
from config import obtener_cliente_groq

def cargar_base_conocimiento(directorio_fuente="base_conocimiento"):
    """Carga y consolida los documentos Markdown de la base de conocimiento."""
    contexto_consolidado = ""
    if not os.path.exists(directorio_fuente):
        st.error(f"❌ Error crítico: El directorio '{directorio_fuente}' no existe.")
        sys.exit(1)
        
    for archivo_nombre in os.listdir(directorio_fuente):
        if archivo_nombre.endswith(".md"):
            ruta_completa = os.path.join(directorio_fuente, archivo_nombre)
            try:
                with open(ruta_completa, "r", encoding="utf-8") as archivo:
                    contexto_consolidado += f"\n\n--- INICIO DOCUMENTO: {archivo_nombre} ---\n"
                    contexto_consolidado += archivo.read()
                    contexto_consolidado += f"\n--- FIN DOCUMENTO: {archivo_nombre} ---\n"
            except Exception as e:
                st.warning(f"⚠️ No se pudo leer {archivo_nombre}: {e}")
    return contexto_consolidado

def inicializar_instrucciones_sistema():
    """Genera las instrucciones del sistema con las reglas anti-alucinación."""
    base_conocimiento = cargar_base_conocimiento()
    return (
        "Eres el agente inteligente oficial de atención al cliente para la tienda 'BimBam Buy'.\n"
        "Tu única fuente de verdad es la 'Base de Conocimiento' provista a continuación.\n\n"
        "REGLAS ESTRICTAS DE COMPORTAMIENTO:\n"
        "1. Responde de manera sumamente educada, empática, clara y profesional.\n"
        "2. Responde única y exclusivamente utilizando la información contenida en la Base de Conocimiento.\n"
        "3. Si el usuario te pregunta algo que NO está detallado o implícito en los documentos proporcionados, "
        "deben responder exactamente con la siguiente estructura, sin inventar ni agregar suposiciones:\n"
        "   'Lo siento, actualmente no manejo esa información en mi base de datos. Por favor, contacta a un asesor humano para asistirte.'\n"
        "4. Está estrictamente prohibido alucinar, simular políticas, inventar precios o condiciones.\n"
        "5. Usa un formato limpio, viñetas y saltos de línea cuando sea necesario.\n\n"
        f"=== BASE DE CONOCIMIENTO ===\n{base_conocimiento}\n============================="
    )

# Configuración de la interfaz de la página en Streamlit
st.set_page_config(page_title="Soporte Inteligente - BimBam Buy", page_icon="🤖", layout="centered")
# Mensaje de bienvenida y contexto para el usuario
st.info("""
👋 **¡Bienvenido al asistente inteligente de BimBam Buy!**
Aquí podrás gestionar tus dudas y consultas sobre nuestras operaciones en tiempo real. 
Puedes preguntarme con total libertad acerca de:
* 🚚 **Guía de Envíos:** Tiempos de entrega para ciudades principales y zonas remotas.
* 🛡️ **Políticas de Garantía:** Coberturas, plazos de soporte técnico y exclusiones.
* 🔄 **Devoluciones:** Derecho de retracto, reportes de incidencias y reembolsos.
* 🤝 **Programa de Afiliados:** Comisiones y lineamientos para socios comerciales.
""")

# Inicializar estados de memoria avanzada si no existen
if "mensajes_historial" not in st.session_state:
    st.session_state.mensajes_historial = []
if "instrucciones" not in st.session_state:
    st.session_state.instrucciones = inicializar_instrucciones_sistema()

st.title("🤖 BimBam Buy")
st.subheader("Módulo de Atención al Cliente Inteligente")
st.markdown("---")

# Renderizar el historial visual de la conversación de forma elegante
for mensaje in st.session_state.mensajes_historial:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

# Capturar la consulta del cliente
if consulta_usuario := st.chat_input("Escribe tu consulta aquí..."):
    with st.chat_message("user"):
        st.markdown(consulta_usuario)
    st.session_state.mensajes_historial.append({"role": "user", "content": consulta_usuario})

    # Preparar el contexto completo para la API de Groq (Memoria Avanzada)
    mensajes_api = [{"role": "system", "content": st.session_state.instrucciones}]
    for msg in st.session_state.mensajes_historial:
        mensajes_api.append({"role": msg["role"], "content": msg["content"]})

    # Llamar al motor de inferencia
    with st.chat_message("assistant"):
        contenedor_respuesta = st.empty()
        try:
            cliente_ai = obtener_cliente_groq()
            ref_respuesta = cliente_ai.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=mensajes_api,
                temperature=0.0
            )
            respuesta_final = ref_respuesta.choices[0].message.content
            contenedor_respuesta.markdown(respuesta_final)
            st.session_state.mensajes_historial.append({"role": "assistant", "content": respuesta_final})
        except Exception as e:
            st.error(f"❌ Error de comunicación: {e}")