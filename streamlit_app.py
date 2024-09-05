import streamlit as st


pg = st.navigation([st.Page("pages/page_1.py"), st.Page("pages/page_2.py")])


pg.run()
