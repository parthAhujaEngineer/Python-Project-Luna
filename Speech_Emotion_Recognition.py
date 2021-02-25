import datetime
import webbrowser as wb
import pyttsx3
import pywhatkit
import pyaudio
import speech_recognition as sr
import wikipedia as wiki
import Voice_Navigate_Command

def speakText(sentance):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(sentance)
    engine.runAndWait()


r1 = sr.Recognizer()  # Listen, Microphone ... Command
r2 = sr.Recognizer()

print("[Search Text: Search Youtube: Search Image]")

url = ""
turn = True
while turn:
    with sr.Microphone() as source:
        print("Please Speak Now ...")
        audio = r1.listen(source)
        audio = r1.recognize_google(audio)
        audio = audio.lower()
    if "terminate" in audio:
        speakText("closing now, please wait")
        break
    elif "introduce yourself" in audio:
        speakText("hello world! i am luna, artificial intelligent virtual assistant. i m here to help you out. my location in on c:/program files/LunaAI and currently operating on 64 bit operating system.")
        continue
    elif "date" in audio:
        speakText("sorry, i m currently in relationship with wifi")
        continue
    elif "command mode" in audio:
        speakText("command mode activated")
        with sr.Microphone() as source:
            print("Please Speak Now ...")
            audio = r1.listen(source)
            audio = r1.recognize_google(audio)
            audio = audio.lower()
        if "email" in audio:
            import Email_Speech_Automation
        continue
    elif "navigation mode" in audio:
        speakText("navigation mode activated")
        Voice_Navigate_Command.voiceNavigate()
        continue
    elif "search text" in audio:
        speakText("searching text, please wait")
        url = "https://www.google.com/search?q=" + audio.replace("search text", "")
        continue
    elif "search video" in audio:
        speakText("searching video, please wait")
        url = "http://www.youtube.com/results?search_query=" + audio.replace("search video", "")
        continue
    elif "search image" in audio:
        speakText("searching image, please wait")
        url = "https://www.google.co.in/search?hl=en&tbm=isch&sxsrf=ALeKk03Xp9vL7Fj4hE7BPGltI4l7m07iZQ" \
              "%3A1608188400684&source=hp&biw=1164&bih=516&ei=8AHbX5exJ5jtz7sP9PqooAk&q=" + audio.replace(
            "search image ", "")
        continue
    elif "play" in audio:
        speakText("playing music on youtube, please wait")
        pywhatkit.playonyt(audio.replace("play", ""))
        continue
    elif "time" in audio:
        time = datetime.datetime.now().strftime("%I %M %p")
        speakText("current time is" + time)
        continue
    elif "tell me about" in audio:
        info = wiki.summary(audio.replace("tell me about", ""), 1)
        speakText(info)
        continue
    elif "luna" in audio:
        speakText("luna here, how may i help you?")
        continue
    else:
        speakText("please repeat, listening")
        continue
    try:
        wb.get().open_new(url)
        url = ""
    except sr.UnknownValueError:
        print("Error")  # Google Speech Recognition could not understand audio
    except sr.RequestError as e:
        print("Failed".format(e))  # Could not request results from Google Speech Recognition service
