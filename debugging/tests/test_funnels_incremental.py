import airbyte as ab
import requests
from dotenv import load_dotenv
import os
import pandas as pd
from clients import *


class TestFunnels:
    def test_sanity(self):
        source = pyairbyte_connector(start_date="2021-01-01T00:00:00Z", end_date="2025-01-01T00:00:00Z")
        streams = source.get_available_streams()
        assert "funnels" in streams

    def test_against_api(self):
        start_date = "2023-01-12"
        end_date = "2023-01-14"
        api_result = mixpanel_api_funnels(funnel_id=36152117, start_date=start_date, end_date=end_date)

        source = pyairbyte_connector(start_date=f"{start_date}T00:00:00Z", end_date=f"{end_date}T00:00:00Z")
        source.select_streams(["funnels"])
        pyairbyte_result = source.read()
        pyairbyte_result = pyairbyte_result["funnels"].to_pandas()

        pyairbyte_result = pyairbyte_result["steps"].apply(json.loads).explode().apply(pd.Series)
        pyairbyte_result["date"] = pyairbyte_result.loc[pyairbyte_result.index, "date"].values

        print(pyairbyte_result)
        print(api_result)
        print(api_result.columns)

        # assert api_result.shape[0] == pyairbyte_result.shape[0]
        # assert set(api_result["id"]) == set(pyairbyte_result["id"])
