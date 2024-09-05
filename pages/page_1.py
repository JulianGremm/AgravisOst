import streamlit as st

import pandas as pd
import os
from datetime import datetime, timedelta

from frequenz.client.common.metric import Metric
from frequenz.client.reporting import ReportingApiClient

# Ensure that environment variables are set
try:
    service_address = st.secrets["CHNITTSTELLE"]
    api_key = st.secrets["PI_KEY"]
except KeyError as e:
    raise KeyError(f"Missing environment variable: {e}")

client = ReportingApiClient(service_address=service_address, key=api_key)

#st.write("This is just a sample page!")