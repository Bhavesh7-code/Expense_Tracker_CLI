import requests
from dotenv import load_dotenv
import os

#  Load environment variables from .env file
load_dotenv()

def get_weather(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Get the API key from the environment
    api_key = os.getenv("API_KEY")

    # Safety check: Make sure the key is loaded
    if not api_key:
        print("API key not found. Please check your .env file.")
        return

    # Set up parameters
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    # Send the request
    response = requests.get(base_url, params=params)

    print("Request URL:", response.url)  # Debugging

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        print(f"Weather in {city_name.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print("City not found or error fetching data.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
