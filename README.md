### Research Abstract
Public transportation plays a vital role in urban development and sustainability. This research paper explores the role of subway stations' network value within the Metropolitan Transportation Authority (MTA) subway system and its correlation with the transportation mode chosen by commuters in neighboring areas. Utilizing block group-level census data, the study conducts a geospatial analysis of the subway network and its neighboring areas. Leveraging datasets from the US Census and the MTA, this research seeks to uncover the significance of subway stations' network centrality value — gauged via closeness, betweenness, and PageRank metrics — in relation to neighborhoods with diverse population densities and socio-economic attributes. Findings indicate that subway stations boasting higher network values are correlated with neighborhoods with a propensity to use non vehicular modes of transport, indicating their significance in promoting alternative means of travel. These results can assist policymakers and transportation planners by elucidating the significance of the centrality value of subway stations and its relationship with surrounding neighborhoods, thereby informing decisions regarding public transportation infrastructure investments to enhance accessibility and connectivity. This study underscores the importance of understanding the network value of subway stations within the MTA subway system in devising more efficient and effective public transportation strategies.

***Keywords: network analysis, urban planning, GIS, transportation, machine learning, linear regression, decision trees, XGBoost***

### Layout of the repository
- **./ml_analysis/** : Exploratory US Census Data ML Analysis
- **./qgis_analysis/** : QGis analysis and according shapefiles
- **./geopanda_analysis/** : Full Geospatial data analysis, XGBoost machine learning & OLS Linear regression analysis
 - data retrieval and cleanup is all contained within **./geopanda_analysis/** as a standalone project unrelated to other folders
 - MTA GTFS schedule feed is parsed into daily schedules through the software found at https://github.com/ctjong27/gtfs_to_nodes_and_edges


### Link to High Level Analysis and Full Thesis Paper
https://musingcj.com/#mta_analysis