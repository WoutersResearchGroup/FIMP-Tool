import json
import streamlit as st
from pathlib import Path
from streamlit import session_state as state
from streamlit_elements import elements, sync, event
from types import SimpleNamespace
from .dashboard import Dashboard, P1, P3, P4, P2
import pandas as pd
def main():

    st.write(
        """
        Masterplan Dashboard
        =====================
        Based on the South African Furniture Industry Masterplan.\n
        Prepared for the South African Furniture Initiative (Not for official use).
        """
    )
    # Sidebar slider for selecting the KPI year range.
    st.session_state.sliderOne = st.sidebar.slider("Pillar 1-5: KPI", min_value=2010, max_value=2020, value=(2018, 2019))
    # Load and filter data for each KPI and convert to json for use in nivo charts (dashboard).
    df_P1_KPI = pd.read_csv("data/Pillar 1 KPI.csv")
    df_P1_KPI_year = df_P1_KPI[(df_P1_KPI['Year'] >= st.session_state.sliderOne[0]) & (df_P1_KPI['Year'] <= st.session_state.sliderOne[1])]
    df_P1_KPI_json = [{"id": row["Year"], "data": [
                        {"x": "Domestic Demand in Millions of US Dollars", "y": row["Apparent Consumption"]},
                        {"x": "Imports in Millions of US Dollars", "y": row["Import"]}
                    ]} for _, row in df_P1_KPI_year.iterrows()]
    df_P2_KPI = pd.read_csv("data/Pillar2_KPI.csv")
    df_P2_KPI_year = df_P2_KPI[(df_P2_KPI['TaxYear'] >= st.session_state.sliderOne[0]) & (df_P2_KPI['TaxYear'] <= st.session_state.sliderOne[1])]
    df_P2_KPI_json = [{"id": int(row["TaxYear"]), "Establishments": round(row["Establishments"]), "FTE": round(row["FTE"])} 
                      for _, row in df_P2_KPI_year.iterrows()]
    df_P3_KPI = pd.read_csv("data/Pillar3_KPI.csv")
    df_P3_KPI_year = df_P3_KPI[(df_P3_KPI['Year'] >= st.session_state.sliderOne[0]) & (df_P3_KPI['Year'] <= st.session_state.sliderOne[1])]
    df_P3_KPI_json = [{"id": row["Year"], "value": round(row["Export Value"])} for _, row in df_P3_KPI_year.iterrows()]
    df_P4_KPI = pd.read_csv("data/Pillar4_KPI.csv")
    df_P4_KPI_year = df_P4_KPI[(df_P4_KPI['t'] >= st.session_state.sliderOne[0]) & (df_P4_KPI['t'] <= st.session_state.sliderOne[1])]
    df_P4_KPI_json = [{"id": row["t"], "value": round(row["importVal"])} for _, row in df_P4_KPI_year.iterrows()]

    # Initialize the dashboard if it does not exist yet.
    if "dashboard_layout" not in state:
        board = Dashboard()
        w = SimpleNamespace(
            dashboard=board,
            P1=P1(board, 6, 0, 6, 6, minW=2, minH=4),
            P2=P2(board, 6, 0, 5, 7, minW=3, minH=3),
            P3=P3(board, 6, 0, 5, 7, minW=3, minH=3),
            P4=P4(board, 6, 0, 5, 7, minW=2, minH=4),
        )
        state.dashboard_layout = w

    # Set up the dashboard elements with the current layout in session_state
    with elements("dashboard"):
        event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)
        with state.dashboard_layout.dashboard(rowHeight=57):
            state.dashboard_layout.P1(json.dumps(df_P1_KPI_json))
            state.dashboard_layout.P2(json.dumps(df_P2_KPI_json))
            state.dashboard_layout.P3(json.dumps(df_P3_KPI_json))
            state.dashboard_layout.P4(json.dumps(df_P4_KPI_json))

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
