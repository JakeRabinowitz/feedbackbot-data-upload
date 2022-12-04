import requests
import json

UPLOAD_URL = "https://www.discordfeedbackbot.com/upload/"
# You can upload Alpha or Beta data using the "development_stage" query parameter.
# Alpha: https://www.discordfeedbackbot.com/upload/?development_stage=alpha
# Beta: https://www.discordfeedbackbot.com/upload/?development_stage=beta

AUTH_TOKEN = None  # You can put your auth token here.

# You can put your json string here, or leave it as None to be prompted to upload a json file.
UPLOAD_DATA_JSON = None


def interactive_upload():
    if UPLOAD_DATA_JSON is None:
        filename = input("Please enter the name of the file to upload.\n> ")
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except Exception as e:
            print(e)
            return
    else:
        data = json.loads(UPLOAD_DATA_JSON)

    token = AUTH_TOKEN if AUTH_TOKEN is not None else input("Please enter your auth token.\n> ").strip()

    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    response = requests.put(UPLOAD_URL, headers=headers, json=data)
    print(f"{response}: {response.text}")


if __name__ == "__main__":
    interactive_upload()
