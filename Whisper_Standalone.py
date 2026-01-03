#Whisper Speech to Text
import time #Benchmarking purposes
start_time = time.time()
import whisper
model=whisper.load_model("medium")
out=model.transcribe('D:\Kaigo AI\KaiGoSourceCode\output.wav')
#out['text'] useful part
transcription=out['text']
print(transcription) #Hash in main file

#Benchmark times:26min audio clip: 126.5s with 99% 4070m GPU usage 
#22% UHD Graphics Usage [4070m entirely allocated to temp AI/ML tasks]
#VRAM: 7.3/8 GiB
result = sum(range(1000000))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")
