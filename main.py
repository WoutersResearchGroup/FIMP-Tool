import streamlit as st

import views,components  
from utils.page import (page_group)
import pandas as pd


def main():
    page = page_group("p")

    with st.sidebar:
        st.title("Masterplan Menu")
        # Expander selection box
        # with st.expander("🧩 COMPONENTS", True):
        page.item("Dashboard", components.dashboard_app, default=True)

        # Expander selection box
        # with st.expander("✨ APPS", True):
        # page.item("Pillar 1", apps.gallery, default=True)

        # Adding all pillars as options
        page.item("Pillar 1", views.pillar_1)
        page.item("Pillar 2", views.pillar_2)
        page.item("Pillar 3", views.pillar_3)
        page.item("Pillar 4", views.pillar_4)
        page.item("Pillar 5", views.pillar_5)
        page.item("Methodology", views.methodology)

        st.subheader("Year Selection")
        # From constant display to within each pillar selected
        # st.session_state.sliderP1DS = st.sidebar.slider("Pillar 1: DS", min_value=2010, max_value=2020, value=(2020))
        # sliderTwo = st.sidebar.slider("Years for Pillar 4-5", min_value=2001, max_value=2011, value=(2001, 2011))

        # def get_session_state():
        #   if 'sliderOne' not in st.session_state:
        #      st.session_state.sliderOne = st.sidebar.slider("Years for Pillar 1-3", min_value=2010, max_value=2020,
        #                                                value=(2018, 2019))
    page.show()


if __name__ == "__main__":
    st.set_page_config(page_title="South African Furniture Industry Masterplan Dashboard", page_icon="🎈", layout="wide")
    main()
