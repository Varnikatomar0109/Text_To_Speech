from gtts import gTTS
import os
from tkinter import *
root= Tk()
canvas= Canvas(root,width=400,height=300)
canvas.pack()

def texttospeech():
    text=entry.get()
    language='en'
    output=gTTS(text=text,lang=language,slow=False)
    output.save("result.mp3")
    os.system("start result.mp3")

entry = Entry(root)
canvas.create_window(200,180,window=entry)

button =Button(text="start",command=texttospeech) 
canvas.create_window(200,250,window=button)

root.mainloop()
