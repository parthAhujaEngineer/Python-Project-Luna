import smtplib #Simple Mail Transfer Protocol Library
import speech_recognition as sr
import pyaudio
import pyttsx3
from email.message import EmailMessage


listener = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate',150)

emailList = {
    'bro':'ahujasid84@gmail.com',
    'programmer':'parthahuja315@gmail.com',
    'friend':'Atishayajain27@gmail.com'
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
        speakText("error, please retry!")
        pass

def emailInfo():
    speakText("to whom you want to send email?")
    receiverName = getInfo()
    emailId = emailList[receiverName]
    print(emailId)
    speakText("tell me the subject of your email?")
    emailSubject = getInfo()
    speakText("what message you want to send?")
    emailBody = getInfo()
    return emailId,emailSubject,emailBody


emailId,emailSubject,emailBody = emailInfo() 
bot = smtplib.SMTP('smtp.gmail.com',587)
bot.starttls() #Start Transport Layer Security
bot.login('levy.artificial.intelligence@gmail.com','Levy@2020')
email = EmailMessage()
email['From'] = 'levy.artificial.intelligence@gmail.com'
email['To'] = emailId
email['Subject'] = emailSubject
email.set_content(emailBody)
bot.send_message(email)
speakText('email sent successfuly')


