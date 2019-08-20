import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objs as go

app=dash.Dash()
server = app.server

app.layout = html.Div([
    dcc.Dropdown(
        id='stock-input',
        options=[
            {'label': 'S&P500', 'value': 'SP'},
            {'label': 'Old Orchard', 'value': 'Old Orchard'},

        ],
        value='SP'
    ),
    html.Div([
            html.Div([
                dcc.Graph(
                    id="graph_close",
                )
    ])
])
])

@app.callback(dash.dependencies.Output("graph_close","figure"),
              [dash.dependencies.Input("stock-input","value")]
              )
def update_fig(input_value):
    df=pd.read_csv(r"SP500.csv");
    data=[]
    if input_value=="SP":
        trace_close = go.Scatter(x=list(df.Month), y=list(df.SP))
    else:
        trace_close = go.Scatter(x=list(df.Month), y=list(df.Fund))
    data.append(trace_close)
    layout={"title":input_value}
    return{
        "data":data,
        "layout":layout
      }
if __name__=="__main__":
    app.run_server(debug=True)
