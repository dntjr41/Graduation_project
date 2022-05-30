import os
from . import inference
#from spleeter.separator import Separator

"""
print(inference.parser)
print(inference.checkpoint_path)
inference.checkpoint_path = 'Wav2Lip/checkpoints/wav2lip.pth'
inference.face = 'D:/SimSwap/SimSwap/output/demo.mp4'
inference.audio = 'D:/SimSwap/SimSwap/output/demoa.wav'
inference.pads = [0, 20, 0, 0]
inference.resize_factor = 2
"""

vid_path = 'D:/Unity Project/Unity-Study/Flutter/assets/demo.mp4'
wav2_path = 'D:/Unity Project/Unity-Study/Flutter/assets/result_voice.mp4'
aud_path = './demo_file/voice2.wav'
spleeter_wav_path = "./output/after.wav"

"""
def get_stems(filePath, fileSavePath):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(filePath, fileSavePath, codec="wav", bitrate="128k")

def set_path(vid, aud):
    video_path = vid
    audio_path = aud
"""

def wav2_main(video_path, audio_path):
    #get_stems(audio_path, spleeter_wav_path)
    print(video_path, audio_path)
    inference.convert(video_path, audio_path)


def wav_test():
    wav2_main(vid_path,aud_path)
