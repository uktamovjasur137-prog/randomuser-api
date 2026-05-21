import requests

base_url = "https://randommer.io"

def get_cultures():
    url = f"{base_url}/api/Misc/Cultures"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_random_address(number: int, culture="en"):
    url = f"{base_url}/api/Misc/Random-Address"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    query_params = {"number": number, "culture":culture}

    response = requests.get(url=url, headers=headers, params=query_params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
print(get_random_address(3))