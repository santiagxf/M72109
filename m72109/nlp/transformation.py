# -*- coding: utf-8 -*-
# +
# ME72: Maestría en Métodos Cuantitativos para la Gestión y Análisis de Datos
# M72109: Analisis de Datos no Estructurados
# Universidad de Buenos Aires - Facultad de Ciencias Economicas (UBA-FCE)
# Año: 2020
# Profesor: Facundo Santiago, Javier Ignacio Garcia Fronti

# +
import sys, os, io, pathlib
import math
from typing import List

import sklearn
import numpy as np
import gensim.downloader
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
from tqdm import tqdm
from tensorflow.keras.preprocessing.sequence import pad_sequences

# -

class Word2VecVectorizer(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    
    UNKNOWN_WORD_TOKEN = "<UNK>"
    
    def __init__(self, model: str, sequence_to_idx: bool=False):
        """Permite vectorizar una secuencia de palabras utilizando un modelo entrenado y especificado en 
        `model` en formato binario. Alternativamente, `model` se refiere al nombre de un modelo de `gesim`.
        Este vectorizador puede devolver o bien los indices de las palabras en el vocabulario de acuerdo al 
        modelo indicado o bien los vectores de word2vec de acuerdo este especificado en el parámetro
        `sequence_to_idx`. Un nuevo tokens es agregado automaticamente para indicar tokens que no están
        en el vocabulario original. El vector de este token está inicializado con un valor aleatorio.

        Parameters
        ----------
        model: str
            Directorio donde se encuentran los pesos de los embeddings de Word2Vec o el nombre de un modelo
            de `gesim`.
        sequence_to_idx:
            Indica si se deben retornar los vectores de Word2Vec o los indices correspondientes a la matriz
            de pesos de Word2Vec.
        """
        if pathlib.Path(model).exists():
            path = os.path.abspath(model)
            self.embeddings = KeyedVectors.load_word2vec_format(datapath(path), binary=True)
        else:
            self.embeddings = gensim.downloader.load(model)
    

        # Agregamos una representacion para las palabras que no estan en el vocabulario
        self.embeddings.add(self.UNKNOWN_WORD_TOKEN, (np.random.rand(self.embeddings.vector_size) - 0.5) / 5.0)
        
        self.vocab_size = len(self.embeddings.vocab)
        self.emdedding_size = self.embeddings.vector_size
        self._sequence_to_idx = sequence_to_idx
        
    def get_vector(self, word: str) -> np.ndarray:
        """
        Devuelve el vector word2vec correspondiente a la palabra indicada.

        Parameters
        ----------
        word: str
            Palabra de la cual buscar el vector. Si la palabra no existe, devuelve el embedding de la
            palabra desconocida `UNKNOWN_WORD_TOKEN`.
        """
        try:
            return self.embeddings[word]
        except KeyError:
            return self.embeddings[self.UNKNOWN_WORD_TOKEN]
    
    def get_weights(self):
        """
        Devuelve la matriz que representa los vectores para cada una de las palabras del vocabulario. Esta matriz tiene
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
        """
        Devuelve el indice correspondiente a la palabra indicada. Si la palabra no forma parte del
        vocabulario entonces se devuelve la representación del token `UNKNOWN_WORD_TOKEN`

        Parameters
        ----------
        word: str
            Palabra de la cual buscar el índice. Si la palabra no existe, devuelve el índice de la
            palabra desconocida `UNKNOWN_WORD_TOKEN`.
        """
        try:
            return self.embeddings.wv.vocab[word].index
        except KeyError:
            return self.embeddings.wv.vocab[self.UNKNOWN_WORD_TOKEN].index
    
    def idx2word(self, idx: int) -> str:
        """
        Devuelve la palabra que está representada por el indice indicado.

        Parameters
        ----------
        idx: int
            Palabra de la cual buscar el índice. Si la palabra no existe, devuelve el índice de la
            palabra desconocida `UNKNOWN_WORD_TOKEN`.
        """
        return self.embeddings.wv.index2word[idx]
    
    def sequence_to_text(self, seqs: List[int]) -> str:
        """
        Devuelve el texto asociado a una secuencia de IDs de vectores de word2vec.

        Parameters
        ----------
        seqs: List[int]
            Secuencia de indices de palarbas a transformar.
        """
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

class PadSequenceTransformer(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    def __init__(self, max_len: int=None, padding: str="pre"):
        """
        Esta función transforma una lista de `num_samples` secuencias (lista de enteros) en un Numpy 2D 
        array de `(num_samples, num_tokens)`. `num_tokens` es o bien el valor del argumento `max_len` si 
        especificado, o la longitud mas larga en las secuencias especificadas.

        Parameters
        ----------
        max_len: int
            Longitud máxima que debe tener la secuencia. Secuencias de texto con mayor longitud son truncadas.
            Secuencias de menor longitud son completadas utilizando padding.
        padding: str
            La strategia de padding a utilizar: `pre` (padding se agrega al comienzo de la secuencia) o `pos`
            (padding se agrega al final de la secuencia).
        """
        self.max_len = max_len
        self.padding = padding

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return pad_sequences(list(X), maxlen=self.max_len, padding=self.padding)

def split_text_with_context(text: str, unique_words: int = 150, context_words: int = 50) -> List[str]:
    """
    Divide una secuencia de palabras de longitud arbitraria en una lista de secuencias de no mas que
    `context_words + unique_words` palabras. Cada subsecuencia tendra `unique_words` palabras del texto
    original y las restantes palabras seran arrastradas de la subsecuencia anterior para manetener el 
    contexto de la oración.

    Parameters
    ----------
    text : str
        El texto que queremos dividir en subsequencias.
    unique_words : int
        Cantidad de palabras únicas que deben manetenerse en cada subsecuencia.
    context_words : int
        Cantidad de palabras que deben traerse de la subsequencia anterior como contexto.

    Returns
    -------
    List[str]
        A list of sub-sequences of text of no more than `unique_words` + `context_words`.
    """

    words = text.split()
    num_seqs = math.ceil(len(words)/unique_words)

    seqs = [' '.join(words[max(seq*unique_words - context_words, 0):(seq + 1)*unique_words]) for seq in range(num_seqs)]
    return seqs
