import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_SECRET = os.environ["API_SECRET"]
USERNAME = os.environ["USERNAME"]
SECRET = os.environ["SECRET"]
PROJECT_ID = int(os.environ["PROJECT_ID"])

# url = f"https://eu.mixpanel.com/api/query/cohorts/list?project_id={PROJECT_ID}"
url = f"https://eu.mixpanel.com/api/query/engage?project_id={PROJECT_ID}"

headers = {"accept": "application/json", "content-type": "application/x-www-form-urlencoded"}

for cohort_id in ["1478097", "4269287"]:
    payload = {"filter_by_cohort": f'{{"id":{cohort_id}}}'}
    response = requests.post(url, headers=headers, data=payload, auth=(USERNAME, SECRET))
    # response = requests.get(url, headers=headers, data=payload, auth=(USERNAME, SECRET)).json()["results"]

    print(response.status_code)
    print(response.text)
