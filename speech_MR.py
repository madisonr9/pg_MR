import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb
speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("Hello!. What is your name?")

answer = pg.prompt ("Enter your name.")

if answer == "Madison":
    speak.speak("Hi, Madison!")
elif answer == "Jamie":
    speak.speak("aaaaahhhh")
else:
    speak.Speak("Nice to meet you")

answer = pg.prompt("Whats your favorite food?")

if answer == "Mac and Cheese":
    speak.Speak("Me too!")
elif answer == "Quesidillas":
    speak.Speak("Those are pretty good!")
else:
    speak.Speak("Whats wrong with you! how do you like " + answer + " over Mac and Cheese")
    





            
