import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_SECRET = os.environ["API_SECRET"]
USERNAME = os.environ["USERNAME"],
SECRET =  os.environ["SECRET"],
PROJECT_ID = int(os.environ["PROJECT_ID"]),

url = "https://data.mixpanel.com/api/2.0/export"

headers = {"accept": "text/plain"}

response = requests.get(url, headers=headers)

print(response.text)