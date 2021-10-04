import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import cufflinks as cf

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

bkg_color = "#343434"
lighter_bkg = "#414141"
offwhiteclr = "#f8f8ff"
darkerneonclr = "hsl(157, 100%, 41%)"

app = dash.Dash(__name__)
server = app.server

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.update_layout(paper_bgcolor=bkg_color, font_color='white')

app.layout = html.Div(
    style={
        'borderRadius': '1em',
        'backgroundColor': 'white',
        'textAlign':'center',
        'paddingBottom':'50px',
        'boxShadow':'hsl(156.83 100% 71.57%)',
    },
    children=[
    html.H1("Dash Python Graph",style={'margin':'auto','padding':'10px', 'font-family': '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif',
}),
    #create the dropdown for each selection
    html.Div([
        #NOT INCLUDING DATA FRAME SELECTION - CAN ADD LATER
        #html.Div(
            #dcc.Dropdown(
                #id='df-select',
                #options= [
                    #{'label': 'Tips','value':'tps'},
                    #{'label': 'Flights','value':'flg'},
                    #{'label': 'Iris','value':'irs'}
                    #],
                    #value='tps',searchable=False,clearable=False,placeholder="Dataframe",
                    #style={'background-color':darkerneonclr,'border-radius':'.5em','color':'#f8f8ff'}
            #),
            #style={'width':'49%','display':'inline-block'},
        #),
        html.Div(
            dcc.Dropdown(
                id='xaxis-select',
                options= [
                    {'label': 'Sepal Length','value':'sepal_length'},
                    {'label': 'Sepal Width','value':'sepal_width'},
                    {'label': 'Petal Length','value':'petal_width'},
                    {'label': 'Petal Width','value':'petal_length'},
                    {'label': 'Species','value':'species'}
                    ],
                    value='sepal_length',searchable=False,clearable=False,placeholder="Dataframe",
                    style={'background-color':darkerneonclr,'border-radius':'.5em','color':'#f8f8ff'}
            ),
            style={'width':'49%','display':'inline-block'},
        ),
        html.Div(
            dcc.Dropdown(
                id='yaxis-select',
                options= [
                    {'label': 'Sepal Length','value':'sepal_length'},
                    {'label': 'Sepal Width','value':'sepal_width'},
                    {'label': 'Petal Length','value':'petal_length'},
                    {'label': 'Petal Width','value':'petal_width'},
                    {'label': 'Species','value':'species'}
                    ],
                    value='sepal_width',searchable=False,clearable=False,placeholder="Dataframe",
                    style={'background-color':darkerneonclr,'border-radius':'.5em','color':'#f8f8ff'}
            ),
            style={'width':'49%','display':'inline-block'},
        ),
        html.Div(
            dcc.Dropdown(
                id='graphType-select',
                options= [
                    {'label': 'Bar','value':'bar'},
                    {'label': 'Box','value':'box'},
                    {'label': 'Violin','value':'violin'},
                    {'label': 'Scatter','value':'scatter'},
                    {'label': 'Scatter 3D','value':'scatter3d'}
                    ],
                    value='bar',searchable=False,clearable=False,placeholder="Dataframe",
                    style={'background-color':darkerneonclr,'border-radius':'.5em','color':'white !important'}
            ),
            style={'width':'49%','display':'inline-block','color':'white'},
        )],
    style={
            'display':'flex',
            'justify-content':'space-evenly',
            'flex-direction':'row'
        },
    ),
    #create the graph
    dcc.Graph(
        id='main-graph',
        figure=fig
    )
])

@app.callback(
    Output('main-graph','figure'),
    [Input('xaxis-select','value'),
     Input('yaxis-select','value'),
     Input('graphType-select','value')])

def update_graph(xaxis_column,yaxis_column,graph_type):
    if graph_type == 'bar':
        fig = px.bar(df,x=xaxis_column,y=yaxis_column)
    elif graph_type == 'box':
        fig = px.box(df,x=xaxis_column,y=yaxis_column)
    elif graph_type == 'violin':
        fig = px.violin(df,x=xaxis_column,y=yaxis_column)
    elif graph_type == 'scatter':
        fig = px.scatter(df,x=xaxis_column,y=yaxis_column)
    elif graph_type == 'scatter3d':
        fig = px.scatter_3d(df,x=xaxis_column,y=yaxis_column,z='sepal_width')
    
    return fig
    

if __name__ == '__main__':
    app.run_server()
