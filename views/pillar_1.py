import streamlit as st
# Ensure the file is included in the path
from pathlib import Path

import plotly.express as px
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def main():
    #st.session_state.sliderP1DS = st.sidebar.slider("Pillar 1: DS", min_value=2010, max_value=2020, value=(2020))
    sliderP1DS = st.sidebar.slider("Pillar 1: Decision Support", min_value=2010, max_value=2020, value=(2020))
    dfP1_DS = pd.read_csv('Pillar1_DS.csv')
    dfP1_DS_year = dfP1_DS[(dfP1_DS['t'] == sliderP1DS)]
    median_density = dfP1_DS_year['density'].median()
    median_importVal = dfP1_DS_year['importVal'].median()
    #dfP1_DS_year = dfP1_DS[(dfP1_DS['t'] == st.session_state.sliderP1DS)]
    #dfP1_DS = pd.read_csv('Pillar 1 KPI.csv')

    st.write(
        """
        Pillar 1: Localisation
        =====================
        """
    )
    st.subheader("KPI: Furniture Import to Domestic Demand")
    st.write(""" "The agreed targets are to **reduce the import to domestic demand ratio**, from an estimated baseline of 30% 
        of R48.7billion total value of sales recorded in 2019 (WhoownsWhom, 2023) to 25% by 2026 and 20% by 
        2030, aligned to the Nedlac commitment to increase import replacement by 20% of the 2019 base over 5". [1]""")

    #(South African Department of Trade, Industry and Competition)
    st.subheader("DS: What Furniture Products to Localise")
    st.write("The formulated decision support indicator is the quantity of imports of each furniture product versus how related (density) that product is to the South African economy.")

    # Removed cache to update slider
    #@st.cache_data
    def Pillar1():
        # Define the colors for imports, exports, and apparent consumption
        #colors = ['lightblue', 'steelblue', 'darkblue', 'darkslateblue']

        # Create a scatter plot with hover labels
        fig = px.scatter(dfP1_DS_year, x='density', y='importVal', hover_data=['k','rca', 'description'],
                         labels={'density': 'Relatedness Density', 'importVal': 'Import Value', "k": "HS Product Code", "description": "Description"},
                         title='Scatter Plot of Imports vs. Fit',
                         color_discrete_sequence=['purple'])

        # Add a vertical line at the median of `density`
        fig.add_shape(
            type="line",
            x0=median_density, x1=median_density, y0=dfP1_DS_year['importVal'].min(), y1=dfP1_DS_year['importVal'].max(),
            line=dict(color="Black", width=2, dash="dash")
        )
        # Add a horizontal line at the median of `pci`
        fig.add_shape(
            type="line",
            x0=dfP1_DS_year['density'].min(), x1=dfP1_DS_year['density'].max(), y0=median_importVal, y1=median_importVal,
            line=dict(color="Black", width=2, dash="dash")
        )
        # Create a grouped bar chart with individual bars for each category
        # fig = go.Figure()
        # fig.add_trace(go.Bar(x=years, y=imports, name='Imports', marker=dict(color=colors[0])))
        # fig.add_trace(go.Bar(x=years, y=exports, name='Exports', marker=dict(color=colors[1])))
        # fig.add_trace(go.Bar(x=years, y=output, name='Output', marker=dict(color=colors[2])))
        # fig.add_trace(go.Bar(x=years, y=consumption, name='Local Consumption (Apparent)', marker=dict(color=colors[3])))

        fig.update_layout(title='South African Furniture Products Import Value versus their Density')
        fig.update_traces(mode='markers', marker_size=8)

        fig.update_layout(
            barmode='group',
            xaxis_title='Relatedness Density',
            yaxis_title='Import Value (Thousands of US Dollars)',
            legend_title='Category'
        )
        return fig

    fig = Pillar1()
    # Render the chart in Streamlit
    st.plotly_chart(fig)



if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()



# Old Graph
# @st.cache_data
#     def Pillar1():
#         # Define the years and production values for imports, exports, and consumption
#         years = [2017, 2018, 2019]
#         imports = [9.0, 9.7, 9.6]
#         exports = [4.9, 4.9, 4.5]
#         output = [19.0, 19.3, 17.5]
#         consumption = np.array(imports) + np.array(output) - np.array(exports)
#
#
#         # Define the colors for imports, exports, and apparent consumption
#         #colors = ['lightblue', 'steelblue', 'darkblue', 'darkslateblue']
#
#         # Create a grouped bar chart with individual bars for each category
#         # fig = go.Figure()
#         # fig.add_trace(go.Bar(x=years, y=imports, name='Imports', marker=dict(color=colors[0])))
#         # fig.add_trace(go.Bar(x=years, y=exports, name='Exports', marker=dict(color=colors[1])))
#         # fig.add_trace(go.Bar(x=years, y=output, name='Output', marker=dict(color=colors[2])))
#         # fig.add_trace(go.Bar(x=years, y=consumption, name='Local Consumption (Apparent)', marker=dict(color=colors[3])))
#
#         fig.update_layout(title='South African Furniture Import Quantity versus Relatedness to the Economy')
#
#         # Set the layout
#         fig.update_layout(
#             barmode='group',
#             xaxis_title='Year',
#             yaxis_title='Value (in Billion Rands)',
#             legend_title='Category'
#         )
#         return fig
#
#     fig = Pillar1()
#     # Render the chart in Streamlit
#     st.plotly_chart(fig)




    # st.subheader("Tracking the Import to Domestic Demand Ratio")
    # st.write("""Ratio.""")
    #
    # st.header("DS: Import Replacement Strategy")
    #
    # ZARdf = pd.read_csv("SARS_Imports_2023.csv")
    # selected_value = st.selectbox('Select a Country', ZARdf['CountryOfOriginName'].unique())
    # ZARdf.loc[ZARdf["CountryOfOriginName"] == "selected_value"]
    # grouped_ZAR_District = ZARdf[
    #     ["Tariff", 'CustomsValue', 'StatisticalQuantity', 'DistrictOfficeName', 'TariffAndDescription']]
    # grouped_ZAR_District = grouped_ZAR_District.groupby(['Tariff', 'DistrictOfficeName', 'TariffAndDescription'],
    #                                                     observed=True).sum()
    # grouped_ZAR_District = grouped_ZAR_District.reset_index()
    # grouped_ZAR_District['Tariff'] = grouped_ZAR_District['Tariff'].astype(str)
    # fig = px.bar(grouped_ZAR_District, x='Tariff', y='CustomsValue', title='South Africa 2023 FUrniture Imports',
    #              color='DistrictOfficeName', hover_data=["TariffAndDescription"])
    # st.plotly_chart(fig)
