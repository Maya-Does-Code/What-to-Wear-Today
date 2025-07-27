# 👚 W2W2 - What 2 Wear 2Day, your Daily Outfit Recommender.

![Alt text: Clip from *Clueless* movie of the outfit selection tool on Cher's PC ](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3EzOHk4OHNocXl5M25vZWZscDJ1d3d6MnkxcW5kbGU2bjBzOXp3biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT9KVgmGTooXz0iDPW/giphy.gif)
*<br>GIF from Clueless (1995)*

## 📝 Project Description
W2W2 is a Python console app that suggests outfits based on your city’s weather using the OpenWeatherMap API. 

This project demonstrates how to:
- Integrate a real-time API
- Transform data into something user-friendly 
- Apply core Python concepts such as functions, conditionals, loops, dictionaries and file handling

This simple tool is designed for users who need a quick decision on what to wear today. Sun's out? Arms out! Grey skies and frozen fingers? Put those tights on! Oh, and don't forget the brolly!

## ⭐️ Features

- User inputs their city (e.g. "London", "Paris", "New York")
- Weather data is fetched using the OpenWeatherMap API
- Outfit suggestions are based on temperature thresholds and rain conditions 
- Automatically logs the date, city, temperature and outfit suggestion to a local text file for record-keeping and any future analysis
- Emojis for fun 😄

## ⚙️ Setup Instructions
1. Clone or download the project folder. This will include the Python file, the example .env file and the text file where the entries are saved 
2. Install the following package (if not already installed): **pip install python-dotenv**
3. Get your API key from [OpenWeatherMap](https://openweathermap.org/api)
4. Create a .env file in the folder to store your API key. <br> **NOTE** ⚠️ Do not share your API key publicly or push your .env file to GitHub! I've created an example doc for guidance
5. Run the script!

## 🖥️ Example output
*Here is an example of what the user will see in the terminal*:

Today is Sun 27 Jul and it's 21°c in LON, so you should wear:\
\-  A nice t-shirt <br> 
\-  Some loose trousers <br>
\- 👟


## 🧩 Challenges
- String slicing shows the first three letters of the city. Cities that start with the same letters will show the same abbreviation e.g. New York, New Jersey, New Delhi, etc
- As it's based on current conditions, it doesn't allow for future weather changes. It might not be raining now, but it could be in a few hours. 
- The suggestions are very general and very obvious! If it's 30°c, it's best to leave the fur coat in the wardrobe...

## 💡What I've Learnt
- How to access and implement a public API
- Using environment variables to keep sensitive data secure
- Parsing JSON data in Python
- Writing to and appending local files
- The importance of user experience, even with a basic console app!

