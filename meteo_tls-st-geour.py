import requests

def get_weather_data(city_name, api_key):
    """
    Récupère les données météorologiques pour une ville donnée.

    Args:
        city_name (str): Le nom de la ville pour laquelle récupérer les données météorologiques.
        api_key (str): La clé API pour accéder au service OpenWeatherMap.

    Returns:
        dict: Les données météorologiques sous forme de dictionnaire JSON.
    """
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def print_forecast(city_name, forecast_data):
    """
    Affiche les prévisions météorologiques pour une ville donnée.

    Args:
        city_name (str): Le nom de la ville pour laquelle afficher les prévisions.
        forecast_data (dict): Les données de prévision météorologique.

    Returns:
        None
    """
    print(f"Prévisions pour {city_name}:")
    if 'list' in forecast_data:
        for forecast in forecast_data['list']:
            date = forecast['dt_txt']
            temp_min = forecast['main']['temp_min']
            temp_max = forecast['main']['temp_max']
            print(f"{date}: Min {temp_min}°C, Max {temp_max}°C")
    else:
        print("Aucune donnée de prévision disponible.")

api_key = "52efdb79afc4b99cc384ab2aedc451b5"
cities = ["Toulouse,FR", "Saint-Geours-de-Maremne,FR"]

for city in cities:
    weather_data = get_weather_data(city, api_key)
    print_forecast(city, weather_data)