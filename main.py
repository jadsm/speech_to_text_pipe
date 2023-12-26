
import os
from utils import *

# Set the path to your JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/juandelgado/Desktop/Juan/code-personal/creds/gcreds_speech.json"

wav_transform_flag = False
savewav_flag = False
batch_size = 30

# Usage example
m4a_file = "data/New Recording 38.m4a"
wav_file = "data/New Recording 38.wav"
if wav_transform_flag:
    convert_m4a_to_wav(m4a_file, wav_file)


# Usage example
wav_file = "data/New Recording 38.wav"
audio_data, sample_width, num_channels, sample_rate = read_wav_file(wav_file)

T = ""
Tp = ""

for i in range(0, len(audio_data), sample_rate * batch_size):

    # Cut sound file to x seconds
    audio_data_cut = audio_data[i:i+batch_size * sample_rate]

    # write to 
    if savewav_flag:
        write_wav(audio_data_cut, sample_width, num_channels, sample_rate, sample_rate * batch_size)

    # Usage example
    text = transcribe_speech(audio_data_cut, sample_rate)

    text_with_punctuation = add_punctuation(text)

    # add to text
    Tp += text_with_punctuation
    T += " "+text

T = add_punctuation(T)
