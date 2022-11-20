# -*- coding: utf-8 -*-
# +
# ME72: Maestría en Métodos Cuantitativos para la Gestión y Análisis de Datos
# M72109: Analisis de Datos no Estructurados
# Universidad de Buenos Aires - Facultad de Ciencias Economicas (UBA-FCE)
# Año: 2020
# Profesor: Facundo Santiago, Javier Ignacio Garcia Fronti

# +
import sys, os, io, pathlib
import numpy as np
import sklearn

import gensim.downloader
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
from tqdm import tqdm
# -

class Word2VecVectorizer(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    
    UNKNOWN_WORD_TOKEN = "<UNK>"
    
    def __init__(self, model_path, from_pretrained=False, sequence_to_idx=False):
        """Permite vectorizar una secuencia de palabras utilizando un modelo entrenado y especificado en 
        `model_path` en formato binario. Alternativamente, se puede especificar `from_pretrained=True` en cuyo caso model_path se refiere al nombre de
        un modelo de `gesim`. Este vectorizador puede devolver o bien los indices de las palabras
        en el vocabulario de acuerdo al modelo indicado o bien los vectores de word2vec de acuerdo esté
        especificado en el parametro `sequence_to_idx`. Un nuevo tokens es agregado automaticamente para indicar
        tokens que no están en el vocabulario original. El vector de este token está inicializado con un valor
        aleatorio.
        """
        if from_pretrained:
            self.embeddings = gensim.downloader.load(model_path)
        else:
            path = os.path.abspath(model_path)
            self.embeddings = KeyedVectors.load_word2vec_format(datapath(path), binary=True)

        # Agregamos una representacion para las palabras que no estan en el vocabulario
        self.embeddings.add(self.UNKNOWN_WORD_TOKEN, (np.random.rand(self.embeddings.vector_size) - 0.5) / 5.0)
        
        self.vocab_size = len(self.embeddings.vocab)
        self.emdedding_size = self.embeddings.vector_size
        self._sequence_to_idx = sequence_to_idx
        
    def get_vector(self, word):
        """Devuelve el vector word2vec correspondiente a la palabra indicada."""
        try:
            return self.embeddings[word]
        except KeyError:
            return self.embeddings[self.UNKNOWN_WORD_TOKEN]
    
    def get_weights(self):
        """Devuelve la matriz que representa los vectores para cada una de las palabras del vocabulario. Esta matriz tiene
        dimensiones `vocab_size, emdedding_size`.
        """
        # get_keras_embedding requiere tener instalado Keras, el cual es incomplatible con la version de TF de Colab
        #return self.embeddings.wv.get_keras_embedding(train_embeddings=False)
        
        # Construirmos la matriz manualmente
        wv_matrix = (np.random.rand(self.vocab_size, self.emdedding_size) - 0.5) / 5.0
        for word in tqdm(self.embeddings.vocab):
            try:
                wv_matrix[self.word2idx(word)] = self.get_vector(word)
            except:
                pass
        
        return wv_matrix
    
    def word2idx(self, word):
        """Devuelve el indice correspondiente a la palabra indicada. Si la palabra no forma parte del
        vocabulario entonces se devuelve la representación del token `UNKNOWN_WORD_TOKEN`
        """
        try:
            return self.embeddings.wv.vocab[word].index
        except KeyError:
            return self.embeddings.wv.vocab[self.UNKNOWN_WORD_TOKEN].index
    
    def idx2word(self, idx):
        """Devuelve la palabra que está representada por el indice indicado.
        """
        return self.embeddings.wv.index2word[idx]
    
    def sequence_to_text(self, seqs):
        """Devuelve el texto asociado a una secuencia de IDs de vectores de word2vec."""
        return [' '.join([self.idx2word(idx) for idx in seq]) for seq in seqs]
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if (self._sequence_to_idx):
            for doc in X:
                yield [self.word2idx(token) for token in doc]
        else:
            for doc in X:
                yield [self.get_vector(token) for token in doc]
