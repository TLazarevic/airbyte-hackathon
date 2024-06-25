import airbyte as ab
import requests
from dotenv import load_dotenv
import os
import pandas as pd
from clients import *


class TestCohortMembers:
    """
    Detected begavior: PyAirbyte's cohort members streams returns rows with duplicate distinct ids.
    """

    def test_against_api(self):
        api_result = mixpanel_api_cohort_members()
        api_result["cohort_id"] = api_result["cohort_id"].astype(str)

        source = pyairbyte_connector(start_date="2020-01-01T00:00:00Z", end_date="2025-01-01T00:00:00Z")
        source.select_streams(["cohort_members"])
        pyairbyte_result = source.read()
        pyairbyte_result = pyairbyte_result["cohort_members"].to_pandas()
        pyairbyte_result["cohort_id"] = pyairbyte_result["cohort_id"].astype(str)

        cohort_ids = set(pyairbyte_result["cohort_id"])
        for cohort_id in cohort_ids:
            assert set(api_result[api_result["cohort_id"] == cohort_id]["distinct_id"]) == set(
                pyairbyte_result[pyairbyte_result["cohort_id"] == cohort_id]["distinct_id"]
            )
            assert api_result.shape[0] == pyairbyte_result.shape[0]
