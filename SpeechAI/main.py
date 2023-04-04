import speech_recognition as sr
from gtts import gTTS
import os

def perintah():
    mendengar = sr.Recognizer()
    with sr.Microphone() as source:
        print('Mendengarkan...')
        audio = mendengar.listen(source, phrase_time_limit=5)
        try:
            print('Diterima....')
            dengar = mendengar.recognize_google(audio, language='id-ID')
            print(dengar)
        except:
            pass
        return dengar
    
def speakAI(self):
    text = (self)
    bahasa = 'id'
    namaFile = 'audio.mp3'
    def reading():
        audio = gTTS(text=text, lang=bahasa, slow=False)
        audio.save(namaFile)
        os.system(namaFile)
    reading()

def run():
    # perintah()
    # perintah2()
    speakAI(perintah())

run()

