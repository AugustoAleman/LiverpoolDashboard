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
        html.Img(src='your_logo.png', className='logo'),  # Customize logo path
        html.Div([
            html.A('Option 1', className='nav-option'),
            html.A('Option 2', className='nav-option'),
        ], className='nav-options'),
    ], className='navbar'),
    
    # Two-column layout
    html.Div([
        # Left column
        html.Div([
            html.H1('Dashboard Title', className='title'),
            html.H3('Subtitle', className='subtitle'),
            html.P('Description paragraph goes here.', className='description'),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Option 1', 'value': 'option1'},
                    {'label': 'Option 2', 'value': 'option2'},
                ],
                value='option1',
            ),
            dcc.DatePickerRange(
                id='date-picker',
                start_date=datetime(2023, 1, 1),
                end_date=datetime(2023, 12, 31),
            ),
        ], className='left-column', style={'width': '30%'}),
        
        # Right column with charts
        html.Div([
            html.Div('Chart 1 Title', className='chart-title'),
            html.Hr(),  # Horizontal line
            dcc.Graph(
                figure=px.bar(data, x='Category', y='Value', title='Bar Chart'),
            ),
            html.Div('Chart 2 Title', className='chart-title'),
            html.Hr(),
            dcc.Graph(
                figure=px.pie(data, names='Category', values='Value', title='Pie Chart'),
            ),
            # Add more charts here as needed
        ], className='right-column', style={'width': '70%'}),
    ], className='two-column-layout'),
])

# Define callback function(s) here if needed

if __name__ == '__main__':
    app.run_server(debug=True)
