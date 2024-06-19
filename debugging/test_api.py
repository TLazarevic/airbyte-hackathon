import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_SECRET = os.environ["API_SECRET"]
USERNAME = os.environ["USERNAME"]
SECRET = os.environ["SECRET"]
PROJECT_ID = int(os.environ["PROJECT_ID"])

#url = f"https://eu.mixpanel.com/api/query/cohorts/list?project_id={PROJECT_ID}"
url = f"https://eu.mixpanel.com/api/query/engage?project_id={PROJECT_ID}"

headers = {
    "accept": "text/plain",
}

response = requests.get(url, headers=headers, auth=(USERNAME, SECRET))

print(response.status_code)
print(response.text)
