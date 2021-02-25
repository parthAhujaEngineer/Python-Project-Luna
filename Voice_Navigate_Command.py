import speech_recognition as sr
import pyttsx3
import os
import pyaudio
from pynput.keyboard import Key, Controller
from keyboard import press_and_release as winPress

listener = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate',150)

keyboard = Controller()

pathDir=""
localDisk = {
    'os':'c:',
    'data':'d:',
    'files':'e:',
    'entertainment':'f:'
    }

def speakText(sentance):
    speaker.say(sentance)
    speaker.runAndWait()

def getInfo():
    try:
        with sr.Microphone() as source:
            print("Please Speak Now ...")
            audio = listener.listen(source)
            info = listener.recognize_google(audio)
            print(info)
            return info.lower()
    except:
        import Speech_Emotion_Recognition
        pass

def selectFolder():
    return getInfo()

def openDir(path):
    global pathDir
    pathDir = pathDir+path+'\\'
    locateDir = os.path.realpath(pathDir)
    os.startfile(locateDir)
    
def voiceNavigate():
    global pathDir
    winPress('win+e')
    speakText('select local disk you want to enter')
    path = localDisk[getInfo()]
    winPress('alt+f4')
    openDir(path)
    speakText('tell me the folder you want to enter')
    while True:
        dirFolder = selectFolder()
        if 'end' in dirFolder:
            return 'navigation terminated'
        else:
            winPress('alt+f4')
            if 'open' in dirFolder:
                dirFolder = dirFolder.replace('open','')
            elif 'select mode' in dirFolder:
                dirFolder = ""
                speakText('select mode activated')
                winPress('down')
                curserDir = getInfo()
                while True:
                    if 'open' in curserDir:
                        winPress('enter')
                    elif 'up' in curserDir:
                        winPress('down')
                    elif 'close' in curserDir:
                        break
                    
                
            openDir(dirFolder)
            speakText('tell me the folder you want to enter')
            continue
            
    


