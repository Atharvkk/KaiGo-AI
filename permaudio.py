import os
import time
import pyaudio
import wave
from tkinter import Tk, Label, Button, messagebox
import threading
import customtkinter as ctk

def display_script():
    script_path = r"D:/Kaigo AI/script.txt"
    if os.path.exists(script_path):
        with open(script_path, 'r') as file:
            script_content = file.read()
    else:
        script_content = "Script file not found."
    script_label.configure(text=script_content)

def record_audio():
    chunk = 1024  
    sample_format = pyaudio.paInt16  
    channels = 1 
    fs = 44100  
    seconds = 75  

    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []

    messagebox.showinfo("Recorder","Recording...")
    for _ in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
        
    messagebox.showinfo("Recorder","Recording finished")
    stream.stop_stream()
    stream.close()
    p.terminate()
    audio_path = r"D:/Kaigo AI/CareGiverInput/permanent_audio.wav"
    with wave.open(audio_path, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved at {audio_path}")
def start_recording():
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()

window = ctk.CTk()
window.title("Record Audio with Script")
window.geometry("600x750")

script_label = ctk.CTkLabel(window, text="Loading script...", wraplength=400, justify="left")
script_label.pack(pady=20)

start_button = ctk.CTkButton(window, text="Start Recording", command=start_recording)
start_button.pack(pady=20)

display_script()

window.mainloop()
