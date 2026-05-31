Procesamiento de documentos
===========================

Introducción
------------

Hasta ahora hemos trabajado con texto, imágenes y audio como modalidades relativamente separadas. Sin embargo, muchos de los datos no estructurados que aparecen en la industria no llegan como una secuencia limpia de palabras ni como una imagen natural: llegan como **documentos**. Un contrato escaneado, una factura, una orden médica, una planilla enviada como PDF o un formulario fotografiado contienen texto, pero también contienen estructura visual.

La pregunta sería: ¿alcanza con aplicar OCR y luego usar un modelo de NLP tradicional? En algunos casos sí, pero en muchos otros no. En un documento, la posición de una palabra, su cercanía a una tabla, el título de la sección o el orden de lectura pueden ser tan importantes como el texto mismo. Por eso resulta útil pensar el procesamiento de documentos como un problema multimodal donde conviven texto, imagen y layout.

En este módulo vamos a introducir dos ideas centrales:

:Modelos de procesamiento de documentos: modelos capaces de extraer texto, reconocer entidades, responder preguntas o interpretar formularios teniendo en cuenta OCR, imagen y layout.
:Retrieval-Augmented Generation (RAG): un patrón de arquitectura que permite recuperar fragmentos relevantes de documentos y utilizarlos como contexto para responder preguntas o asistir a un LLM.

.. note::
   Podemos pensar este módulo como un puente entre NLP, visión por computadora y sistemas de búsqueda. El objetivo no es reemplazar lo visto anteriormente, sino combinarlo para resolver problemas donde la información está distribuida en documentos extensos o visualmente estructurados.

.. toctree::
   :maxdepth: 1
   :caption: En esta sección veremos

   Embeddings de oraciones y documentos <sentence-embeddings>
