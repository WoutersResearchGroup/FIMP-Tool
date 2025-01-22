import streamlit as st
import views,components
from utils.page import (page_group)
import pandas as pd

def main():
    page = page_group("p")
    with st.sidebar:
        st.title("Masterplan Menu")
        # Set the KPI dashboard as the default view.
        page.item("Dashboard", components.dashboard_app, default=True)
        # Add all the Pillar DSIs and the methodology as seperate views.
        page.item("Pillar 1", views.pillar_1)
        page.item("Pillar 2", views.pillar_2)
        page.item("Pillar 3", views.pillar_3)
        page.item("Pillar 4", views.pillar_4)
        page.item("Pillar 5", views.pillar_5)
        page.item("Methodology", views.methodology)
        # Create a subheading for the year selection slider in the sidebar.
        st.subheader("Year Selection")
    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="South African Furniture Industry Masterplan Dashboard", page_icon="🎈", layout="wide")
    main()
