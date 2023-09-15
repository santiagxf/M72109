# -*- coding: utf-8 -*-
# +
# ME72: Maestría en Métodos Cuantitativos para la Gestión y Análisis de Datos
# M72109: Analisis de Datos no Estructurados
# Universidad de Buenos Aires - Facultad de Ciencias Economicas (UBA-FCE)
# Año: 2020
# Profesor: Facundo Santiago, Javier Ignacio Garcia Fronti
# -

import torch
import numpy as np
from transformers.data.processors.utils import InputFeatures

class ClassificationDataset(torch.utils.data.Dataset):
    def __init__(self, examples, labels, tokenizer, max_length=400):
        """Un dataset de PyTorch para resolver problemas de clasificación de texto. El dataset se construye a partir de una lista de textos indicada en `examples`,
        en donde las categorias a las que pertenece cada observación pertenece está indicada en `labels`. `tokenizer` debe ser el tokenizador con el que se 
        generen los encodings del modelo.
        ."""
        self.batch_encoding = tokenizer.batch_encode_plus(list(examples), padding='longest', truncation=True, max_length=max_length, return_attention_mask=True, return_tensors = None) #return_tensors='pt' tokenizer.model_max_length
        self.batch_labels = list(labels)
        self.batch_size = len(examples)
        
        label_list = np.unique(labels)
        self.label_map = {label: i for i, label in enumerate(label_list)}

    def __getitem__(self, idx):
        inputs = {k: self.batch_encoding[k][idx] for k in self.batch_encoding}
        return InputFeatures(**inputs, label=self.label_map[self.batch_labels[idx]])

    def __len__(self):
        return self.batch_size
    
    def get_labels(self):
        """Obtiene una lista de todas las distintas categorias que se vieron en el set de datos"""
        return list(self.label_map.keys())


class RegressionDataset(torch.utils.data.Dataset):
    def __init__(self, examples, labels, tokenizer, max_length=400):
        """Un dataset de PyTorch para resolver problemas de regression de texto. El dataset se construye a partir de una lista de textos indicada en `examples`,
        en donde los valores a las que pertenece cada observación pertenece está indicado en `labels`. `tokenizer` debe ser el tokenizador con el que se 
        generen los encodings del modelo.
        ."""
        self.batch_encoding = tokenizer.batch_encode_plus(list(examples), padding='longest', truncation=True, max_length=max_length, return_attention_mask = True, return_tensors = None) #return_tensors='pt'
        self.batch_labels = list(labels)
        self.batch_size = len(examples)
        
    def __getitem__(self, idx):
        inputs = {k: self.batch_encoding[k][idx] for k in self.batch_encoding}
        return InputFeatures(**inputs, label=self.batch_labels[idx])

    def __len__(self):
        return self.batch_size