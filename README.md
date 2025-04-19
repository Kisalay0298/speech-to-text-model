# 🎙️ ForensicWhisper – Audio Forensics CLI Tool

**ForensicWhisper** is a Python-based CLI tool that performs forensic analysis on audio files. It detects adversarial noise, extracts audio features, generates spectrograms, and performs transcription using OpenAI's Whisper model. Ideal for digital forensics, audio integrity validation, and research purposes.

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

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/forensicwhisper.git
   cd forensicwhisper

## 📁 Project Structure

1. **Clone the repository**
   .tree -L 1 -I "__pycache__"





