import pandas as pd
import os
from tkinter import filedialog as fd
from tkinter import messagebox
"""import speech_recognition as sr
import pyaudio
r= sr.Recognizer()

with sr.Microphone() as source:
    print("you may speak now")
    audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        print("you said:{}".format(text))
    except:
        print("sorry i could not hear you")"""



global keyfile
keyfile = fd.askopenfilename()
ext = os.path.splitext(keyfile)[-1].lower()
if ext == ".csv":
    print ("valid file")
    messagebox.showinfo("information", "valid file")
else:
    print("non valid")
    messagebox.showinfo("information", "in valid file")
df= pd.read_csv(keyfile)
print(df.head())
name=[]
price=[]
for key,value in df.iteritems():
    if key =='Candidate ID':
        name.append(value)
    elif key == 'TC ID':
        price.append(value)
print(*name)
print(*price)

        
        
      
