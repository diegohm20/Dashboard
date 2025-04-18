import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Dados de exemplo (você já deve ter isso definido)
data = {'Ano': [2018, 2019, 2020, 2021, 2022],
        'Vendas': [100, 150, 200, 250, 300]}
df = pd.DataFrame(data)

st.write("""
# Dashboard de Vendas
Este dashboard interativo permite visualizar os dados de vendas anuais.
Use os sliders abaixo para filtrar os dados conforme necessário.
""")

# Filtros interativos
ano_min, ano_max = st.slider(
    'Selecione o período de anos',
    min_value=int(df['Ano'].min()),
    max_value=int(df['Ano'].max()),
    value=(int(df['Ano'].min()), int(df['Ano'].max()))
)

vendas_min = st.slider(
    'Selecione o valor mínimo de vendas',
    min_value=int(df['Vendas'].min()),
    max_value=int(df['Vendas'].max()),
    value=int(df['Vendas'].min())
)

# Filtragem do DataFrame
df_filtered = df[(df['Ano'] >= ano_min) & (
    df['Ano'] <= ano_max) & (df['Vendas'] >= vendas_min)]

# Gráfico com Plotly Express
fig_plotly = px.line(df_filtered, x='Ano', y='Vendas', title='Vendas Anuais')
st.plotly_chart(fig_plotly)

st.dataframe(df_filtered)

# Gráfico com Matplotlib
fig_matplotlib, ax = plt.subplots()
ax.plot(df_filtered['Ano'], df_filtered['Vendas'], marker='o')
ax.set_title('Vendas Anuais')
ax.set_xlabel('Ano')
ax.set_ylabel('Vendas')
st.pyplot(fig_matplotlib)

st.dataframe(df_filtered)
