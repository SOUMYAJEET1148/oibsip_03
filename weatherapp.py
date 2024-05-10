
import requests

api_key = '057cb0855e2cccb44eca5210d7b524a7'

city_name = input("Enter Your Location:")
weather_data = (requests.get
                (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID={api_key}"))

if weather_data.json()['cod'] == '404':

    print("No City Found!!!Try again")

else:
 weather = weather_data.json()['weather'][0]['main']

 temp = round(weather_data.json()['main']['temp'])

 humidity = weather_data.json()['main']['humidity']

 temp_max = weather_data.json()['main']['temp_max']

 temp_min = weather_data.json()['main']['temp_min']



print(f"The weather in {city_name} is: {weather}")

print(f"The temperature in {city_name} is: {temp}ºC")

print(f"Humidity is {city_name} is: {humidity}")

print(f"temp_max is {city_name} is: {temp_max}ºC")

print(f"temp_min is {city_name} is: {temp_min}ºC")
