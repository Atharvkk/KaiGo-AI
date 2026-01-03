#Emotion -DistilroBERTa-base
from transformers import pipeline
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)
text = "You are so kind!"
result = classifier(text)
inner_list = result[0]
#print(result)            #Use for debug
highest_score = max(inner_list, key=lambda x: x['score'])
uncap=(highest_score["label"])
temp=str(uncap)
temp=temp.capitalize()
emotion=temp
print(emotion)
