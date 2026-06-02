Modelos de procesamiento de documentos
======================================

Introducción
------------

Un documento no es solamente texto. Si observamos una factura, por ejemplo, encontramos palabras, números, encabezados, tablas, firmas, sellos y regiones visuales que organizan la información. A grandes rasgos, el problema de procesamiento de documentos consiste en convertir esa representación visual en información útil para una tarea: extraer campos, clasificar documentos o validar datos.

El pipeline clásico solía dividirse en pasos bien separados:

#. Convertir la página a imagen.
#. Aplicar OCR para detectar palabras y coordenadas.
#. Reconstruir líneas, tablas o bloques.
#. Aplicar reglas o modelos de NLP sobre el texto resultante.

Este enfoque sigue siendo útil, pero tiene una limitación importante: los errores de un paso se propagan al siguiente. Además, si tratamos el resultado del OCR como texto plano, perdemos parte de la estructura visual que hacía comprensible al documento.

OCR y layout
------------

OCR (por las siglas en inglés de *Optical Character Recognition*) es la tarea de reconocer caracteres o palabras dentro de una imagen. En documentos modernos, el OCR suele producir dos tipos de salida:

:Texto: las palabras o líneas detectadas.
:Coordenadas: la ubicación de cada palabra o bloque dentro de la página.

Recordemos que, para un modelo de NLP tradicional, dos secuencias con las mismas palabras suelen verse muy similares aunque provengan de layouts distintos. En cambio, para un documento, la ubicación importa. La palabra "total" cerca del final de una factura no cumple necesariamente el mismo rol que la palabra "total" dentro de una tabla intermedia.

Podemos representar una palabra detectada como:

.. math::

   (w_i, b_i) = (w_i, x_0, y_0, x_1, y_1)

donde :math:`w_i` es el token o palabra y :math:`b_i` es su caja delimitadora (*bounding box*) dentro de la página. La idea de los modelos sensibles al layout es utilizar tanto :math:`w_i` como :math:`b_i`, y en algunos casos también los pixeles originales.

Modelos modernos
----------------

Existen varias familias de modelos para procesamiento de documentos. La diferencia principal está en qué modalidades utilizan y cuánto dependen de un OCR externo.

:Modelos basados en OCR + NLP:
   Primero extraen texto con OCR y luego aplican modelos de NLP. Son simples y efectivos cuando el layout no es crítico, por ejemplo para clasificar documentos por tema.

:Modelos layout-aware:
   Incorporan texto y coordenadas. LayoutLM, LayoutLMv2 y LayoutLMv3 son ejemplos de esta familia. Estos modelos extienden la idea de los transformers para que los tokens no solo tengan embeddings de texto, sino también embeddings espaciales.

:Modelos OCR-free:
   Procesan directamente la imagen del documento y generan texto estructurado. Donut (*Document Understanding Transformer*) es un ejemplo importante: evita depender de un motor OCR externo y formula muchas tareas como generación de secuencias.

:Modelos multimodales generales:
   Modelos vision-language más recientes pueden analizar imágenes de documentos o razonar sobre regiones visuales. Suelen ser potentes, pero también más costosos y dependientes de instrucciones o prompts bien diseñados.

LayoutLM y la idea de embeddings espaciales
-------------------------------------------

La idea central de LayoutLM es simple de explicar si recordamos los embeddings posicionales de los transformers. En NLP agregamos información de posición para indicar el orden de los tokens. En documentos, además del orden, necesitamos indicar dónde aparece cada token en la página.

Por eso, un modelo layout-aware puede combinar:

:Token embeddings: representación semántica de la palabra.
:Position embeddings: posición dentro de la secuencia.
:Spatial embeddings: coordenadas 2D de la caja delimitadora.
:Visual embeddings: características extraídas de la imagen, dependiendo de la versión del modelo.

Esto permite que el modelo aprenda patrones como "un valor ubicado a la derecha de una etiqueta suele ser su contenido" o "las palabras alineadas verticalmente pueden pertenecer a una columna".

Advertencias prácticas
----------------------

.. warning::
   En aplicaciones reales, los documentos suelen tener ruido: páginas rotadas, baja resolución, sellos, firmas, tablas incompletas o formatos que cambian entre proveedores. Un notebook pequeño sirve para entender el concepto, pero un sistema productivo requiere evaluación con documentos representativos del dominio.

Algunas preguntas útiles antes de elegir un enfoque son:

- ¿El documento es nativamente digital o escaneado?
- ¿Necesitamos extraer campos exactos o sintetizar información general?
- ¿El layout es estable o cambia frecuentemente?
- ¿Podemos usar OCR externo o necesitamos un modelo OCR-free?
- ¿Tenemos ejemplos anotados para hacer fine-tuning?

Ejemplos
--------

.. toctree::
   :maxdepth: 1
   :caption: Ejemplos
   :glob:

   OCR avanzado para documentos empresariales <advanced-ocr-enterprise.ipynb>

Referencias
-----------

- `LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking <https://arxiv.org/abs/2204.08387>`_.
- `Donut: Document Understanding Transformer without OCR <https://arxiv.org/abs/2111.15664>`_.
