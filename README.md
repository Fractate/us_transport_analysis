US Transit usage analysis

https://medium.com/@ctjong27/zip-area-data-for-us-commute-61d69c60b55e

Projection used in the project is EPSG Projection 4269 - NAD83
https://epsg.io/4269

I attempt to analyze the cause and effect of transit usage.

I hypothesize that in areas with higher percentage non-personal vehicle means of commute is strongly correlated to higher density of housing as seen in various research papers that calculate 'walkability' index.
- In order to use the aggregate number of vehicles in a given area, I am using census tract data rather than block groups

Furthermore, I hypothesize that buffer of station coverage (in the means of the-way-crow-walks) can demonstrate that a certain level of coverage in a census tract will coincide with less vehicle usage and higher levels of transit use. This would be most interesting to observe as a contrast between large metropolitian area such as New York and relatively smaller and less dense cities such as Albany.

I also suspect that a network effect plays a factor in the value of public transit usage, meaning a more inter-connected network facilitates greater use in non-personal vehicle use.

It would be worth researching vehicle ownership per census tract and its correlation with the "power" of local transit use.

# Variables of note
Constant year for shapefile & american community survey 5 year retrieval = 2019
State in focus = 'ny'
