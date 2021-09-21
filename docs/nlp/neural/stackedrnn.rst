Redes Neurales Recurrentes Produndas (apiladas)
===============================================

Motivación
----------

De la misma forma que multiples capas pueden ser apiladas para construir lo que comunmente llamamos **red neuronal profunda**, multiples capas de redes de tipo RNN pueden apilarse también para formar una **Red Neural Recurrente Produnda** o **Redes Neuronales Recurrentes apiladas**. En estas construcciones disponemos de *N* redes de tipo RNN, y donde la entrada de la primera red es la secuencia de entrada :math:`x _ {1:n}`, mientras que la entrada de las restantes es la salida de las redes que se encuentran en una capa más arriba. La salida de toda la arquitectura corresponde a la salida de la última red neuronal en el apilamiento.

..note:: Aunque teoricalmente no está claro el por qué una red reunonal recurrente profunda debería de proveer mayor poder de apendizaje, en la práctica el apilamiento de 2-5 redes de este tipo suelen ser superadoras a sus contrapartes de 1 sola capa.

En frameworks como `TensorFlow y Keras`, podemos consturir este tipo de redes de la sigueinte forma:

.. code:: python

  import tensorflow.keras as keras
  from tensorflow.keras.models import Sequential, Model
  from tensorflow.keras.layers import Embedding, LSTM, Dense, SpatialDropout1D

  model = Sequential([
        Embedding(...),
        SpatialDropout1D(0.2),
        LSTM(hidden_state_size, return_sequences = True),
        LSTM(hidden_state_size, return_sequences = True),
        LSTM(hidden_state_size),
        Dense(number_of_classes, activation='softmax')
    ])

Otra forma de lograr la misma estructura, aunque un poco más eficiente es:

.. code:: python

    import tensorflow.keras as keras
    from tensorflow.keras.models import Sequential, Model
    from tensorflow.keras.layers import Embedding, RNN, LSTMCell, Dense, SpatialDropout1D

    cells = [
        LSTMCell(hidden_state_size),
        LSTMCell(hidden_state_size),
        LSTMCell(hidden_state_size),
    ]

    model = Sequential([
        Embedding(...),
        SpatialDropout1D(0.2),
        RNN(cells),
        Dense(number_of_classes, activation='softmax')
    ])


Extracción de predictores
-------------------------

Una de las características más importantes del aprendizaje profundo es la capacidad de extraer predictores de forma automática y aprender representaciones que resulten útiles para resolver la tarea encomendada. Esta misma idea se puede lograr en arquitecturas basadas en RNN al quitar la restricción de que cada una de las RNN de la pila solo puedan acceder a las representaciones de las que están en las capas superiores.

Arquitectura
^^^^^^^^^^^^

La idea principal de esta arquitectura es que un apilamiento de redes de tipo RNN es, también, una secuencia y por lo tanto tal apilamiento puede ser representado por una red RNN cuya entrada es la salida de cada una de multiples RNNs, puetas en orden. Esto quiere decir que la salida de esta ultima RNN de nivel 2, puede considerarse como la representación o codificación del estado general de todo el apilamiento de redes. 




