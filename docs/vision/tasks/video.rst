Procesamiento de video
======================


Principales tareas en el procesamiento de video
-----------------------------------------------

.. _rst_object_tracking:

Seguimiento de objetos (Object tracking)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una forma de detectar objetos en un video es utilizando cada uno de los cuadros del mismo y aplicar sobre ellos técnicas :ref:`rst_object_detection`. Sin embargo, sabemos que la posición de un objeto en movimiento en el cuado *t+1* está relacionada con la posición del mismo objeto en el cuadro *t*. Por lo tanto, existe un beneficio en modelar la secuencia de cuadros en su conjunto en lugar de tratar a los cuadros como instancias de imágenes independientes. Está tarea se conoce como **Seguimiento de objetos**.

.. _rst_object_tracking:

Reconocimiento de acciones
^^^^^^^^^^^^^^^^^^^^^^^^^^

De igual forma que :ref:`rst_object_tracking` nos permite realizar el seguimiento de un objeto como una generalización de :ref:`rst_object_detection`, el reconocimiento de acciones nos permite estimar la acción que un determinado objeto o persona está realizando como una generalización de :ref:`rst_pose_estimation`. Por ejemplo, para las personas estas acciones podrían ser **bailando, levantandose, sentandose, dibujando, etc**. 

Slow-motion
^^^^^^^^^^^

Estos modelos tienen como objetivo realizar la interpolación entre dos cuadros, con el objetivo de generar videos que hagan que las "camara lenta" de un video se vean de una forma mas fluida.


Modelos de procesamiento de video
---------------------------------

El procesamiento de video ofrece sus propios desafios principalmente por la cantidad de información de diferentes tipos que continene: imagenes, audio, dialogos, etc. Estos desafios deberemos atacarlos de alguna forma.

.. toctree::
   :maxdepth: 1
   :caption: En esta sección veremos

   Videos como secuencias <sequences/rnn>
   Redes de convolución 3D <sequences/conv3d>
