'''
Built in:
webbrowser module
datetime module
os module
random

Things to download:
pip install pyttsx3
pip install speechRecognition
pip install .
pip install .
'''
import pyttsx3             # Text to speech module needed to be downloaded by pip install pyttsx3
import speech_recognition as sr # Converts Spoken Voice to Text ; Also takes input from Microphone
import datetime
import webbrowser as web # Allows to use web with a given url
import os
import random
import email

voice_engine = pyttsx3.init('sapi5')    # Defines the voice; Is a speech engine; for more search speech-api or sapi5
type_voice = voice_engine.getProperty('voices')     # Defines voice_engine to be get voices

voice_engine.setProperty('voice', type_voice[0].id)         # This is setting the voice to male voice
# print(type_voice[0].id) This will give a male voice david and [1].id  will give female!

# To speak
def speaker(text):
    '''This will Turn text into voice'''
    voice_engine.say(text)
    voice_engine.runAndWait()       # This awaits the rest of the program until It is finished speaking

# To Greet
def greet():
    '''This will greet people appropriately according to the time'''
    hour = int(datetime.datetime.now().hour)        # gives a total of 24 hours
    if hour >= 0 and hour < 12:
        speaker('Good Morning')
    elif hour >= 12 and hour < 18:
        speaker('Good AfterNoon')
    else:
        speaker('Good Evening')
    # speaker('')

def Mic():
    '''Converts Voice to Text'''
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 200        # How much energy required to talk and input
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Understanding...')
        user = r.recognize_google(audio, language='en')     # Searches for English audio to turn to text
        print(f'User: {user}')
        # add hot word detection later
    except:
        print('\nCouldn\'t understand. Please Speak Again')
        return 'None'
    return user

if __name__ == '__main__':
    greet()

    # Function logics
    while True:
        # user_said = Mic()
        # user_said = user_said.lower()
        user_said = input()

        # Web browser functions
        if 'youtube' in user_said:
            print('Entering Youtube....\n')
            web.open_new_tab('youtube.com')

        elif 'google' in user_said:
            web.open_new_tab('google.com')

        elif 'github' in user_said:
            web.open_new_tab('https://github.com/Irfan1286/Coding-Journey')

        elif 'play music' in user_said:
            music_dir = 'C:\\Users\\TOSHIBA\\Music\\audio\\vidtrim'
            songs = os.listdir(music_dir)   # Makes list of songs which the folder contains
            print(songs)
            # first path needs to be joined to the name of the file for the startfile function to start
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs))]))

        elif 'time' in user_said:
            speaker(datetime.datetime.now().strftime('Sir, The time is %H hour and %M minutes'))

        elif 'pycharm' in user_said:
            os.startfile(r'"C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.1\bin\pycharm64.exe"')
            # Click on properties of file and copy the target

        elif 'speak' in user_said:
            speaker(Mic())

        elif 'hangman' in user_said:
            os.startfile('Hangman.py')


        else:
            ran = False















