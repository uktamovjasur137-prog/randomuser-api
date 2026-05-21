import requests

base_url = "https://randommer.io"

def get_crypto_types():
    url = f"{base_url}/api/Finance/CryptoAddress/Types"
    
    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}
    
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def get_crypto_address():
    url = f"{base_url}/api/Finance/CryptoAddress"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    query_params = {"cryptoType": "Bitcoin"}

    response = requests.get(url=url, headers=headers, params=query_params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    


def get_country_code(countryCode):
    url = f"{base_url}/api/Finance/Iban/{countryCode}"

    headers = {
        "X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        return response.json()

    print(f"Error: {response.status_code}")
    print(response.text)
    return None

def get_available_countries():
    url = f"{base_url}/api/Finance/Countries"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}
    
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def post_data(country, vat):
    url = f"{base_url}/api/Finance/Vat/Validator"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    query_params = {"country": country, "vat": vat}

    response = requests.post(url=url, headers=headers, params=query_params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
