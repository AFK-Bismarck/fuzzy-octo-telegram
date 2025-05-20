
import requests



def weather_data(lati, long, timezone):

    api = f"https://api.open-meteo.com/v1/forecast?latitude={lati}&longitude={long}&daily=temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,wind_speed_10m_max&current=temperature_2m,relative_humidity_2m,precipitation,rain,showers,snowfall,apparent_temperature,wind_speed_10m,weather_code,cloud_cover&timezone=Europe%2F{timezone}"

    result = requests.get(api)
    weather_code = result.json()['current']['weather_code']
    temperature = result.json()['current']['temperature_2m']
    minimum_temperature = result.json()['daily']['temperature_2m_min']
    maximum_temperature = result.json()['daily']['temperature_2m_max']
    feels_like = result.json()['current']['apparent_temperature']
    mapping_ranges = {
            ((0, 0), "Clear sky"),
            ((1, 1), "Mainly clear"),
            ((2, 19), "Partly cloudy/Cloudy"),
            ((36, 39), "Blowing/drifting snow"),
            ((40, 49), "Fog"),
            ((50, 59), "Drizzle"),
            ((60, 69), "Rain"),
            ((70, 79), "Snow"),
            ((80, 84), "Rain showers"),
            ((85, 90), "Snow showers"),
            ((91, 99), "Thunderstorm")
    }
    weather_mapping = {}

    for (start, end), description in mapping_ranges:
        for code in range(start, end + 1):
            weather_mapping[code] = description

# Now you can use .get() directly on the dictionary.
    weather_condition = weather_mapping.get(weather_code, "Unknown")

    weather_condition =  weather_mapping.get(weather_code)


    temperature = int(temperature)
    minimum_temperature[0] = int(minimum_temperature[0])
    maximum_temperature[0] = int(maximum_temperature[0])

    return weather_condition, temperature, minimum_temperature[0], maximum_temperature[0], feels_like 

def outfit_recommender (temperature, weather_condition):
    if temperature < 0:
        outfit = "heavy coat and gloves."
    elif temperature < 15:
        outfit = "a jacket with layered clothing."
    elif temperature < 20:
        outfit = "a light shirt with jeans."
    else:
        outfit = "shorts and a t-shirt."

    if "rain" in weather_condition.lower():
        outfit += " Don't forget an umbrella!"
    if "snow" in weather_condition.lower():
        outfit += " Wear warm boots."
    return f"Recommended outfit: {outfit}"

#print (outfit_recommender(temperature,weather_condition))



"""weather_mapping = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Cloudy",
    45: "Fog", 48: "Depositing rime fog", 55: "Light drizzle", 61: "Rain showers", 
    71: "Snow showers", 80: "Rain", 85: "Heavy snow showers"
}"""
## q={location}&units=metric

##{'latitude': 56.944096, 'longitude': 24.109085, 'generationtime_ms': 0.24020671844482422,
#  'utc_offset_seconds': 10800, 'timezone': 'Europe/Moscow', 'timezone_abbreviation': 'GMT+3',
#  'elevation': 6.0, 'current_units': {'time': 'iso8601', 'interval': 'seconds', 'temperature_2m': '°C',
#  'relative_humidity_2m': '%', 'precipitation': 'mm', 'rain': 'mm', 'showers': 'mm', 'snowfall': 'cm',
#  'apparent_temperature': '°C', 'wind_speed_10m': 'km/h', 'weather_code': 'wmo code', 'cloud_cover': '%'},
#  'current': {'time': '2025-05-16T19:30', 'interval': 900, 'temperature_2m': 8.3, 'relative_humidity_2m': 75,
#  'precipitation': 0.0, 'rain': 0.0, 'showers': 0.0, 'snowfall': 0.0, 'apparent_temperature': 5.1,
#  'wind_speed_10m': 12.2, 'weather_code': 1, 'cloud_cover': 30}, 'daily_units': {'time': 'iso8601',
#  'temperature_2m_max': '°C', 'temperature_2m_min': '°C', 'apparent_temperature_max': '°C',
#  'apparent_temperature_min': '°C', 'wind_speed_10m_max': 'km/h'}, 'daily': {'time': ['2025-05-16',
#  '2025-05-17', '2025-05-18', '2025-05-19', '2025-05-20', '2025-05-21', '2025-05-22'],
#  'temperature_2m_max': [8.6, 14.8, 13.1, 13.1, 13.6, 15.8, 13.2], 
# 'temperature_2m_min': [3.9, 6.9, 10.2, 9.4, 6.9, 7.3, 6.6], 'apparent_temperature_max': [5.6, 11.2, 11.3,
#  10.4, 11.6, 12.6, 11.2], 'apparent_temperature_min': [1.2, 3.4, 7.3, 5.6, 3.4, 3.1, 0.4], 
# 'wind_speed_10m_max': [13.0, 19.4, 19.4, 26.6, 28.3, 20.2, 33.8]}}