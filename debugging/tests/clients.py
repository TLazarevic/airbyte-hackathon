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


def pyairbyte_connector(start_date="2023-01-01T00:00:00Z", end_date="2023-01-02T00:00:00Z"):
    source = ab.get_source(
        "source-mixpanel",
        config={
            "credentials": {
                "username": USERNAME,
                "secret": SECRET,
                "project_id": PROJECT_ID,
            },
            "start_date": start_date,
            "end_date": end_date,
            "region": "EU",
            "attribution_window": 0,
            "date_window_size": 180,
        },
        install_if_missing=True,
    )

    return source


def mixpanel_api_cohorts():
    url = f"https://eu.mixpanel.com/api/query/cohorts/list?project_id={PROJECT_ID}"

    headers = {
        "accept": "text/plain",
    }

    result = requests.get(url, headers=headers, auth=(USERNAME, SECRET)).json()
    return pd.DataFrame.from_records(result)


def mixpanel_api_cohort_members():
    url = f"https://eu.mixpanel.com/api/query/engage?project_id={PROJECT_ID}"

    headers = {"accept": "text/plain", "content-type": "application/x-www-form-urlencoded"}

    # Actual cohort IDs, this saves on API requests
    results = []
    for cohort_id in ["1478097", "4269287"]:
        payload = {"filter_by_cohort": f'{{"id":{cohort_id}}}'}
        response = requests.post(url, headers=headers, data=payload, auth=(USERNAME, SECRET)).json()["results"]
        for result in response:
            results.append({"cohort_id": cohort_id, "distinct_id": result["$distinct_id"]})

    return pd.DataFrame(results)


def mixpanel_api_funnels(funnel_id, start_date, end_date):
    url = f"https://eu.mixpanel.com/api/query/funnels?project_id={PROJECT_ID}&funnel_id={funnel_id}&from_date={start_date}&to_date={end_date}"

    headers = {"accept": "text/plain", "content-type": "application/x-www-form-urlencoded"}

    result = requests.get(url, headers=headers, auth=(USERNAME, SECRET)).json()
    return pd.DataFrame.from_records(result)
