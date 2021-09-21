.. _rst-seq2seq:

Modelos de secuencias-a-secuencias
==================================

En las arquitecturas :ref:`rst-conditioned-generator` el vector *c* puede tomar diversas formas y como bien mencionamos, este mismo vector puede ser la salida de otra red RNN. Este tipo de modelos se los conoce como modelos *secuencias-a-secuencia* o *sequence2sequence* y la arquitectura general se la conoce como :ref:`rst-encoder-decoder`.

.. _rst-encoder-decoder:

Encoder-Decoder
---------------

En esta configuración disponemos de una secuencia de entrada :math:`x _ {1:n}` y estamos interesados en generar otra secuencia :math:`t _ {1:m}`, donde la secuencia :math:`x _ {1:n}` es codificada en un vector de contexto *c* a traves de una función de codificación comunmente llamado *encoder*. Este *encoder* es en general una RNN. Luego, utilizando la ya conocida arquitectura :ref:`rst-conditioned-generator`, ahora llamada *decoder*, generamos la salida :math:`t _ {1:m}` estando condicionados por el vector *c*.

.. figure:: ../_images/rnn_encoder_decoder.png
  :alt: Arquitectura de RNN de tipo encoder-decoder.

  *Arquitectura de RNN de tipo encoder-decoder.*

Notemos aquí que las longitudes de las secuencias *x*, que es la entrada del encoder, y *t*, que es la salida del decoder, pueden ser distintas. Ambos el *encoder* como el *decoder* son entrenados al mismo tiempo, aunque *la supervisión* solo sucede en el decoder. Sin embargo, la propagación del gradiente se realiza en toda la red, incluyendo el *encoder*. 

.. warning:: Es fácil ver que en esta configuración existe una gran presión sobre el decoder, quién tiene una tarea mucho más compleja que la del encoder. Este hecho se hará realidad durante las rutinas de entrenamiento donde deberemos ajustar la arquitectura para balancear la carga en los componentes.

En frameworks como `TensorFlow y Keras`, podemos consturir este tipo de redes de la sigueinte forma:

.. code:: python

  import tensorflow.keras as keras
  from tensorflow.keras.models import Sequential, Model
  from tensorflow.keras.layers import Embedding, LSTM, Dense, SpatialDropout1D

  model = Sequential([
        Embedding(...),
        LSTM(hidden_state_size),
        RepeatVector(),
        LSTM(hidden_state_size, return_sequences=True)
        TimeDistributed(Dense(vocabulary_size, activation='softmax'))
    ])

Los modelos de secuencia-a-secuencia son ampliamente utilizado en la industria y en las organizaciones para resolver problemas concretos, ademas de formar parte del corazón de técnicas avanzadas de :ref:`rst-language-model`.