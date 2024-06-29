import airbyte as ab
import requests
from dotenv import load_dotenv
import os
import pandas as pd
from clients import *


class TestEngage:
    def test_sanity(self):
        source = pyairbyte_connector(start_date="2021-01-01T00:00:00Z", end_date="2025-01-01T00:00:00Z")
        streams = source.get_available_streams()
        assert "engage" in streams
