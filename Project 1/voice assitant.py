import pyttsx3
import speech_recognition as sr
import webbrowser
import smtplib
import requests
import json
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voicespeed = 145
engine.setProperty('rate',voicespeed)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def intro():
    say("Hello sir, mam how may i help you?")

def Commandds ():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("wait a sec...")
        user_in = r.recognize_google(audio, language='en-in')
        print("User said:",user_in)

    except Exception as e:
        print("Can you please repeat yourself...")
        say("Can you please repeat yourself")
        return "None"
    return user_in

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('interproject777@gmail.com', 'ektf azxt mrhc sugd')
    server.sendmail('&&&&&&&&&&&', to, content)
    server.close()

if __name__ == "__main__":
    intro()
    while True:
        user_in = Commandds().lower()

        if 'hello assistant' in user_in:
                say('hello sir')

        elif 'open google' in user_in:
                say('sure sir')
                webbrowser.open("google.com")

        elif 'current time' in user_in:
                time = datetime.datetime.now().strftime('%H:%M:%S')
                say(f"current time is {time}")

        elif 'send email' in user_in:
                try:
                    say("What should I say?")
                    content = Commandds()
                    to = "duraiswamy500@gmail.com"
                    sendEmail(to, content)
                    say("Email has been sent!")
                except Exception as e:
                    say("sorry some error occured while sending email")

        elif 'weather' in user_in:
            key ="a370cac5acb69219d83f99786dc5fb65"
            speak = ""
            site_url = "https://api.openweathermap.org/data/2.5/weather?"
            ind = user_in.split().index("in")
            location = user_in.split()[ind + 1:]
            location = "".join(location)
            main_url = site_url + "appid=" + key + "&q=" + location
            js = requests.get(main_url).json()
            if js["cod"] != "404":
                weather = js["main"]
                temperature = weather["temp"]
                temperature = temperature - 273.15
                humidity = weather["humidity"]
                additional = js["weather"][0]["description"]
                response = "the temperature is " + str(temperature) + "the humididty is " + str(humidity) + " and weather description is " + str(additional)
                say(response)
                print(response)
            else:
                say("city not found")

        elif 'ok bye assistant' in user_in:
            say("bye sir have a great day")
            break

        elif "wikipedia" in user_in:
            user_in = user_in.replace("wikipedia","")
            rl = wikipedia.summary(user_in,sentences = 1)
            say("wikipedia says")
            say(rl)

