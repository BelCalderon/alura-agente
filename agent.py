import os
import sys
from config import obtener_cliente_groq

def cargar_base_conocimiento(directorio_fuente="base_conocimiento"):
    """
    Escanea el directorio y consolida el contenido de los archivos Markdown.
    """
    contexto_consolidado = ""
    
    if not os.path.exists(directorio_fuente):
        print(f"❌ Error crítico: El directorio '{directorio_fuente}' no existe.")
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
                print(f"⚠️ Advertencia: No se pudo leer el archivo {archivo_nombre}. Error: {e}")
                
    return contexto_consolidado

def inicializar_agente():
    """Carga los documentos y estructura las directrices del sistema."""
    base_conocimiento = cargar_base_conocimiento()
    
    instrucciones_sistema = (
        "Eres el agente inteligente oficial de atención al cliente para la tienda 'BimBam Buy'.\n"
        "Tu única fuente de verdad es la 'Base de Conocimiento' provista a continuación.\n\n"
        "REGLAS ESTRICTAS DE COMPORTAMIENTO:\n"
        "1. Responde de manera sumamente educada, empática, clara y profesional.\n"
        "2. Responde única y exclusivamente utilizando la información contenida en la Base de Conocimiento.\n"
        "3. Si el usuario te pregunta algo que NO está detallado o implícito en los documentos proporcionados, "
        "debes responder exactamente con la siguiente estructura, sin inventar ni agregar suposiciones:\n"
        "   'Lo siento, actualmente no manejo esa información en mi base de datos. Por favor, contacta a un asesor humano para asistirte.'\n"
        "4. Está estrictamente prohibido alucinar o inventar datos corporativos externos.\n\n"
        f"=== BASE DE CONOCIMIENTO ===\n{base_conocimiento}\n============================="
    )
    return instrucciones_sistema

def ejecutar_chat_conversacional():
    """Gestiona el bucle de conversación e interactúa con la API de Groq."""
    try:
        cliente_ai = obtener_cliente_groq()
    except ValueError as e:
        print(e)
        return

    # Usamos llama-3.3-70b-versatile, el modelo de código abierto más potente y gratuito en Groq
    modelo_seleccionado = "llama-3.3-70b-versatile"
    instrucciones = inicializar_agente()

    # Historial de conversación estructurado para mantener el contexto del chat
    historial_mensajes = [
        {"role": "system", "content": instrucciones}
    ]

    print("\n======================================================================")
    print("🤖 AGENTE INTELIGENTE BIMBAM BUY - MÓDULO DE ATENCIÓN AL CLIENTE (GROQ)")
    print("El sistema se ha inicializado correctamente.")
    print("Escribe tu consulta en lenguaje natural. Escribe 'salir' para finalizar.")
    print("======================================================================\n")

    while True:
        try:
            usuario_entrada = input("👤 Cliente: ").strip()
            
            if not usuario_entrada:
                continue
                
            if usuario_entrada.lower() == "salir":
                print("\n🤖 Agente: Gracias por comunicarte con BimBam Buy. Que tengas un excelente día. Sesión finalizada.")
                break

            print("\n🤖 Agente analizando y procesando...")
            
            # Agregamos la entrada del cliente al historial
            historial_mensajes.append({"role": "user", "content": usuario_entrada})
            
            # Llamada al endpoint de inferencia de Groq
            ref_respuesta = cliente_ai.chat.completions.create(
                model=modelo_seleccionado,
                messages=historial_mensajes,
                temperature=0.0  # Máxima precisión determinista
            )
            
            bot_respuesta = ref_respuesta.choices[0].message.content
            
            print(f"\n🤖 Agente: {bot_respuesta}")
            print("-" * 70)
            
            # Persistimos la respuesta en el historial para mantener la memoria
            historial_mensajes.append({"role": "assistant", "content": bot_respuesta})

        except Exception as e:
            print(f"\n❌ Ocurrió un error inesperado durante la comunicación: {e}")
            break

if __name__ == "__main__":
    ejecutar_chat_conversacional()