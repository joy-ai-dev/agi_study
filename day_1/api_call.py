import requests

city = input("Give a city name: ")

url = "https://wttr.in/" + city + "?format=j1"

response = requests.get(url)

print(response.status_code)

data = response.json()
#print(data.keys())

temperature = data["current_condition"][0]["temp_C"]
humidity = data["current_condition"][0]["humidity"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]

print("City: ", city)
print("Temperature (C): ", temperature)
print("Humidity: ", humidity)
print("Weather: ", weather)
