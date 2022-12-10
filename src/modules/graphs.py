import plotly.express as px
import pandas as pd

# Dataframe base
df = pd.read_csv("./data/estatisticas-modulo1.csv")

# ===================================#
# Dataframe para o primeiro gráfico
df_fig = df.drop(8)
# print(df_fig)

# Quantidade de dúvidas por aula
bar_graph = px.bar(df_fig, y=["Conceitual", "Working", "Interpretação", "Técnica"],
 x="Aulas", title="Quantidade de dúvidas por aula" ,labels={"value": "Quantidade", "variable": "Dúvidas"},
 
 color_discrete_sequence=px.colors.sequential.RdBu)


# ================================= #
# Dataframe para o segundo gráfico
df_fig2 = df.loc[8]
# print(df_fig2)
labels = list(df.columns.values)

# Porcentagem de dúvidas no total
pie_graph = px.pie(df_fig2, values=8, names=labels, color_discrete_sequence=px.colors.sequential.RdBu, title="Porcentagem de dúvidas no total")


if __name__ == "__main__":
  bar_graph.show()
  pie_graph.show()
