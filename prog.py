import tkinter as tk
from tkinter import ttk
from gtts import gTTS
import os
import pygame

def convert_text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    language = language_var.get()
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    root.after(1000, lambda: os.remove("output.mp3"))  # Remove the file after 1 second

# Create main application window
root = tk.Tk()
root.title("Text to Speech")

# Create text entry widget
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

# Create label for language selection
language_label = tk.Label(root, text="Select Language:")
language_label.pack()

# Create language selection combobox
language_var = tk.StringVar()
language_combobox = ttk.Combobox(root, textvariable=language_var, state="readonly", width=10)
language_combobox['values'] = ('en', 'es', 'fr', 'de', 'it')  # English, Spanish, French, German, Italian
language_combobox.current(0)
language_combobox.pack()

# Create button to convert text to speech
convert_button = tk.Button(root, text="Convert", command=convert_text_to_speech)
convert_button.pack(pady=10)

# Run the application
root.mainloop()


