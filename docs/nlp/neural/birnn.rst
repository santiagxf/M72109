Redes Neurales Recurrentes Bidireccionales
==========================================

Introducción
------------

Las redes RNN nos permiten computar funciones basadas en el pasado, es decir, basadas en todos las palabras de la secuencia que estan antes de una posición dada. Sin embargo, existen numerosas tareas donde la información que se encuentra más adelante de la secuencia es importante para saber si una determinada palabra es importante o no. 

De la misma forma que una RNN nos permite abstraernos de la suposición de Markov y dependender arbitrariamente de las palabras que aparecen antes de una palabra dada, las redes BI-RNN o Bidirectional Recurrent Neural Networks nos permiten depender arbitrariamente tanto de palabras que aparecen antes como de aquellas que aparecen despues. 

Arquitectura
------------

Las redes BI-RNN funcionan al mantener no uno sino 2 estados internos separados, :math:`s _ {i} ^ {f} y s _ {i} ^ {b}` para cada posición *i*. El estado :math:`s _ {i} ^ {f}` está basado en la secuencia de entrada :math:`x _ {1:i}` y :math:`s _ {i} ^ {b}` está basado en la secuencia de entrada :math:`x _ {n:i}`. El estado interno de la red está representado por ambos estados, teniendo en cuenta entonces información del futuro y del pasado.

Internamente entonces esto representa la concatenación de dos RNN, una que lee la secuencia de derecha a izquierda y otra que la lee de izquierda a derecha. La representación de la palabra en la posición *i* entonces es la concatenación de ambos estados internos. Estos vectores resultantes pueder ser utilizados luego como entrada en una red neuronal más compleja.

En frameworks como `TensorFlow y Keras`, podemos consturir este tipo de redes de la sigueinte forma:

.. code:: python

  import tensorflow.keras as keras
  from tensorflow.keras.models import Sequential, Model
  from tensorflow.keras.layers import Embedding, LSTM, Dense, SpatialDropout1D, Bidirectional

  model = Sequential([
        Embedding(...),
        SpatialDropout1D(0.2),
        Bidirectional(LSTM(hidden_state_size)),
        Dense(number_of_classes, activation='softmax')
    ])

El ejemplo anterior construye una red para resolver un problema de clasificación utilizando las siguientes capas:

- **Embedding:** Esta capa transforma vectores que representan indices dentro de una matriz en representaciones vectoriales densas. Básicamente en este caso nos resolverá la busqueda de las representaciones vectoriales para nuestras palabras.
- **SpatialDropout1D:** Este tipo de capas ayudan a promover la independencia entre filtros (feature maps). Funciona en forma análoga a `Dropout` pero en lugar de desconectar elementos individuales, desconecta el filtro completo.
- **Bidirectional:** Long Short-Term Memory layer en una construcción bidireccional - Hochreiter 1997
- **Dense:** Una típica capa de una red neuronal completamente conectada (fully connected)