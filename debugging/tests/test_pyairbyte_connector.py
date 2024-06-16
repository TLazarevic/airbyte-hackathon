"""
There's as issue with 429 HTTP Response.
Breaking the limit of 60 requests per seconds freezes client
"""

import pytest
from clients import pyairbyte_connector
import threading


def test_connection_hanging():
    pyairbyte_connector.select_streams(["cohorts"])

    thread = threading.Thread(target=pyairbyte_connector.read())

    thread.start()
    result = thread.join(timeout=10)

    if thread.is_alive():
        pytest.fail("pyairbyte connection is still trying to connect")
    else:
        # assert result, it should returns 429 HTTP code
        assert result == 429
