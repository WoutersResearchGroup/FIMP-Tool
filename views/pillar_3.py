import streamlit as st
# Ensure the file is included in the path
from pathlib import Path
import pandas as pd
import plotly.express as px

def main():
    sliderP3DS = st.sidebar.slider("Pillar 3: Decision Support", min_value=2010, max_value=2020, value=(2020))
    dfP3_DS = pd.read_csv('data/Pillar3_DS.csv')
    dfP3_DS_year = dfP3_DS[(dfP3_DS['t'] == sliderP3DS)]
    median_density = dfP3_DS_year['density'].median()
    median_pci = dfP3_DS_year['pci'].median()

    st.title("Pillar 3: Exports")
    st.subheader("KPI: South African Furniture Exports")
    st.write(""" "The agreed targets by 2030 are: **Increase exports of South Africa manufactured furniture and components** by at least 20%  by of 2030?". [1]""")
    st.subheader("DSI: What Products to Export")
    st.write( "The formulated decision support indicator is the level of furniture Product Complexity versus how related (density) it is to the South African economy to be able to export it competitively.")

    def Pillar3():
        fig = px.scatter(dfP3_DS_year, x='density', y='pci', hover_data=['k', 'description', 'v'], size="v",
                         labels={'density': 'Density', 'pci': 'Product Complexity', "v" : "Export Value",
                                 "k": "Product Code", "description": "Description"},
                         title='Scatter Plot of Imports vs. Fit',
                         color_discrete_sequence=['purple'])
        fig.add_shape(
            type="line",
            x0=median_density, x1=median_density, y0=dfP3_DS_year['pci'].min(), y1=dfP3_DS_year['pci'].max(),
            line=dict(color="Black", width=2, dash="dash")
        )
        fig.add_shape(
            type="line",
            x0=dfP3_DS_year['density'].min(), x1=dfP3_DS_year['density'].max(), y0=median_pci, y1=median_pci,
            line=dict(color="Black", width=2, dash="dash")
        )
        fig.update_layout(title='Furniture Product Complexity versus South African Relatedness Density to each Product')
        fig.update_layout(
            barmode='group',
            xaxis_title='Relatedness Density',
            yaxis_title='Product Complexity',
            legend_title='Category'
        )
        return fig
    fig = Pillar3()
    st.plotly_chart(fig)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
