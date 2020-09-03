# -*- coding: utf-8 -*-
# +
# ME72: Maestría en Métodos Cuantitativos para la Gestión y Análisis de Datos
# M72109: Analisis de Datos no Estructurados
# Universidad de Buenos Aires - Facultad de Ciencias Economicas (UBA-FCE)
# Año: 2020
# Profesor: Facundo Santiago

# +
import sys, os, io, pathlib
import numpy as np
import sklearn

from gensim.models import KeyedVectors
from gensim.test.utils import datapath

# -

class Word2VecVectorizer(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    
    UNKNOWN_WORD_TOKEN = "<UNK>"
    
    def __init__(self, model_path, sequence_to_idx=False):
        path = os.path.abspath(model_path)
        self.embeddings = KeyedVectors.load_word2vec_format(datapath(path), binary=True)
        
        # Agregamos una representacion para las palabras que no estan en el vocabulario
        self.embeddings.add(self.UNKNOWN_WORD_TOKEN, (np.random.rand(self.embeddings.vector_size) - 0.5) / 5.0)
        
        self.vocab_size = len(self.embeddings.vocab)
        self.emdedding_size = self.embeddings.vector_size
        self._sequence_to_idx = sequence_to_idx
        
    def get_vector(self, word):
        try:
            return self.embeddings[word]
        except KeyError:
            return self.embeddings[self.UNKNOWN_WORD_TOKEN]
    
    def get_weights(self):
        # get_keras_embedding requiere tener instalado Keras, el cual es incomplatible con la version de TF de Colab
        #return self.embeddings.wv.get_keras_embedding(train_embeddings=False)
        
        # Construirmos la matriz manualmente
        wv_matrix = (np.random.rand(self.vocab_size, self.emdedding_size) - 0.5) / 5.0
        for word in self.embeddings.vocab:
            try:
                wv_matrix[self.word2idx(word)] = self.get_vector(word)
            except:
                pass
        
        return wv_matrix
    
    def word2idx(self, word):
        try:
            return self.embeddings.wv.vocab[word].index
        except KeyError:
            return self.embeddings.wv.vocab[self.UNKNOWN_WORD_TOKEN].index
    
    def idx2word(self, idx):
        return self.embeddings.wv.index2word[idx]
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if (self._sequence_to_idx):
            for doc in X:
                yield [self.word2idx(token) for token in doc]
        else:
            for doc in X:
                yield [self.get_vector(token) for token in doc]
