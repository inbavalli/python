import speech_recognition as sr
import webbrowser

r = sr.Regonizer()


with sr.Microphone() as source:
    print("what you want to search\n")
    audio = r.listen(source)

print('opening: ' + r.recognize_google(audio))


p = r.recognize_google(audio)
webbrowser.open(p)
