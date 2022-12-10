import modules.graphs as graphs
from dash import Dash, dcc, html

app = Dash(__name__)
app.title = 'Introcomp'

colors = {
    'background': '#020220',
    'text': '#FFFFFF'
}

# ==========================================#
# Editando as cores dos gráficos
graphs.bar_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)

graphs.pie_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# Criando dashboard ============================================================== #
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Introcomp - Monitorias',
    style={
      'textAlign': 'center',
      'color': colors['text']
    }),
    html.H3(children='''
        Dados colhidos durante o módulo 1
    ''',
    style={
      'textAlign': 'center',
      'color': colors['text']
    }),
    dcc.Graph(
        id='bg',
        figure=graphs.bar_graph
    ),
    dcc.Graph(
        id='pg',
        figure=graphs.pie_graph
    )
])

if __name__ == '__main__':
    app.run_server()
