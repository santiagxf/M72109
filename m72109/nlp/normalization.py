# -*- coding: utf-8 -*-
# +
# ME72: Maestría en Métodos Cuantitativos para la Gestión y Análisis de Datos
# M72109: Analisis de Datos no Estructurados
# Universidad de Buenos Aires - Facultad de Ciencias Economicas (UBA-FCE)
# Año: 2020
# Profesor: Facundo Santiago, Javier Ignacio Garcia Fronti
# -

import unidecode
import spacy
import re
import sklearn
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize.casual import TweetTokenizer
from nltk.tokenize.api import TokenizerI

LANGUAGE_MODULES = {
    'spanish': 'es_core_news_sm',
    'english': 'en_core_web_sm'
}

class TextNormalizer(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    """Un normalizador de texto pensado para procesamiento de texto en multiples idiomas. Este normalizador puede devolver o bien un texto transformado o bien una
    secuencia de tokens si se indica el parametro `return_tokens`. Dentro de los procesamientos disponibles son lemmatization, stemming, reducir la longitud
    de caracteres repetidos, eliminar URLs y eliminar mayusculas."""
    
    def __init__(self, tokenizer:TokenizerI, language:str = 'spanish', lemmatize:bool=True, stem:bool = False, strip_stopwords:bool = True, 
                 strip_urls:bool = True, strip_accents:bool = True, token_min_len:int = -1, preserve_case:bool = True, return_tokens:bool = False):
        self.tokenizer = tokenizer

        assert not (lemmatize and stem), "Utilize `lematize=True` o `stem=True`, pero no ambos."
        assert language in LANGUAGE_MODULES.keys(), f"`language` debe ser alguno de los siguientes valores: {LANGUAGE_MODULES.keys()}"
        
        if stem:
            self.stemmer = nltk.stem.SnowballStemmer(language=language) # Creamos un steammer
        else:
            self.stemmer = False
        
        if lemmatize:
            try:
                self.parser = spacy.load(LANGUAGE_MODULES[language])
            except Exception:
                raise ImportError(f"El modelo de procesamiento de texto en '{language}' no está instalado. Ejecute 'python -m spacy download {LANGUAGE_MODULES[language]}' para instalarlo. Es posible que tenga que reiniciar el kernel para que los cambios tengan efecto.")
            self.lemmatizer = lambda word : " ".join([token.lemma_ for token in self.parser(word)]) # Creamos un lemmatizer
        else:
            self.lemmatizer = False
        
        if strip_stopwords:
            nltk.download("stopwords", quiet=True)
            self.stopwords = set(stopwords.words(language)) # Instanciamos las stopwords en español
        
        self.preserve_case = preserve_case
        self.strip_stopwords = strip_stopwords
        self.strip_accents = strip_accents
        self.strip_urls = strip_urls
        self.urls_regex = re.compile('http\S+') # Usamos una expresion regular para encontrar las URLs
        self.token_min_len = token_min_len
        self._return_tokens = return_tokens
    
    def process_text(self, text):
        """Procesa una secuencia de texto de acuerdo a la configuración del normalizador. Este método
        devuelve una secuencia de tokens."""
        if not self.preserve_case:
            text = text.lower()

        tokens = self.tokenizer.tokenize(text)

        if self.strip_urls:
            tokens = [token for token in tokens if not re.match(self.urls_regex, token)]
        if self.token_min_len > 1:
            tokens = [token for token in tokens if len(token) > self.token_min_len]
        if self.strip_accents:
            tokens = [unidecode.unidecode(token) for token in tokens]
        if self.strip_stopwords:
            tokens = [token for token in tokens if token not in self.stopwords]
        if self.lemmatizer:
            tokens = [self.lemmatizer(token) for token in tokens]
        if self.stemmer:
            tokens = [self.stemmer.stem(token) for token in tokens]
        return tokens
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        results = np.ndarray(shape=(len(X)), dtype=object)
        if self._return_tokens:
            for idx, doc in enumerate(X):
                results[idx] = self.process_text(text=doc)
        else:
            for idx, doc in enumerate(X):
                results[idx] = ' '.join(self.process_text(text=doc))
        return results

class TweetTextNormalizer(TextNormalizer):
    def __init__(self, language:str = 'spanish', lemmatize:bool = True, stem:bool = False, reduce_len:bool = True, strip_handles:bool = True, strip_stopwords:bool = True,
                 strip_urls:bool = True, strip_accents:bool = True, token_min_len:int = -1, preserve_case:bool = True, return_tokens:bool = False):
        """Un normalizador de texto pensado para procesamiento de Tweets en multiples idiomas. Este normalizador puede devolver o bien un texto transformado o bien
        una secuencia de tokens si se indica el parametro `return_tokens`. Dentro de los procesamientos disponibles son lemmatization, stemming, reducir la
        longitud de caracteres repetidos, eliminar handles, eliminar URLs, eliminar mayusculas."""
        
        super().__init__(TweetTokenizer(strip_handles=strip_handles, reduce_len=reduce_len, preserve_case=preserve_case),
                         language=language,
                         lemmatize=lemmatize,
                         stem=stem,
                         strip_stopwords=strip_stopwords,
                         strip_urls=strip_urls,
                         strip_accents=strip_accents,
                         token_min_len=token_min_len,
                         preserve_case=preserve_case,
                         return_tokens=return_tokens
                        )
