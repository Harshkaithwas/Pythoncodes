import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os 
import smtplib
import random
import os.path


rndm=[]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Harsh, I love to spend time with you ")
    elif hour <= 12 and hour < 18:
        speak("Good afternoon Harsh")
    else:
        speak("Good Evening Harsh")

    speak("I am edith your personal assistent , any orders for me my master ")


def takeCommand():
      r = sr.Recognizer()
      with sr.Microphone() as source:
            print("....Listning....")
            r.pause_threshold = 1
            audio = r.listen(source)

      try:
            print(".....Recognising.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}\n")
      except Exception as e:
            print("Please Command again....")
            return None
      return query

def sendEmail(to, content):
      server = smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.login(FROM, PASS)
      server.sendmail(FROM,to,content)



if __name__ == '__main__':
      wishMe()
      while(True):
            
            query = str(takeCommand()).lower()   
            if("bhai yaar" in query):
                  query.replace("bhai yaar","")
                        # logics
                  if "wikipedia" in query:
                        speak("searching on wikipedia")
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=3)
                        speak("accordinf to wikipedia")
                        print(results)
                        speak(results)
                  elif "youtube" in query:
                        webbrowser.open("youtube.com")      
                  elif "google" in query:
                        webbrowser.open("google.com")
                  elif "my blog" in query:
                        webbrowser.open("techharsh.co")
                  elif "songs" in query:
                        music_dir ='C:\\Users\\rc261\\Desktop\\New folder\\Sounds'
                        rndm= random.randint(1,100)
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join(music_dir,songs[rndm]))
                  elif "the time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        print(strTime)
                        speak(f"sir, the time is :{strTime}")
                  elif "jarvis" in query:
                        speak("what can i do for you my master ")
                  elif "open code" in query:
                        codePath = "C:\\Users\\rc261\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codePath)
                  elif "mail " in query:
                        try:
                              speak("Whats the message")
                              content = takeCommand()
                              to = "mail@gmail.com"
                              sendEmail(to, content)
                              speak("your email has been sended")
                        except Exception as e:
                              speak("please retry ")
                  elif "chrome" in query:
                        cpath ="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                        os.startfile(cpath)
            
                        
 
