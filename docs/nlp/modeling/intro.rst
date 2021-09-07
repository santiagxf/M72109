Métodos clásicos de procesamiento de texto
==========================================

En NLP, la mayoritariamente trabajaremos con problemas de clasificación, y en particular, con problemas de clasificación supervisada. Esto quiere decir que dado un conjunto de datos que representa un conjunto de `documentos` con sus respectivas `etiquetas` o `labels`, el objetivo es construir un clasificador de forma automática que identifique características dentro de cada uno de los documentos que permita identificar patrones dentro del texto relevantes para cada una de las etiquetas que tenemos disponibles.

Un procedimiento típico entonces para alcanzar esto sería construir el siguiente flujo de trabajo:

.. figure:: https://github.com/santiagxf/M72109/blob/master/NLP/Docs/atap_0406.png?raw=1
  :alt: Diseño de un pipeline de procesamiento de texto

  *Diseño de un pipeline de procesamiento de texto*

En la sección anterior revisamos diferentes técnicas de preprocesamiento para la :doc:`../preprocessing/Normalization`. La mayoria de los modelos con los que trabajamos requieren que las caracteríticas estén indicadas en forma de números y es por eso que revisamos técnicas de :doc:`../vectorization/Vectorization` que nos permiten obtener representaciones más prácticas a partir de texto preprocesado.

Sin embargo, lo que quizás caracteriza a los modelos de procesamiento de lenguaje natural clásicos la necesidad de realizar **ingenieria de predictores**. Al igual que en el modelado clásico de modelos de aprendizaje automático (Clasical Machine Learning), la ingeniería de predictores nos permite extraer características altamente informativas a partir del texto de entrada. Estas caraterísticas en general permiten a nuestros modelos poder generalizar de mejor manera y hacer sentido de la información con mayor facilidad.

Estas técnicas se diferencian de las técnicas de :doc:`../deepnlp/intro` donde nuestros modelos directamente son capaces de aprender representaciones que resultan utiles para la tarea que intentan representar.


.. toctree::
   :maxdepth: 1
   :caption: En esta sección veremos

   Reducción de dimensionalidad <topic-modeling.ipynb>
   Modelado clásico de lenguaje natural <classic-modeling.ipynb>