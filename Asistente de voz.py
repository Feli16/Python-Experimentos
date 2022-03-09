from gtts import gTTS
from playsound import playsound
import os
import random
import speech_recognition as sr

def speal(text):
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save("speak.mp3")
    playsound("speak.mp3", True)
    os.remove("speak.mp3")

r = sr.Recognizer()
while(1):
    try:

         with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            MyText = r.recognize_google(audio, language="en")
            MyText = MyText.lower()
            print("Did you say"+MyText)

    except sr.RequestError as e:
        print("could not request results;{0}".format(e))

    except sr.UnknownValueError: 
        
        greetings = ["hello dodo","ok dodo","hi dodo", "hey dodo"]
        greetings_rep = ["hi i am your Assistant, how can i help you?", "ohh... , so its my turn to help you",
            "i am glad to serve , so what my task?"]
    

    if MyText in greetings:
        rep = random.choice(greetings_rep)
        speak(rep)


