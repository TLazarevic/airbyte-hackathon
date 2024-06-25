import airbyte as ab
import requests
from dotenv import load_dotenv
import os
import pandas as pd
from clients import *


class TestCohorts:
    def test_against_api(self):
        start_date = "2023-01-12"
        end_date = "2023-01-14"
        api_result = mixpanel_api_funnels(funnel_id=36152117, start_date=start_date, end_date=end_date)

        source = pyairbyte_connector(start_date=f"{start_date}T00:00:00Z", end_date=f"{end_date}T00:00:00Z")
        source.select_streams(["funnels"])
        pyairbyte_result = source.read()
        pyairbyte_result = pyairbyte_result["funnels"].to_pandas()

        assert api_result.shape[0] == pyairbyte_result.shape[0]
        assert set(api_result["id"]) == set(pyairbyte_result["id"])
