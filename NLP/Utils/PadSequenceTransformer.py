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
        """This function transforms a list of `num_samples` sequences (lists of integers) into a 2D Numpy 
        array of shape `(num_samples, num_timesteps)`. `num_timesteps` is either the `maxlen` argument if
        provided, or the length of the longest sequence otherwise."""
        self.max_len = max_len

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return pad_sequences(list(X), maxlen=self.max_len, padding="pre")
