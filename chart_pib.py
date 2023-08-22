
import pandas as pd
import matplotlib as plt
import numpy as np
import seaborn as sns; sns.set()
import plotly.express as px
from dash import Dash, html, dcc

app = Dash(__name__)

url = pd.read_excel("gapminder_final.xlsx")

df = pd.DataFrame(url)

rename_columns = df.rename(
    columns={
        "country": "pais",
        "year": "ano",
        "gdpPercap": "rendaPer",
        "lifeExp": "expVida",
        "pop": "populacao",
        "continent": "continente"
    }
)
data = pd.DataFrame(rename_columns)
data.head()

# Apresenta de maneira randômica os 1000(mil) países
df_sample = data.sample(n=1000)

fig = px.scatter(df_sample, x="rendaPer", y="expVida", hover_name="pais", log_x = True, width = 1000, height = 800)
fig.update_traces(marker = dict(size=12, line = dict(width=2)), selector=dict(mode='markers'))
fig.update_xaxes(title = "Log(PIB per capita)")
fig.update_yaxes(title = "Expectativa de vida")

app.layout = html.Div(children=[
    html.H1(children='PIB x Expectativa de vida'),
    html.P(children="google.com"),

    html.Div(children='''
        Logaritmo do PIB per capita X Expectativa de vida
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)








