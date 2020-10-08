import os
from tqdm import tqdm
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

class CognitiveServicesExtractor():
    def __init__(self, endpoint, subscription_key, frames_path):
        self.subscription_key = subscription_key
        self.endpoint = endpoint
        self.frames_path = frames_path
        
        self.client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key));
        
    def __init_file(self, features, group_name):
        f = open(group_name + '_features.csv', 'w')
        f.write('sequence_name')
        for feature in features:
            f.write(',' + feature)
        f.write('\n')
        
        return f;
        
    def describe(self, feature):
        f=self.__init_file([feature], group_name='captions')
        frames_count=0
        for dir_, sequence_, frames_ in tqdm(os.walk(self.frames_path, )):
            for frame_ in frames_:
                file_path = os.path.join(dir_, frame_)
                sequence_name = os.path.split(dir_)[-1]
                frames_count+=1
                local_image = open(file_path, "rb")
                results = self.client.analyze_image_in_stream(local_image, visual_features=[feature], language='es')
                for caption in results.captions:
                    f.write(sequence_name, caption.text, sep=',')
                    f.write('\n')
                    break;
                local_image.close()
        
        f.close()
        print("Cuadros procesados:", frames_count, "cuadros totales.")
        
    def colors(self):
        f=self.__init_file(features=['dominant_background','dominant_foreground'], group_name='colors')
        frames_count=0
        for dir_, sequence_, frames_ in tqdm(os.walk(self.frames_path, )):
            for frame_ in frames_:
                file_path = os.path.join(dir_, frame_)
                sequence_name = os.path.split(dir_)[-1]
                frames_count+=1
                local_image = open(file_path, "rb")
                results = self.client.analyze_image_in_stream(local_image, visual_features=['color'], language='es')
                f.write(','.join([sequence_name, results.color.dominant_color_background, results.color.dominant_color_foreground]))
                f.write('\n')
                local_image.close()
        
        f.close()
        print("Cuadros procesados:", frames_count, "cuadros totales.")
    