# 🎙️ ForensicWhisper – Audio Forensics CLI Tool

**ForensicWhisper** is a Python-based CLI tool for forensic analysis of audio files. It detects adversarial noise, extracts features, generates spectrograms, and performs transcription using OpenAI's Whisper model. Ideal for digital forensics, audio integrity validation, and research.

---

## ✨ Features

- 🔍 **Anomaly Detection**: Uses Isolation Forest to detect adversarial manipulation in audio.
- 🗣️ **Speech-to-Text**: Transcribe audio using OpenAI’s Whisper model.
- 📊 **Spectrogram Visualization**: Creates mel spectrograms for audio insights.
- 🧪 **Adversarial Simulation**: Simulate noise-based attacks on clean audio.
- 📄 **Auto-Generated Report**: Comprehensive analysis saved in `audio_report.txt`.

---

## 🧰 Requirements

- Python 3.7 or higher
- `ffmpeg` installed and added to system `PATH`
- Python packages in `requirements.txt`

---


## 🚀 Getting Started

1. **📥 Clone the repository**
   ```bash
   git clone https://github.com/Kisalay0298/speech-to-text-model.git
   cd speech-to-text-model

2. **📦 Install the requirements**
   ```bash
   pip install -r requirements.txt

3. **🎯 Run the code**
   ```bash
   python testy.py example_audio.mp3

## 📁 Project Structure

<pre>
   . 
   ├── testy.py 
   ├── spectrogram.png 
   ├── audio_report.txt 
   ├── example_audio.mp3 
   ├── requirements.txt 
   └── README.md 
</pre>





