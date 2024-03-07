# Breathing Audio Analysis Project

Welcome to the Breathing Audio Analysis Project! This project aims to analyze breathing patterns by recording breathing sounds through a headset earphone placed inside a mask, and then processing the audio to extract relevant information.

## Mini Project Description

### Recording Setup
For this mini project, I utilized a high-quality headset earphone with an integrated microphone. The microphone was strategically placed inside a N95 mask, ensuring optimal capture of breathing sounds. I wore the mask and connected the headset earphone to my laptop to record the audio.

### Sampling Rate Determination
After recording the breathing sounds, I analyzed the audio file to determine its sampling rate. By inspecting the audio properties, I found that the sampling rate of the recorded audio was 44.1 kHz.

### Filtering
To filter out higher frequencies in the recorded audio, I employed a digital signal processing tool. Using a low-pass filter with a cutoff frequency of 4 kHz, I effectively removed unwanted high-frequency noise while preserving the breathing sounds.

### Frequency Range Analysis
After filtering the audio, I conducted a frequency analysis to identify the range in which the breathing information is present. Through spectral analysis, I determined that the breathing sounds predominantly occupy the frequency range between 50 Hz and 200 Hz.
