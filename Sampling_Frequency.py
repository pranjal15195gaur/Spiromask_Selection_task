import librosa

# Load the audio file
audio_file = 'Breathing_Audio.wav'
y, sr = librosa.load(audio_file, sr=None)

# sr will contain the sampling rate of the audio file
print("Sampling rate:", sr)
