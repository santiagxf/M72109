Modelado utilizando secuencias
==============================

Introducción
------------

Cuando trabajamos con texto inmediatamente nos hace sentido pensar en secuencias, tales como palabras (secuencias de letras), oraciones (secuencias de palabras) o documentos (secuencias de oraciones). Hemos visto hasta ahora como determinadas representaciones que si bien efectivas, al estar basadas en bolsa de palabras - bag of words - nos fuerzan a descartar el orden de las palabras.

Las redes neuronales recurrentes (RNN) nos permiten representar secuencias de longitudes arbitrarias donde se mantienen las propiedades estructurales de las mismas. Las `RNN`, y en particular aquellas con arquitecturas basadas en compuertas (gates) como son las `LSTM` or las `GRU`, son muy eficientes a la hora de captural la estructura y las regularidades dentro de una secuencia dada. Podríamos decir que todas las arquitectura de NLP modernas basadas en aprendizaje profundo están basadas en estas arquitecturas.

.. toctree::
   :maxdepth: 1
   :caption: En esta sección veremos

   Redes Neurales Recurrentes en secuencias <rnn>
   Redes Neurales Recurrentes Bidireccionales <birnn>
   Redes Neurales Recurrentes Produndas <stackedrnn>