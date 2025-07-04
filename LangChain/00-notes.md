# Intro a LangChain: Construye sobre LLMs/GPT4

Para crear un proyecto con AI se utiliza una API que de acceso al LLM que se va a utilizar, Ej: GPT, Gemini, etc.

## LangChain

Es un framework que permite construir aplicaciones basadas en modelos de lenguaje.
-Con flujos complejos.
-Consultas a APIs.
-Procesamiento de archivos como .txt, word, excel, etc.

### Modelos LLM (Large Language Models)

Es la red neuronal previamente entrenada con Machine Learning, la cual va a procesar el texto que le enviamos para generar una respuesta. Ej: GPT, Gemini etc.

Existen modelos de:
-Texto
-Chat
-Emdeddings

### Prompts

Es el texto que se envia al modelo para que genere una predicción.

En LangChain tenemos 4 clases principales de Prompts para estandarizar y hacer mejores prompt en nuestro sistema.
-Prompt template: Formatear todos los prompts de una manera en especifico con variable tipo {name}.
-Chat prompt template: Estructurar prompts para modelos de Chat.
-Prompt Value: Es el valor final del prompt que recibira el modelo, es decir el resultado final de los templates.
-Example Selector: Guia al modelo para generar respuestas como las que esperamos. Se dan ejemplos de Prompts y ejemplos de como queremos que nos responda.
-Output Parser: Transforma el resultado del modelo a un tipo JSON o un formato en especifico.

### Indices

Estas son fuentes de datos como un Word, PDF, txt, etc. Estos indices permiten indexar estos volumenes de datos para pasarlos a nuestro modelo para que tengan acceso.

En LangChain tenemos 4 clases principales de Indices:
-Document Loader: Abrir, cargar y procesar distintos tipos de archivos para pasarlos al modelo.
-Text Splitter: Partir un archivo muy grande en varias partes para su procesamiento.
-Vector Stores: Libreria para procesar vectores y almacenarlos en un espacio de memoria; como los generados con Embeddings.
-Retriever: Clase que ayuda a traer informacion de un documento en especifico.

### Memoria

La memoria ayuda a mantener un historial de la conversación.

### Chains

Permite unir modelos entre si, esto es una cadena, pero tambien se pueden unir cadenas entre si.
Es decir un modelo recibe una entrada, genera una salida y esta salida puede ser la entrada a otro modelo.
Esto nos ayuda a automatizar procesos largos.

### Agentes

Son modelos o cadenas a las que les damos acceso a Herramientas para que la usen y generen una respuesta en funcion de esta herramienta.
