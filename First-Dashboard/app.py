import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from datetime import datetime
import pandas as pd

# Sample data for the charts
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [20, 40, 10, 25, 30]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.Link(href="/assets/styles.css", rel="stylesheet"),
    # Navbar with logo and options
    html.Div([
        html.Img(src='assets/src/liverpool-logo.png', className='logo'),  # Customize logo path
        html.Div([
            html.Div(html.A('INICIO'), style = {'text-decoration': 'underline'}, className='nav-option'),
            html.Div(html.A('USUARIOS'), className='nav-option'),
            html.Div(html.A('PANEL DE CONTROL'), className='nav-option'),
            html.Div(html.Button('SALIR', className='rounded-button')),
        ], className='nav-options')

    ], className='navbar'),
    
    # Two-column layout
    html.Div([
        # Left column
        html.Div([
            html.H1('Liverpool Human Analytics', className='title'),
            html.H3('Bienvenido al Dashboard de Human Analytics de Liverpool', className='subtitle'),
            html.P('Explora los datos más recientes de Human Analytics dentro de Liverpool. Selecciona si deseas visualizar un sector o periodo específicos.', className='description'),
            html.H4('Selecciona un sector', className='picker-description'),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Todos', 'value': 'Todos'},
                    {'label': 'Liverpool', 'value': 'Liverpool'},
                    {'label': 'Suburbia', 'value': 'Suburbia'},
                    {'label': 'CeDis', 'value': 'CeDis'},
                    {'label': 'Otros', 'value': 'Otros'},
                ],
                value='Todos',
            ),
            html.H4('Selecciona un periodo', className='picker-description'),
            dcc.DatePickerRange(
                id='date-picker',
                start_date=datetime(2023, 1, 1),
                end_date=datetime(2023, 12, 31),
            ),
        ], className='left-column', style={'width': '30%'}),
        
        # Right column with charts
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Chart 1 Title', className='chart-title'),
                    html.Hr(className='divider'),  # Horizontal line
                    dcc.Graph(
                        figure=px.bar(data, x='Category', y='Value', title='Bar Chart'),
                    ),
                ], className = 'chart-container'),
                html.Div([
                    html.Div('Chart 2 Title', className='chart-title'),
                    html.Hr(className='divider'),
                    dcc.Graph(
                        figure=px.pie(data, names='Category', values='Value', title='Pie Chart'),
                    ),
                ], className = 'chart-container'),
                # Add more charts here as needed
            ], className='charts-column')
        ], className='right-column', style={'width': '70%'}),
    ], className='two-column-layout'),
])

# Define callback function(s) here if needed

if __name__ == '__main__':
    app.run_server(debug=True)
