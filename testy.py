import argparse
import os
import numpy as np
import librosa
import librosa.display
import soundfile as sf
import matplotlib.pyplot as plt
import torch
import whisper
from sklearn.ensemble import IsolationForest
from datetime import datetime


# Load Whisper STT Model
def load_model():
    print("[+] Loading Whisper model...")
    return whisper.load_model("base")

# Extract MFCC Features
def extract_mfcc(audio, sr):
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    return mfcc

# Anomaly Detection using Isolation Forest
def detect_anomalies(mfcc):
    mfcc_mean = np.mean(mfcc, axis=1)
    clf = IsolationForest(contamination=0.1)
    result = clf.fit_predict(mfcc_mean.reshape(-1, 1))
    return result[0] == -1

# Add Adversarial Noise
def add_adversarial_noise(audio, epsilon=0.01):
    print("[!] Adding adversarial noise to the audio...")
    noise = np.sign(np.random.randn(len(audio))) * epsilon
    adversarial_audio = audio + noise
    return np.clip(adversarial_audio, -1.0, 1.0)

# Show and Save Spectrogram
def save_spectrogram(audio, sr, output_path="spectrogram.png"):
    print("[+] Saving spectrogram...")
    S = librosa.feature.melspectrogram(y=audio, sr=sr)
    S_DB = librosa.power_to_db(S, ref=np.max)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_DB, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title("Mel Spectrogram")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# Transcribe Audio using Whisper
def transcribe(model, filepath):
    try:
        result = model.transcribe(filepath)
        return result['text']
    except Exception as e:
        return f"Error: {str(e)}"

# Save Report
def save_report(filepath, transcription, is_adversarial, duration, sr, simulated):
    print("[+] Saving report...")
    report_path = "audio_report.txt"
    with open(report_path, "w") as f:
        f.write("=== Forensic Audio Analysis Report ===\n")
        f.write(f"Audio File: {filepath}\n")
        f.write(f"Duration: {duration:.2f} seconds\n")
        f.write(f"Sample Rate: {sr} Hz\n")
        f.write(f"Adversarial Simulation: {'Yes' if simulated else 'No'}\n")
        f.write(f"Manipulation Detected: {'Yes' if is_adversarial else 'No'}\n\n")
        f.write("=== Transcription ===\n")
        f.write(transcription)
    print(f"[✓] Report saved as {report_path}")

def main():
    parser = argparse.ArgumentParser(description="Forensic Audio Analyzer CLI Tool")
    parser.add_argument("audio_file", help="Path to input audio file (WAV or MP3)")
    parser.add_argument("--simulate", action="store_true", help="Simulate adversarial noise")
    args = parser.parse_args()

    # Load audio
    audio_path = args.audio_file
    if not os.path.exists(audio_path):
        print(f"[X] File not found: {audio_path}")
        return

    print("[+] Loading audio...")
    audio, sr = librosa.load(audio_path, sr=None)
    duration = librosa.get_duration(y=audio, sr=sr)
    print(f"[i] Audio Duration: {duration:.2f} seconds | Sample Rate: {sr} Hz")

    if args.simulate:
        audio = add_adversarial_noise(audio)

    temp_audio = os.path.abspath("temp_audio.wav")
    if os.path.exists(temp_audio):
        try:
            os.remove(temp_audio)
        except Exception as e:
            print(f"[!] Warning: Could not remove existing temp audio file: {str(e)}")

    # Save modified audio
    sf.write(temp_audio, audio, sr)

    # Spectrogram
    save_spectrogram(audio, sr)

    # Feature Extraction and Detection
    mfcc = extract_mfcc(audio, sr)
    is_adversarial = detect_anomalies(mfcc)
    print("[✓] Adversarial Audio Detected" if is_adversarial else "[✓] No Manipulation Detected")

    # Load model and transcribe
    model = load_model()
    print("[...] Transcribing...")
    transcription = transcribe(model, temp_audio)
    print("[✓] Transcription Complete:\n")
    print(transcription)

    # Save report
    save_report(audio_path, transcription, is_adversarial, duration, sr, args.simulate)

    # Clean up temp audio file
    try:
        if os.path.exists(temp_audio):
            os.remove(temp_audio)
            print("[✓] Temporary audio file removed.")
    except Exception as e:
        print(f"[!] Warning: Could not remove temp audio file: {str(e)}")

    print("[✓] Forensic Audio Analysis Completed.")
    print("[✓] All tasks completed successfully.")
    print("[✓] Exiting...")

if __name__ == "__main__":
    main()
