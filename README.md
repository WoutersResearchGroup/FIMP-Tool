# FIMP Tool
Public repository of the prototype Python code related to research on an economic complexity based decision support tool for South African industrial policy masterplans. 

## Web-App
The developed Furniture Industry Masterplan Tool (FIMP) can be accessed as a web application on Streamlit from: https://fimp-tool.streamlit.app

The application features one Key Performance Indicator (KPI) and one Decision Support Indicator (DSI) for each key focus area (pillar) of the South African Furniture Industry Masterplan.

The KPIs for each pillar are organised in a dashboard view while each DSI occupies its own view. The dashboard is customizable and each KPI element can be resized and moved.

## Future Efforts
- Update the tool with more recent data.
- Expand the tool to encompass a full decision support system with a focus on data quality, scalability and reproducibility.
- Further stakeholder engagement and integation to determine the feasibility of solutions and facilitate solution implementation.
- Application to other masterplans and industrial policies.
- Upgrading the tool to an enterprise-level web application beyond a prototype (e.g. using Django).

## References
The data sources used to inform and compute the metrics are included in the methodology view of the application.

An altered version of the py-IO-PS package was used to compute metrics related to Economic Complexity.

The py-IO-PS package is available from: https://github.com/WoutersResearchGroup/py-IO-PS

An altered version of the Streamlit Elements package was used to create the application and dasbhoard.

Streamlit Elements is available from: https://github.com/okld/streamlit-elements
