Embeddings de oraciones y documentos
=====================================

Introducción
------------

En secciones anteriores del curso hablamos de embeddings de palabras: vectores densos que ubican tokens como *perro*, *gato* o *contrato* en un espacio donde la cercanía tiene algún significado semántico. Esa idea resulta muy poderosa, pero cuando trabajamos con documentos aparece una pregunta natural: ¿qué vector representa una oración completa, un párrafo o una página?

Esta pregunta es central en procesamiento de documentos. Un sistema que debe buscar cláusulas dentro de contratos, agrupar tickets de soporte, detectar facturas similares o responder preguntas sobre PDFs no puede comparar palabra por palabra todo el tiempo. Necesita una representación compacta del contenido. A grandes rasgos, los **sentence embeddings** y **document embeddings** cumplen ese rol: convertir unidades de texto más largas que una palabra en vectores densos comparables.

De palabras a oraciones
-----------------------

Recordemos que un embedding de palabra asigna un vector a cada token:

.. math::

   w_i \rightarrow \mathbf{x}_i \in \mathbb{R}^d

donde :math:`w_i` es una palabra o token y :math:`\mathbf{x}_i` es su representación d-dimensional. En cambio, un embedding de oración intenta representar una secuencia completa:

.. math::

   (w_1, w_2, ..., w_n) \rightarrow \mathbf{s} \in \mathbb{R}^d

La diferencia parece pequeña, pero conceptualmente es importante. El vector :math:`\mathbf{s}` no debería representar solamente las palabras que aparecen, sino también la idea expresada por la oración. Por ejemplo:

.. code::

   "El cliente canceló la orden"
   "La orden fue anulada por el cliente"

Estas dos oraciones comparten pocas palabras en la misma posición, pero significan algo muy parecido. Un buen modelo de sentence embeddings debería ubicarlas cerca en el espacio vectorial.

¿Por qué no promediar palabras?
-------------------------------

Una primera solución sería calcular el promedio de los embeddings de las palabras de una oración:

.. math::

   \mathbf{s} = \frac{1}{n} \sum_{i=1}^{n} \mathbf{x}_i

Esta estrategia puede ser útil como línea base. De hecho, muchas representaciones simples de documentos funcionan razonablemente bien cuando el vocabulario es claro y el dominio es acotado. Sin embargo, tiene limitaciones:

:Orden:
   El promedio no distingue fácilmente entre "el proveedor pagó al cliente" y "el cliente pagó al proveedor".

:Contexto:
   Una palabra ambigua puede tener distintos significados según la oración. Recordemos el ejemplo clásico de "banco" como institución financiera o como asiento.

:Importancia relativa:
   No todas las palabras aportan la misma información. En documentos reales, encabezados, entidades, fechas y términos técnicos pueden ser mucho más relevantes que conectores o frases comunes.

Por eso, los modelos modernos suelen usar arquitecturas contextuales, como transformers, para generar representaciones que dependen de toda la secuencia.

Embeddings contextuales
-----------------------

Los transformers producen una representación para cada token considerando el contexto donde aparece. Si la secuencia tiene :math:`n` tokens, el modelo genera una matriz:

.. math::

   H \in \mathbb{R}^{n \times d}

donde cada fila representa un token contextualizado. La pregunta sería: ¿cómo obtenemos un único vector para la oración o el fragmento?

Existen varias estrategias comunes:

:Token especial:
   Algunos modelos utilizan la representación de un token especial, como ``[CLS]`` en BERT, como resumen de la secuencia.

:Pooling promedio:
   Se promedian las representaciones de todos los tokens, usualmente ignorando padding.

:Pooling máximo:
   Se toma el valor máximo por dimensión, capturando señales fuertes aunque aparezcan en pocos tokens.

:Modelos entrenados específicamente:
   Modelos como Sentence-BERT ajustan la arquitectura y el entrenamiento para que la distancia entre vectores refleje mejor la similitud semántica entre oraciones.

Note que no todo embedding producido por un transformer es automáticamente un buen sentence embedding. Un modelo puede ser excelente para completar texto o clasificar tokens, pero no necesariamente producir vectores bien calibrados para búsqueda semántica.

Entrenamiento por similitud
---------------------------

Para que dos oraciones con significado similar queden cerca, el modelo necesita una señal de entrenamiento apropiada. Una estrategia muy común es el aprendizaje contrastivo. La intuición es simple: acercar pares positivos y alejar pares negativos.

Podemos pensar en pares como:

:Par positivo:
   Dos textos que expresan la misma intención, responden la misma pregunta o son versiones parafraseadas.

:Par negativo:
   Dos textos que tratan temas distintos o que no deberían recuperarse juntos.

Durante el entrenamiento, el modelo aprende un espacio donde la similitud coseno entre pares relacionados sea alta y entre pares no relacionados sea baja:

.. math::

   sim(\mathbf{a}, \mathbf{b}) =
   \frac{\mathbf{a} \cdot \mathbf{b}}{||\mathbf{a}|| \, ||\mathbf{b}||}

Esta idea conecta directamente con sistemas de búsqueda semántica y RAG. Si la pregunta y el fragmento relevante terminan cerca en el espacio, podemos recuperar el fragmento usando un índice vectorial.

Embeddings de documentos
------------------------

Cuando pasamos de oraciones a documentos completos aparece otro desafío: los documentos suelen ser largos, heterogéneos y estructurados. Un contrato puede tener secciones, anexos y tablas; una factura puede combinar encabezados, líneas de detalle y totales; un informe puede extenderse por muchas páginas.

En la práctica, existen varias formas de representar documentos:

:Documento completo:
   Se genera un único embedding para todo el texto. Es simple, pero puede perder detalles importantes y suele estar limitado por la longitud máxima del modelo.

:Fragmentos o chunks:
   Se divide el documento en partes más pequeñas y se genera un embedding para cada chunk. Esta es la estrategia más común en RAG, porque permite recuperar solo las secciones relevantes.

:Representación jerárquica:
   Se generan embeddings de párrafos, secciones y documento completo. Resulta útil cuando necesitamos navegar desde una búsqueda general hacia evidencia específica.

:Embeddings con metadatos:
   El vector representa el contenido textual, mientras que filtros adicionales usan metadatos como fecha, tipo de documento, cliente, página o sección.

En general, para procesamiento de documentos conviene evitar pensar en "el embedding del PDF" como una sola entidad. Resulta más útil preguntarse: ¿qué unidad necesito recuperar o comparar para mi tarea?

Importancia en procesamiento de documentos
------------------------------------------

Los embeddings de oraciones y documentos son importantes porque permiten convertir tareas de comprensión textual en operaciones geométricas sobre vectores. Esto habilita varios patrones:

:Búsqueda semántica:
   Recuperar fragmentos aunque no compartan exactamente las mismas palabras con la consulta.

:RAG:
   Buscar chunks relevantes y usarlos como contexto para un LLM, como veremos en :doc:`rag`.

:Clustering:
   Agrupar documentos o secciones similares para exploración, deduplicación o análisis temático.

:Clasificación con pocos ejemplos:
   Comparar un documento contra descripciones de clases o ejemplos prototípicos.

:Detección de duplicados:
   Identificar textos casi equivalentes aunque tengan pequeñas variaciones de redacción.

En documentos empresariales, esto suele ser más robusto que depender solamente de palabras clave. Por ejemplo, una consulta como "documentos donde el proveedor no cumplió la entrega" podría recuperar cláusulas que hablan de "incumplimiento", "demora", "penalidad" o "fecha límite vencida", aunque no repitan literalmente la consulta.

Advertencias prácticas
----------------------

.. warning::
   La cercanía entre embeddings no equivale necesariamente a verdad factual. Dos fragmentos pueden ser semánticamente parecidos pero contener valores, fechas o entidades diferentes. Para tareas donde los detalles exactos importan, conviene combinar embeddings con filtros, extracción estructurada, reranking o validaciones adicionales.

Algunas decisiones prácticas suelen tener mucho impacto:

:Modelo de embeddings:
   Debe estar alineado con el idioma, dominio y tipo de texto. Un modelo general puede fallar con lenguaje legal, médico o financiero especializado.

:Tamaño de chunk:
   Chunks muy pequeños pueden perder contexto; chunks muy grandes pueden mezclar temas distintos.

:Normalización:
   Muchos sistemas normalizan los vectores antes de usar similitud coseno o producto punto.

:Evaluación:
   No basta con mirar ejemplos aislados. Conviene medir si los fragmentos relevantes aparecen entre los primeros resultados recuperados.

:Actualización:
   Si cambia el modelo de embeddings, usualmente hay que recalcular los vectores del índice.

Referencias
-----------

- `Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks <https://arxiv.org/abs/1908.10084>`_.
- `Sentence Transformers <https://www.sbert.net/>`_.
- `Embeddings en HuggingFace <https://huggingface.co/tasks/sentence-similarity>`_.
