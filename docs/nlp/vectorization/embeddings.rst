Vectorizado con vectores densos (embeddings)
============================================

Introducción
------------

Los métodos anteriores de vectorizado tenian la peculiaridad de que **cada característica o predictor tenía su propia dimensión** y por lo tanto representaban vectores poco densos. Esto quiere decir que tendremos tantas dimensiones como características, predictores o mejor dicho, palabras. La ventaja y desventaja que tiene esta representación es que cada característica es independiente de las restantes. El predictor que corresponde a la palabra *perro* es tan distinto al vector que corresponde a *gato* como lo es al que corresponde con *heladera*.

Una alternativa a esta es **dejar de representar a nuestros predictores en su propia dimensión para pasar a representarlos como vectores densos**. Esto significa que cada predictor está códificado y embebido en un vector de dimensión d-dimensional (de aquí porque reciben el nombre de embeddings). La dimensión *d* es en general mucho más pequeña que el número de predictores - en el orden de 100-300.

.. figure:: ../_images/dense_sparse_vectors.png
  :alt: Diferencia entre vectores densos y poco densos

  *Diferencia entre vectores densos y poco densos*

Como consecuencia, las representaciones tienen una dimensionalidad menor pero más aún, un poder de generalización mas grande ya que si creemos que dos palabras serven el mismo proposito o tienen un significado similar, debereríamos de asignarles el mismo vector y permitirle al modelo compartir significancia estadística a ambas palabras por igual.

.. figure:: ../_images/words_dense_space.png
  :alt: Ejemplo de vectores densos y sus posiciones en el espacio - manifold

  *Ejemplo de vectores densos y sus posiciones en el espacio - manifold*

Aquí, sin embargo, hay una suposición importante y es que las representaciones de las palabras **son buenas**. Tales representaciones requeriran una cantidad de datos importante para ser útiles, y es por eso que en general utilizaremos *embeddings* preentrenados para nuestros modelos.

.. note:: Los vectores densos también serán útiles cuando utilicemos modelos basados en redes neuronales, los cuales no suelen funcionar correctamente con vectores altamente dimensionales y poco densos.

Representaciones distribuidas
-----------------------------

Un enfoque distinto al de los métodos de vectorizado basados en cantidad de palabras es utilizar el concepto de respresentaciones distribuidas. Cuando trabajamos con respresentaciones distribuidas, cada palabra está asociada con un vector multidimensional donde el significado de la misma no solo está codificado en las diferentes dimensiones de este vector, sino que también en las dimensiones de otras palabras (otros vectores). Esto quiere decir que, por ejemplo el vector "perro" cobra significado no solo por su representación, sino que también por su representación relativa a la palabra "gato", "animal", etc. Note también que aquí las diferentes dimensiones de las representaciones carecen de un significado específico sino que es el espacio resultante al que le podemos atribuir significado.

Similaridad
^^^^^^^^^^^

Una vez que tenemos representaciones de vectores, podemos computar la similaridad entre diferentes palabras computando la similaridad entre sus respectivos vectores. Una de las métricas más comunes para medir la similaridad es la *similaridad del coseno* o *cosine similarity* la cual mide el coseno del angulo entre dos vectores dados:

.. math::

  sim(u,v) = \frac { u \cdot v } {\lVert u \rVert _ 2 \lVert v \rVert _ 2}


Otra métrica comunmente utilizada e la *similaridad de Jaacard generalizada*.

.. toctree::
   :maxdepth: 1
   :caption: En esta sección veremos
   :hidden:

   Representaciones de Word2vec <Word2Vec.ipynb>