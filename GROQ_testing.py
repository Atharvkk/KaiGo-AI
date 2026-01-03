from groq import Groq
groq_api_key = "#"
client = Groq(api_key=groq_api_key)
human_response = "I'm scared, the world is too loud for me right now"
emotion = "fear"

prompt_sequence = [
    {"role": "system", "content": "You are a caretaker offering comforting and supportive responses."},
    {"role": "user", "content": f"My response: {human_response}, and my current emotion is: {emotion}"}
]
info = client.chat.completions.create(
    model="llama3-8b-8192",
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

print(f'Final API Response: "{apiresponse_limited}"')
