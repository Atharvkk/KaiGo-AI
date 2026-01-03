import os
import threading
import time
from grpc import StatusCode
import requests
from tkinter import messagebox
import subprocess
import customtkinter as ctk
import winsound
from PIL import Image
import pygame  

dark_theme = {
    "primary": "#1E1E1E",
    "secondary": "#2D2D2D",
    "accent": "#453D9E",
    "danger": "#FF6B6B",
    "text": "#E0E0E0",
    "highlight": "#3A3A3A",
    "online": "#0DD606"
}

def check_internet_connection():
    try:
        response = requests.get("https://groq.com", timeout=5)
        return response.status_code == 200
    except:
        return False

def tcol():
 if check_internet_connection:
     return "online"     
 else:
     return "danger"

def run_script1():
    subprocess.run(["python", "permaudio.py"])
    
def run_script2():
    subprocess.run(["python","tempaudio.py"])

def run_script(mode):
    if mode == "ONLINE":
        filepath = "KaiGo_ONLINE.py"
    else:
        filepath = "KaiGo_OFFLINE.py"
    os.system(f'python "{filepath}"')

def play_audio():
    file_path = "Output/output.wav"
    if os.path.exists(file_path):
        os.system(f'start "" "{file_path}"')
    else:
        messagebox.showerror("Error", "No output audio found!")

def play_preset_quote():
    preset_path = "Output/preset.wav"
    if os.path.exists(preset_path):
        os.system(f'start "" "{preset_path}"')
    else:
        messagebox.showerror("Error", "Preset audio file not found!")

class MusicPlayer:
    def __init__(self):
        self.thread = None
        self.stop_event = threading.Event()
        pygame.mixer.init()

    def play_ambient_music(self):
        sound_path = "Misc/ambient_music.wav"
        if os.path.exists(sound_path):
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play(-1) 
            while not self.stop_event.is_set():
                time.sleep(0.1)
            pygame.mixer.music.stop()
        else:
            print("Ambient music file not found!")

    def start(self):
        if self.thread and self.thread.is_alive():
            self.stop()
        self.stop_event.clear()
        self.thread = threading.Thread(target=self.play_ambient_music, daemon=True)
        self.thread.start()

    def stop(self):
        self.stop_event.set()
        pygame.mixer.music.stop()

class KaigoAIApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kaigo AI V1.0")
        self.geometry("1000x750")
        self.resizable(True,True)
        self.music_player = MusicPlayer()
        self.music_playing = False  
        self.music_button = None    

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.main_frame = ctk.CTkFrame(self, fg_color=dark_theme["primary"])
        self.main_frame.pack(fill="both", expand=True, padx=0, pady=0)

        self.setup_ui()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def setup_ui(self):
        header_frame = ctk.CTkFrame(self.main_frame, 
                                  fg_color=dark_theme["secondary"],
                                  height=80,
                                  corner_radius=0)
        header_frame.pack(fill="x", pady=(0, 20))
        
        title_label = ctk.CTkLabel(header_frame, 
                                 text="K A I G O   A I",
                                 text_color=dark_theme["accent"],
                                 font=ctk.CTkFont(size=32, weight="bold", family="Consolas"))
        title_label.pack(side="left", padx=40, pady=20)
        
        self.connection_status = ctk.StringVar(value="Checking connection...")
        internet_label = ctk.CTkLabel(header_frame, 
                                    textvariable=self.connection_status,
                                    text_color=dark_theme[tcol()],
                                    font=ctk.CTkFont(size=14))
        internet_label.pack(side="right", padx=40)
        self.after(100, self.update_connection_status)

        content_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=40, pady=(0, 40))

        left_frame = ctk.CTkFrame(content_frame, 
                                fg_color=dark_theme["secondary"],
                                corner_radius=12)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        ctk.CTkLabel(left_frame, 
                    text="VOICE SETUP",
                    text_color=dark_theme["accent"],
                    font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(20, 15))
        
        record_buttons = [
            ("  RECORD CAREGIVER VOICE  [0]", run_script1),
            ("  RECORD USER THOUGHTS  [1]", run_script2)
        ]
        
        for text, command in record_buttons:
            btn = ctk.CTkButton(left_frame,
                              text=text,
                              command=command,
                              fg_color=dark_theme["highlight"],
                              hover_color=dark_theme["accent"],
                              text_color=dark_theme["text"],
                              font=ctk.CTkFont(size=16, weight="bold"),
                              height=60,
                              corner_radius=8)
            btn.pack(fill="x", padx=20, pady=12)

        right_frame = ctk.CTkFrame(content_frame, 
                                 fg_color=dark_theme["secondary"],
                                 corner_radius=12)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        ctk.CTkLabel(right_frame, 
                    text="AUDIO PLAYBACK",
                    text_color=dark_theme["accent"],
                    font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(20, 15))
        
        playback_buttons = [
            ("  PLAY CAREGIVER RESPONSE [5]", play_audio),
            ("  PLAY PRESET QUOTES [4]", play_preset_quote),
    
        ]
        
        for text, command in playback_buttons:
            btn = ctk.CTkButton(right_frame,
                              text=text,
                              command=command,
                              fg_color=dark_theme["highlight"],
                              hover_color=dark_theme["accent"],
                              text_color=dark_theme["text"],
                              font=ctk.CTkFont(size=16, weight="bold"),
                              height=60,
                              corner_radius=8)
            btn.pack(fill="x", padx=20, pady=12)

      
        self.music_button = ctk.CTkButton(
            right_frame,
            text="  PLAY AMBIENT MUSIC [3]",
            command=self.toggle_music,
            fg_color=dark_theme["highlight"],
            hover_color=dark_theme["accent"],
            text_color=dark_theme["text"],
            font=ctk.CTkFont(size=16, weight="bold"),
            height=60,
            corner_radius=8
        )
        self.music_button.pack(fill="x", padx=20, pady=12)

        action_frame = ctk.CTkFrame(content_frame, 
                                  fg_color=dark_theme["secondary"],
                                  corner_radius=12)
        action_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=20)
        
        ctk.CTkLabel(action_frame, 
                    text="SYSTEM ACTIONS",
                    text_color=dark_theme["accent"],
                    font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(20, 15))
        
        action_buttons = [
            ("  USAGE INSTRUCTIONS [A]", self.start_app),
            ("  RUN KAIGO AI [2]", self.run_mode_selection)
        ]
        
        for text, command in action_buttons:
            btn = ctk.CTkButton(action_frame,
                              text=text,
                              command=command,
                              fg_color=dark_theme["highlight"],
                              hover_color=dark_theme["danger"],
                              text_color=dark_theme["text"],
                              font=ctk.CTkFont(size=16, weight="bold"),
                              height=60,
                              corner_radius=8)
            btn.pack(side="left", fill="x", expand=True, padx=20, pady=10)

        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)
        content_frame.rowconfigure(0, weight=1)
        content_frame.rowconfigure(1, weight=0)

    def update_connection_status(self):
        try:
            status = "ONLINE" if check_internet_connection() else "OFFLINE"
            color = dark_theme["accent"] if status == "ONLINE" else dark_theme["danger"]
            self.connection_status.set(f"STATUS: {status}")
            for child in self.main_frame.winfo_children():
                if isinstance(child, ctk.CTkFrame) and "header" in str(child):
                    for label in child.winfo_children():
                        if isinstance(label, ctk.CTkLabel) and "STATUS" in str(label.cget("textvariable")):
                            label.configure(text_color=color)
        finally:
            self.after(5000, self.update_connection_status)

    def start_app(self):
        messagebox.showwarning("Warning","Record both caregiver and user messages before running")
        self.show_info()
        
    def show_info(self):
        instructions = [
            "1. First record the caregiver's voice",
            "2. Then record the user's thoughts",
            "3. The system will analyze emotions and content",
            "4. Processing takes ~3 minutes",
            "5. Use the ambient music while waiting",
            "6. Click RUN when ready to process"
        ]
        messagebox.showinfo("Instructions", "\n".join(instructions))

    def run_mode_selection(self):
        online = check_internet_connection()
        mode = "Online" if online else "Offline"
        messagebox.showinfo("Starting", f"Running in {mode} mode...")
        threading.Thread(target=run_script, args=(mode,), daemon=True).start()

    def toggle_music(self):
        if not self.music_playing:
            self.music_player.start()
            self.music_playing = True
            self.music_button.configure(text="  STOP AMBIENT MUSIC [3]")
        else:
            self.music_player.stop()
            self.music_playing = False
            self.music_button.configure(text="  PLAY AMBIENT MUSIC [3]")

    def on_close(self):
        self.music_player.stop()
        self.destroy()

if __name__ == "__main__":
    app = KaigoAIApp()

    app.mainloop()
