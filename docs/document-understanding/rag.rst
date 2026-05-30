Retrieval-Augmented Generation para documentos
==============================================

Introducción
------------

Los modelos de lenguaje grandes, LLM (por las siglas en inglés de *Large Language Models*), pueden responder preguntas y generar texto con gran fluidez. Sin embargo, tienen una limitación práctica: no siempre conocen el contenido privado, reciente o específico de una organización. Además, incluso cuando conocen un tema, pueden producir respuestas plausibles pero incorrectas.

Una estrategia muy utilizada para reducir este problema es Retrieval-Augmented Generation, generalmente abreviado como **RAG**. La idea es sencilla: antes de pedirle al modelo que responda, buscamos en una colección de documentos los fragmentos más relevantes y los agregamos al prompt como contexto.

La pregunta sería: ¿por qué no hacer fine-tuning del modelo con todos los documentos? En general, RAG resulta más simple, más barato y más fácil de actualizar. Si cambia un documento, actualizamos el índice de búsqueda; no necesariamente re-entrenamos el modelo.

Patrón general
--------------

Un sistema RAG para documentos suele tener dos fases.

Indexación
^^^^^^^^^^

#. Cargar documentos desde PDFs, páginas web, archivos de texto o sistemas internos.
#. Dividirlos en fragmentos (*chunks*) de tamaño razonable.
#. Convertir cada fragmento en un embedding.
#. Guardar los embeddings en un índice de búsqueda vectorial.

Consulta
^^^^^^^^

#. Recibir la pregunta del usuario.
#. Convertir la pregunta en un embedding.
#. Recuperar los fragmentos más similares.
#. Construir un prompt con la pregunta y los fragmentos recuperados.
#. Generar una respuesta condicionada al contexto.

Podemos pensar el componente de retrieval como una memoria externa. El LLM no necesita memorizar todos los documentos; necesita saber usar el contexto recuperado.

Embeddings y similitud
----------------------

Para recuperar documentos usamos embeddings, es decir, vectores densos que representan el significado de un texto. Si dos fragmentos hablan de temas parecidos, esperamos que sus vectores estén cerca.

Una medida común es la similitud coseno:

.. math::

   sim(q, d) = \frac{q \cdot d}{||q|| \, ||d||}

donde :math:`q` es el embedding de la pregunta y :math:`d` es el embedding de un fragmento de documento. Cuanto mayor es el valor, más similares son los textos.

En ejemplos pequeños podemos calcular esta similitud con ``scikit-learn`` o ``numpy``. En colecciones grandes, resulta común usar índices especializados como FAISS, Chroma, Milvus, Elasticsearch/OpenSearch o servicios administrados.

Chunking
--------

Dividir documentos parece un detalle menor, pero suele determinar la calidad del sistema. Si los chunks son demasiado grandes, el recuperador puede traer mucho ruido. Si son demasiado pequeños, puede faltar contexto para responder.

En general se busca un equilibrio:

:Chunks cortos: mejor precisión local, pero riesgo de perder contexto.
:Chunks largos: más contexto, pero mayor ruido y consumo de tokens.
:Solapamiento: repetir algunas palabras entre chunks ayuda a no cortar ideas importantes.

.. note::
   El tamaño adecuado depende del dominio, del modelo de embeddings, del LLM y del tipo de pregunta. No existe un valor universal.

RAG no es solamente búsqueda
----------------------------

Aunque el ejemplo mínimo puede implementarse como "buscar los textos más parecidos", un sistema RAG real tiene más componentes:

:Ingesta: limpieza, OCR, extracción de texto, metadatos y control de versiones.
:Retrieval: búsqueda vectorial, búsqueda lexical o combinaciones híbridas.
:Reranking: reordenamiento de los resultados recuperados con un modelo más preciso.
:Generación: construcción del prompt y respuesta del LLM.
:Evaluación: medición de relevancia, fidelidad al contexto y cobertura.

Una advertencia importante es que RAG no garantiza respuestas correctas por sí solo. Si el recuperador trae fragmentos irrelevantes, el generador probablemente responderá mal. Por eso suele decirse que la calidad de un sistema RAG está limitada por la calidad de su retrieval.

Ejemplos prácticos
------------------

Los notebooks de esta sección avanzan de forma incremental. Primero implementaremos el núcleo del patrón sin depender de servicios externos ni credenciales. Luego construiremos un ejemplo un poco más cercano a una arquitectura productiva: chunking con metadatos, índice documental y un SLM que responde usando los fragmentos recuperados.

.. toctree::
   :maxdepth: 1
   :caption: Ejemplos
   :glob:

   RAG mínimo con embeddings <rag-minimo.ipynb>
   RAG con índice documental y un SLM <rag-index-slm.ipynb>

Referencias
-----------

- `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks <https://arxiv.org/abs/2005.11401>`_.
- `Sentence Transformers en HuggingFace <https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2>`_.
- `LlamaIndex <https://docs.llamaindex.ai/>`_.
- `Tutorial de RAG en LangChain <https://python.langchain.com/docs/tutorials/rag/>`_.
