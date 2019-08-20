import dash
import dash_core_components as dcc
import dash_html_components as html
from iexfinance.stocks import get_historical_data
from iexfinance.stocks import Stock
from dash.dependencies import Input,Output
import datetime
from  dateutil.relativedelta import relativedelta
import pandas as pd
import plotly.graph_objs as go
start=datetime.datetime.today()-relativedelta(years=5)
end=datetime.datetime.today()


app=dash.Dash()
#
# app.layout=html.Div([
#     html.Div([dcc.Input(id="stock-input",value="SPY",type="text")]),
#     html.H1(children="Stock Chart"),
#
# html.Div([
#         html.Div([
#             dcc.Graph(
#                 id="graph_close",
#             )
#
# ])
# ])
# ])

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



# app.css.append_css({
#     "external_url":"https://contextsummits.com/wp-content/themes/contextsummits/css/fx3.css"
# }


@app.callback(dash.dependencies.Output("graph_close","figure"),
              [dash.dependencies.Input("stock-input","value")]
              )
def update_fig(input_value):
    # df = get_historical_data(input_value, start=start, end=end, output_format='pandas',
    #                           token='pk_15ba07e215294ebda89c0d0950f0fdba')
    df=pd.read_csv(r"SP500.csv");
    data=[]
    # trace_close = go.Scatter(x=list(df.index), y=list(df.close))
    if input_value=="SP":
        trace_close = go.Scatter(x=list(df.Month), y=list(df.SP))
    else:
        trace_close = go.Scatter(x=list(df.Month), y=list(df.Fund))
    # df = df.sort_values(['SP', 'Fund'], ascending=[True, True])
    # df=df.head(10)
    # trace_close = go.Figure(data=[
    #     go.Bar(name='SP', x=df.Month, y=df.SP),
    #     go.Bar(name='OldOrchard', x=df.Month, y=df.Fund)
    # ])
    # # Change the bar mode
    # trace_close.update_layout(barmode='group')
    data.append(trace_close)
    layout={"title":input_value}
    return{
        "data":data,
        "layout":layout
      }
if __name__=="__main__":
    app.run_server(debug=True)


