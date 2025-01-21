import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

def main():
    sliderP2_DS = st.sidebar.slider("Pillar 2: Decision Support", min_value=2010, max_value=2020, value=(2020))
    dfP2_DS = pd.read_csv('data/Pillar2_DS.csv')
    dfP2_DS_year = dfP2_DS[(dfP2_DS['TaxYear'] == sliderP2_DS)]

    st.title("Pillar 2: Competitiveness")
    st.subheader("KPI: Furniture Employment Level and Quantity of Establishments")
    st.write(
        """ "Stategic Objective: **Invest in the competitiveness, stability, and growth of small- and medium-sized furniture manufacturers**" [1].""")

    st.subheader("DSI: Where should the Furniture Industry be Developed")
    st.write(
        "The formulated decision support indicator is the total furniture industry employment versus the quantity of establishments in each municipality.")

    def Pillar2():
        fig = px.scatter(dfP2_DS_year,x='Establishments', y='FTE', hover_data=['CAT_B'],
                         labels={'FTE': 'Employment',"CAT_B": "Municipality"},
                         title='Scatter Plot of Imports vs. Fit',
                         color_discrete_sequence=['purple'])
        fig.update_layout(title='South African Furniture Industry Employment and Quantity of Establishments per Municipality')
        fig.update_layout(
            barmode='group',
            xaxis_title='Quantity of Establishments',
            yaxis_title='Total Employment',
            legend_title='Category'
        )
        return fig
    fig = Pillar2()
    st.plotly_chart(fig)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
