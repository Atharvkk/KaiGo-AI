#Whisper Speech to Text
import time #Benchmarking purposes
start_time = time.time()
import whisper
model=whisper.load_model("medium")
out=model.transcribe('D:/Kaigo AI/USERInput/recorded_audio.wav')
#out['text'] useful part of dict()
transcription=out['text']
#print(transcription) #Hash in main file

#Benchmark times:26min audio clip: 126.5s with 99% 4070m GPU usage 
#22% UHD Graphics Usage [4070m entirely allocated to temp AI/ML tasks]
#VRAM: 7.3/8 GiB

import torch
device = "cuda" if torch.cuda.is_available() else "cpu"

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

#Emotions: PreSet Quotes/Responses to cover up processing times **IMPLEMENT Parallel processing Libs to ensure that these play WHILE background processing is occurring
#Avg. Processing time: 3s, average play time, ~4s
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
    fsr="Its alright,you are safe, no-one can harm you when you are with me..."
    
#TTS-PreSetResponses
from IPython.display import Javascript
from base64 import b64decode
from IPython.display import Audio, display
import torch
from TTS.api import TTS
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
text = fsr
tts.tts_to_file(text=text, speaker_wav="D:/Kaigo AI/CaregiverInput/permanent_audio.wav", language="en", file_path="D:/Kaigo AI/Output/preset.wav")
display(Audio("preset.wav", autoplay=True))


#LLAMA_LLM from GROQ
from groq import Groq
groq_api_key = "#"
client = Groq(api_key=groq_api_key)
human_response = transcription
emotion = emotion

prompt_sequence = [
    {"role": "system", "content": "You are a caretaker offering comforting and supportive responses."},
    {"role": "user", "content": f"My response: {human_response}, and my current emotion is: {emotion}"}
]
info = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=prompt_sequence,
    temperature=0.8,  
    max_tokens=500,
    top_p=1,
    stream=True,
    stop=None,
)

apiresponse = ""

for chunk in info:
    content = chunk.choices[0].delta.content
    if content:  
        apiresponse += content

response_words = apiresponse.split()
apiresponse_limited = " ".join(response_words[:200])

#print(f'Final API Response: "{apiresponse_limited}"')


#TTS-AI
from IPython.display import Javascript
from base64 import b64decode
from IPython.display import Audio, display
import torch
from TTS.api import TTS
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
text = apiresponse_limited
tts.tts_to_file(text=text, speaker_wav="D:/Kaigo AI/CaregiverInput/permanent_audio.wav", language="en", file_path="D:/Kaigo AI/Output/output.wav")
display(Audio("output.wav", autoplay=True))

result = sum(range(1000000))
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.4f} seconds")
