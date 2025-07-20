# To import the API, you first need to sign up and create a free account at https://openweathermap.org/api
# After signing up, add your API key to an .env file for secure access

import requests
from datetime import datetime
# To include the current date, you need to import the datetime module using the code above.
# This code is used to display the date and/or time and can be formatted in various ways.

from dotenv import load_dotenv
import os
load_dotenv()

city_input = input("Enter your city (e.g., London, Paris, New York): ")

appid = os.getenv("my_app_id") #This retrieves the API key stored in the environment variable 'my_app_id'
endpoint = 'http://api.openweathermap.org/data/2.5/weather'
payload = {
    'q': city_input, #the city name entered by the user
    'units': 'metric', #the temperature (Celsius)
    'appid': appid,
}

response = requests.get(url=endpoint, params=payload)
data = response.json()

# This code will check for errors such as incorrect spelling or city not found.
# If no errors are found, the loop will run
if data.get("cod") != 200:
    print("Sorry, that city wasn't found. Please check the spelling and try again.")
else:
    temp = data["main"]["temp"]
    condition = data["weather"]
    city = data["name"]
    short_city = city[:3].upper()
# short_city uses string slicing and will only show the first 3 letters of the city and converts to uppercase

# Formatted the date to display the weekday, day of the week and month, but shortened.
today = datetime.now().strftime("%a %d %b")

outfits = {
    "cold": ["thick coat", "jeans (with tights underneath!)", "👢"],
    "warm": ["a nice t-shirt", "some loose trousers", "👟"],
    "hot": ["some shorts or a skirt, whatever you're feeling", "a sleeveless top", "🩴"],
    "rain": ["Bring an umbrella! ☂️"]
}

#The temperature ranges will determine which outfit choice is selected.
def get_outfit(temp):
    if temp < 15:
        return outfits["cold"]
    elif 15 <= temp < 23:
       return outfits["warm"]
    else:
       return outfits["hot"]

chosen_outfit = get_outfit(temp)

# If it's also raining, add a reminder to bring an umbrella
if "rain" in condition[0]["description"]:
    chosen_outfit += outfits["rain"]

#Print the outfit suggestion, capitalising the first letter in each sentence
print(f"Today is {today} and it's {temp:.0f}°c in {short_city}, so you should wear:")
for item in chosen_outfit:
    print("-", item.capitalize())

# This will save the results to a file
with open("outfit_suggestions.txt", "a") as file:
        file.write(f"Date: {today}\n")
        file.write(f"City: {city} ({short_city})\n")
        file.write(f"Temperature: {temp:.0f}°C\n")
        file.write(f"Suggested outfit:{chosen_outfit}\n\n")
