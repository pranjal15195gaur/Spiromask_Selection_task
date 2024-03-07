import numpy as np
from scipy import signal
import soundfile as sf

# Load the audio file
audio_file = 'Breathing_Audio.wav'
data, samplerate = sf.read(audio_file)

# Define the cutoff frequency (in Hz) to trim higher frequencies
cutoff_frequency = 4000  # Adjust this value according to your requirements

# Design a low-pass filter with a cutoff frequency
b, a = signal.butter(4, cutoff_frequency, 'low', fs=samplerate)

# Apply the filter to the audio data
filtered_data = signal.lfilter(b, a, data)

# Save the filtered audio to a new file
filtered_audio_file = 'filtered_audio_file.wav'
sf.write(filtered_audio_file, filtered_data, samplerate)
