import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        
        print("City:", weather_data['name'])
        print("Temperature:", weather_data['main']['temp'], "°C")
        print("Weather:", weather_data['weather'][0]['description'])
        print("Humidity:", weather_data['main']['humidity'], "%")
        print("Wind Speed:", weather_data['wind']['speed'], "m/s")
    else:
        print("Failed to fetch weather data. Status code:", response.status_code)

# Example usage
city_name = input("Enter the name of the city: ")
api_key = "61637af4bae4ab5d10434c169f335f4c"  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
get_weather(city_name, api_key)
