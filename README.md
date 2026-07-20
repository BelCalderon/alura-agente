# 🤖 Agente de Atención al Cliente Inteligente - BimBam Buy

¡Bienvenido/a al repositorio oficial del Agente de IA para BimBam Buy! Este proyecto ha sido desarrollado como parte del desafío **Alura Agente**, con el objetivo de automatizar, optimizar y elevar la calidad de la atención al cliente en operaciones de comercio electrónico para LATAM utilizando Inteligencia Artificial de última generación.

La solución consiste en un asistente virtual interactivo dotado de una interfaz web intuitiva. El agente procesa de forma precisa las consultas de los usuarios sobre envíos, garantías, devoluciones y políticas comerciales, garantizando respuestas alineadas con los manuales corporativos y eliminando el riesgo de alucinaciones en el modelo de lenguaje.

---

## 📐 Arquitectura de la Solución

La aplicación implementa una arquitectura basada en **Inyección de Contexto en Tiempo Real (RAG Simplificado)**. Este enfoque asegura que el modelo de lenguaje base no dependa de su conocimiento general, sino de la información oficial provista:

1. **Capa de Datos (Base de Conocimiento)**: Los manuales y políticas operativos de la tienda se almacenan en archivos estructurados en formato Markdown (`.md`) dentro del directorio `base_conocimiento/`.
2. **Carga y Centralización de Configuraciones (`config.py`)**: Este módulo se encarga de gestionar de forma segura el entorno del sistema, cargando las variables de entorno (`.env`) y estructurando las rutas de los archivos de conocimiento para su consumo.
3. **Orquestación del Agente e Interfaz (`agent.py`)**: Al inicializar la aplicación, el script lee dinámicamente los documentos de la base de conocimiento y los inyecta de manera estructurada en el *System Prompt* del modelo de IA, delimitando estrictamente el marco de las respuestas permitidas.
4. **Inferencia de Baja Latencia (Groq Cloud)**: Cuando un usuario envía un mensaje a través de la interfaz web desarrollada en **Streamlit**, la consulta se procesa mediante la API de Groq utilizando un modelo fundacional de alta velocidad, garantizando tiempos de respuesta mínimos.

---

## 🛠️ Tecnologías y Herramientas Utilizadas

* **Python 3.14**: Entorno de programación principal utilizado para la lógica del agente y la manipulación de datos.
* **Streamlit**: Framework ágil utilizado para el diseño y despliegue de la interfaz gráfica de usuario (UI).
* **Groq Cloud API**: Infraestructura de inferencia de alto rendimiento para el procesamiento del lenguaje natural.
* **Python-dotenv**: Librería para la gestión segura de credenciales y variables de entorno.
* **Markdown**: Estándar utilizado para la redacción limpia y jerárquica de los manuales de soporte.

---

## 📂 Estructura del Repositorio

La disposición de los archivos en el proyecto sigue estándares de modularidad y orden limpio:

```text
challenge-bimbambuy/
├── base_conocimiento/         # Documentos oficiales que alimentan el contexto del agente
│   ├── Guia_Envios.md
│   ├── Manual_Garantia.md
│   ├── Politica_Devoluciones.md
│   ├── Preguntas_Frecuentes.md
│   └── Programa_Afiliados.md
├── venv/                      # Entorno virtual de Python (omitido en el control de versiones)
├── .env                       # Variables de entorno secretas (Clave de API de Groq)
├── .gitignore                 # Archivo de configuración para omitir archivos locales en Git
├── agent.py                   # Lógica principal del agente e interfaz de Streamlit
├── config.py                  # Módulo de configuración y carga de variables del sistema
├── README.md                  # Documentación técnica del proyecto
└── requirements.txt           # Dependencias y librerías del proyecto
```
---

## 🚀 Instrucciones para Ejecutar el Proyecto (Localmente)

Si deseas replicar este entorno de desarrollo localmente, sigue estos pasos estructurados:

1.  ****Clonar el repositorio:****
    Bash
    
    git clone \[https://github.com/BelCalderon/alura-agente.git\](https://github.com/BelCalderon/alura-agente.git)  
    cd challenge-bimbambuy  
    
2.  ****Configurar y activar el entorno virtual:**** 
    PowerShell
    
    python -m venv venv  
    .\\venv\\Scripts\\activate  
    
3.  *****Instalar dependencias necesarias:****  
    Bash
    
    pip install --upgrade pillow  
    pip install -r requirements.txt  
    
4.  ****Variables de entorno:**** Crea un archivo `.env` en la raíz del proyecto y añade tu API Key:  
    Plaintext
    
    GROQ\_API\_KEY=tu\_gsk\_key\_aqui  
    
5.  ****Iniciar la aplicación:****  
    PowerShell
    
    streamlit run agent.py  

--- 

## 💬 Ejemplos de Preguntas y Respuestas del Agente

Aquí se muestran escenarios reales de interacción con el asistente inteligente basados en los manuales operativos:

-   ****Pregunta:**** __¿Cuáles son las comisiones para afiliados?__
-   ****Respuesta del Agente:**** "¡Hola! De acuerdo con nuestro Programa de Afiliados, los socios comerciales reciben una estructura de comisiones competitiva basada en la atribución directa de ventas validadas a través de sus enlaces de referencia. Los detalles específicos de los porcentajes varían según la categoría del producto promocionado."
-   ****Pregunta:**** __¿Cuántos días tengo para devoluciones?__
-   ****Respuesta del Agente:**** "Revisando nuestra Política de Devoluciones oficial, cuentas con un plazo estricto de hasta 48 horas posteriores a la recepción de tu paquete para reportar cualquier incidencia física o faltante. Adicionalmente, se contempla el derecho de retracto bajo los lineamientos legales estándar de la región."
---

## ☁️ Evidencia del Despliegue en la Nube

La aplicación ha sido desplegada con éxito en producción y se encuentra totalmente operativa para acceso público:

-   🔗 ****Enlace de la aplicación en producción:****
[https://alura-agente-vs3dlek7qffqrjuxz4hqmf.streamlit.app/](https://alura-agente-vs3dlek7qffqrjuxz4hqmf.streamlit.app/)