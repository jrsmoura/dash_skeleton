import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

external_stylesheet =[dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheet)


fig = go.Figure()
fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 300,
    domain = {'row': 0, 'column': 1}))


app.layout = dbc.Container([
        dbc.Row([

            html.H1("teste")
            ])
    ])


if __name__=='__main__':
    app.run_server(debug=True)