from clients import *


class TestAnnotations:

    def test_sanity(self):
        source = pyairbyte_connector(start_date="2021-01-01T00:00:00Z", end_date="2025-01-01T00:00:00Z")
        streams = source.get_available_streams()
        assert "annotations" in streams
