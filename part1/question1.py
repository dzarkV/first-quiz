################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/
#
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

def get_city_temperature(city_searched: str) -> int|str:
   """Returns the temperature for a given city."""
    
   cities_and_temperatures: dict = {city["name"]:city["temperature"] for city in cities}
   return cities_and_temperatures.get(city_searched)


def get_city_weather(city: str) -> str:
   """Returns the weather for a given city."""
   
   sky_condition: str = None
   temperature: int = None

   for city_data in cities:
      if city_data["name"] == city:
         sky_condition = city_data.get("sky_condition", "unknown conditions")
         temperature = get_city_temperature(city)
         break
      else:
         sky_condition = "uncertain conditions"
         temperature = "uncertain temperature"

   return str(temperature) + " degrees and " + sky_condition


# Source of cities and weather data:
cities = [
    {"name": "Quito", "temperature": 22, "sky_condition": "sunny"},
    {"name": "Sao Paulo", "temperature": 17, "sky_condition": "cloudy"},
    {"name": "San Francisco", "temperature": 16},
    {"name": "New York", "temperature": 14, "sky_condition": "rainy"}
]
