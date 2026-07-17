# Agente de Atención al Cliente Inteligente - BimBam Buy

¡Bienvenido/a al repositorio oficial del Agente de IA para BimBam Buy! Este proyecto fue desarrollado como parte del desafío **Alura Agente**, con el objetivo de automatizar y optimizar la atención al cliente para operaciones en LATAM utilizando Inteligencia Artificial.

El chatbot está diseñado para interactuar con los usuarios de forma clara, amable y dinámica, respondiendo con total precisión con base en las políticas oficiales de la tienda y evitando cualquier tipo de "alucinación" o información falsa.

---

## 📂 Estructura del Repositorio

Para mantener el proyecto limpio, modular y organizado, la información se distribuye de la siguiente manera:

* **`base_conocimiento/`**: Carpeta que almacena los manuales oficiales de la tienda en formato Markdown (.md) para alimentar el contexto del agente.
  * `Manual_Garantia.md`: Políticas de cobertura, plazos y exclusiones de soporte técnico.
  * `Politica_Devoluciones.md`: Reglas de derecho de retracto, reportes de 48 horas y reembolsos.
  * `Guia_Envios.md`: Tiempos estimados de entrega, costos y gestión de incidencias logísticas.
  * `Programa_Afiliados.md`: Lineamientos, comisiones y atribución de ventas para socios comerciales.
  * `Preguntas_Frecuentes.md`: Base de preguntas y respuestas internas para criterios de soporte directos.
* **`agent.py`**: Archivo principal que contiene el código en Python que da vida y ejecuta el chatbot de IA.
* **`requirements.txt`**: Archivo de configuración con la lista de librerías y dependencias necesarias para ejecutar el entorno de desarrollo.

---

## 🛠️ Tecnologías y Herramientas Utilizadas

* **Python**: Lenguaje de programación principal para la lógica del agente.
* **Markdown**: Formato utilizado para la estructuración limpia de la base de conocimiento.
* **Git & GitHub**: Herramientas para el control de versiones y alojamiento del código en la nube.

---

## 🚀 Próximos Pasos del Desarrollo

1. **Configuración del Entorno Virtual**: Aislar el espacio de trabajo en Python.
2. **Estructura del Código (`agent.py`)**: Conectar la base de conocimiento con el modelo de IA.
3. **Pruebas de Simulación**: Evaluar las respuestas del agente frente a casos reales de clientes.