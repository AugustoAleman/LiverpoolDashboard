import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt
import pathlib

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "Liverpool Human Analytics Dashboard"

server = app.server
app.config.suppress_callback_exceptions = True

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()

# Read data
# In this simplified example, we're not reading the data

sector_list = ["Todos", "Liverpool", "Suburbia", "CeDis", "Otros"]

def description_card():
    return html.Div(
        id="description-card",
        children=[
            html.H5("Liverpool Analytics"),
            html.H3("Bienvenido al Dashboard de Human Analytics de Liverpool"),
            html.Div(
                id="intro",
                children="Explora los datos más recientes de Human Analytics dentro de Liverpool. Selecciona si deseas visualizar un sector o periodo específicos.",
            ),
        ],
    )

def generate_control_card():
    return html.Div(
        id="control-card",
        children=[
            html.P("Selecciona un Sector"),
            dcc.Dropdown(
                id="clinic-select",
                options=[{"label": i, "value": i} for i in sector_list],
                value=sector_list[0],
            ),
            html.Br(),
            html.P("Selecciona un periodo"),
            dcc.DatePickerRange(
                id="date-picker-select",
                start_date=dt(2019, 1, 1),
                end_date=dt(2019, 12, 31),
                min_date_allowed=dt(2019, 1, 1),
                max_date_allowed=dt(2023, 12, 31),
                initial_visible_month=dt(2019, 1, 1),
            ),
        ],
    )

# Define layout
app.layout = html.Div(
    id="app-container",
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(src=app.get_asset_url("liverpool-logo.png"))],
        ),
        # Left column
        html.Div(
            id="left-column",
            className="four columns",
            children=[description_card(), generate_control_card()],
        ),
        # Right column
        html.Div(
            id="right-column",
            className="eight columns",
            children=[
                # Histogram 1
                html.Div(
                    id="histogram-1",
                    children=[
                        html.B("Histograma 1"),
                        dcc.Graph(
                            id="histogram-1-graph",
                            config={"displayModeBar": False},
                        ),
                    ],
                ),
                # Histogram 2
                html.Div(
                    id="histogram-2",
                    children=[
                        html.B("Histograma 2"),
                        dcc.Graph(
                            id="histogram-2-graph",
                            config={"displayModeBar": False},
                        ),
                    ],
                ),
            ],
        ),
    ],
)

# Callback to update histograms
@app.callback(
    Output("histogram-1-graph", "figure"),
    Output("histogram-2-graph", "figure"),
    Input("clinic-select", "value"),
    Input("date-picker-select", "start_date"),
    Input("date-picker-select", "end_date"),
)
def update_histograms(selected_clinic, start_date, end_date):
    # In this example, we generate random data for the histograms
    np.random.seed(42)
    data1 = np.random.normal(0, 1, 1000)
    data2 = np.random.normal(2, 1, 1000)

    # Create histograms
    histogram1 = {
        "data": [
            {
                "x": data1,
                "type": "histogram",
                "name": "Histogram 1",
                "opacity": 0.7,
                "marker": {"color": "#1f77b4"},
            }
        ],
        "layout": {
            "title": "Histogram 1",
            "xaxis": {"title": "X-axis"},
            "yaxis": {"title": "Frequency"},
        },
    }

    histogram2 = {
        "data": [
            {
                "x": data2,
                "type": "histogram",
                "name": "Histogram 2",
                "opacity": 0.7,
                "marker": {"color": "#ff7f0e"},
            }
        ],
        "layout": {
            "title": "Histogram 2",
            "xaxis": {"title": "X-axis"},
            "yaxis": {"title": "Frequency"},
        },
    }

    return histogram1, histogram2

if __name__ == "__main__":
    app.run_server(debug=True)