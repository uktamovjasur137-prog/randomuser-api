import requests

base_url = "https://randommer.io"

def get_name(name_type, quantity):
    url = f"{base_url}/api/Name"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    query_params = {
        "nameType": name_type,
        "quantity": quantity
    }
    response = requests.get(url=url, headers=headers, params=query_params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_name_suggestions(starting_with):
    url = f"{base_url}/api/Name/Suggestions"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}
    
    query_params = {
    "startingWith": starting_with
    }

    response = requests.get(url=url, headers=headers, params=query_params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_name_cultures():
    url = f"{base_url}/api/Name/Cultures"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    

    
def get_business_names(number: int, culture_code="en"):
    url = f"{base_url}/api/Name/BusinessName"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    query_params = {"number": number, "cultureCode":culture_code}

    response = requests.get(url=url, headers=headers, params=query_params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    

def get_brand_name(starting_words):
    url = f"{base_url}/api/Name/BrandName"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    query_params = {"startingWords": starting_words}

    response = requests.get(url=url, headers=headers, params=query_params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None