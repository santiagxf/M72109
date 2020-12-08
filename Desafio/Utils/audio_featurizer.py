import os
import numpy as np
import pandas as pd
import librosa
import logging

from tqdm import tqdm
from yamnet.yamnet import yamnet_frames_model
from yamnet.params import Params

YAMNET_PATH = "Models/Yamnet/yamnet.h5"

class AudioFeaturizer():
    def __init__(self, yamnet_weights):
        if os.path.isfile(yamnet_weights):
            self.yamnet_weights = yamnet_weights
        else:
            raise FileNotFoundError(yamnet_weights)

    def extract_features_from_audio(self, path):
        samples, features, classes = [], [], []
        model = yamnet_frames_model(Params())
        model.load_weights(self.yamnet_weights)
        for sound in tqdm(os.listdir(path)):
            basename = os.path.splitext(sound)[0]
            extension = os.path.splitext(sound)[1]
            
            try:
                wav = librosa.load(os.path.join(path, sound), sr=16000)[0].astype(np.float32)
                
                scores, embeddings, spectrogram = model(wav)
                for feature in embeddings:
                    samples.append(basename)
                    features.append(feature)
                    
                for feature in scores:
                    classes.append(feature)
                    
            except:
                logging.error('Unable to process file: {0}'.format(sound))
                continue

        self.samples = np.asarray(samples)
        self.features = np.asarray(features)
        self.classes = np.asarray(classes)

        return self.samples, self.features

    def to_csv(self, file_name='./audio_features.csv', data='features'):
        if self.samples is None:
            logging.error('Nothing to save. Call extract_features_from_audio() first')
        else:
            if data == 'features':
                to_export = self.features
                ranger = 1025
            else:
                to_export = self.classes
                ranger = 522
                
            alldata = np.concatenate((self.samples.reshape((-1,1)),to_export), axis=1)
            df = pd.DataFrame(data=alldata, columns=['sequence_name', *range(1,ranger)])

            df.to_csv(file_name)