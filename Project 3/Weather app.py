from tkinter import *
import requests
import json
from datetime import datetime

root = Tk()
root.geometry("400x400")
root.title("Weather App")
root.config(bg="light green")


def time_format(utc):
    local_time = datetime.utcfromtimestamp(utc)
    return local_time.time()

cityv = StringVar()

def reset():
    in_city.delete(0,'end')
    outputarea.delete('1.0','end')

def showWeather():
    api_key = "a370cac5acb69219d83f99786dc5fb65"
    city_name = cityv.get()
    site_url = ('https://api.openweathermap.org/data/2.5/weather?q=' + city_name +'&appid=' +api_key)
    response = requests.get(site_url)
    weather_info = response.json()
    outputarea.delete('1.0', 'end')


    if weather_info['cod'] == 200:
        kelvin = 273
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format(sunrise + timezone)
        sunset_time = time_format(sunset + timezone)

        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nWindspeed: {wind_speed}\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    outputarea.insert(INSERT, weather)


can_wid = Canvas(root, height=160, width=395, bg="light green",highlightbackground="light green")
can_wid.pack()
can_wid.create_rectangle(55, 250, 340, 1, fill="beige",outline="beige")
can_wid.create_oval(100, 162, 2, 2, fill="beige",outline="beige")
can_wid.create_oval(396, 162, 300, 2, fill="beige",outline="beige")

l1 = Label(can_wid, text='Enter City Name', font='times 15 bold',bg="beige").place(x=120,y=30)

in_city = Entry(can_wid, textvariable=cityv, width=24, font='times 14 bold',bg="beige",borderwidth=3)
in_city.place(x=80,y=70)

b1=Button(can_wid, command=showWeather, text="Check Weather", font="times 12 bold", bg='beige', fg='black', padx=5, pady=5,borderwidth=2,activebackground="beige",).place(x=140,y=115)

weather_now = Label(root, text="The Weather is:", font='times 15 bold',bg="light green")
weather_now.place(x=30,y=180)

reset_btn = Button(root,text='R',font='times 12 bold',bg='beige',activebackground="beige",command=reset)
reset_btn.place(x=340,y=180)

outputarea = Text(root, width=46, height=10,bg="beige")
outputarea.place(x=15,y=220)


root.mainloop()