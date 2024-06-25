import requests
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

API_SECRET = os.environ["API_SECRET"]
USERNAME = os.environ["USERNAME"]
SECRET = os.environ["SECRET"]
PROJECT_ID = int(os.environ["PROJECT_ID"])

# url = f"https://eu.mixpanel.com/api/query/cohorts/list?project_id={PROJECT_ID}"
# url = f"https://eu.mixpanel.com/api/query/engage?project_id={PROJECT_ID}"
url = f"https://eu.mixpanel.com/api/query/funnels?project_id={PROJECT_ID}&funnel_id=36152117&from_date=2023-01-12&to_date=2023-01-14"

# headers = {"accept": "application/json", "content-type": "application/x-www-form-urlencoded"}
headers = {"accept": "application/json"}

response = requests.get(url, headers=headers, auth=(USERNAME, SECRET))
# response = requests.get(url, headers=headers, data=payload, auth=(USERNAME, SECRET)).json()["results"]

print(response.status_code)
print(response.text)

print(pd.DataFrame.from_records(response.json()["data"]))
