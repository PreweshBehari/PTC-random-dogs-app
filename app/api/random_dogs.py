# Import packages
import requests

def get_api_data(data=[], times=5):
    # Stop recursive call when condition is met
    if times == 0:
        return data

    # API call
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    api_data = response.json()

    # Process response
    if "status" in api_data and api_data["status"] == "success":
        data.append(api_data["message"])

    # Make next call
    return get_api_data(data, times - 1)