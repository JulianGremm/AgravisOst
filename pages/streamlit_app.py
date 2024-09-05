import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(layout="wide")

#sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

nav = get_nav_from_toml(
    "pages/.streamlit/pages.toml"
)

#st.logo("logo.png")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()

import pandas as pd
import os
from datetime import datetime, timedelta

from frequenz.client.common.metric import Metric
from frequenz.client.reporting import ReportingApiClient

# Ensure that environment variables are set
try:
    service_address = st.secrets["SCHNITTSTELLE"]
    api_key = st.secrets["API_KEY"]
except KeyError as e:
    raise KeyError(f"Missing environment variable: {e}")

client = ReportingApiClient(service_address=service_address, key=api_key)



data_listFürstenwalde = []


for i in range(10):
    match i:
        case 0:
            component_id = 394
        case _:  # This is the syntax to handle all other cases
            if i > 0:
                component_id = 395 + i

    data_sample = [
        sample async for sample in client.list_single_component_data(
            microgrid_id=116,
            component_id=component_id,
            metrics=[Metric.AC_ACTIVE_POWER],
            start_dt=datetime.fromisoformat(f"2024-09-04T22:00:00"),
            end_dt=datetime.fromisoformat(f"2024-09-05T00:00:00"),
            resolution=300,#300
        )
    ]
    data_listFürstenwalde.append(data_sample)