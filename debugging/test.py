import airbyte as ab
from dotenv import load_dotenv
import os

load_dotenv()

API_SECRET = os.environ["API_SECRET"]

# TODO: Test all connection options

# source_config = ProjectSecret(api_secret=API_SECRET)
source = ab.get_source(
    "source-mixpanel",
    config={
        "credentials": {"api_secret": API_SECRET, "option_title": "Project Secret"},
        "region": "US",
    },
    install_if_missing=True,
)

source.check()
source.select_all_streams()
result = source.read()

for name, records in result.streams.items():
    print(f"Stream {name}: {len(list(records))} records")
