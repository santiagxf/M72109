import os
import numpy as np
import pandas as pd
import librosa
import logging

from tqdm import tqdm
from yamnet.yamnet import yamnet_frames_model
from yamnet.params import Params

YAMNET_PATH = "Models/yamnet.h5"

def class AudioFeaturizer():
    def __init__(self, yamnet_weights):
        if os.path.isfile(yamnet_weights):
            self.yamnet_weights = yamnet_weights
        else:
            raise FileNotFoundError(yamnet_weights)

    def extract_features_from_audio(self, path):
        samples, features = [], []
        model = yamnet_frames_model(Params())
        model.load_weights(YAMNET_PATH)
        for sound in tqdm(os.listdir(path)):
            wav = librosa.load(os.path.join(path, sound), sr=16000)[0].astype(np.float32)

            for feature in model(wav)[1]:
                samples.append(os.path.splitext(sound)[0])
                features.append(feature)
        self.samples = np.asarray(samples)
        self.features = np.asarray(features)

        return self.samples, self.features

    def audio_features_to_csv(self, file_name='./audio_features.csv'):
        if self.samples:
            alldata = np.concatenate((samples.reshape((-1,1)),features), axis=1)
            df = pd.DataFrame(data=alldata, columns=['sequence_name', *range(1,1025)])

            df.to_csv(file_name)
        else:
            logging.error('Nothing to save. Call extract_features_from_audio first')