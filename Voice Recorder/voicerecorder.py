from tkinter import *
from tkinter import messagebox
import sounddevice as sd
import wavio as wv
from tkinter.filedialog import askdirectory

time =int(input("Enter Time In Second You Want To Record : "))
freq = 44100  
sec = time


def savefile():
    print("Recording.............")
    recording = sd.rec(sec * freq, samplerate=freq, channels=2)
    sd.wait()
    wv.write("recording.wav", recording , freq , sampwidth=2)
    print("Recording Finished")

savefile()