from cgitb import text
from playsound import playsound
import pyttsx3 
import speech_recognition as sr
from datetime import datetime
import os
from requests import get
import wikipedia
import webbrowser
import speech_recognition as sr    #To convert speech into text
import pyttsx3                     #To convert text into speech
import datetime                    #To get the date and time
import wikipedia                   #To get information from wikipedia
import webbrowser                  #To open websites
import os                          #To open files
import time                        #To calculate time
import subprocess                  #To open files
from tkinter import *              #For the graphics
import pyjokes                     #For some really bad jokes
import keyboard 
from PIL import ImageTk
import sys
import random

name_file = open("C:\\Users\\sony\\Documents\\VoiceAssistant\\Assistant_name.txt", "r")
name_assistant = name_file.read()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio): #function to convert text to audio
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishme():
    # hour = int(datetime.now().hour)
    hour = 15
    if hour > 0 and hour < 12:
        speak("Good morning sir..")
    elif hour > 12 and hour < 17:
        speak("Good afternoon sir..")
    elif hour > 17:
        speak("Good evening sir..")
    treat = "Im "+name_assistant+", How May i help you..."
    speak(treat)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # so that jarvis wont stop when you are not speaking
        audio = r.listen(source, timeout = 5, phrase_time_limit = 5)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        print(query)
    except Exception as e:
        speak("Say that again please..")
        return 'none'
    return query

def Process_audio():
        i = 0
        while i < 1:
            speak("Sir, Tell me what should i do")
            query = takecommand().lower()

            if 'open notepad' in query:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                speak("Opening notepad sir")
                os.startfile(npath)

            elif 'ip address' in query:
                ip = get("https://api.ipify.org/").text
                speak(f"Your Ip Address is {ip}")

            elif 'wikipedia' in query:
                speak("searching wikipedia")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences = 3)
                speak("According to wikipedia")
                print(result)
                speak(result)

            elif 'open youtube' in query:
                speak("about what you want to search on youtube")
                s = takecommand()
                webbrowser.open("www.youtube.com/results?search_query=" + s + "")

            elif 'facebook' in query:
                webbrowser.open('https://www.Facebook.com/')
                speak('opening Facebook sir')

            elif 'coin' in query:
                moves=["head", "tails"]
                cmove=random.choice(moves)
                speak("It's " + cmove)

            elif 'university' in query:
                webbrowser.open("https://uims.cuchd.in/uims/")
                speak("Opening your university account sir")

            elif 'whatsapp' in query:
                webbrowser.open("https://web.whatsapp.com/")
                speak("opening whatsapp sir")
                
            elif 'blackboard' in query:
                webbrowser.open("https://cuchd.blackboard.com/?new_loc=%2Fultra%2Fcourse")
                speak("Best of luck for your classes sir.")
            
            elif 'cricket' in query:
                webbrowser.open("https://www.cricbuzz.com/")
                speak("Opening sir..")

            elif 'stack overflow' in query:
                webbrowser.open('https://www.stackoverflow.com/')
                speak('opening stack overflow')

            elif 'google' in query:
                speak("sir what should i search on google")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")
            
            elif 'the time' in query:
                strtime = datetime.datetime.now().strftime("%I:""%M:""%S")
                speak(f"the time is{strtime}")

            elif 'joke' in query:
                s = pyjokes.get_joke(language='en', category='all')
                speak(s)
                
            elif 'stop' in query:
                screen.destroy()

            elif "how are you" in query:
                speak("I'm fine, sir what about you")
                s = takecommand().lower()
                if 'fine' or 'good' or 'great' in s:
                    speak("Thanks god.")
            
            elif "i love you" in query:
                speak("It's hard to understand, Love you too sir")

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by Aryan and jatin")

            elif "weather" in query:
                speak(" City name ")
                print("City name : ")
                city_name = takecommand()
                webbrowser.open("https://www.accuweather.com/en/in/" + city_name + "/189231/weather-forecast/189231")
                speak("opening wether for")
                speak(city_name)
                
            elif "Instagram" in query:
                speak("Opening instagram sir")
                print("Opening instagram sir")
                webbrowser.open("https://www.instagram.com/aryanverma_04/")

            elif "what can you do" in query:
                speak("Sir I can do some of your task, just say what can i do")
                
            elif "what is your name" in query:
                speak("My name is " + name_assistant)
                
            elif "language" in query:
                speak("i was coded in python sir, but i can understant English language")
                print("Coded in Python")
                print("Talks in English")
                
            elif 'time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif "news" in query:
                speak("Here are some of the top Headlines")
                print("Here are some of the top Headlines")
                webbrowser.open("https://timesofindia.indiatimes.com/")
            elif "bored" in query:
                speak("Sir i can play some songs for you")
                print("Sir i can play some songs for you")
                webbrowser.open("https://amitness.com/shuffle/")
            elif "song" in query: 
                speak("which song you want to listen")
                print("which song you want to listen")
                s = takecommand()
                webbrowser.open("www.youtube.com/results?search_query=" + s + "")


            i = 2

def change_name():
  name_info = name.get()
  file=open("Assistant_name.txt", "w")
  file.write(name_info)
  file.close()
  settings_screen.destroy()
  screen.destroy()

def change_name_window():
    
      global settings_screen
      global name


      settings_screen = Toplevel(screen)
      settings_screen.title("Settings")
      settings_screen.geometry("300x300")
      settings_screen.iconbitmap('app_icon.ico')
      settings_screen.configure(bg='black')
      
      
      name = StringVar()

      current_label = Label(settings_screen, text = "Current name: "+ name_assistant)
      current_label.pack()

      enter_label = Label(settings_screen, text = "Please enter your Virtual Assistant's name below") 
      enter_label.pack(pady=10)   
      

      Name_label = Label(settings_screen, text = "Name")
      Name_label.pack(pady=10)
     
      name_entry = Entry(settings_screen, textvariable = name)
      name_entry.pack()


      change_name_button = Button(settings_screen, text = "Ok", width = 10, height = 1, command = change_name)
      change_name_button.pack(pady=10)

def info():

  info_screen = Toplevel(screen)
  info_screen.title("Info")
  info_screen.iconbitmap("C:\\Users\\sony\\Documents\\VoiceAssistant\\app_icon.ico")
  info_screen.geometry("400x300")
  info_screen.configure(bg='black')

  creator_label = Label(info_screen,text = "\nThis app called 'Voice Assistant' is made by Aryan verma, Jatin mangwani \n as an mior project", background='black', fg='white')
  creator_label.pack()

  Age_label = Label(info_screen, text= "We have created this app by using the Python Language", background='black', fg='white')
  Age_label.pack()

  for_label = Label(info_screen, text = "This is version 1.01", background='black', fg='white')
  for_label.pack()

  nor_label = Label(info_screen, text = "We had used various python libraries like \n \n 𝗦𝗽𝗲𝗲𝗰𝗵 𝗥𝗲𝗰𝗼𝗴𝗻𝗶𝘁𝗶𝗼𝗻, 𝗽𝘆𝘁𝘁𝘀𝘅𝟯, 𝗪𝗶𝗸𝗶𝗽𝗲𝗱𝗶𝗮, 𝗪𝗲𝗯𝗯𝗿𝗼𝘄𝘀𝗲𝗿, \n𝗢𝗦, 𝗗𝗮𝘁𝗲𝘁𝗶𝗺𝗲, 𝗧𝗸𝗶𝗻𝘁𝗲𝗿 \n\n This voice assistant can help you with a variety of things like \n ➥ Surfing web, \n ➥ Accessing apps, \n ➥ Surfing the web, \n ➥ And a few more.", background='black', fg='white')
  nor_label.pack()

  speak("This is version 1.01")

from PIL import Image, ImageTk, ImageSequence

def Play_gif():
    from PIL import Image, ImageTk, ImageSequence

    img = Image.open("bg.gif")

    lbl = Label(screen)
    lbl.place(x=40, y=27)
    
    for img in ImageSequence.Iterator(img):
        # img = img.resize((300,300))
        img = ImageTk.PhotoImage(img)
        lbl.config(image = img)
        screen.update()
        time.sleep(0.01)
    screen.after(0,Play_gif)
    return 



def stop():
    speak("Thanks for using me boss, have a good day")
    screen.destroy()

keyboard.add_hotkey("F7", Process_audio)
keyboard.add_hotkey("F9", Process_audio)

def main_screen():

    from PIL import Image, ImageTk, ImageSequence
    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("600x500")
    screen.configure(bg='black')
    screen.iconbitmap('C:\\Users\\sony\\Documents\\VoiceAssistant\\app_icon.ico')
    # playsound("//Voice Assistant//sound.mp3")
    Play_gif()
    wishme()
    speak("Sir you can click on 'Ask me anything button' or F7")
    

    name_label = Label(text = name_assistant,width = 100, bg = "OrangeRed", fg="white", font = ("Calibri", 13))
    name_label.pack()

    microphone_photo = PhotoImage(file = "C:\\Users\\sony\\Documents\\VoiceAssistant\\jaj_2.png")
    microphone_button = Button(image=microphone_photo, command = Process_audio)
    microphone_button.place(x = 160, y = 360)

    info_photo = PhotoImage(file="C:\\Users\\sony\\Documents\\VoiceAssistant\\button_info_2.png")
    info_button = Button(image=info_photo, command=info)
    info_button.place(x = 40, y = 430)

    settings_photo = PhotoImage(file = "C:\\Users\\sony\\Documents\\VoiceAssistant\\button_setting_2.png")
    settings_button = Button(image=settings_photo, command = change_name_window)
    settings_button.place(x = 190, y = 430)

    stop_photo = PhotoImage(file="C:\\Users\\sony\\Documents\\VoiceAssistant\\stoper_2.png")
    stop_button = Button(image=stop_photo, command=stop)
    stop_button.place(x = 390, y = 430)

    screen.mainloop()  

main_screen()
