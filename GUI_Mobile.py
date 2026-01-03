import os
import threading
import time
import requests
from tkinter import messagebox
import subprocess
import customtkinter as ctk
from PIL import Image
import pygame

import tkfontawesome

dark_theme = {
    "primary": "#1A1A1A",
    "secondary": "#252525",
    "accent": "#6A67FF",
    "danger": "#FF6B6B",
    "text": "#F5F5F5",
    "highlight": "#333333",
}


def simulate_recording():
    """Placeholder function to simulate an audio recording process."""
    print("Starting recording simulation...")
    # In a real app, this would be your audio recording logic.
    time.sleep(4) # Simulate a 4-second recording
    print("Recording finished.")
    return True

def simulate_running_ai():
    """Placeholder function to simulate running the AI analysis."""
    print("Starting AI analysis simulation...")
    # This would trigger your KaiGo_ONLINE.py or KaiGo_OFFLINE.py scripts.
    time.sleep(3) # Simulate a 3-second analysis
    print("AI analysis complete.")
    # For the demo, we'll create a dummy output file if it doesn't exist.
    if not os.path.exists("Output/output.wav"):
        if not os.path.exists("Output"):
            os.makedirs("Output")
        # Creating a dummy file to ensure playback works for the demo.
        with open("Output/output.wav", "w") as f:
            f.write("dummy file")
    return True

def play_audio():
    """Plays the generated audio file."""
    file_path = "Output/output.wav"
    if os.path.exists(file_path):
        # This command works on Windows. You may need different commands for macOS/Linux.
        os.system(f'start "" "{file_path}"')
    else:
        messagebox.showerror("Error", "No output audio found! Please record and run the analysis first.")

# --- Main Application ---
class KaigoAIApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Kaigo AI")
        self.geometry("450x800")
        self.minsize(400, 700)

        ctk.set_appearance_mode("dark")

        self.main_frame = ctk.CTkFrame(self, fg_color=dark_theme["primary"])
        self.main_frame.pack(fill="both", expand=True)

        self.setup_ui()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def setup_ui(self):
        # --- Top Info Button ---
        info_icon = tkfontawesome.icon_to_image("info-circle", fill=dark_theme["text"], scale_to_height=24)
        self.info_button = ctk.CTkButton(
            self.main_frame,
            text="",
            image=info_icon,
            command=self.show_info,
            fg_color="transparent",
            hover_color=dark_theme["highlight"],
            width=40,
            height=40
        )
        self.info_button.pack(anchor="ne", padx=10, pady=10)

        # --- Main Content Frame ---
        content_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, pady=20)

        # --- Status Label ---
        self.status_label = ctk.CTkLabel(content_frame, text="Press the microphone to start", font=ctk.CTkFont(size=16), text_color=dark_theme["text"])
        self.status_label.pack(pady=(20, 30))

        # --- Circular Record Button ---
        mic_icon = tkfontawesome.icon_to_image("microphone", fill=dark_theme["text"], scale_to_height=80)
        self.record_button = ctk.CTkButton(
            content_frame,
            text="",
            image=mic_icon,
            command=self.record_and_run_thread,
            fg_color=dark_theme["accent"],
            hover_color="#5855D6",
            width=180,
            height=180,
            corner_radius=90 # This makes the button circular
        )
        self.record_button.pack(pady=20)

        # --- Call for Support Button ---
        call_icon = tkfontawesome.icon_to_image("phone", fill=dark_theme["text"], scale_to_height=32)
        self.call_button = ctk.CTkButton(
            content_frame,
            text="Call for Support",
            image=call_icon,
            command=self.call_support,
            fg_color=dark_theme["secondary"],
            hover_color=dark_theme["highlight"],
            font=ctk.CTkFont(size=18, weight="bold"),
            height=70,
            corner_radius=12
        )
        self.call_button.pack(fill="x", padx=40, pady=20)

        # --- Play Output Button ---
        play_icon = tkfontawesome.icon_to_image("play", fill=dark_theme["text"], scale_to_height=32)
        self.run_button = ctk.CTkButton(
            content_frame,
            text="Play Generated Audio",
            image=play_icon,
            command=play_audio,
            fg_color=dark_theme["secondary"],
            hover_color=dark_theme["highlight"],
            font=ctk.CTkFont(size=18, weight="bold"),
            height=70,
            corner_radius=12
        )
        self.run_button.pack(fill="x", padx=40, pady=10)

        # --- Caregiver UID Entry ---
        uid_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        uid_frame.pack(side="bottom", fill="x", padx=40, pady=20)
        
        ctk.CTkLabel(uid_frame, text="Caregiver UID", text_color=dark_theme["text"]).pack(anchor="w")
        self.uid_entry = ctk.CTkEntry(
            uid_frame,
            placeholder_text="Enter UID...",
            height=50,
            font=ctk.CTkFont(size=16),
            corner_radius=10
        )
        self.uid_entry.pack(fill="x")

    def record_and_run_thread(self):
        """Starts the recording and analysis process in a separate thread to keep the UI responsive."""
        self.record_button.configure(state="disabled")
        threading.Thread(target=self.record_and_run, daemon=True).start()

    def record_and_run(self):
        """The core logic for recording, running AI, and updating the UI."""
        # Step 1: Recording
        self.status_label.configure(text="Recording...")
        self.record_button.configure(fg_color=dark_theme["danger"]) # Change color to indicate recording
        
        recording_success = simulate_recording()
        
        if not recording_success:
            self.status_label.configure(text="Recording failed. Please try again.")
            self.record_button.configure(state="normal", fg_color=dark_theme["accent"])
            return

        # Step 2: Auto-run AI analysis
        self.status_label.configure(text="Analyzing audio...")
        self.record_button.configure(fg_color=dark_theme["highlight"]) # Change color for processing
        
        analysis_success = simulate_running_ai()

        # Step 3: Final state
        if analysis_success:
            self.status_label.configure(text="Analysis complete. Press Play to listen.")
        else:
            self.status_label.configure(text="Analysis failed. Please try again.")
        
        self.record_button.configure(state="normal", fg_color=dark_theme["accent"])

    def call_support(self):
        """Placeholder for the call support functionality."""
        messagebox.showinfo("Support", "Connecting to support...\n(This would launch a call or chat.)")

    def show_info(self):
        """Displays the information panel."""
        info_text = (
            "Kaigo AI - Simplified Interface\n\n"
            "1. Press the large microphone button to record audio.\n"
            "2. The app will automatically analyze the audio after recording.\n"
            "3. Press 'Play Generated Audio' to hear the result.\n"
            "4. Use 'Call for Support' to connect with help."
        )
        messagebox.showinfo("Information", info_text)

    def on_close(self):
        """Handles window closing."""
        self.destroy()

if __name__ == "__main__":
    # Pygame is not used for music in this version, so initialization is removed.
    app = KaigoAIApp()
    app.mainloop()
