import streamlit as st
import pandas as pd
import plotly.express as px
# Ensure the file is included in the path
from pathlib import Path


def main():

    st.title("Pillar 2: Competitiveness")

    sliderP2_DS = st.sidebar.slider("Pillar 2: Decision Support", min_value=2010, max_value=2020, value=(2020))
    dfP2_DS = pd.read_csv('Pillar2_DS.csv')
    dfP2_DS_year = dfP2_DS[(dfP2_DS['TaxYear'] == sliderP2_DS)]

    st.subheader("KPI: Furniture Employment and Total Establishments")

    st.write(
        """ "Stategic Objective: **Invest in the competitiveness, stability, and growth of small- and medium-sized furniture manufacturers**" [1].""")

    st.subheader("DS: Where should the Furniture Industry be Developed")
    st.write(
        "The formulated decision support indicator is the Employment versus the quantity of Establishments in each municipality.")

    def Pillar2():
        # Define the colors for imports, exports, and apparent consumption
        # colors = ['lightblue', 'steelblue', 'darkblue', 'darkslateblue']

        # Create a scatter plot with hover labels
        fig = px.scatter(dfP2_DS_year,x='Establishments', y='FTE', hover_data=['CAT_B'],
                         labels={'FTE': 'Employment',"CAT_B": "Municipality"},
                          #       "k": "Product Code", "description": "Description"},
                         title='Scatter Plot of Imports vs. Fit',
                         color_discrete_sequence=['purple'])

        # Create a grouped bar chart with individual bars for each category
        # fig = go.Figure()
        # fig.add_trace(go.Bar(x=years, y=imports, name='Imports', marker=dict(color=colors[0])))
        # fig.add_trace(go.Bar(x=years, y=exports, name='Exports', marker=dict(color=colors[1])))
        # fig.add_trace(go.Bar(x=years, y=output, name='Output', marker=dict(color=colors[2])))
        # fig.add_trace(go.Bar(x=years, y=consumption, name='Local Consumption (Apparent)', marker=dict(color=colors[3])))

        fig.update_layout(title='South African Furniture Industry Employment and Establishments per Municipality')
        # fig.update_traces(mode='markers', marker_size=8)

        fig.update_layout(
            barmode='group',
            xaxis_title='Establishments',
            yaxis_title='Employment',
            legend_title='Category'
        )
        return fig

    fig = Pillar2()
    # Render the chart in Streamlit
    st.plotly_chart(fig)


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
