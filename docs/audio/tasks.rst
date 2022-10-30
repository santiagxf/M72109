Principales tareas en procesamiento de audio
--------------------------------------------

Las tareas que en general involucran procesamiento de audio pueden dividirse en las siguiente categorías dependiendo de que tipo de objetivo intentan predecir a partir de los datos de entrada.

Clasificación de audio
^^^^^^^^^^^^^^^^^^^^^^

Se trata de una de las tareas más comunes e implica tomar un sonido y asignarlo a una de varias clases. Por ejemplo, identificar el tipo de sonido pertenciendo a clases como "guitarra", "piano", "martillando", "cantando", etc. 

Evidentemente, esto tiene infinitas aplicaciones. Esto podría aplicarse para detectar la falla de maquinaria o equipo en función del sonido que produce, por ejemplo. Dado que asigna una única clase a todo un audio (el cúal representa una secuencia), esta tarea también se la denomina clasificación de secuencias o *sequence classification*. Cuando la clasificación se realiza en fragmento del audio general, esta tarea se la suele denominar *sequence labeling*.

Clasificación de audio multi-etiqueta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En este caso particular de clasificación, el objetivo es predecir un subset de todas las posibles clases. Por ejemplo, el objetivo podria ser un conjunto de distintos tonos musicales. 

Regresión de audio
~~~~~~~~~~~~~~~~~~

También conocida como *sequence regression*, el objetivo de esta tarea es predecir un valor perteneciente a un rango continuo de valores. Estimar el tempo musical o predecir la siguiente muestra de audio podria configurarse como este tipo de tareas. Note que cualquier problema de regresión puede siempre formularse como un problema de clasificación aplicando discretización.

Separación o segmentación
^^^^^^^^^^^^^^^^^^^^^^^^^

La separación de audio implica aislar una señal de interés de un conjunto de señales para que luego pueda procesarse especificamente. Por ejemplo, es posible que desee separar las voces individuales de las personas de una gran cantidad de ruido de fondo o el sonido del violín del resto de la interpretación musical.

Generación de audio
^^^^^^^^^^^^^^^^^^^

Hemos visto muchas noticias en estos días sobre el uso del aprendizaje profundo para generar de manera programática imágenes de rostros y otras escenas que lucen extremadamente auténticas. De igual forma, podemos generar música sintéticamente.

Reconocimiento de voz
^^^^^^^^^^^^^^^^^^^^^

Esta tarea busca clasificar un sonido dependiendo de la persona que está hablando. Es decir, detectar quién es la persona que está al habla en cada momento. Multiples sistemas que operan con comandos de voz realizan este tipo de procesamiento. Auque técnicamente es una tarea análoga a clasificación de audio, debido a la pecularidad de la implementación, suelen tener su propia categoría. 

Texto-a-voz y voz-a-texto
^^^^^^^^^^^^^^^^^^^^^^^^^

Cuando se trata del habla humana, podemos dar un paso más y no solo reconocer quien habla, sino comprender lo que está diciendo. Esto implica extraer las palabras del audio, en el idioma en el que se habla y transcribirlo en oraciones de texto. Esto se refiere como "speech-to-text". Esta es una de las aplicaciones más desafiantes porque se ocupa no solo del análisis de audio, sino también requiere el desarrollo de alguna capacidad lingüística básica para descifrar palabras distintas a partir de los sonidos pronunciados. Ser capaz de comprender el habla humana, obviamente, permite una gran cantidad de aplicaciones útiles tanto en en el ámbito empresarial como personal.

Modelos neurales se utilzan en la actualidad para producir secuencias de texto directamente del sonido, de forma opuesta a como se hacía hace algunos años donde el audio se descomponía en fonémas con el objetivo de poder mapearlos a cada una de las palabras.

De forma inversa, es posible producir el sonido resultante de un determinado texto. Esto se refiere como "text-to-speech" o "sintentizado de voz". 
