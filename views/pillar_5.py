import streamlit as st
import pandas as pd
import plotly.express as px
# Ensure the file is included in the path
from pathlib import Path


def main():

    st.title("Pillar 5: Skills")

    #sliderP5_DS = st.sidebar.slider("Pillar 5: Decision Support", min_value=2010, max_value=2020, value=(2020))
    dfP5_DS = pd.read_csv('Pillar5_DS.csv')
    #dfP5_DS_year = dfP5_DS[(dfP5_DS['TaxYear'] == sliderP5_DS)]
    median_Importance = dfP5_DS['Importance'].median()
    median_Level= dfP5_DS['Level'].median()
#
    st.subheader("KPI: South African Furniture Export")

    st.write(
        """ "The agreed targets by 20230 are: **Increase exports of South Africa manufactured furniture and components** by at least 50% of baseline by 2030". [1] """)


    st.subheader("DS: What furniture industry knowledge, skills and abilities should be targetted")
    st.write(
        """ "Strategic objective: Invest in **skills development** to improve current and future skills across value chain". [1]""")
    st.write(
        "The formulated decision support indicator is measuring the average importance and required level of competence associated with the top 50 knowledge, skills and abilities per furniture industry occupation.")

    def Pillar5():
        # Define the colors for imports, exports, and apparent consumption
        # colors = ['lightblue', 'steelblue', 'darkblue', 'darkslateblue']

        # Create a scatter plot with hover labels
        fig = px.scatter(dfP5_DS,x='Importance', y='Level', hover_data=['Element Name'],
                         labels={'Level': "Required Level of Competence"},
                          #       "k": "Product Code", "description": "Description"},
                         title='Scatter Plot of Imports vs. Fit',
                         color_discrete_sequence=['purple'])

        # Add a vertical line at the median of `density`
        fig.add_shape(
            type="line",
            x0=median_Importance, x1=median_Importance, y0=dfP5_DS['Level'].min(),
            y1=dfP5_DS['Level'].max(),
            line=dict(color="Black", width=2, dash="dash")
        )
        # Add a horizontal line at the median of `importVal`
        fig.add_shape(
            type="line",
            x0=dfP5_DS['Importance'].min(), x1=dfP5_DS['Importance'].max(), y0=median_Level,
            y1=median_Level,
            line=dict(color="Black", width=2, dash="dash")
        )
        # Create a grouped bar chart with individual bars for each category
        # fig = go.Figure()
        # fig.add_trace(go.Bar(x=years, y=imports, name='Imports', marker=dict(color=colors[0])))
        # fig.add_trace(go.Bar(x=years, y=exports, name='Exports', marker=dict(color=colors[1])))
        # fig.add_trace(go.Bar(x=years, y=output, name='Output', marker=dict(color=colors[2])))
        # fig.add_trace(go.Bar(x=years, y=consumption, name='Local Consumption (Apparent)', marker=dict(color=colors[3])))

        fig.update_layout(title='Top 50 Most Important Furniture Industry Knowledge, Skills and Abilities<br>versus their Required Level of Competence')
        # fig.update_traces(mode='markers', marker_size=8)

        fig.update_layout(
            barmode='group',
            xaxis_title='Importance',
            yaxis_title='Competence',
            legend_title='Category'
        )
        return fig



    fig = Pillar5()
    # Render the chart in Streamlit
    st.plotly_chart(fig)


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
