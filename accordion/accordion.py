#https://www.dash-mantine-components.com/components/accordion 

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, html

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

accordion = html.Div(
    [
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    "This is the content of the first section",
                    title="Item 1",
                    item_id="item-1",
                ),
                dbc.AccordionItem(
                    "This is the content of the second section",
                    title="Item 2",
                    item_id="item-2",
                ),
                dbc.AccordionItem(
                    "This is the content of the third section",
                    title="Item 3",
                    item_id="item-3",
                ),
            ],
            id="accordion",
            active_item="item-1",
        ),
        html.Div(id="accordion-contents", className="mt-3"),
    ]
)


@app.callback(
    Output("accordion-contents", "children"),
    [Input("accordion", "active_item")],
)
def change_item(item):
    return f"Item selected: {item}"


app.layout = dbc.Container(
    [
        accordion
        ],
    fluid=True
    )


if __name__ == "__main__":
    app.run_server(debug=True, port=1234)