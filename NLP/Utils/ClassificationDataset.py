import torch
import numpy as np
from transformers.data.processors.utils import InputFeatures

class ClassificationDataset(torch.utils.data.Dataset):
    def __init__(self, examples, labels, tokenizer):
        """Un dataset de PyTorch para resolver problemas de clasificación de texto. El dataset se construye a partir de una lista de textos indicada en `examples`,
        en donde las categorias a las que pertenece cada observación pertenece está indicada en `labels`. `tokenizer` debe ser el tokenizador con el que se 
        generen los encodings del modelo.
        ."""
        self.batch_encoding = tokenizer.batch_encode_plus(list(examples), pad_to_max_length=True, return_attention_mask = True, return_tensors = None) #return_tensors='pt'
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
        