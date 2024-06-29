import airbyte as ab
from dotenv import load_dotenv
import os

load_dotenv()

source = ab.get_source(
    "source-mixpanel",
    config={
        "credentials": {
            "username": os.environ["USERNAME"],
            "secret": os.environ["SECRET"],
            "project_id": int(os.environ["PROJECT_ID"]),
        },
        "start_date": "2020-01-01T00:00:00Z",
        "end_date": "2025-01-01T00:10:00Z",
        "region": "EU",
        "attribution_window": 0,
        "date_window_size": 180,
    },
    install_if_missing=True,
)

source.check()
# source.select_all_streams()
source.select_streams(["funnels"])
result = source.read()

for name, records in result.streams.items():
    print(f"Stream {name}: {len(list(records))} records")

pyairbyte_result_df = result["funnels"].to_pandas()
print(pyairbyte_result_df.head())
pyairbyte_result_df.to_csv("funnels.csv")
