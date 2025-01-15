import json

from streamlit_elements import mui
from .dashboard import Dashboard


class P2(Dashboard.Item):

    DEFAULT_COLUMNS = [
        { "field": 'id', "headerName": 'Year', "width": 90 },
        { "field": 'Establishments', "headerName": 'Establishments', "width": 150, "editable": True, },
        { "field": 'FTE', "headerName": 'Employment', "width": 150, "editable": True, },
        #{ "field": 'age', "headerName": 'Age', "type": 'number', "width": 110, "editable": True, },
    ]
    DEFAULT_ROWS = [
        { "id": 1, "lastName": 'Snow', "firstName": 'Jon', "age": 35 },
        { "id": 2, "lastName": 'Lannister', "firstName": 'Cersei', "age": 42 },
        { "id": 3, "lastName": 'Lannister', "firstName": 'Jaime', "age": 45 },
        { "id": 4, "lastName": 'Stark', "firstName": 'Arya', "age": 16 },
        { "id": 5, "lastName": 'Targaryen', "firstName": 'Daenerys', "age": None },
        { "id": 6, "lastName": 'Melisandre', "firstName": None, "age": 150 },
        { "id": 7, "lastName": 'Clifford', "firstName": 'Ferrara', "age": 44 },
        { "id": 8, "lastName": 'Frances', "firstName": 'Rossini', "age": 36 },
        { "id": 9, "lastName": 'Roxie', "firstName": 'Harvey', "age": 65 },
    ]

    def _handle_edit(self, params):
        print(params)

    def __call__(self, json_data):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            data = self.DEFAULT_ROWS

        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar(padding="10px 15px 10px 15px", dark_switcher=False):
                mui.Typography("Pillar 2 KPI: Furniture Employment and Total Establishments")

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                mui.DataGrid(
                    columns=self.DEFAULT_COLUMNS,
                    rows=data,
                    pageSize=5,
                    rowsPerPageOptions=[5],
                    colors={"scheme": 'purpleRed_green'}
                    #checkboxSelection=True,
                    #disableSelectionOnClick=True,
                    #onCellEditCommit=self._handle_edit,
                )
