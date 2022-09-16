import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()

voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine. setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
     
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        # said = ""

        try:
            said = r.recognize_google(audio, language='es-ES')
            said = said.lower()
        except sr.RequestError:
            speak('Lo siento, parece que estoy teniendo problemas...')
            print("API era inaccesible o no respondía" + said)
        except sr.UnknownValueError:
            speak('Lo siento, no te entiendo, motomami')
            print("Incapaz de reconocer el habla" + said)

    return said