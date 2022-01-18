import tkinter as tk
import requests
import time
from datetime import date


def getWeather(canvas):
    city = textfield.get()

    # Gather the API from a third party service to obtain weather information
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=712d1165813aaa86525e576009d566c7"
    json_data = requests.get(api).json()

    # Weather conditions, temperature, etc.
    weather_condition = json_data["weather"][0]["main"]

    temperature = int(json_data["main"]["temp"] - 273.15) * 9 / 5 + 32
    feels_like = int(json_data["main"]["feels_like"] - 273.15) * 9 / 5 + 32
    min_temperature = int(json_data["main"]["temp_min"] - 273.15) * 9 / 5 + 32
    max_temperature = int(json_data["main"]["temp_max"] - 273.15) * 9 / 5 + 32

    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind_speed = json_data["wind"]["speed"]

    # Time format of Hour, Minutes, Seconds.
    sunrise = time.strftime("%I:%M:%S%p", time.gmtime(json_data["sys"]["sunrise"] - 21600))
    sunset = time.strftime("%I:%M:%S%p", time.gmtime(json_data["sys"]["sunset"] - 21600))
    today = time.strftime("%b/%d/%Y")

    # Format and displays the formatted data below
    final_info = weather_condition + "\n" + str(temperature) + "°F"
    final_data = today + "\n" \
                 + "Max Temp: " + str(max_temperature) + "°F" + "\n" \
                 + "Min Temp: " + str(min_temperature) + "°F" + "\n" \
                 + "Feels Like: " + str(feels_like) + "°F" + "\n" \
                 + "Pressure: " + str(pressure) + "\n" \
                 + "Humidity: " + str(humidity) + "\n" \
                 + "Wind Speed: " + str(wind_speed) + "Mph" + "\n" \
                 + "Sunrise: " + str(sunrise) + "\n" \
                 + "Sunset: " + str(sunset) + "\n"
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x480")
canvas.title("Weather - " + str(date.today()))

small_font = ("poppins", 15, "bold")
large_font = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = large_font)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind("<Return>", getWeather)

label1 = tk.Label(canvas, font = large_font)
label1.pack()
label2 = tk.Label(canvas, font = small_font)
label2.pack()

canvas.mainloop()
