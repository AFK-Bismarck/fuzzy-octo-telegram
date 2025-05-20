
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
    
