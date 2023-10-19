import requests

# Get a api key in https://www.weatherapi.com/ 
api_key = ""

def get_current_weather(place_request):
    url = "http://api.weatherapi.com/v1/forecast.json"
    users_params = {
        "key":api_key,
        "q":place_request,
        "days":2,
        "aqi":"yes"
    }
    response = requests.get(url=url, params=users_params)
    print(response.json())

    return response.json()

def get_autocomplete_weather(text):
    url = "http://api.weatherapi.com/v1/search.json"
    users_params = {
        "key":api_key,
        "q":f"{text}"
    }
    response = requests.get(url=url, params=users_params).json()

    new_response = []
    if text != "":
        for item in response:
            name = item['name']
            region = item['region']
            country = item['country']
            new_response.append(f"{name}, {region}, {country}")

    return new_response