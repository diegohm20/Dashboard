import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Interativo com Streamlit")

data = {'Ano': [2018, 2019, 2020, 2021, 2022],
        'Vendas': [100, 150, 200, 250, 300]}
df = pd.DataFrame(data)

fig, ax = plt.subplots()
ax.plot(df['Ano'], df['Vendas'], marker='o')
ax.set_title('Vendas Anuais')
ax.set_xlabel('Ano')
ax.set_ylabel('Vendas')
st.pyplot(fig)
