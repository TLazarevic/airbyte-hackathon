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

        source = pyairbyte_connector(start_date="2020-01-01T00:00:00Z", end_date="2025-01-01T00:00:00Z")
        source.select_streams(["cohort_members"])
        pyairbyte_result = source.read()
        pyairbyte_result = pyairbyte_result["cohort_members"].to_pandas()

        assert set(api_result["$distinct_id"]) == set(pyairbyte_result["distinct_id"])
        assert api_result.shape[0] == pyairbyte_result.shape[0]
