# -*- coding: utf-8 -*-
# +
# ME72: Maestría en Métodos Cuantitativos para la Gestión y Análisis de Datos
# M72109: Analisis de Datos no Estructurados
# Universidad de Buenos Aires - Facultad de Ciencias Economicas (UBA-FCE)
# Año: 2020
# Profesor: Facundo Santiago
# -

import sklearn
from tensorflow.keras.preprocessing.sequence import pad_sequences

class PadSequenceTransformer(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    def __init__(self, max_len=None):
        """Esta función transforma una lista de `num_samples` secuencias (lista de enteros) en un Numpy 2D 
        array de `(num_samples, num_timesteps)`. `num_timesteps` es o bien el valor del argumento `maxlen` si 
        especificado, o la longitud mas larga en las secuencias especificadas."""
        self.max_len = max_len

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return pad_sequences(list(X), maxlen=self.max_len, padding="pre")
