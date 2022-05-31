.. _nlp-vocabulary:

Corpus, documento y vocabulario
===============================

Existen algunos conceptos importantes que vale la pena presentar y que utilizaremos a lo largo de toda esta sección. Estos conceptos son propios del procesamiento de lenguaje natural.

Corpus
------
Llamamos *corpus* a todo el conjunto de datos sobre el cual un modelo de aprendizaje automático de NLP será entrenado y validado. Representa todo el conjunto de texto disponible. Por ejemplo, en el contexto de un modelo que detecta el sentimiento de las conversaciones telefónicas de un call center, el corpus sería el conjunto de todas las transcripciones de las llamadas telefónica disponibles.

Documento
---------
Llamamos *documento* a cada una de las porciones de texto que componen el *corpus* y sobre las cuales nuestro modelo de aprendizaje automático debe operar. Es decir, que un *corpus* es un set de *documentos*. Por ejemplo, en el mismo contexto de un modelo que detecta el sentimiento de las conversaciones telefónicas de un call center, un documento sería cada una de las transcripciones disponibles (que corresponden a cada una de las llamadas) y sobre la que se quiere obtener el sentimiento.

El vocabulario
--------------
Mientras el corpus de texto se refiere al conjunto total de textos utilizados para una tarea particular, llamamos vocabulario al conjunto de palabras únicas que aparecen en tal corpus.

El concepto de **vocabulario** es importante ya que los modelos de aprendizaje automático no pueden trabajar con texto directamente, sino que necesitan representar las palabras como vectores. Para representar una palabra como un vector es necesario conocer el espacio en el cual la vamos a representar. Dicho espacio está definido por todas las palabras que son posible encontrar dentro del corpus, es decir el **vocabulario**. Ya sea que estamos trabajando con modelos clásicos o modelos de aprendizaje profundo, el concepto del **vocabulario** es clave ya que sus dimensiones afectan las representaciones de las palabras.

Vocabularios a nivel de caracteres
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Además de utilizar las palabras de un corpus como vocabulario, también se puede utilizar un vocabulario basado en caracteres. En este caso, cada carácter único en el corpus (por ejemplo, cada letra, cada número) sería un elemento dentro del vocabulario. En general, nos centraremos en vocabularios basados ​​en palabras, que son mucho más comunes que sus homólogos basados ​​en caracteres pero tengan en cuenta que existen casos de uso donde quisieramos que nuestro modelo opere a nivel de caracteres en lugar de sobre palabras.

Dilemas
~~~~~~~
Si el vocabulario es demasiado chico, nuestro modelo tendrá poca capacidad o poder expresivo para concentrar información importante, ya que muchas palabras terminan siendo desconocidas para nuestros modelos. Todas las palabras que no están dentro de nuestro vocabulario son ignoradas. Por el contrario, si el vocabulario es demasiado grande, introducimos un problema conocido como sparcity, donde hay “grandes regiones del espacio” que no contienen información: Por ejemplo, palabras que o bien nunca se usan o palabras que se usan demasiado. Si bien disponemos de modelos que pueden lidiar con este tipo de datos, cuando esta característica se encuentra presente en gran medida, la mayoria de los modelos encontrarán dificultades.

Esto quiere decir que el vocabulario deber ser justamente el necesario. El proceso de :doc:`Normalization` nos ayudará en esta tarea ya que acotará la cantidad de palabras que están en nuestro vocabulario.
