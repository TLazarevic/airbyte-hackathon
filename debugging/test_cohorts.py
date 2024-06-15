import airbyte as ab
import requests
from dotenv import load_dotenv
import os


def get_api_cohorts():
    load_dotenv()

    USERNAME = os.environ["USERNAME"]
    SECRET = os.environ["SECRET"]
    PROJECT_ID = int(os.environ["PROJECT_ID"])

    url = f"https://eu.mixpanel.com/api/query/cohorts/list?project_id={PROJECT_ID}"

    headers = {
        "accept": "text/plain",
    }

    return requests.get(url, headers=headers, auth=(USERNAME, SECRET))


def get_pyairbyte_cohorts():
    load_dotenv()

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
    
    source.select_streams(["cohorts"])
    return source.read()


class TestCohorts:
    def test_count(self):
        result_api = get_api_cohorts()
        results_pyairbyte=get_pyairbyte_cohorts()
        
        print(result_api)
        print(results_pyairbyte)
