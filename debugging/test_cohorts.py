import airbyte as ab
import requests
from dotenv import load_dotenv
import os
import pandas as pd


def get_api_cohorts():
    # Cohorts api returns a list of cohort objects
    
    load_dotenv()

    USERNAME = os.environ["USERNAME"]
    SECRET = os.environ["SECRET"]
    PROJECT_ID = int(os.environ["PROJECT_ID"])

    url = f"https://eu.mixpanel.com/api/query/cohorts/list?project_id={PROJECT_ID}"

    headers = {
        "accept": "text/plain",
    }

    # result = requests.get(url, headers=headers, auth=(USERNAME, SECRET)).json()
    result = [{"id": 1478097, "project_id": 2529987, "name": "Cohort1", "description": "", "data_group_id": None, "count": 2, "is_visible": 1, "created": "2021-09-14 15:57:43"}, {"id": 4269287, "project_id": 2529987, "name": "cohort2", "description": "", "data_group_id": None, "count": 0, "is_visible": 1, "created": "2024-05-14 10:02:05"}]
    return pd.DataFrame.from_records(result)



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
            "region": "EU",
        },
        install_if_missing=True,
    )
    
    source.select_streams(["cohorts"])
    result = source.read()

    return result['cohorts'].to_pandas()


class TestCohorts:
    def test_count(self):
        api_result = get_api_cohorts()
        pyairbyte_result = get_pyairbyte_cohorts()
        
        print(api_result)
        print(pyairbyte_result)

        assert api_result.shape[0] == pyairbyte_result.shape[0]