De texto a vectores: Consideraciones
====================================

.. _vectorizer-bos-eos:

Comienzo y fin de una oración
-----------------------------

Al procesar una palabra, muchas veces necesitamos obtener información sobre las palabras que estaban antes o después. Sin embargo, ¿que sucede si estamos en el comienzo o en el final de la oración? ¿Que debería hacerse en esos casos? Si estubieramos utilizando un modelo basado en `bag-of-features`, esto no representaría un problema ya que simplemente podríamos dejar la característica o feature como 0, fuera de la suma. Sin embargo, probablemente el saber que no existen más palabras antes o despues de la secuencia es informativo. Esta solución implicaría que exista un simbolo especial dentro del vocabulario que nos pueda indicar estas situaciones. Dependiendo de la situación podrían ser los mismos tanto para el comienzo (` begining-of-sequence`) de la secuencia como para el final de la secuencia (`end-of-sequence`). Estos simbilos en general se los suele llamar `paddings` y son comunmente utilizados para mejorar la performance de los modelos.

Palabras fuera del vocabulario (out-of-vocabulary)
--------------------------------------------------

Cuando trabajamos con vectores a nivel de palabras o subpalabras, es complejo disponer de un diccionario que contemple todos los casos posibles. En este sentido, muchas veces intentaremos asignar un vector a una palabra que no está dentro del diccionario de palabras con el cual nuestro modelo se entrenó. Esto es altamente probable de suceder en tiempo de inferencia por ejemplo. La solución a este problem es similar a lo que mencionamos en [Comienzo y fin de una oración](#Comienzo-y-fin-de-una-oración) y consite en utilizar un símbolo especial para codificar aquellas palabras fuera del vocabulario o `out-of-vocabulary (OOV)`.

En este caso, cada vez que nuestro modelo se encuentra con una palabra que no está en el vocabulario, la misma se 

Enmascaramiento de palabras (word signature)
--------------------------------------------

Otra forma distinta de lidear con palabras fuera del vocabulario es remplazarlas por firmas de palabras o enmascararlas. Por ejemplo, similar a la estrategia de `out-of-vocabulary`, las palabras que no estan dentro del vocabulario podrían remplazarse con el símbolo `<UNK>` para denotar palabras desconocidas. Dependiendo de la tarea, quizás resulte más útil por ejemplo enmascarar o remplazar parte de la palabra. Por ejemplo, palabras que implican la negativa como en "**des**conocimiento" podrian remplazarse por "**des**\<UNK\>".

Otra técnica ampliamente utilizada es tratar a los números de forma distintiva, como por ejemplo remplazarlos con un simbolo `<NUM>`. Esta lista con mapeaos específicos se realiza manualmente y los casos que son útiles agregar dependen de la tarea en cuestión, pero son ampliamente eficientes. Si bien existen técnicas para aprender estos mapeos de forma automática cuando se utilizan tokenizadores que operan a nivel de partes de la palabra (word-piece), su contrapartida manual muchas veces resulta práctica, computacionalmente eficiente y sencilla de implementar.

Word dropout
------------
Disponer de un vector especial para aquellos casos donde la palabra dada no forma parte de nuestro vocabulario lamentablemente no es suficiente para manejar estas condiciones. Esto sucede porque durante entrenamiento, todas las palabras del corpus terminan estando dentro del vocabulario y, por lo tanto, la rutina de entrenamiento nunca se encontró con un caso del cual aprender como el símbolo `<UNK>` es útil. Esto implica que estos vectores nunca reciben actualizaciones durante el proceso de entrenamiento.

Una solución a este problema podría ser, pro ejemplo, remplazar algunas de las palabras que tienen una frecuencia baja de aparición en el texto por el símbolo de palabra-fuera-de-vocabulario. Esta solución funciona pero tiene la desventaja de que se pierden datos de entrenamiento - estas palabras ráras serán impactadas y el modelo no tendrá demansiada señal sobre las mismas.

Una mejor solución podría ser la utilización de lo que conocemos como *dropout*. El concepto de *dropout* basciamente nos permite, durante la fase de entrenamiento, aleatoriamente descartar palabras al remplazarlas con el símbolo `<UNK>`. Este remplazado se realiza de forma probabilistica basandose en la frecuencia de las palabras. Esto quiere decir que palabras más frecuentes tiene más chances de ser remplazadas que palabras más raras, pero no siempre son remplazadas. ¿Que tanto *dropout* deberíamos de realizar? La respuesta a esta pregunta viene en la forma de un hiperparámetro a calcular. Una forma típica puede ser :math:`p = \frac {\alpha} {freq(w_i) + \alpha}` donde :math:`\alpha` es un parámetro que controla que tan agresivamente debe realizar esta operación.

Dropout como forma de regularización
------------------------------------

Ademas de proveer una forma de que nuestros modelos aprendan a lidear con palabras fuera del vocabulario, *dropout* es útil a la hora de prevenir **overfitting** y así mejorar su rubustés dado que límita que tanto nuestro modelo puede descansar en alguna palabra en particular.
