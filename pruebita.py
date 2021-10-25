#pip install gTTS
from gtts import gTTS
import os

def load(fileName = "message", language = "es", slow = False, tld = "com"):
    file = fileName + ".txt"
    name = fileName + ".mp3"

    f = open(file)
    mytext = f.read()
    f.close()
    
    myobj = gTTS(text = mytext, tld = tld, lang = language, slow = slow)

    myobj.save(name)
    return name

def play(name):
    os.system(name)

def a(*args):
    [print(i) for i  in args]

args = [1, 2, 3]

a(*args)

# pip install SpeechRecognition 
# pip install pipwin
# py -m pipwin install pyaudio

import speech_recognition as sr
import webbrowser as wb

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
  
import speech_recognition as sr
  
mic_name = "Micrófono (Realtek High Definition Audio)"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()

for i, microphone_name in enumerate(mic_list):
    if  mic_name == microphone_name:
        device_id = i

with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                        chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Say Something")
    audio = r.listen(source)
    try:
        try:
            text = r.recognize_google(audio, language = 'es-CL', show_all = True )
        except:
            text = r.recognize_sphinx(audio, language = 'en-IN', show_all = True )
        print("I think you said '" + r.recognize_google(audio) + "'")
        f_text='https://www.google.co.in/search?q=' + text
        wb.get(chrome_path).open(f_text)
    except:
        pass