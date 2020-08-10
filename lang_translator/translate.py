import gtts
from textblob import TextBlob
import speech_recognition as sr 
import playsound

def translate(filename,org_lang="hi",dest_lang="en"):
    recogniser = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recogniser.record(source)
    text =recogniser.recognize_google(audio,language=org_lang)
    if not org_lang==dest_lang:
        text= TextBlob(text)
        text=str(text.translate(to=dest_lang))
    speaker = gtts.gTTS(text,lang=dest_lang)
    speaker.write_to_fp(audio)
    return text,speaker
