import requests
import json


UPLOAD_URL = None  # You can put your upload url here.
AUTH_TOKEN = None  # You can put your auth token here.

UPLOAD_DATA = None  # You can put your data here.


def interactive_upload():
    if UPLOAD_DATA is None:
        filename = input("Please enter the name of the file to upload.\n> ")
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except Exception as e:
            print(e)
            return
    else:
        data = UPLOAD_DATA

    url = UPLOAD_URL if UPLOAD_URL is not None else input("Please enter your upload url.\n> ").strip()
    token = AUTH_TOKEN if AUTH_TOKEN is not None else input("Please enter your auth token.\n> ").strip()

    build_type = input("Please enter the build type you are uploading to [alpha/beta]. Default is normal.\n> ").strip()
    if build_type.lower() == "alpha":
        url = f"{url}/alpha"
    elif build_type.lower() == "beta":
        url = f"{url}/beta"

    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    response = requests.put(url, headers=headers, json=data)
    print(f"{response}: {response.text}")


if __name__ == "__main__":
    interactive_upload()
