Preprocesamiento
================

Motivación
----------
Como con todo problema que se resuelve utilizando aprendizaje automático, la calidad de los datos es importante para obtener un modelo que generalize de la mejor manera. **NLP** no es la excepción. El procedimiento por el cual preparamos los datos en una tarea de procesamiento de lenguaje natural se conoce como *preprocesamiento*. En general, este preprocesamiento tendrá dos objetivos:

- **Canonización:** Donde buscamos que nuestro texto tenga un conjunto de caracteres conocido y las longitudes o dimensiones esperadas.
- **Preparación del vocabulario:** Donde buscaremos reducir el tamaño del vocabulario que nuestro modelo interpretará, tal como se explica en :ref:`nlp-vocabulary` y es un paso importante en los modelos clásicos.


.. toctree::
   :maxdepth: 2
   :caption: En esta sección
   :hidden:

   El vocabulario <vocabulary>
   Normalización de texto <Normalization.ipynb>
   Trabajando con secuencias largas <long_sequences.ipynb>