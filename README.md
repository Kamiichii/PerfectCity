# Perfect City

## Purpose:
A terminal-based Python app that helps users find the best cities to live in based on their climate and population preferences.

## How It Works
City Data:

Cities and their attributes are stored in a CSV file.
Attributes (for MVP) include:
Average temperature [bucketed: Freezing(<0C°)/Cold(0C°-10C°)/Cool(10C°-18C°)/Warm(18C°-24C°)/Hot(24C°>)]
Rainfall [Arid(<250mm)/Dry(250mm-500mm)/Moderate(500mm-1000mm)/Wet(1000mm-2000mm)/Very wet(2000mm>)]
Cloudiness [Very Cloudy(0-20%)//Mostly Cloudy(20-40%)/Balanced(40-60%)/Mostly Clear(60-80%)/Very Clear(>80%)]
Population [Tiny(<50,000)/Small(50,000-200,000)/Medium(200,000-1,000,000)/Large(1,000,000-5,000,000)/Very Large(5,000,000-10,000,000)/Mega(>10,000,000)]
Each city is mapped to a “bucket” for each attribute.
User Input:

The app presents choices for each attribute (e.g., “Warm (18–24°C)”).
The user selects their preferred bucket for each attribute.
For each attribute, the user also selects an importance level (options like: “I don’t care,” “Nice to have,” “Absolutely essential!”), which maps to a numeric weight (0 for “don’t care,” up to 5 for “essential”).

## Scoring System:

For each city and attribute, compute the “distance” between the user’s preference and the city’s value (for example, distance = absolute difference between chosen buckets).
Multiply this distance by the user’s importance weight for that attribute.
Sum these weighted distances across all attributes to get a total “match score” for each city (lower is better).
Output:

    Sort cities by total score (best matches = lowest scores).
    Display the top 10 recommended cities, showing their names and attribute values.
    