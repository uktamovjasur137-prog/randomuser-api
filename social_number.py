import requests

base_url = "https://randommer.io"

def generate_social_number():
    url = f"{base_url}/api/SocialNumber"

    headers = {"X-Api-Key": "7bad631663cf4d15aaa6b407a41cf183"}


    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None