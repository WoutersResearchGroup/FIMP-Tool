import json
from streamlit_elements import nivo, mui
from .dashboard import Dashboard

class P4(Dashboard.Item):

    DEFAULT_DATA = [
        {"id": "Category A", "value": 30, "color": "hsl(200, 70%, 50%)"},
        {"id": "Category B", "value": 70, "color": "hsl(240, 70%, 50%)"},
        # Add more default data as needed
    ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._theme = {
    #         "dark": {
    #             "background": "#252526",
    #             "textColor": "#FAFAFA",
    #             "tooltip": {
    #                 "container": {
    #                     "background": "#3F3F3F",
    #                     "color": "FAFAFA",
    #                 }
    #             }
    #         },
    #         "light": {
    #             "background": "#FFFFFF",
    #             "textColor": "#31333F",
    #             "tooltip": {
    #                 "container": {
    #                     "background": "#FFFFFF",
    #                     "color": "#31333F",
    #                 }
    #             }
    #         }
    #     }

    def __call__(self, json_data=None, custom_data=None):
        try:
            if json_data is not None:
                data = json.loads(json_data)
            elif custom_data is not None:
                data = custom_data
            else:
                data = self.DEFAULT_DATA
        except json.JSONDecodeError:
            data = self.DEFAULT_DATA

        with mui.Paper(key=self._key,
                       sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"},
                       elevation=1):
            with self.title_bar(dark_switcher=False):
                mui.Typography("Pillar 4 KPI: Raw Material Imports (including Furniture Industry)", sx={"flex": 1})

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

# Exports in Thousands of US Dollars"
