Procesamiento de audio
======================

¿Que es el sonido?
------------------

El sonido humanamente audible consiste en ondas sonoras y ondas acústicas que se producen cuando las oscilaciones de la presión del aire, son convertidas en ondas mecánicas en el oído humano y percibidas por el cerebro. La propagación del sonido se realiza a través de un medio (fluido o sólido) entre el emisor y el receptor. En los fluidos el sonido toma la forma de fluctuaciones de presión mientras que en los cuerpos sólidos la propagación del sonido involucra variaciones del estado tensional del medio.

Características
---------------

Desde el punto de vista del procesamiento de datos, el audio/sonido posee propiedades peculiares que nos interesa resaltar. Las señales de sonido a menudo se repiten a intervalos regulares para que cada onda tenga la misma forma. La altura muestra la intensidad del sonido y se conoce como amplitud. El tiempo que tarda la señal en completar una onda completa es el **período**. La cantidad de ondas producidas por la señal en un segundo se llama **frecuencia**. La frecuencia es la recíproca del período. La unidad de frecuencia es **Hertz**.

.. figure:: _images/intro_signal.png
  :alt: Simple repeating signal showing Amplitude vs Time

  *Simple repeating signal showing Amplitude vs Time*

La mayoría de los sonidos que encontramos pueden no seguir patrones periódicos tan simples y regulares como el que mostramos más arriba. Pero estas señales pueden descomponerse en señales de diferentes frecuencias para crear señales compuestas con patrones repetidos más complejos. Todos los sonidos que escuchamos, incluida nuestra propia voz humana, consisten en formas de onda como estas. Por ejemplo, este podría ser el sonido de un instrumento musical.

.. figure:: _images/intro_composed.png
  :alt: Simple repeating signal showing Amplitude vs Time

  *Simple repeating signal showing Amplitude vs Time*


Representaciones digitales
--------------------------

Al igual que una imagen es representada utilizando la luminosidad de cada pixel en cada canal de color, para digitalizar una onda de sonido debemos convertir la señal en una serie de números para que podamos almacenarla. Esto se hace midiendo la amplitud del sonido a intervalos de tiempo fijos.

Cada una de estas medidas se denomina **muestreo** y la frecuencia de muestreo es el número de muestras por segundo. Por ejemplo, una frecuencia de muestreo común es de aproximadamente 44,100 muestras por segundo, o 44.1 kHz.

.. figure:: _images/intro_sampling_rate.png
  :alt: Sampling rate
  :width: 500

  *Sampling rate* `Fuente. <https://www.masteringthemix.com/blogs/learn/113159685-sample-rates-and-bit-depth-in-a-nutshell>`_


Principales tareas en procesamiento de audio
--------------------------------------------

Clasificación de audio
^^^^^^^^^^^^^^^^^^^^^^

Se trata de una de las tareas más comunes e implica tomar un sonido y asignarlo a una de varias clases. Por ejemplo, identificar el tipo de sonido pertenciendo a clases como "guitarra", "piano", "martillando", "cantando", etc.

Evidentemente, esto tiene infinitas aplicaciones Esto podría aplicarse para detectar la falla de maquinaria o equipo en función del sonido que produce, por ejemplo.

Separación o segmentación
^^^^^^^^^^^^^^^^^^^^^^^^^

La separación de audio implica aislar una señal de interés de un conjunto de señales para que luego pueda procesarse especificamente. Por ejemplo, es posible que desee separar las voces individuales de las personas de una gran cantidad de ruido de fondo o el sonido del violín del resto de la interpretación musical.

Generación de audio
^^^^^^^^^^^^^^^^^^^

Hemos visto muchas noticias en estos días sobre el uso del aprendizaje profundo para generar de manera programática imágenes de rostros y otras escenas que lucen extremadamente auténticas. De igual forma, podemos generar música sintéticamente.

Reconocimiento de voz
^^^^^^^^^^^^^^^^^^^^^

Auquen técnicamente es una tarea análoga a clasificación de audio, debido a la pecularidad de la implementación, suelen tener su propia categoría. Esta tarea busca clasificar un sonido dependiendo de la persona que está hablando. Es decir, detectar quien es la persona que está al habla en cada momento. Multiples sistemas que operan con comandos de voz realizan este tipo de procesamiento.

Texto-a-voz y voz-a-texto
^^^^^^^^^^^^^^^^^^^^^^^^^

Cuando se trata del habla humana, podemos dar un paso más y no solo reconocer quien habla, sino comprender lo que está diciendo. Esto implica extraer las palabras del audio, en el idioma en el que se habla y transcribirlo en oraciones de texto. Esto se refiere como "speech-to-text". Esta es una de las aplicaciones más desafiantes porque se ocupa no solo del análisis de audio, sino también requiere el desarrollo de alguna capacidad lingüística básica para descifrar palabras distintas a partir de los sonidos pronunciados. Ser capaz de comprender el habla humana, obviamente, permite una gran cantidad de aplicaciones útiles tanto en en el ámbito empresarial como personal.

Modelos neurales se utilzan en la actualidad para producir secuencias de texto directamente del sonido, de forma opuesta a como se hacía hace algunos años donde el audio se descomponía en fonémas con el objetivo de poder mapearlos a cada una de las palabras.

De forma inversa, es posible producir el sonido resultante de un determinado texto. Esto se refiere como "text-to-speech" o "sintentizado de voz". 

.. toctree::
   :maxdepth: 1
   :caption: En esta sección veremos

   Técnicas basadas en espectográmas <spectrogram>
   Modelos de industría para voz-a-texto y texto-a-voz <cognitive-services.ipynb>
   