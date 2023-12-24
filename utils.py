from pydub import AudioSegment
import wave
from google.cloud import speech_v1p1beta1 as speech
import string



# transform to wav
def convert_m4a_to_wav(m4a_file, wav_file):
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    audio.export(wav_file, format="wav")

# split into 10MB chunks
def read_wav_file(wav_file):
    with wave.open(wav_file, 'rb') as wav:
        # Get the audio file properties
        sample_width = wav.getsampwidth()
        num_channels = wav.getnchannels()
        sample_rate = wav.getframerate()
        num_frames = wav.getnframes()

        # Read the audio data
        audio_data = wav.readframes(num_frames)

    return audio_data, sample_width, num_channels, sample_rate

# Write 10 seconds to file
def write_wav(audio_data, sample_width, num_channels, sample_rate,time):
    with wave.open('data/New Recording 38_10s.wav', 'wb') as wav_file:
        wav_file.setparams((num_channels, sample_width, sample_rate, time, "NONE", "Uncompressed"))
        wav_file.writeframes(audio_data)


# call the google speech api
def transcribe_speech(audio_data, sample_rate):
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code="es-US",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        for alt in result.alternatives:
            print("Transcript: {}".format(alt.transcript))
    return alt.transcript


def add_punctuation(text):
    # Remove leading/trailing whitespaces
    text = text.strip()

    # Add punctuation at the end of the text if it doesn't already have one
    if text[-1] not in string.punctuation:
        text += "."

    return text
