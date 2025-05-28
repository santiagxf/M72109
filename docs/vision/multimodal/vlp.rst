Vision-Language Pre-training (VLP)
==================================

Modelos como CLIP (que veremos en esta sección) y sus similares representaron un cambio de paradigma en la forma de trabajar con modelos multimodales que procesan texto e imágenes. Estos modelos poseen capacidades únicas que se pueden aplicar a varias tareas de aprendizaje automático al combinar aspectos del lenguaje con entendimiento de imágenes. Esta categoría de modelos suele denominarse *Vision-Language Pre-training (VLP)*.

Contrastive Language-Image Pre-training (CLIP)
----------------------------------------------

`CLIP (Contrastive Language-Image Pre-Training) <https://openai.com/blog/clip/>`_ es un modelo creado por OpenAI en Enero de 2021. Se trata de un modelo que combina el conocimiento del idioma con la semántica de las imágenes. El mismo fué entrenado sobre **400M de imágenes y sus respectivas descripciones**. Si bien este modelo no alcanzó una performance mejor que las de otros modelos de la industría que ya estan establecidos, CLIP es muy útil en aquellos escenarios donde los datos de entrenamiento son escasos. Esto se lo debe a sus capacidades de generalización y de **Zero-shot Learning**. En esta configuración, si por ejemplo quisieramos que CLIP resuelva un problema de clasificación puntual, uno solo debe "describir las etiquetas" sobre las que quiere que el modelo opere. CLIP es capaz de resolver la tarea a pesar de nunca haber sido entrenado para esa etiqueta en particular.

Arquitectura
~~~~~~~~~~~~

CLIP es capaz de generalizar más alla de las imagenes que posee en su conjunto de datos de entrenamiento gracias al contexto que le aporta el texto de las mismas. Esto hace que CLIP sea capaz de extraer representaciones de imagenes utilizando la descripción textual de la misma a pesar de nunca haber visto una imágen tal cual se describe. Esto lo vuelve extremadamente potente para la búsqueda semántica de imágenes.

.. figure:: _images/state_clip_constrastive.png
  :alt: Arquitectura general del modelo CLIP y su uso de la técninca Contrastive Learning.

  *Arquitectura general del modelo CLIP y su uso de la técninca Contrastive Learning* [4]_

La técnica de entrenamiento de CLIP esta basada en **Constrastive Learning**. Para más información sobre esta técnica y como se implementa puede ver `Contrastive Learning: Effective Anomaly Detection with Auto-Encoders <https://santiagof.medium.com/contrastive-learning-effective-anomaly-detection-with-auto-encoders-98c6e1a78ada>`_

GroupViT
--------

`GroupViT <https://arxiv.org/abs/2202.11094>`_ es un modelo que inova en el ambito de la segmentación de imagenes al aplicar las ideas y aspectos de lenguaje que introdujo CLIP con el entendimiento semantico de una imagen.

BLIP
----

`BLIP (Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation) <https://arxiv.org/abs/2201.12086>`_ es un método de preentrenamiento que busca unificar la comprensión visual y lingüística mediante el aprovechamiento de un conjunto de datos a gran escala de pares imagen-texto. El proceso de preentrenamiento se inicia mediante un modelo de lenguaje para generar texto para imágenes (sin su texto correspondiente), y luego utiliza este texto generado para ajustar el modelo con el conjunto de datos original. Este enfoque permite que el modelo aprenda tanto de datos etiquetados como sin etiquetar, lo que resulta en un mejor rendimiento en diversas tareas de visión y lenguaje, como la creación de subtítulos de imágenes.


.. toctree::
   :maxdepth: 2
   :caption: Ejemplos
   :glob:

   CLIP <clip.ipynb>
