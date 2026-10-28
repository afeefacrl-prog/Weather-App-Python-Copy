import requests

# Enter your OpenWeatherMap API Key
API_KEY = "fba8e6a7c584271bcf2503143cf44938"

# Get city name from user
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
 
# Request weather data
response = requests.get(url)

# Check if request is successful
if response.status_code == 200:
    data = response.json()

    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"].title()
    wind_speed = data["wind"]["speed"]

    print("\n========== WEATHER REPORT ==========")
    print(f"City        : {city_name}, {country}")
    print(f"Temperature : {temperature} °C")
    print(f"Feels Like  : {feels_like} °C")
    print(f"Weather     : {weather}")
    print(f"Humidity    : {humidity}%")
    print(f"Wind Speed  : {wind_speed} m/s")
    print("====================================")

else:
    print("City not found or Invalid API Key!")