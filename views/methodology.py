import streamlit as st
from pathlib import Path

def main():
   st.title("Methodology")
    st.header("Data")
    st.write("**Masterplan for the South African Furniture Industry:**")
    st.write(
        "Furniture industry pillars, strategic objectives and targets drawn from the Furniture Industry Masterplan (FIMP). [1]"
    )
    st.write("**Import, Export, Output and Apparent Consumption:**")
    st.write(
        "Drawn from the United Nations Industrial Development Organization's (UNIDO) Industrial Demand-Supply Balance Database (ISDB) Revision 3 from 2010-2020. [2]"
    )
    st.write("**Knowledge, Skills and Abilities:**")
    st.write(
        "Knowledge, Skills, and Abilities mappings of the Standard Occupational Classification (SOC) codes from the U.S. Bureau of Labour Statistics (BLS) by the Occupational Information Network (O\*NET). O\*NET mapped the importance and competence of 35 skills, 33 knowledge areas, and 52 abilities for 873 occupations. [3]"
    )
    st.write("**Occupation Data:**")
    st.write(
        "South African Census 2011, 10% Sample data's 39 P30A_OCCUPATION (occupation) codes. [4]"
    )
    st.write("**Trade Data:**")
    st.write(
        "Bilateral, international trade flows per 6-digit Harmonised System (HS) codes drawn from the CEPII-BACI database for 2010-2020. [5]"
    )
    st.write("**Tax Data:**")
    st.write(
        "South African Spatial Tax Panel data containing Full-Time Equivalent (FTE) and establishment data for each 2-digit Standard Industrial Classifaction (SIC) industry per local municipality, metro and nationally from 2014-2020. [6]"
    )
    st.header("Dashboard")
    st.write("**Furniture Imports and Domestic Demand:** ")
    st.write(
        "ISDB data filtered to South Africa and International Standard Industrial Classification (ISIC) code 3610 (furniture manufacturing)."
    )
    st.write("**Furniture Industry Total Employment and Total Establishments:**")
    st.write("Tax panel data at the 2-digit level filtered to the furniture industry.")
    st.write("**Furniture Exports Values:**")
    st.write(
        "Export trade data aggregated per 6-digit HS code and filtered to South Africa and SAFI furniture products of interest."
    )
    st.write("**Raw Material Import Values:**")
    st.write(
        "Import trade data aggregated per 6-digit HS code and filtered to South Africa and SAFI raw material products of interest."
    )
    st.header("Decision Support")
    st.write("**Furniture Products Import Values:**")
    st.write(
        "Import trade data aggregated per 6-digit HS code and filtered to South Africa and SAFI furniture product of interest."
    )
    st.write("**Relatedness Density:**")
    st.write(
        "A measure of the similarity between a country's existing production capability and a specific product. Captures the similarity between a product and all the products the economy already produces and exports competitively. [7]"
    )
    st.write("**Furniture Industry Employment and Establishments per Municipality:**")
    st.write(
        "Tax Panel Data at the 2-digit level per local municipality and metro filtered to the furniture industry."
    )
    st.write("**Product Complexity:**")
    st.write(
        "A measure of the level of sophistication required to to manufacture a product. Complex economies are made up of complex products and a higher economic complexity is correlated with higher levels of development across a broad range of indicators (e.g. Economic growth, GDP/capita, inequality). [7]"
    )
    st.write("**Raw Material Import Values:**")
    st.write(
        "Import trade data aggregated per 6-digit HS code and filtered to South Africa and SAFI raw material products of interest."
    )
    st.write("**Top 50 Knowledge, Skills and Abilities' Importance and Competence:**")
    st.write(
        "Skills, abilities and Knowledege elements per SOC occupation filetered to top 50 per occupation. Thereafter, the top 50 per SOC code was concorded to the South African occupation codes in the Census data and the average competence and importance associated with each element was calculated based on respondents who selected furniture manufacturing as their industry of employment."
        " O\*NET measures importance as the degree to which the element is required by the occupation, while competence is a measure of the proficiency required in the skill to perform it satisfactorily per occupation. [3]"
    )

    st.header("References")
    st.write(
        "[1] Department: Trade, Industry and Competition. Republic of South Africa. (2023). Masterplan for the South African Furniture Industry Version 3."
    )  
    st.write(
        "[2] United Nations Industrial Development Organisation. “IDSB Revision 3.” UNIDO Statistics Portal, 2024, stat.unido.org/data/table?dataset=idsb&revision=3. Accessed 26 Oct. 2024."
    )
    st.write(
        "[3] National Center for O\*NET Development. O*NET 29.0 Database. O\*NET Resource Center. Retrieved October 26, 2024, from https://www.onetcenter.org/database.html"
    )
    st.write(
        "[4] Statistics South Africa. South African Census 2011, 10\% sample [dataset]. Version 2. Pretoria: Statistics South Africa [producer], 2015. Cape Town: DataFirst [distributor], 2015. DOI: https://doi.org/10.25828/vjy1-tz66/"
    )
    st.write(
        "[5] Guillaume Gaulier & Soledad Zignago , 2010. BACI: International Trade Database at the Product-Level. The 1994-2007 Version, CEPII Working Paper 2010- 23 , October 2010 , CEPII."
    )
    st.write(
        "[6] Nell, A. Visagie, J. Spatial Tax Panel 2014-2022 [dataset]. Version 3.2. National Treasury - Cities Support Programme and Human Sciences Research Council [producer and distributor], 2023."
    )
    st.write(
        "[7] Hausmann, R. et al. (2011) The Atlas of economic complexity : mapping paths to prosperity. Cambridge, Mass. : Center for International Development, Harvard University : Harvard Kennedy School : Macro Connections, MIT : Massachusetts Institute of Technology. Available at: http://archive.org/details/TheAtlasOfEconomicComplexity (Accessed: 17 May 2022)."
    )

    
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
