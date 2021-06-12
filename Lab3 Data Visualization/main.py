import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

app = dash.Dash()
server = app.server
# 数据载入
df = pd.read_csv('data/data.csv')


def get_first_pic():
    figure = dict(
        data=[
            go.Scatter(
                x=df[df['Category'] == i]['Rating'],
                y=df[df['Category'] == i]['Reviews'],
                text=df[df['Category'] == i]['App'],
                name=i,
                mode='markers',
                opacity=0.8,
                marker=dict(size=15, color=np.random.randn(400), colorscale='amp', line=dict(width=0.5, color='white'))
            ) for i in df.Category.unique()],
        layout=go.Layout(
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            hovermode='closest'
        )
    )

    return figure


def get_second_pic():
    free_count = len(df[df['Type'] == 'Free'])
    paid_count = len(df[df['Type'] == 'Paid'])
    labels = ['免费应用', '付费应用']
    values = [free_count, paid_count]
    colors = ['#9d2933', '#b36d61']
    trace = [go.Pie(labels=labels, values=values, marker=dict(colors=colors), hole=.3)]
    fig = go.Figure(data=trace)
    return fig


def get_third_pic():
    figure = dict(
        data=[
            go.Scatter3d(
                x=df[df['Category'] == i]['Size'],
                y=df[df['Category'] == i]['Rating'],
                z=df[df['Category'] == i]['Reviews'],
                text=df[df['Category'] == i]['App'],
                name=i,
                mode='markers',
                opacity=0.8,
                marker=dict(size=3, color=np.random.randn(400), colorscale='amp', line=dict(width=0.5, color='white'))
            ) for i in df.Category.unique()],
        layout=go.Layout(
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            hovermode='closest'
        )
    )

    return figure


# app的layout
app.layout = html.Div([
    html.H1(id="h1-element", className='h1', children='Lab3: Google Play Store',
            style={'textAlign': 'center', 'color': '#9d2933','backgroundColor':'#ffffff'}),

    html.Div([
        html.H3(children='应用评论数与评分的相关性分析', style={'textAlign': 'center', 'color': '#9d2933'}),
        dcc.Graph(
            id='1',
            figure=get_first_pic()
        ),
    ], style={
        'margin': 50,
        'height': 500,
    }),

    html.Div([
        html.Div(children='由上表可知，app的评分与评论数有一定的相关性，显然评分越高，评论数越高。'
                          '并且可见3.7分到4.8分之间的应用评论数目是最多的'
                          '根据统计结果，Facebook、WhatsApp Messenger和Instagram是评论数最多三个app。'
                          '并且可见评论数目远超其他app的四个app都是social类和communication类，'
                          '可见当下网络信息时代人们的大部分社交都通过网络设备终端完成。',
                 style={'color': '#9d2933','font-size':15}),
    ], style={
        'margin-left': 100,
        'margin-right': 100,
    }),

    html.Div([
        html.H3(children='免费应用于付费应用的数量比较', style={'textAlign': 'center', 'color': '#9d2933'}),
        dcc.Graph(
            id='2',
            figure=get_second_pic()
        ),
    ], style={
        'margin': 50,
        'height': 500,

    }),

    html.Div([
        html.Div(children='由图可知，大多数app都是免费软件。则很符合目前人们对于虚拟电子产品的消费观念。'
                          '付费应用萧条的原因很多，比如定价原因，比如没有特别好的应用发现机制，'
                          '还比如没有试用、付费更新和包月付费这样的推广和付费方式。',
                 style={'color': '#9d2933','font-size':15}),
    ], style={
        'margin-left': 100,
        'margin-right': 100,
    }),

    html.Div([
        html.H3(children='应用大小、应用评分、评价数量的三维分析', style={'textAlign': 'center', 'color': '#9d2933'}),
        dcc.Graph(
            id='3',
            figure=get_third_pic()
        ),
    ], style={
        'margin-top': 100,
        'margin-left': 90,
        'width': 1200,
        'height': 500,
    }),

    html.Div([
        html.H4(children=' Copyright © 2021 同济大学1854025杨晶. ', style={'textAlign': 'center', 'color': '#9d2933'}),
    ], style={
        'margin-top': 100,
    })

], className="page", style = dict(backgroundColor = '#FFDAB9'))


# css的设置
external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "https://codepen.io/ffzs/pen/mjjXGM.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]


for css in external_css:
    app.css.append_css({"external_url": css})


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
