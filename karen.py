from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3
import datetime
import sys
import wikipedia
import wolframalpha
import os
import smtplib
import random
import webbrowser
import pygame
import subprocess

client = wolframalpha.Client('9RPWHU-ARQAK42G8R')

folder = 'C:\\Users\\Gaurav Yadav\\Videos\\k\\'

engine = pyttsx3.init()
voices = engine.getProperty('voices')

b_music = ['3']
#b_music = ['flying high', 'limitless', 'Scott_Holmes', 'band']
pygame.mixer.init()
pygame.mixer.music.load(folder + random.choice(b_music) + '.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)


def speak(audio):
    print('Karen:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Try again')
        pass
        #query = str(input('Command: '))

    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


class Widget:
    def __init__(self):
        root = Tk()
        root.title('KAREN(MK-1)')
        root.config(background='Red')
        root.geometry('350x600')
        root.resizable(0, 0)
        root.iconbitmap(
            r'C:\Users\Gaurav Yadav\Videos\u\Untitled-1.ico')
        img = ImageTk.PhotoImage(Image.open(
            r"C:\Users\Gaurav Yadav\Videos\u\karen image 2.png"))
        panel = Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="no")

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click \'Start Listening\' to Give commands')

        userFrame = LabelFrame(
            root, text="USER", font=('Black ops one', 10, 'bold'))
        userFrame.pack(fill="both", expand="yes")

        left2 = Message(userFrame, textvariable=self.userText,
                        bg='dodgerBlue', fg='white')
        left2.config(font=("Comic Sans MS", 10, 'bold'))
        left2.pack(fill='both', expand='yes')

        compFrame = LabelFrame(
            root, text="KAREN", font=('Black ops one', 10, 'bold'))
        compFrame.pack(fill="both", expand="yes")

        left1 = Message(compFrame, textvariable=self.compText,
                        bg='Red', fg='white')
        left1.config(font=("Comic Sans MS", 10, 'bold'))
        left1.pack(fill='both', expand='yes')

        btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'),
                     bg='deepSkyBlue', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'),
                      bg='deepSkyBlue', fg='white', command=root.destroy).pack(fill='x', expand='no')

        speak('Hello sir, I am digital assistance Karen! What should I do for You?')
        self.compText.set(
            'Hello sir, I am digital assistance Karen! What should I do for You?')

        # handle the enter key event of your keyboard
        root.bind("<Return>", self.clicked)
        root.mainloop()

    def clicked(self):
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'notepad plus plus' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(
                r'C:\Program Files\Notepad++\notepad++.exe')

        elif 'firefox' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(
                r'C:\Program Files\Mozilla Firefox\firefox.exe')

        elif 'pycharm' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(
                r'C:\Program Files\JetBrains\PyCharm Community Edition 2019.2\bin\pycharm64.exe')

        elif 'java editor' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(
                r'C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2019.2\bin\idea64.exe')

        elif 'internet explorer' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(
                r'C:\Program Files\internet explorer\iexplore.exe')

        elif 'the time' in query or 'current time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            #self.compText.set(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'project report' in query:
            codePath = "C:\\Users\\Gaurav Yadav\\Videos\\p\\yoy.docx"
            os.startfile(codePath)

        elif 'google chrome' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(
                r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        elif 'powerpoint' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(
                r'C:\Program Files (x86)\Microsoft Office\Office15\POWERPNT.exe')

        elif 'open youtube' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('shutdown -s')

        elif "what\'s going on " in query or "what is going on" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!',
                      'Nice!', 'I am nice and full of energy']
            yo = random.choice(stMsgs)
            self.compText.set(yo)
            speak(yo)

        elif 'email' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            recipient = myCommand()
            self.userText.set(recipient)
            recipient = recipient.lower()

            if 'john' or 'saurav'or 'myself' in recipient:
                try:
                    self.compText.set('What should I say? ')
                    speak('What should I say? ')
                    content = myCommand()
                    self.userText.set(content)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("sauravyadavmr80g4@gmail.com", 'm16a2m4a1')
                    server.sendmail('sauravyadavmr80g4@gmail.com',
                                    "sauravyadav1958@gmail.com", content)
                    server.close()
                    self.compText.set('Email sent!')
                    speak('Email sent!')

                except:
                    self.compText.set(
                        'Sorry sir, I am unable to send message at this moment!')
                    speak('Sorry ' + 'Sir' +
                          '!, I am unable to send your message at this moment!')

        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'quit' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye Sir, have a good day.')
            speak('Bye Sir, have a good day.')

        elif 'hello' in query or 'hi' in query:
            self.compText.set('Hello Sir')
            speak('Hello Sir')

        elif 'bye' in query:
            self.compText.set('Bye ' + 'Sir' + ', have a good day.')
            speak('Bye ' + 'Sir' + ', have a good day.')

        elif 'play music' in query:
            music_folder = 'C:\\Users\\Gaurav Yadav\\Videos\\k\\'
            music = ['sparelax','Scott_Holmes','tobu','arrow','vitality']
            music_folder = 'C:\\Users\\Gaurav Yadav\\Videos\\k'
            music = os.listdir(music_folder)
            os.startfile(os.path.join(music_folder, random.choice(music)))
            '''random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)'''

            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')

        elif 'play video' in query:
            video_folder = 'C:\\Users\\GauravYadav\\Videos\\k\\'
            video = ['Love, Simon - Official Trailer 2 [HD] - 20th Century FOX']
            video_folder = 'C:\\Users\\Gaurav Yadav\\Videos\\v'
            video = os.listdir(video_folder)
            os.startfile(os.path.join(video_folder, random.choice(video)))
            '''random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)'''

            self.compText.set('Okay, here is your video! Enjoy!')
            speak('Okay, here is your video! Enjoy!')

        else:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    self.compText.set(results)
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    self.compText.set(results)
                    speak(results)

            except:
                speak('I don\'t know Sir! Google is smarter than me!')
                self.compText.set(
                    'I don\'t know Sir! Google is smarter than me!')
                webbrowser.open('www.google.com')


if __name__ == '__main__':
    greetMe()
    widget = Widget()
