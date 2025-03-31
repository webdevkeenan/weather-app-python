import requests

api_key = '8774ee223921aa27f2c5a81708eae1fa'

# Get user inputs for city, state, and optionally zip code
city = input("Enter city: ")
state = input("Enter state (optional): ")
zip_code = input("Enter zip code (optional): ")

# Determine which API query to use
if zip_code.strip() != "":
    # Use the zip code query (for US zip codes)
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},US&units=imperial&APPID={api_key}"
elif state.strip() != "":
    # Use city and state query (US assumed)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},US&units=imperial&APPID={api_key}"
else:
    # Use only the city query (US assumed)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},US&units=imperial&APPID={api_key}"

# Make the API request
weather_data = requests.get(url)

# Check the API response code to see if a valid location was found
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {city} is: {weather}")
    print(f"The temperature in {city} is: {temp}ºF")
