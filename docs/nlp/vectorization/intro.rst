Vectorización de texto
======================

Un modelos de aprendizaje automático es, a groso modo, una función parametrizada f(x) que toma como entrada un vector x, n-dimensional, y produce un vector de salida m-dimensional. Tal función puede ser simple (para un modelo lineal por ejemplo) o más compleja (como una red neuronal).

Cuando trabajamos con lenguaje natural, la mayoría de nuestros datos de entrada representarán características discretas y categóricas, ya sean palabras, letras o incluso utterancias (partes del discurso). La pregunta que nos haremos entonces es ¿Cómo codificamos esos datos categóricos de una manera que sea práctica para ser utilizada por un modelo de aprendizaje automático?

.. toctree::
   :maxdepth: 1
   :caption: En esta sección veremos

   Vectorizado con métodos clásicos <vectorization.ipynb>
   Vectorizado con vectores densos <embeddings>
   Consideraciones <considerations>