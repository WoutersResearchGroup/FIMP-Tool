import streamlit as st
# Ensure the file is included in the path
from pathlib import Path
import pandas as pd
import plotly.express as px

def main():
    sliderP3DS = st.sidebar.slider("Pillar 3: Decision Support", min_value=2010, max_value=2020, value=(2020))
    dfP3_DS = pd.read_csv('Pillar3_DS.csv')
    dfP3_DS_year = dfP3_DS[(dfP3_DS['t'] == sliderP3DS)]
    #dfP2_DS = pd.read_csv('Pillar2_DS.csv')
    #dfP2_DS_year = dfP2_DS[(dfP2_DS['t'] == st.session_state.sliderOne)]
    # Calculate medians
    median_density = dfP3_DS_year['density'].median()
    median_pci = dfP3_DS_year['pci'].median()

    st.title("Pillar 3: Exports")

    st.subheader("KPI: South African Furniture Exports")

    st.write(""" "The agreed targets by 20230 are: **Increase exports of South Africa manufactured furniture and components** by at least 20%  by of 2030?". [1]""")

    st.subheader("DS: What Products to Export")
    st.write( "The formulated decision support indicator is the level of furniture Product Complexity versus how related (Density) it is to the South African economy to be able to export it competitively.")

    def Pillar3():
        # Define the colors for imports, exports, and apparent consumption
        # colors = ['lightblue', 'steelblue', 'darkblue', 'darkslateblue']

        # Create a scatter plot with hover labels
        fig = px.scatter(dfP3_DS_year, x='density', y='pci', hover_data=['k', 'description', 'v'], size="v",
                         labels={'density': 'Density', 'pci': 'Product Complexity', "v" : "Export Value",
                                 "k": "Product Code", "description": "Description"},
                         title='Scatter Plot of Imports vs. Fit',
                         color_discrete_sequence=['purple'])

        # Add a vertical line at the median of `density`
        fig.add_shape(
            type="line",
            x0=median_density, x1=median_density, y0=dfP3_DS_year['pci'].min(), y1=dfP3_DS_year['pci'].max(),
            line=dict(color="Black", width=2, dash="dash")
        )
        # Add a horizontal line at the median of `pci`
        fig.add_shape(
            type="line",
            x0=dfP3_DS_year['density'].min(), x1=dfP3_DS_year['density'].max(), y0=median_pci, y1=median_pci,
            line=dict(color="Black", width=2, dash="dash")
        )

        # Create a grouped bar chart with individual bars for each category
        # fig = go.Figure()
        # fig.add_trace(go.Bar(x=years, y=imports, name='Imports', marker=dict(color=colors[0])))
        # fig.add_trace(go.Bar(x=years, y=exports, name='Exports', marker=dict(color=colors[1])))
        # fig.add_trace(go.Bar(x=years, y=output, name='Output', marker=dict(color=colors[2])))
        # fig.add_trace(go.Bar(x=years, y=consumption, name='Local Consumption (Apparent)', marker=dict(color=colors[3])))

        fig.update_layout(title='Furniture Product Complexity versus South African Relatedness Density to each Product')
        #fig.update_traces(mode='markers', marker_size=8)

        fig.update_layout(
            barmode='group',
            xaxis_title='Relatedness Density',
            yaxis_title='Product Complexity',
            legend_title='Category'
        )
        return fig

    fig = Pillar3()
    # Render the chart in Streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
