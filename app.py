import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.markdown(
           """
 # Análise de performance de Estudantes
"""             
            )

def mostra_linhas(df):
    qtd = st.sidebar.slider("Selecione quantas linhas você quer", min_value=1, max_value=len(df),step=1)
    st.write(df.head(qtd).style.format(subset=['math score'], formatter='{:.2f}'))
    

    #st.pyplot(sns.heatmap(df[['math score','reading score', 'writing score']].corr(), annot=True, fmt='.2f'))

df = pd.read_csv('StudentsPerformance.csv', sep=';')
df['Media'] = (df['math score'] + df['writing score'] + df['reading score'])/3
df['Status'] = df['Media'].apply(lambda x: 'Aprovado' if x >= 70 else 'Reprovado')

checkbox = st.sidebar.checkbox("Show table")

if checkbox:

    st.sidebar.markdown('## Filtro de dados')

    gen = list(df['gender'].unique())
    gen.append("All")

    genders = st.sidebar.selectbox("Selecione o gênero", options=gen)

    if genders != "All":

        df_gen = df.query('gender == @genders')
        mostra_linhas(df_gen)
        st.pyplot(sns.pairplot(df_gen))
        x = df[['math score','reading score', 'writing score']].corr()
        st.table(x)

    
        #st.plotly_chart(sns.boxplot(data=df))
    else:
        mostra_linhas(df)
        st.pyplot(sns.pairplot(df))
        x = df[['math score','reading score', 'writing score']].corr()
        st.table(x)
        #st.plotly_chart(sns.boxplot(data=df))



    
# st.dataframe(df)
# plt.title('Pairplot')
# st.pyplot(sns.pairplot(df))

#

