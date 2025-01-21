import streamlit as st
# Ensure the file is included in the path
from pathlib import Path
import pandas as pd
import plotly.express as px

def main():
    sliderP4DS = st.sidebar.slider("Pillar 4: Decision Support", min_value=2010, max_value=2020, value=(2020))
    dfP4_DS = pd.read_csv('data/Pillar4_DSI.csv')
    dfP4_DS_year = dfP4_DS[(dfP4_DS['t'] == sliderP4DS)]
    median_density = dfP4_DS_year['density'].median()
    median_importVal = dfP4_DS_year['importVal'].median()

    st.title("Pillar 4: Raw Materials")
    st.subheader("KPI: South African Furniture Raw Material Imports")
    st.write(""" "The agreed targets by 2030 are: **Build local capacity to manufacture imported products or raw material.** " [1]""")
    st.subheader("DSI: What Raw Materials to Produce Locally")
    st.write( "The formulated decision support indicator is the level of furniture raw materials imports versus how related (Density) it is to economy to be able to export it competitively.")

    def Pillar4():
        fig = px.scatter(dfP4_DS_year, x='density', y='importVal', hover_data=['k', 'description'],
                         labels={'density': 'Density', 'pci': 'Product Complexity', "importVal" : "Import Value",
                                 "k": "Product Code", "description": "Description"},
                         title='Scatter Plot of Imports vs. Fit',
                         color_discrete_sequence=['purple'])
        fig.add_shape(
            type="line",
            x0=median_density, x1=median_density, y0=dfP4_DS_year['importVal'].min(), y1=dfP4_DS_year['importVal'].max(),
            line=dict(color="Black", width=2, dash="dash")
        )
        fig.add_shape(
            type="line",
            x0=dfP4_DS_year['density'].min(), x1=dfP4_DS_year['density'].max(), y0=median_importVal, y1=median_importVal,
            line=dict(color="Black", width=2, dash="dash")
        )
        fig.update_layout(title='South African Import Value versus Density for Furniture Raw Materials')
        fig.update_layout(
            barmode='group',
            xaxis_title='Relatedness Density',
            yaxis_title='Import Value (Thousands of US Dollars)',
            legend_title='Category'
        )
        return fig
    fig = Pillar4()
    st.plotly_chart(fig)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
