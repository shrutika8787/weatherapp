import requests
import json
import win32com.client as wincom

city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=2d03131552b44bf693a84244232711&q={city}"

r = requests.get(url)
print(r.text)
# the r.text is string to parse it into dictionary i used json module
# json.loads loads the strings
wdic = json.loads(r.text)
text = wdic["current"]["temp_c"]
h = wdic["current"]["wind_kph"]
humidity = wdic["current"]["humidity"]
speak = wincom.Dispatch("SAPI.SpVoice")
print(text)
speak.Speak(f"Current temprature of {city} is {text} degree celcius")

if __name__ == '__main__':
    x = input("Would you like to know more details. Write y if you want to know or n if you don't want to know")
    if x == "y":
        print(f"wind speed is {h}km/hr ,humidity is {humidity}%")
        speak.Speak(f"The wind speed is {h}kilometer per hour and humidity is {humidity} percent")
        if humidity < 50:
            speak.Speak("The chances of rain are less you can enjoy outdoors")
        else:
            speak.Speak("you must carry an umbrella while going out")
    elif x == "n":
        speak.Speak("Thank you")
        exit()
