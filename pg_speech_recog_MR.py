import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r=sr.Recongizer()
with sr.Microphone () as source:
    speak.Speak("Hi comp Sci class, what do you want to search for?")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")

try:try:
        words = r.recognize_google(audio)
        speak.Speak("Ok Madison. let's look for" + r.recognize_google(audio) + " On Google.")
        wb.open("https://www.google.com/search?q=" + words)

    except sr.UnknownValueError:
        print("Google Speech Recongnition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}" .format(e))
