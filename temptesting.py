from IPython.display import Javascript
from base64 import b64decode
from IPython.display import Audio, display
import torch
from TTS.api import TTS
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
text = "HELLO KIDS"#apiresponse_limited
tts.tts_to_file(text=text, speaker_wav="D:\Kaigo AI\KaiGoSourceCode\Recording (15).mp3", language="en", file_path="output.wav")
display(Audio("output.wav", autoplay=True))
