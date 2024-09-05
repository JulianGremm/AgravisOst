import streamlit as st

import pandas as pd
import os
from datetime import datetime, timedelta

from frequenz.client.common.metric import Metric
from frequenz.client.reporting import ReportingApiClient

# Ensure that environment variables are set
try:
    service_address = "$SCHNITTSTELLE"
    api_key = "$API_KEY"
except KeyError as e:
    raise KeyError(f"Missing environment variable: {e}")
st.write(api_key)
#client = ReportingApiClient(service_address=service_address, key=api_key)

#st.write("This is just a sample page!")