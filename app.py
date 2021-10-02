import pandas as pd
import dash
import plotly.express as px
import dash.dcc as dcc
import dash.html as html

app = dash.Dash(__name__)

colors = {
    'background': '#e4ccbb',
    'text': '#614e40',
    'brown2': '#8b7667',
    'brown3': '#b6a090',
    'brown1': '#fffae9'
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 3, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)

app.layout = html.Div(style={'backgroundColor': colors['brown1']},
children=[
    html.H1(
        "Olá Mundo",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    html.Div(
        html.H2(
                "Uma aplicação Simples",
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
               )
            ),
    
    dcc.Graph(
        id="graph-example",
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)