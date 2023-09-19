import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, html

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

#contents =

app.layout = dbc.Container(
    [
        #contants
        ],
    fluid=True
    )

if __name__ == "__main__":
    app.run_server(debug=True, port=1234)
