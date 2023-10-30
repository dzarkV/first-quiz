from question1 import get_city_weather

def test_get_city_weather():

  assert get_city_weather("Quito") == "22 degrees and sunny"

  assert get_city_weather("New York") == "14 degrees and rainy"

  assert get_city_weather("San Francisco") == "16 degrees and unknown conditions"

  assert get_city_weather("Bogotá") == "uncertain temperature degrees and uncertain conditions"
