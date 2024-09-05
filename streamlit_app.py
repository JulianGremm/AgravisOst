import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

pg = st.navigation([st.Page("pages/page_1.py"), st.Page("pages/page_2.py")])


pg.run()
