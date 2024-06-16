import pytest
import requests
from dotenv import load_dotenv
import os
import airbyte as ab
import pandas as pd


load_dotenv()

API_SECRET = os.environ["API_SECRET"]
USERNAME = os.environ["USERNAME"]
SECRET = os.environ["SECRET"]
PROJECT_ID = int(os.environ["PROJECT_ID"])


@pytest.fixture
def pyairbyte_connector():
    source = ab.get_source(
        "source-mixpanel",
        config={
            "credentials": {
                "username": os.environ["USERNAME"],
                "secret": os.environ["SECRET"],
                "project_id": int(os.environ["PROJECT_ID"]),
            },
            "start_date": "2023-01-01T00:00:00Z",
            "end_date": "2023-01-01T00:10:00Z",
            "region": "EU",
            "attribution_window": 0,
            "date_window_size": 180,
        },
        install_if_missing=True,
    )

    return source


@pytest.fixture
def airybyte_connector():
    def cohorts():
        url = f"https://eu.mixpanel.com/api/query/cohorts/list?project_id={PROJECT_ID}"

        headers = {
            "accept": "text/plain",
        }

        result = requests.get(url, headers=headers, auth=(USERNAME, SECRET)).json()
        return pd.DataFrame.from_records(result)
