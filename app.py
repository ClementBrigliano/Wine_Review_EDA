import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import numpy as np
import ipywidgets as widgets
from tools import plot_dist_price_quantiles_quality

df = pd.read_csv('data/winemag-data_first150k.csv',)

# only keep the columns we need points and price
df = df[['points', 'price']]

# rename points to quality
df = df.rename(columns={'points': 'quality'})



# Create widgets
df_widget = widgets.fixed(df)
nb_quantiles_slider = widgets.IntSlider(min=2, max=10, step=1, value=2)

# Set up Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dcc.Graph(id='interactive-plot'),
    html.Label('Number of Quantiles'),
    dcc.Slider(
        id='nb-quantiles-slider',
        min=2,
        max=20,
        step=1,
        value=2,
        marks={i: str(i) for i in range(2, 21)}
    )
])

# Define callback to update the plot based on slider value
@app.callback(
    Output('interactive-plot', 'figure'),
    [Input('nb-quantiles-slider', 'value')]
)
def update_plot(nb_quantiles):
    return plot_dist_price_quantiles_quality(df, nb_quantiles)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
