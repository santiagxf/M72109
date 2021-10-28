Redes de convolución en 3 dimensiones
=====================================

Una convolución 3D es un tipo de convolución donde el kernel se desliza en 3 dimensiones en lugar de 2 dimensiones con convoluciones 2D. Un caso de uso de ejemplo son las imágenes médicas donde se construye un modelo utilizando cortes de imágenes en 3D. Además, los datos basados en video tienen una dimensión temporal adicional sobre las imágenes, lo que los hace adecuados para este módulo.

.. figure:: /vision/_images/cnn_3d.png
  :alt: Convolución 3D
  :width: 400

  *Convolución 3D*

Una diferencia clave entre imágenes estáticas y videos es la dimensión temporal adicional. Como vimos en :doc:`rnn`, podemos tratar las dimensiones espaciales y temporales por separado. Sin embargo resulta atractivo explorar características a través de las dimensiones espacial y temporal al mismo tiempo
mediante el uso de convoluciones 3D o auto-atención.

.. note:: Este tipo de modelos escapan al alcance de este curso, pero una lectura recomendada para quienes estén interesados es el paper: `Revisiting 3D ResNets for Video Recognition <https://arxiv.org/pdf/2109.01696v1.pdf>`_