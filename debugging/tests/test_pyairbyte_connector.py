"""
There's as issue with 429 HTTP Response.
Breaking the limit of 60 requests per seconds freezes client
"""

import pytest
from clients import pyairbyte_connector

@pytest.mark.timeout(10, method="thread")
def test_connection_hanging():
    source = pyairbyte_connector()
    
    source.select_streams(["cohorts"])
    result = source.read()
    
    assert result == 429
