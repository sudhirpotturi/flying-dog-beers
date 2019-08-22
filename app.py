# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.plotly as py

py.sign_in("sudhirjntu", "Srikar*9")


app = dash.Dash(__name__)
server=app.server


data=pd.read_csv(r"SP500.csv");
df = data.sort_values(['SP', 'Fund'], ascending=[True, True])
df=df.head(10)

df1=pd.read_csv(r"VAMI1.csv");
df1=df1.sample(10)
df1 = df1.sort_values(['VAMI'], ascending=[True])


app.layout = html.Div(children=[
    html.H1(children='Tear sheet Visualization'),


    dcc.Graph(
        id='graph1',
        figure={
            'data': [
                {'x': df['Month'], 'y': df['SP'], 'type': 'bar', 'name': 'SP'},
                {'x': df['Month'], 'y': df['Fund'] , 'type': 'bar', 'name': u'Fund'},
            ],
            'layout': {
                'title': 'PERFORMANCE DURING WORST 10 MONTHS OF S&P 500 PERFORMANCE'
            }
        }
    ),

    dcc.Graph(
        id='graph2',
        figure={
            'data': [
                {'x': data['SP'], 'y': data['Fund'], 'type': 'scatter', 'name': 'SP','mode': 'markers'}
            ],
            'layout': {
                'title': 'FUND RETURNS VS SPX RETURNS'
            }
        }
    ),
    dcc.Graph(
        id='graph3',
        figure={
            'data': [
                {'x': data['Fund'], 'type': 'histogram', 'name': 'SP', 'xbins': {'end':50, 'size':5, 'start': -50}}
            ],
            'layout': {
                'title': 'Distribution of Returns'
            }
        }
    ),
    dcc.Graph(
        id='graph4',
        figure={
            'data': [
                {'x': df1['Month'], 'y': df1['VAMI'], 'type': 'scatter', 'name': 'SP','mode': 'markers+lines'}
            ],
            'layout': {
                'title': 'VAMI',
                'yaxis': dict(range=[0, 4000])
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
