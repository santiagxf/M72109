Métodos neurales
================

Introducción
------------
El uso de redes neutrales para la NLP no comenzó hasta principios de la década de 2000. Sin embargo, para fines de la década de 2010, las redes neuronales y en particular los métodos neurales transformaron la forma de hacer NLP, mejorando o incluso reemplazando técnicas anteriores. Esto fué posible gracias a la utilización de grandes cuerpos de texto, avances en el diseño de arquitecturas específicas de redes neuronales y la disponibilidad de basto poder de computo.

En el procesamiento de texto tradicional, las características o predictores generalmente se generan de forma manual, llevandolas a estar incompletas o en su defecto, a requerir gran cantidad de tiempo por parte del desarrollador para generarlas. Las redes neuronales pueden aliviar estos problemas. 


Representaciones y aprendizaje profundo
---------------------------------------

El concepto de representaciones es central para la idea de deep learning. Más aún, se podría decir que la capacidad de aprender estas representaciones de forma no supervisada y automática es el centro del por qué deep learning funciona tan bien. Sin embargo, esto conlleva un precio. Si pensamos en el caso de las representaciones lineales, estas son interpretables en el sentido de que podemos asignarle un significado a cada dimensión dentro del vector. Sin embargo, en deep learning este no es generalmente el caso ya que suelen aprender representaciones multidimensionales que incluso están compuestas por multiples capas donde los valores de una capa dependen de las anteriores. 

.. toctree::
   :maxdepth: 1
   :caption: En esta sección veremos

   Modelos basados en secuencias <sequences>
   Modelos de secuencias-a-secuencias <seq2seq>
   Modelos de lenguaje neurales <language-models>
   Modelos de industria <cognitive-services.ipynb>
   Interpretación de modelos <interpret>
