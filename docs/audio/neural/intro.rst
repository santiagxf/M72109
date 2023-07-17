Modelos neurales
================

Los modelos de aprendizaje profundo han sido adoptados ampliamente para el procesamiento de imágenes y texto. Sin embrago, existen importantes diferencias entre estos tipos de datos y el audio que representan complicaciones a la hora de aplicar las mismas técnicas sobre ellos. En primer lugar, el audio generalmente se representa usando una serie de tiempo univariada, lo cual es una diferencia fundamental con las imágenes. Para resolver esta limitante, los audios son comunmente transformados a espacios bidimensionales de tiempo-frecuencia, sin embargo, este espacio no es homogeneo como sucede con las imágenes.


Ingeniería de predictores
-------------------------

En general, es importante generar las representaciones correctas con las cuales codificar la información antes de suministrarla a nuestros modelos de aprendizaje automático. Sin embargo, una desventaja de la ingeniera de predictores es que el preprocesamiento realizado en estos predictores podría no ser óptimo para la tarea en cuestión. Los modelos basados en aprendizaje profundo en general están diseñados para realizar esta tarea de forma no supervisada y aprender una representación útil para la tarea a resolver durante el proceso de aprendizaje.

Por decadas la utilización de espectogramas ha sido una de las técnicas más frecuentes a la hora de generar representaciones para el procesamiento de audio. Dado su amplio éxito, muchos modelos (incluso modelos basados en aprendizaje profundo) utilizan estas transformaciones como representaciones iniciales. Veremos un ejemplo de estos modelos en la sección :doc:`spectogram`.

En aquellos modelos donde buscamos evitar tener que diseñar estas transformaciones, existen varios métodos que buscan simplificar el proceso de extracción de predictores y pasar a una estrategia totalmente basada en aprendizaje automático. Esto significa que estas transformaciones son aprendidas como parte del proceso de optimización del modelo utilizando directamente la información de la onda de sonido. Por ejemplo, los autores H. Lee, Y. Largman, P. Pham and Andrew Y. Ng.  exploran estas ideas en el paper `Unsupervised feature learning for audio classification using convolutional deep belief networks. 2009 <https://ai.stanford.edu/~ang/papers/nips09-AudioConvolutionalDBN.pdf>`_.

.. note:: Esta fuera del alcance de este curso la exploración de arquitecturas neurales que aprendan esta representaciones de forma no supervisada. Queda a disposición del alumno explorar las mismas. 


Modelos
-------

Los modelos neurales para el procesamiento de audio, ya sean utilizando secuencias de representaciones intermedias o la información de onda del sonido directamente, puede ser suministrada a modelos de aprendizaje automático basados en aprendizaje profundo. En general podemos utilizar:

:Modelos basados en redes neurales convolucionales: Estas redes utilizan capas de convolución de 1 dimensión (tiempo) o 2 dimensiones (tiempo-frencuencia) para computar predictores (feature maps) útiles para la tarea a resolver. Al igual que con imágenes, capas de pooling suelen ser agregadas para reducir la dimensionalidad de los predictores que se aprenden. :ref:`YAMNet <yamnet_class.ipynb>` es un ejemplo de este tipo de modelos. 
:Modelos basados en redes recurrentes: Estos modelos computan un estado latente intermedio por cada paso de la secuencia y por lo tanto pueden capturar dependencias temporales en las mismas. Ademas de modelar diractamente secuencias temporales, estos modelos pueden ser extendidos para modelar la señal en los dominios de frecuencia-tiempo. Modelos como TF-LSTM (Time-Frequency LSTM) son alternativas a las CNNs, las cuales capturan la correlación entre diferentes frencuencias y por lo tanto pueden ser utilizadas para modelar tanto relaciones temporales como espectrales. Alternativamente, RNNs pueden ser utilizadas para procesar la salida de una red CNN. Estas arquitecturas suelen llamarse CRNN (Convolutional Recurrent Neural Network).

.. note:: Para una lectura más en profundidad de estas técnicas se recomienda la lectura: `Deep Learning for Audio Signal Processing <https://arxiv.org/abs/1905.00078#>`_.

.. toctree::
   :maxdepth: 1
   :caption: En esta sección veremos

   Modelos basados en espectogramas <spectogram>
   Modelos basados en embeddings <embedding>
   Modelos de industria <cognitive-services.ipynb>
