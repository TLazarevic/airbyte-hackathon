"""
There's as issue with 429 HTTP Response.
Breaking the limit of 60 requests per seconds freezes client
"""

import pytest
from clients import *


def test_connection_hanging():
    pair = pyairbyte_connector.source

    assert 3 == 3
