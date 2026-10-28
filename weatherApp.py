import requests

#enter OpenWheatherMap API key
api_key = "fba8e6a7c584271bcf2503143cf44938"


#get city name from user
city= input("enter city name:")


#API URL
url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={"fba8e6a7c584271bcf2503143cf44938"}&units=metric"


#request wheather data
response = requests.get(url)  #sends GET request to the OpenWheather API,stores the servers response in the variable.


#check if request is successful
if response.status_code ==200:   #200 means successful
    data =response.json()     #convert into python dictionary , can access the values
 


            #data= the dictionary containing all the wheather data from the API.

    city_name = data["name"]           #retrieves the city name from the API responses
    country = data ["sys"]["country"]   #sys means system = is a dictionary that contains system related information.sunrise
    temperature =data["main"] ["temp"]   #API response the main wheather information.
    humidity =data["main"] ["humidity"]
    weather =data  ["weather"]
    wind_speed =data ["wind"]

    print(f"City: {city_name}")
    print(f"country: {country}")
    print(f"temperature: {temperature} °C")
    print(f"humidity: {humidity} %")
    print(f"weather: {weather}")
    print(f"wind_speed: {wind_speed}")

else:
    print("city not found or invalid api key:")