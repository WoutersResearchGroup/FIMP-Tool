import json
from streamlit_elements import nivo, mui
from .dashboard import Dashboard

class P4(Dashboard.Item):

    def __call__(self, json_data=None, custom_data=None):
        try:
            if json_data is not None:
                data = json.loads(json_data)
            elif custom_data is not None:
                data = custom_data
            else:
                raise ValueError("Either 'json_data' or 'custom_data' must be provided.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data provided: {e}")

        with mui.Paper(key=self._key,
                       sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"},
                       elevation=1):
            with self.title_bar(dark_switcher=False):
                mui.Typography("Pillar 4 KPI: Raw Material Imports (including the Furniture Industry)", sx={"flex": 1})

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.Bar(
                    data=data,
                    keys=["value"],
                    indexBy="id",
                    margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                    axisBottom={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
                    axisLeft={"tickSize": 5, "tickPadding": 5, "tickRotation": 0, 'legend': "Raw Material Imports in Millions of US Dollars", "legendOffset": -60, 'legendPosition': 'middle'},
                    enableGridX=False,
                    enableGridY=True,
                    axisTop=None,
                    axisRight=None,
                    colors="#D8A5FF"
                )
