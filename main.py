
import os
from utils import *

# Set the path to your JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/juandelgado/Desktop/Juan/code-personal/creds/gcreds_speech.json"

wav_transform_flag = False
savewav_flag = False


# Usage example
m4a_file = "data/New Recording 38.m4a"
wav_file = "data/New Recording 38.wav"
if wav_transform_flag:
    convert_m4a_to_wav(m4a_file, wav_file)


# Usage example
wav_file = "data/New Recording 38.wav"
audio_data, sample_width, num_channels, sample_rate = read_wav_file(wav_file)

# Cut sound file to 10 seconds
ten_seconds = 10 * sample_rate  # 10 seconds in frames
audio_data_cut = audio_data[:ten_seconds]

# write to 
if savewav_flag:
    write_wav(audio_data_cut, sample_width, num_channels, sample_rate,ten_seconds)

# Usage example
text = transcribe_speech(audio_data_cut, sample_rate)

text_with_punctuation = add_punctuation(text)

