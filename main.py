import requests

base_url = "https://randommer.io"

def get_card():
    url = f"{base_url}/api/Card"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    query_params = {"type": "Visa"}


    response = requests.get(url=url, headers=headers, params=query_params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_card_types():
    url =  url = f"{base_url}/api/Card/Types"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

print(get_card())
print(get_card_types())