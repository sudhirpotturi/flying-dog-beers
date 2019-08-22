import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

data=pd.read_csv(r"SP500.csv");
df = data.sort_values(['SP', 'Fund'], ascending=[True, True])
df=df.head(10)

########### Set up the chart
beers=df['Month']
ibu_values=df['SP']
abv_values=df['Fund']
color1='lightblue'
color2='darkgreen'

bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name='S&P',
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name='Fund',
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Context'),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    )    ]
)

if __name__ == '__main__':
    app.run_server()
