import json
from streamlit_elements import mui, nivo
from .dashboard import Dashboard
import math

class P1(Dashboard.Item):


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
                mui.Typography("Pillar 1 KPIs: Furniture Imports and Domestic Demand")

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.RadialBar(
                    data=data,
                    startAngle={10},
                    endAngle={270},
                    innerRadius={0.5},
                    padAngle={0.1},
                    cornerRadius={3},
                    margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                    legends=[
                        {
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
                    ],
                    colors=["#D8A5FF","#CD43FB"]
                    #colors={"scheme": 'purpleRed_green'}
                    # Add other styling and customization options
                )
