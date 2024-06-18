# Issues

Every issue which we found will be displayed as item in list below.

## Issue Template
- **Issue:** *Issue Name*

  Description
  -  **Proposed improvement:** *Proposed Improvement*
  -  **Bug fix provided:** Yes|No
  -  *Link to bugfix PR*


## List
- **Issue:** Connecting to mixpanel source without specified region fails, even though the region is not marked as mandatory
  - **Proposed improvement:** Region default value is used when omitted (US)
  - **Bug fix provided:** No

- **Issue:** Connecting to a mixpanel source fails with Failure Reason: "'Unable to connect to stream cohorts - Unable to perform a request. Payment Required.'"
  - **Proposed improvement:** A warning is issued, or a more user friendly error that indicates that the Mixpanel account must be a paid one to be able to use the API. This should be added to the docs as well
  - **Bug fix provided:** No

- **Issue:** What is the issue with the exports stream?

  Looks like there are no events.
  - **Proposed improvement:** *Proposed Improvement*
  - **Bug fix provided:** Yes|No

- **Issue:** 492 is not handled properly

  We haven't got 429 response when we reached query limit as it's described in docs. It seems that the connector hangs in order to prevent crossing the limit.
  - **Proposed improvement:** It seems that the sleeping behavior is part of the connector itself, and not the pyairbyte, so it doesn't seem to be easily resolvable.
  - **Bug fix provided:** No
