import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

def main():
    st.title("Pillar 5: Skills")
    dfP5_DS = pd.read_csv('data/Pillar5_DS.csv')
    median_Importance = dfP5_DS['Importance'].median()
    median_Level= dfP5_DS['Level'].median()
    st.subheader("KPI: South African Furniture Exports")
    st.write(
        """ "The agreed targets by 2030 are: **Increase exports of South Africa manufactured furniture and components** by at least 50% of baseline by 2030". [1] """)
    st.subheader("DSI: What furniture industry knowledge, skills and abilities should be targetted")
    st.write(
        """ "Strategic objective: Invest in **skills development** to improve current and future skills across value chain". [1]""")
    st.write(
        "The formulated decision support indicator is measuring the average importance and required level of competence associated with the top 50 knowledge, skills and abilities per furniture industry occupation.")

    def Pillar5():
        fig = px.scatter(dfP5_DS,x='Importance', y='Level', hover_data=['Element Name'],
                         labels={'Level': "Required Level of Competence"},
                         title='Scatter Plot of Imports vs. Fit',
                         color_discrete_sequence=['purple'])
        fig.add_shape(
            type="line",
            x0=median_Importance, x1=median_Importance, y0=dfP5_DS['Level'].min(),
            y1=dfP5_DS['Level'].max(),
            line=dict(color="Black", width=2, dash="dash")
        )
        fig.add_shape(
            type="line",
            x0=dfP5_DS['Importance'].min(), x1=dfP5_DS['Importance'].max(), y0=median_Level,
            y1=median_Level,
            line=dict(color="Black", width=2, dash="dash")
        )
        fig.update_layout(title='Top 50 Most Important South African Furniture Industry Knowledge, Skills and Abilities<br>versus their Required Level of Competence')
        fig.update_layout(
            barmode='group',
            xaxis_title='Importance',
            yaxis_title='Competence',
            legend_title='Category'
        )
        return fig
    fig = Pillar5()
    st.plotly_chart(fig)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
