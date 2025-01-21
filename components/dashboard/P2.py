import json
from streamlit_elements import mui
from .dashboard import Dashboard

class P2(Dashboard.Item):

    DEFAULT_COLUMNS = [
        { "field": 'id', "headerName": 'Year', "width": 90 },
        { "field": 'Establishments', "headerName": 'Total Establishments', "width": 150, "editable": True, },
        { "field": 'FTE', "headerName": ' Total Employment', "width": 150, "editable": True, }
    ]
    def _handle_edit(self, params):
        print(params)

    def __call__(self, json_data):
        try:
            if json_data is not None:
                data = json.loads(json_data)
            else:
                raise ValueError("json_data must be provided.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data provided: {e}")

        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar(padding="10px 15px 10px 15px", dark_switcher=False):
                mui.Typography("Pillar 2 KPI: Furniture Industry Employment and Total Establishments")

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                mui.DataGrid(
                    columns=self.DEFAULT_COLUMNS,
                    rows=data,
                    pageSize=5,
                    rowsPerPageOptions=[5],
                    colors={"scheme": 'purpleRed_green'}
                )
