import airbyte as ab
from dotenv import load_dotenv
import os

load_dotenv()

API_SECRET = os.environ["API_SECRET"]

source = ab.get_source(
    "source-mixpanel",
    config={
        "credentials": {
            "username": os.environ["USERNAME"],
            "secret": os.environ["SECRET"],
            "project_id": os.environ["PROJECT_ID"],
        },
        "start_date": "2023-01-01T00:00:00Z",
        "end_date": "2023-01-01T01:00:00Z",
        "region": "EU",
        "attribution_window": 0,
        "date_window_size": 180,
    },
    install_if_missing=True,
)

source.check()
source.select_all_streams()
result = source.read()

for name, records in result.streams.items():
    print(f"Stream {name}: {len(list(records))} records")
