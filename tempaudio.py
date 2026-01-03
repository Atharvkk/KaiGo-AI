import os
import time
from turtle import window_width
import pyaudio
import wave
from tkinter import Tk, Label, Button, messagebox
import threading
import customtkinter

def record_audio():
    chunk = 1024  
    sample_format = pyaudio.paInt16  
    channels = 1  
    fs = 44100  
    seconds = 20 

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

    audio_path = r"D:/Kaigo AI/USERInput/recorded_audio.wav"
    with wave.open(audio_path, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved at {audio_path}")
def start_recording():
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()

window = customtkinter.CTk()
window.title("User Input")
window.geometry("300x100")
window.resizable(0,0)
window.configure(bg="#1F1F1F")

start_button = customtkinter.CTkButton(window, text="Speak, Express your thoughts:", command=start_recording)
start_button.pack(pady=20)

window.mainloop()
