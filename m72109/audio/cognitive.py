import requests
import base64
import json
import time

class CognitiveServicesPronunciationAssesment():
    # a common wave header, with zero audio length
    # since stream data doesn't contain header, but the API requires header to fetch format information, so you need post this header as first chunk for each query
    WAVE_HEADER_16K_16BIT_MONO = bytes([ 82, 73, 70, 70, 78, 128, 0, 0, 87, 65, 86, 69, 102, 109, 116, 32, 18, 0, 0, 0, 1, 0, 1, 0, 128, 62, 0, 0, 0, 125, 0, 0, 2, 0, 16, 0, 0, 0, 100, 97, 116, 97, 0, 0, 0, 0 ])
    
    def __init__(self, subscription_key, region):
        self.subscription_key = subscription_key
        self.region = region
    
    # a generator which reads audio data chunk by chunk
    # the audio_source can be any audio input stream which provides read() method, e.g. audio file, microphone, memory stream, etc.
    def __get_chunk(self, audio_source, chunk_size=1024):
        yield self.WAVE_HEADER_16K_16BIT_MONO
        while True:
            chunk = audio_source.read(chunk_size)
            if not chunk:
                break
            yield chunk
    
    def assess_pronunciation(self, audio_file, expected_transcript):
        pronAssessmentParamsJson = "{\"ReferenceText\":\"%s\",\"GradingSystem\":\"HundredMark\",\"Dimension\":\"Comprehensive\"}" % expected_transcript;
        pronAssessmentParamsBase64 = base64.b64encode(bytes(pronAssessmentParamsJson, 'utf-8'));
        pronAssessmentParams = str(pronAssessmentParamsBase64, "utf-8")

        # build request
        url = "https://%s.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-us" % self.region
        headers = { 'Accept': 'application/json',
                    'Connection': 'Keep-Alive',
                    'Content-Type': 'audio/wav; codecs=audio/pcm; samplerate=16000',
                    'Ocp-Apim-Subscription-Key': self.subscription_key,
                    'Pronunciation-Assessment': pronAssessmentParams,
                    'Transfer-Encoding': 'chunked',
                    'Expect': '100-continue' }

        audioFile = open(audio_file, 'rb')

        # send request with chunked data
        response = requests.post(url=url, data=self.__get_chunk(audioFile), headers=headers)
        audioFile.close()

        resultJson = json.loads(response.text)
        print(json.dumps(resultJson, indent=4))