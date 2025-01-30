import json
from streamlit_elements import mui, nivo
from .dashboard import Dashboard

class P1(Dashboard.Item):
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
                mui.Typography("Pillar 1 KPIs: Furniture Imports and Domestic Demand")

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.Bar(
                    data=data,
                    keys=["Domestic Demand in Millions of US Dollars", "Imports in Millions of US Dollars"],
                    indexBy="id",
                    margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                    padding=0.2,
                    groupMode="grouped",
                    colors=["#D8A5FF", "#CD43FB"],
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "Year",
                        "legendPosition": "middle",
                        "legendOffset": 32
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "Value (Millions of US Dollars)",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    legends=[
                        {
                            "dataFrom": "keys",
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemWidth": 80,
                            "itemHeight": 20,
                            "itemTextColor": "#999",
                            "symbolSize": 15,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ]
                )
