import ipdata
import requests

key_ipdata = "93ff95c5160e3f21cb9bb6ff795a6f577709ee53f01726d9823c6cb1"
key_geo = "5eb278b9abacf3f5278bc0472c32353fb046867f"

def get_location_and_currency():
    ipdata_service = ipdata.IPData(key_ipdata)
    response = ipdata_service.lookup()
    return response['country_code'], response['currency']['code']

def convert_currency(from_currency, to_currency, amount):
    url = "https://api.getgeoapi.com/v2/currency/convert"
    parameters = {
        "api_key": key_geo,
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "format": "json"
    }
    response = requests.get(url, parameters)
    data = response.json()
    return round(float(data['rates'][to_currency]['rate_for_amount']), 2)

# Uso de las funciones
user_country, user_currency = get_location_and_currency()
result = convert_currency("HNL", user_currency, 700)
print(result)