import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    
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

# Test it
if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "031d53b68c96557f041bc0f348b5aa4e"  # Replace with your API key
    get_weather(city, api_key)
