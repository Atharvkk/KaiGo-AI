#Whisper Speech to Text
import time #Benchmarking purposes
start_time = time.time()
import whisper
model=whisper.load_model("medium")
out=model.transcribe('D:/Kaigo AI/USERInput/recorded_audio.wav')
#out['text'] useful part of dict()
transcription=out['text']
#print(transcriptBion) #Hash in main file

#Benchmark times:26min audio clip: 126.5s with 99% 4070m GPU usage 
#22% UHD Graphics Usage [4070m entirely allocated to temp AI/ML tasks]
#VRAM: 7.3/8 GiB

#Emotion -DistilroBERTa-base
from transformers import pipeline
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)
text = transcription
result = classifier(text)
inner_list = result[0]
#print(result)            #Use for debug
highest_score = max(inner_list, key=lambda x: x['score'])
uncap=(highest_score["label"])
temp=str(uncap)
temp=temp.capitalize()
emotion=temp
#print(emotion)

#Emotions: PreSet Quotes/Responses to cover up processing times **IMPLEMENT Parallel processing Libs
#If emotion-sadness
import random
sr_sadness=random.randint(1,10)
if sr_sadness==1:
    sr_sadness="Its alright, keep walking through the storm"
elif sr_sadness==2:
    sr_sadness="You are not a drop in the ocean. You are the entire ocean in a drop."
elif sr_sadness==3:
    sr_sadness="You are Different, not less"
elif sr_sadness==4:
    sr_sadness="Your uniqueness is your strength. Embrace it."
elif sr_sadness==5:
    sr_sadness="It's okay to be different. It's okay to be you"
elif sr_sadness==6:
    sr_sadness="The world needs your voice. Don't be afraid to use it"
elif sr_sadness==7:
    sr_sadness="You are enough just as you are"
elif sr_sadness==8:
    sr_sadness="In a world where you can be anything, be kind."
elif sr_sadness==9:
    sr_sadness="Your differences are what make you special."
elif sr_sadness==10:
    sr_sadness="Believe in yourself and all that you are."

#If emotion-Fear 
import random
sr_fear=random.randint(1,10)
if sr_fear==1:
    sr_fear="It's okay to be scared. It means you're about to do something really brave."
elif sr_fear==2:
    sr_fear="You are stronger than you think, and braver than you feel."
elif sr_fear==3:
    sr_fear="You are Different, not less"
elif sr_fear==4:
    sr_fear="In the midst of chaos, there is always a calm center within you."
elif sr_fear==5:
    sr_fear="Your feelings are valid, and it's okay to take your time."
elif sr_fear==6:
    sr_fear="Courage doesn't mean you don't get afraid. Courage means you don't let fear stop you"
elif sr_fear==7:
    sr_fear="Every step you take, no matter how small, is a step toward overcoming your fears."
elif sr_fear==8:
    sr_fear="It's okay to ask for help. You are not weak; you are wise"
elif sr_fear==9:
    sr_fear="Remember, it's just a moment. This too shall pass."
elif sr_fear==10:
    sr_fear="You have faced challenges before and emerged stronger. You can do it again"

#If emotion-disgust
import random
sr_disgust=random.randint(1,10)
if sr_disgust==1:
    sr_disgust="Discomfort is a part of life, but it doesn't define you."
elif sr_disgust==2:
    sr_disgust="It's okay to feel what you feel. Your emotions are valid."
elif sr_disgust==3:
    sr_disgust="You have the right to set boundaries and protect your space."
elif sr_disgust==4:
    sr_disgust="It's okay to walk away from what doesn't serve you"
elif sr_disgust==5:
    sr_disgust="Your feelings of disgust are a signal; listen to them and honor your needs."
elif sr_disgust==6:
    sr_disgust="You are allowed to feel uncomfortable. It's a natural part of being human."
elif sr_disgust==7:
    sr_disgust="You are not alone in feeling this way; many people experience similar feelings."
elif sr_disgust==8:
    sr_disgust="It's okay to ask for help. You are not weak; you are wise"
elif sr_disgust==9:
    sr_disgust="Your comfort matters. Prioritize what makes you feel safe and at ease."
elif sr_disgust==10:
    sr_disgust="Remember, it's okay to express your feelings. You deserve to be heard."

#FinalSetResponse (Based on emotion)
if emotion=="Disgust":
    fsr=sr_disgust
elif emotion=="Fear":
    fsr=sr_fear
elif emotion=="Surprise":
    fsr=sr_fear
elif emotion=="Sadness":
    fsr=sr_sadness
else:
    fsr="Its alright,"
    
#TTS-PreSetResponses
from IPython.display import Javascript
from base64 import b64decode
from IPython.display import Audio, display
import torch
from TTS.api import TTS
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
text = fsr
tts.tts_to_file(text=text, speaker_wav="D:\Kaigo AI\CaregiverInput\permanent_audio.wav", language="en", file_path="D:/Kaigo AI/Output/preset.wav")
display(Audio("preset.wav", autoplay=True))

from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch

# Check if GPU is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("GPU is available and being used.")
else:
    device = torch.device("cpu")
    print("GPU is not available, using CPU instead.")

# Load the model and tokenizer
model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B").to(device)  # Move model to device
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")

# Example input
human_prompt = transcription 
emotion = emotion

gptprompt = f"What is something a caretaker comforting an autistic individual would say in response to '{human_prompt}', while feeling {emotion}?"
inputs = tokenizer(gptprompt, return_tensors="pt").to(device)
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_length=100,
        num_return_sequences=1,
        temperature=0.4,
        top_k=50,
        top_p=0.95,
        do_sample=True,       
    )
realop = tokenizer.decode(outputs[0], skip_special_tokens=True)
realop = str(realop)

#TTS-AI
from IPython.display import Javascript
from base64 import b64decode
from IPython.display import Audio, display
import torch
from TTS.api import TTS
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
text = realop
tts.tts_to_file(text=text, speaker_wav="D:\Kaigo AI\CaregiverInput\permanent_audio.wav", language="en", file_path="D:/Kaigo AI/Output/output.wav")
display(Audio("output.wav", autoplay=True))

result = sum(range(1000000))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")