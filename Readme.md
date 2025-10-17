# Purpose

A terminal-based Python app that helps users find the best cities to live in based on their climate and population preferences.

## How to run

1-Download and install python3
##
2-Create an account on Google AI Studio
##
3-Click the Create API Key button in get api key section
##
4-Create a file and name it .env in the root of this project and write this in it:
  GEMINI_API_KEY= Your API key
##
5-Put the API key google gave you instead of the your api key part
##
6-Type `./start.sh` to the console while in the root directory of the project.

### How does it work
<p>The program asks you for your preferences on certain set attributes and the importance this attribute has for you. After entering all of your preferences<br>
program gives you a top 10 list of the cities in its database that fits with your preferences. If you dont like the list you can just answer yes when the<br>
program asks you if you want to select new attributes. If you feel good about the list and you want to know more about a city in the list you can say yes<br>
to the next question and the program will give you a description about the city you want to know more about using gemini ai. When you feel satisfied you<br>
can type quit to close the program.</p>