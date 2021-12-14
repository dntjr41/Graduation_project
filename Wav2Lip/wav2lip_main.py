import inference
from spleeter.separator import Separator

"""
print(inference.parser)
print(inference.checkpoint_path)
inference.checkpoint_path = 'Wav2Lip/checkpoints/wav2lip.pth'
inference.face = 'D:/SimSwap/SimSwap/output/demo.mp4'
inference.audio = 'D:/SimSwap/SimSwap/output/demoa.wav'
inference.pads = [0, 20, 0, 0]
inference.resize_factor = 2
"""

video_path = "D:/SimSwap/SimSwap/output/demo.mp4"
audio_path = "D:/SimSwap/SimSwap/output/demoa.wav"

spleeter_wav_path = "D:/SimSwap/SimSwap/output/after.wav"


def get_stems(filePath, fileSavePath):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(filePath, fileSavePath, codec="wav", bitrate="128k")


def set_path(vid, aud):
    video_path = vid
    audio_path = aud

get_stems(audio_path, spleeter_wav_path)
inference.convert(video_path, spleeter_wav_path)

