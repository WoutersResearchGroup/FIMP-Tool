import streamlit as st
from pathlib import Path
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def main():
    sliderP1DS = st.sidebar.slider("Pillar 1: Decision Support", min_value=2010, max_value=2020, value=(2020))
    dfP1_DS = pd.read_csv('data/Pillar1_DS.csv')
    dfP1_DS_year = dfP1_DS[(dfP1_DS['t'] == sliderP1DS)]
    median_density = dfP1_DS_year['density'].median()
    median_importVal = dfP1_DS_year['importVal'].median()

    st.title("Pillar 1: Localisation")
    st.subheader("KPI: Furniture Import to Domestic Demand")
    st.write(""" "The agreed targets are to **reduce the import to domestic demand ratio**, from an estimated baseline of 30% 
        of R48.7billion total value of sales recorded in 2019 (WhoownsWhom, 2023) to 25% by 2026 and 20% by 
        2030, aligned to the Nedlac commitment to increase import replacement by 20% of the 2019 base over 5 [sic]". [1]""")
    st.subheader("DSI: What Furniture Products to Localise")
    st.write("The formulated decision support indicator is the quantity of imports of each furniture product versus how related (density) that product is to the South African economy.")

    st.write("The median values of both axis are used to create four quadrants by which products can be compared. Where a higher density and higher import value is ideal (top-right quadrant).")

    def Pillar1():
        # Create a scatter plot for Pillar 1's DSI.
        fig = px.scatter(dfP1_DS_year, x='density', y='importVal', hover_data=['k','rca', 'description'],
                         labels={'density': 'Relatedness Density', 'importVal': 'Import Value', "k": "HS Product Code", "description": "Description", "rca":"RCA"},
                         title='Scatter Plot of Imports vs. Fit',
                         color_discrete_sequence=['purple'])
        # Add a vertical line at the median of `density`.
        fig.add_shape(
            type="line",
            x0=median_density, x1=median_density, y0=dfP1_DS_year['importVal'].min(), y1=dfP1_DS_year['importVal'].max(),
            line=dict(color="Black", width=2, dash="dash")
        )
        # Add a horizontal line at the median of `pci`.
        fig.add_shape(
            type="line",
            x0=dfP1_DS_year['density'].min(), x1=dfP1_DS_year['density'].max(), y0=median_importVal, y1=median_importVal,
            line=dict(color="Black", width=2, dash="dash")
        )
        fig.update_layout(title='South African Furniture Products Import Value versus their Relatedness Density')
        fig.update_traces(mode='markers', marker_size=8)
        fig.update_layout(
            barmode='group',
            xaxis_title='Relatedness Density',
            yaxis_title='Import Value (Thousands of US Dollars)',
            legend_title='Category'
        )
        return fig
    fig = Pillar1()
    st.plotly_chart(fig)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
