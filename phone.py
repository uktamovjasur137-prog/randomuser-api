import requests

base_url = "https://randommer.io"

def generate_phone_numbers(country_code, quantity):
    url = f"{base_url}/api/Phone/Generate"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    query_params = {
        "Countrycode": country_code,
        "Quantity": quantity
    }
    response = requests.get(url=url, headers=headers, params=query_params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_imeis(quantity):
    url = f"{base_url}/api/Phone/IMEI"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    query_params = {
        "Quantity": quantity
    }
    response = requests.get(url=url, headers=headers, params=query_params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def validate_number(telephone, country_code):
    url = f"{base_url}/api/Phone/Validate"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    query_params = {
        "CountryCode": country_code,
        "telephone": telephone,
    }
    response = requests.get(url=url, headers=headers, params=query_params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_available_countries():
    url = f"{base_url}/api/Phone/Countries"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}
    
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None