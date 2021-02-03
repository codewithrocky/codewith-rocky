import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioSTRING, lang='en')
    tts.save("audio.mp3 ")
    os.system("mp321 audio.mp3 ")

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something! ")
        audio = r.listen(source)


        data = ""
        try:
            data = r.recognize_google(audio)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition; {0}".format(e))

        return data

def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.spilt(" ")
        location = data[2]
        speak("Hold on Rocky, I will show you where " + location + " is. ")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


time.sleep(2)
speak("HI Rocky, what can i do for you?")
while 1:
    data = recordAudio()
    jarvis(data)



