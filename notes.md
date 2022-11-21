# total cars in an area
# total population in an area
# total commute time

Hypothesis

While walking and public transit may take a bit of time and while driving might seem faster, long term, public transit and walking scales better than everyone driving - this can be measured in time it takes to get to place of work

# variables indexing spreadsheet
https://www2.census.gov/programs-surveys/acs/summary_file/2009/documentation/5_year/user_tools/ACS2009_5-Year_TableShells.xls
https://www2.census.gov/acs2005_2009_5yr/summaryfile/ACS2009_5-Year_TableShells.xls
https://www.census.gov/programs-surveys/acs/technical-documentation/table-shells/2019.html
https://www2.census.gov/programs-surveys/acs/summary_file/2019/documentation/user_tools/ACS2019_Table_Shells.xlsx

# Variable categories I might be interested in 
Own Children Under 18 Years Living in Families or Subfamilies for Whom Poverty Status Is Determined,ACS09_5yr_B05010001
% Own Children Under 18 Years Living in Families or Subfamilies for Whom Poverty Status Is Determined: Under 1.00,PCT_ACS09_5yr_B05010002

Population in the United States for Whom Poverty Status Is Determined,ACS09_5yr_B06012001
% Population in the United States for Whom Poverty Status Is Determined: Below 100 Percent of the Poverty Level,PCT_ACS09_5yr_B06012002

Population 1 Year and Over in the United States for Whom Poverty Status Is Determined,ACS09_5yr_B07012001
% Population 1 Year and Over in the United States for Whom Poverty Status Is Determined: Below 100 Percent of the Poverty Level,PCT_ACS09_5yr_B07012002

Population 1 Year and Over in the United States for Whom Poverty Status Is Determined: Total Living in Area 1 Year Ago,ACS09_5yr_B07412001
% Population 1 Year and Over in the United States for Whom Poverty Status Is Determined: Total Living in Area 1 Year Ago: Below 100 Percent of the Poverty Level,PCT_ACS09_5yr_B07412002

Population 1 Year and Over for Whom Poverty Status Is Determined: Total Living in Area 1 Year Ago,ACS09_5yr_B07412PR001
% Population 1 Year and Over for Whom Poverty Status Is Determined: Total Living in Area 1 Year Ago: Below 100 Percent of the Poverty Level,PCT_ACS09_5yr_B07412PR002


"Workers Whose Means of Transportation Is Car, Truck, or Van: Aggregate Number of Vehicles (Car, Truck, or Van) Used in Commuting",ACS09_5yr_B08015001



## Vehicle related
Workers 16 Years and Over for Whom Poverty Status Is Determined,ACS09_5yr_B08122001
Workers 16 Years and Over for Whom Poverty Status Is Determined: Below 100 Percent of the Poverty Level,ACS09_5yr_B08122002
Workers 16 Years and Over for Whom Poverty Status Is Determined: 100 to 149 Percent of the Poverty Level,ACS09_5yr_B08122003
Workers 16 Years and Over for Whom Poverty Status Is Determined: At or Above 150 Percent of the Poverty Level,ACS09_5yr_B08122004


# all of the variabes are found below, from there, which variables am I interested in?
### workers via transportation (Can be split between men and women)
Workers 16 Years and Over,ACS09_5yr_B08006001  -  total workers
"Workers 16 Years and Over: Car, Truck, or Van",ACS09_5yr_B08006002
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab)",ACS09_5yr_B08006008
"Workers 16 Years and Over: Car, Truck, or Van: Bicycle",ACS09_5yr_B08006014
"Workers 16 Years and Over: Car, Truck, or Van: Walked",ACS09_5yr_B08006015
"Workers 16 Years and Over: Car, Truck, or Van: Taxicab, Motorcycle, or Other Means",ACS09_5yr_B08006016
"Workers 16 Years and Over: Car, Truck, or Van: Worked At Home",ACS09_5yr_B08006017
Workers 16 Years and Over Who Did Not Work At Home.1,ACS09_5yr_B08012001
Workers 16 Years and Over Who Did Not Work At Home: Less than 5 Minutes,ACS09_5yr_B08012002
Workers 16 Years and Over Who Did Not Work At Home: 5 to 9 Minutes,ACS09_5yr_B08012003
Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes,ACS09_5yr_B08012004
Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes,ACS09_5yr_B08012005
Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes,ACS09_5yr_B08012006
Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes,ACS09_5yr_B08012007
Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes,ACS09_5yr_B08012008
Workers 16 Years and Over Who Did Not Work At Home: 35 to 39 Minutes,ACS09_5yr_B08012009
Workers 16 Years and Over Who Did Not Work At Home: 40 to 44 Minutes,ACS09_5yr_B08012010
Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes,ACS09_5yr_B08012011
Workers 16 Years and Over Who Did Not Work At Home: 60 to 89 Minutes,ACS09_5yr_B08012012
Workers 16 Years and Over Who Did Not Work At Home: 90 or More Minutes,ACS09_5yr_B08012013

Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes),ACS09_5yr_B08013001

Workers 16 Years and Over in Households,ACS09_5yr_B08014001
Workers 16 Years and Over in Households: No Vehicle Available,ACS09_5yr_B08014002
Workers 16 Years and Over in Households: 1 Vehicle Available,ACS09_5yr_B08014003
Workers 16 Years and Over in Households: 2 Vehicles Available,ACS09_5yr_B08014004
Workers 16 Years and Over in Households: 3 Vehicles Available,ACS09_5yr_B08014005
Workers 16 Years and Over in Households: 4 Vehicles Available,ACS09_5yr_B08014006
Workers 16 Years and Over in Households: 5 or More Vehicles Available,ACS09_5yr_B08014007

Workers 16 Years and Over: Median Age -- Total,ACS09_5yr_B08103001
"Workers 16 Years and Over: Median Age -- Car, Truck, or Van - Drove Alone",ACS09_5yr_B08103002
"Workers 16 Years and Over: Median Age -- Car, Truck, or Van - Carpooled",ACS09_5yr_B08103003
Workers 16 Years and Over: Median Age -- Public Transportation (Excluding Taxicab),ACS09_5yr_B08103004
Workers 16 Years and Over: Median Age -- Walked,ACS09_5yr_B08103005
"Workers 16 Years and Over: Median Age -- Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08103006
Workers 16 Years and Over: Median Age -- Worked At Home,ACS09_5yr_B08103007


Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Total [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121001
"Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Car, Truck, or Van - Drove Alone [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08121002
"Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Car, Truck, or Van - Carpooled [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08121003
Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Public Transportation (Excluding Taxicab) [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121004
Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Walked [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121005
"Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Taxicab, Motorcycle, Bicycle, or Other Means [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08121006
Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Worked At Home [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121007


Workers 16 Years and Over Who Did Not Work At Home.3,ACS09_5yr_C08134001
Workers 16 Years and Over Who Did Not Work At Home: Less than 10 Minutes,ACS09_5yr_C08134002
Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.1,ACS09_5yr_C08134003
Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.1,ACS09_5yr_C08134004
Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.1,ACS09_5yr_C08134005
Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.1,ACS09_5yr_C08134006
Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.1,ACS09_5yr_C08134007
Workers 16 Years and Over Who Did Not Work At Home: 35 to 44 Minutes,ACS09_5yr_C08134008
Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.1,ACS09_5yr_C08134009
Workers 16 Years and Over Who Did Not Work At Home: 60 or More Minutes,ACS09_5yr_C08134010
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_C08134011
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: Less than 10 Minutes",ACS09_5yr_C08134012
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 10 to 14 Minutes",ACS09_5yr_C08134013
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 15 to 19 Minutes",ACS09_5yr_C08134014
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 20 to 24 Minutes",ACS09_5yr_C08134015
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 25 to 29 Minutes",ACS09_5yr_C08134016
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 30 to 34 Minutes",ACS09_5yr_C08134017
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 35 to 44 Minutes",ACS09_5yr_C08134018
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 45 to 59 Minutes",ACS09_5yr_C08134019
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 60 or More Minutes",ACS09_5yr_C08134020
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled.1",ACS09_5yr_C08134021
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: Less than 10 Minutes",ACS09_5yr_C08134022
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 10 to 14 Minutes",ACS09_5yr_C08134023
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 15 to 19 Minutes",ACS09_5yr_C08134024
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 20 to 24 Minutes",ACS09_5yr_C08134025
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 25 to 29 Minutes",ACS09_5yr_C08134026
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 30 to 34 Minutes",ACS09_5yr_C08134027
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 35 to 44 Minutes",ACS09_5yr_C08134028
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 45 to 59 Minutes",ACS09_5yr_C08134029
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 60 or More Minutes",ACS09_5yr_C08134030
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab).1,ACS09_5yr_C08134031
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): Less than 10 Minutes,ACS09_5yr_C08134032
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 10 to 14 Minutes,ACS09_5yr_C08134033
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 15 to 19 Minutes,ACS09_5yr_C08134034
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 20 to 24 Minutes,ACS09_5yr_C08134035
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 25 to 29 Minutes,ACS09_5yr_C08134036
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 30 to 34 Minutes,ACS09_5yr_C08134037
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 35 to 44 Minutes,ACS09_5yr_C08134038
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 45 to 59 Minutes,ACS09_5yr_C08134039
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 60 or More Minutes,ACS09_5yr_C08134040
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means",ACS09_5yr_C08134041
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: Less than 10 Minutes",ACS09_5yr_C08134042
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 10 to 14 Minutes",ACS09_5yr_C08134043
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 15 to 19 Minutes",ACS09_5yr_C08134044
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 20 to 24 Minutes",ACS09_5yr_C08134045
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 25 to 29 Minutes",ACS09_5yr_C08134046
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 30 to 34 Minutes",ACS09_5yr_C08134047
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 35 to 44 Minutes",ACS09_5yr_C08134048
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 45 to 59 Minutes",ACS09_5yr_C08134049
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 60 or More Minutes",ACS09_5yr_C08134050
% Workers 16 Years and Over Who Did Not Work At Home: Less than 10 Minutes,PCT_ACS09_5yr_C08134002
% Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.1,PCT_ACS09_5yr_C08134003
% Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.1,PCT_ACS09_5yr_C08134004
% Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.1,PCT_ACS09_5yr_C08134005
% Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.1,PCT_ACS09_5yr_C08134006
% Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.1,PCT_ACS09_5yr_C08134007
% Workers 16 Years and Over Who Did Not Work At Home: 35 to 44 Minutes,PCT_ACS09_5yr_C08134008
% Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.1,PCT_ACS09_5yr_C08134009
% Workers 16 Years and Over Who Did Not Work At Home: 60 or More Minutes,PCT_ACS09_5yr_C08134010
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_C08134011
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: Less than 10 Minutes",PCT_ACS09_5yr_C08134012
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 10 to 14 Minutes",PCT_ACS09_5yr_C08134013
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 15 to 19 Minutes",PCT_ACS09_5yr_C08134014
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 20 to 24 Minutes",PCT_ACS09_5yr_C08134015
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 25 to 29 Minutes",PCT_ACS09_5yr_C08134016
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 30 to 34 Minutes",PCT_ACS09_5yr_C08134017
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 35 to 44 Minutes",PCT_ACS09_5yr_C08134018
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 45 to 59 Minutes",PCT_ACS09_5yr_C08134019
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 60 or More Minutes",PCT_ACS09_5yr_C08134020
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_C08134021
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: Less than 10 Minutes",PCT_ACS09_5yr_C08134022
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 10 to 14 Minutes",PCT_ACS09_5yr_C08134023
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 15 to 19 Minutes",PCT_ACS09_5yr_C08134024
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 20 to 24 Minutes",PCT_ACS09_5yr_C08134025
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 25 to 29 Minutes",PCT_ACS09_5yr_C08134026
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 30 to 34 Minutes",PCT_ACS09_5yr_C08134027
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 35 to 44 Minutes",PCT_ACS09_5yr_C08134028
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 45 to 59 Minutes",PCT_ACS09_5yr_C08134029
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 60 or More Minutes",PCT_ACS09_5yr_C08134030
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_C08134031
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): Less than 10 Minutes,PCT_ACS09_5yr_C08134032
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 10 to 14 Minutes,PCT_ACS09_5yr_C08134033
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 15 to 19 Minutes,PCT_ACS09_5yr_C08134034
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 20 to 24 Minutes,PCT_ACS09_5yr_C08134035
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 25 to 29 Minutes,PCT_ACS09_5yr_C08134036
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 30 to 34 Minutes,PCT_ACS09_5yr_C08134037
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 35 to 44 Minutes,PCT_ACS09_5yr_C08134038
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 45 to 59 Minutes,PCT_ACS09_5yr_C08134039
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 60 or More Minutes,PCT_ACS09_5yr_C08134040
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means",PCT_ACS09_5yr_C08134041
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: Less than 10 Minutes",PCT_ACS09_5yr_C08134042
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 10 to 14 Minutes",PCT_ACS09_5yr_C08134043
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 15 to 19 Minutes",PCT_ACS09_5yr_C08134044
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 20 to 24 Minutes",PCT_ACS09_5yr_C08134045
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 25 to 29 Minutes",PCT_ACS09_5yr_C08134046
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 30 to 34 Minutes",PCT_ACS09_5yr_C08134047
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 35 to 44 Minutes",PCT_ACS09_5yr_C08134048
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 45 to 59 Minutes",PCT_ACS09_5yr_C08134049
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 60 or More Minutes",PCT_ACS09_5yr_C08134050

Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes).3,ACS09_5yr_B08135001



# Variables that might be usable from 2009 and 2019 datasets
Workers 16 Years and Over,ACS09_5yr_B08006001
"Workers 16 Years and Over: Car, Truck, or Van",ACS09_5yr_B08006002
"Workers 16 Years and Over: Car, Truck, or Van: Drove Alone",ACS09_5yr_B08006003
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled",ACS09_5yr_B08006004
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 2-Person Carpool",ACS09_5yr_B08006005
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 3-Person Carpool",ACS09_5yr_B08006006
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool",ACS09_5yr_B08006007
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab)",ACS09_5yr_B08006008
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Bus or Trolley Bus",ACS09_5yr_B08006009
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico)",ACS09_5yr_B08006010
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Subway or Elevated",ACS09_5yr_B08006011
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Railroad",ACS09_5yr_B08006012
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Ferryboat",ACS09_5yr_B08006013
"Workers 16 Years and Over: Car, Truck, or Van: Bicycle",ACS09_5yr_B08006014
"Workers 16 Years and Over: Car, Truck, or Van: Walked",ACS09_5yr_B08006015
"Workers 16 Years and Over: Car, Truck, or Van: Taxicab, Motorcycle, or Other Means",ACS09_5yr_B08006016
"Workers 16 Years and Over: Car, Truck, or Van: Worked At Home",ACS09_5yr_B08006017
Workers 16 Years and Over: Male,ACS09_5yr_B08006018
"Workers 16 Years and Over: Male: Car, Truck, or Van",ACS09_5yr_B08006019
"Workers 16 Years and Over: Male: Car, Truck, or Van: Drove Alone",ACS09_5yr_B08006020
"Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled",ACS09_5yr_B08006021
"Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 2-Person Carpool",ACS09_5yr_B08006022
"Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 3-Person Carpool",ACS09_5yr_B08006023
"Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool",ACS09_5yr_B08006024
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab),ACS09_5yr_B08006025
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Bus or Trolley Bus,ACS09_5yr_B08006026
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico),ACS09_5yr_B08006027
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Subway or Elevated,ACS09_5yr_B08006028
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Railroad,ACS09_5yr_B08006029
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Ferryboat,ACS09_5yr_B08006030
Workers 16 Years and Over: Male: Bicycle,ACS09_5yr_B08006031
Workers 16 Years and Over: Male: Walked,ACS09_5yr_B08006032
"Workers 16 Years and Over: Male: Taxicab, Motorcycle, or Other Means",ACS09_5yr_B08006033
Workers 16 Years and Over: Male: Worked At Home,ACS09_5yr_B08006034
Workers 16 Years and Over: Female,ACS09_5yr_B08006035
"Workers 16 Years and Over: Female: Car, Truck, or Van",ACS09_5yr_B08006036
"Workers 16 Years and Over: Female: Car, Truck, or Van: Drove Alone",ACS09_5yr_B08006037
"Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled",ACS09_5yr_B08006038
"Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 2-Person Carpool",ACS09_5yr_B08006039
"Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 3-Person Carpool",ACS09_5yr_B08006040
"Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool",ACS09_5yr_B08006041
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab),ACS09_5yr_B08006042
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Bus or Trolley Bus,ACS09_5yr_B08006043
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico),ACS09_5yr_B08006044
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Subway or Elevated,ACS09_5yr_B08006045
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Railroad,ACS09_5yr_B08006046
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Ferryboat,ACS09_5yr_B08006047
Workers 16 Years and Over: Female: Bicycle,ACS09_5yr_B08006048
Workers 16 Years and Over: Female: Walked,ACS09_5yr_B08006049
"Workers 16 Years and Over: Female: Taxicab, Motorcycle, or Other Means",ACS09_5yr_B08006050
Workers 16 Years and Over: Female: Worked At Home,ACS09_5yr_B08006051
Std. Error: Workers 16 Years and Over,ACS09_5yr_B08006001s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van",ACS09_5yr_B08006002s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Drove Alone",ACS09_5yr_B08006003s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled",ACS09_5yr_B08006004s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 2-Person Carpool",ACS09_5yr_B08006005s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 3-Person Carpool",ACS09_5yr_B08006006s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool",ACS09_5yr_B08006007s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab)",ACS09_5yr_B08006008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Bus or Trolley Bus",ACS09_5yr_B08006009s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico)",ACS09_5yr_B08006010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Subway or Elevated",ACS09_5yr_B08006011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Railroad",ACS09_5yr_B08006012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Ferryboat",ACS09_5yr_B08006013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Bicycle",ACS09_5yr_B08006014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Walked",ACS09_5yr_B08006015s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Taxicab, Motorcycle, or Other Means",ACS09_5yr_B08006016s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Worked At Home",ACS09_5yr_B08006017s
Std. Error: Workers 16 Years and Over: Male,ACS09_5yr_B08006018s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van",ACS09_5yr_B08006019s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van: Drove Alone",ACS09_5yr_B08006020s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled",ACS09_5yr_B08006021s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 2-Person Carpool",ACS09_5yr_B08006022s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 3-Person Carpool",ACS09_5yr_B08006023s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool",ACS09_5yr_B08006024s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab),ACS09_5yr_B08006025s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Bus or Trolley Bus,ACS09_5yr_B08006026s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico),ACS09_5yr_B08006027s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Subway or Elevated,ACS09_5yr_B08006028s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Railroad,ACS09_5yr_B08006029s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Ferryboat,ACS09_5yr_B08006030s
Std. Error: Workers 16 Years and Over: Male: Bicycle,ACS09_5yr_B08006031s
Std. Error: Workers 16 Years and Over: Male: Walked,ACS09_5yr_B08006032s
"Std. Error: Workers 16 Years and Over: Male: Taxicab, Motorcycle, or Other Means",ACS09_5yr_B08006033s
Std. Error: Workers 16 Years and Over: Male: Worked At Home,ACS09_5yr_B08006034s
Std. Error: Workers 16 Years and Over: Female,ACS09_5yr_B08006035s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van",ACS09_5yr_B08006036s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van: Drove Alone",ACS09_5yr_B08006037s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled",ACS09_5yr_B08006038s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 2-Person Carpool",ACS09_5yr_B08006039s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 3-Person Carpool",ACS09_5yr_B08006040s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool",ACS09_5yr_B08006041s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab),ACS09_5yr_B08006042s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Bus or Trolley Bus,ACS09_5yr_B08006043s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico),ACS09_5yr_B08006044s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Subway or Elevated,ACS09_5yr_B08006045s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Railroad,ACS09_5yr_B08006046s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Ferryboat,ACS09_5yr_B08006047s
Std. Error: Workers 16 Years and Over: Female: Bicycle,ACS09_5yr_B08006048s
Std. Error: Workers 16 Years and Over: Female: Walked,ACS09_5yr_B08006049s
"Std. Error: Workers 16 Years and Over: Female: Taxicab, Motorcycle, or Other Means",ACS09_5yr_B08006050s
Std. Error: Workers 16 Years and Over: Female: Worked At Home,ACS09_5yr_B08006051s
"% Workers 16 Years and Over: Car, Truck, or Van",PCT_ACS09_5yr_B08006002
"% Workers 16 Years and Over: Car, Truck, or Van: Drove Alone",PCT_ACS09_5yr_B08006003
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled",PCT_ACS09_5yr_B08006004
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 2-Person Carpool",PCT_ACS09_5yr_B08006005
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 3-Person Carpool",PCT_ACS09_5yr_B08006006
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool",PCT_ACS09_5yr_B08006007
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab)",PCT_ACS09_5yr_B08006008
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Bus or Trolley Bus",PCT_ACS09_5yr_B08006009
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico)",PCT_ACS09_5yr_B08006010
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Subway or Elevated",PCT_ACS09_5yr_B08006011
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Railroad",PCT_ACS09_5yr_B08006012
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Ferryboat",PCT_ACS09_5yr_B08006013
"% Workers 16 Years and Over: Car, Truck, or Van: Bicycle",PCT_ACS09_5yr_B08006014
"% Workers 16 Years and Over: Car, Truck, or Van: Walked",PCT_ACS09_5yr_B08006015
"% Workers 16 Years and Over: Car, Truck, or Van: Taxicab, Motorcycle, or Other Means",PCT_ACS09_5yr_B08006016
"% Workers 16 Years and Over: Car, Truck, or Van: Worked At Home",PCT_ACS09_5yr_B08006017
% Workers 16 Years and Over: Male,PCT_ACS09_5yr_B08006018
"% Workers 16 Years and Over: Male: Car, Truck, or Van",PCT_ACS09_5yr_B08006019
"% Workers 16 Years and Over: Male: Car, Truck, or Van: Drove Alone",PCT_ACS09_5yr_B08006020
"% Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled",PCT_ACS09_5yr_B08006021
"% Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 2-Person Carpool",PCT_ACS09_5yr_B08006022
"% Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 3-Person Carpool",PCT_ACS09_5yr_B08006023
"% Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool",PCT_ACS09_5yr_B08006024
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08006025
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Bus or Trolley Bus,PCT_ACS09_5yr_B08006026
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico),PCT_ACS09_5yr_B08006027
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Subway or Elevated,PCT_ACS09_5yr_B08006028
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Railroad,PCT_ACS09_5yr_B08006029
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Ferryboat,PCT_ACS09_5yr_B08006030
% Workers 16 Years and Over: Male: Bicycle,PCT_ACS09_5yr_B08006031
% Workers 16 Years and Over: Male: Walked,PCT_ACS09_5yr_B08006032
"% Workers 16 Years and Over: Male: Taxicab, Motorcycle, or Other Means",PCT_ACS09_5yr_B08006033
% Workers 16 Years and Over: Male: Worked At Home,PCT_ACS09_5yr_B08006034
% Workers 16 Years and Over: Female,PCT_ACS09_5yr_B08006035
"% Workers 16 Years and Over: Female: Car, Truck, or Van",PCT_ACS09_5yr_B08006036
"% Workers 16 Years and Over: Female: Car, Truck, or Van: Drove Alone",PCT_ACS09_5yr_B08006037
"% Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled",PCT_ACS09_5yr_B08006038
"% Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 2-Person Carpool",PCT_ACS09_5yr_B08006039
"% Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 3-Person Carpool",PCT_ACS09_5yr_B08006040
"% Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool",PCT_ACS09_5yr_B08006041
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08006042
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Bus or Trolley Bus,PCT_ACS09_5yr_B08006043
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico),PCT_ACS09_5yr_B08006044
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Subway or Elevated,PCT_ACS09_5yr_B08006045
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Railroad,PCT_ACS09_5yr_B08006046
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Ferryboat,PCT_ACS09_5yr_B08006047
% Workers 16 Years and Over: Female: Bicycle,PCT_ACS09_5yr_B08006048
% Workers 16 Years and Over: Female: Walked,PCT_ACS09_5yr_B08006049
"% Workers 16 Years and Over: Female: Taxicab, Motorcycle, or Other Means",PCT_ACS09_5yr_B08006050
% Workers 16 Years and Over: Female: Worked At Home,PCT_ACS09_5yr_B08006051
Workers 16 Years and Over.1,ACS09_5yr_B08007001
Workers 16 Years and Over: Worked in State of Residence,ACS09_5yr_B08007002
Workers 16 Years and Over: Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08007003
Workers 16 Years and Over: Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08007004
Workers 16 Years and Over: Worked in State of Residence: Worked Outside State of Residence,ACS09_5yr_B08007005
Workers 16 Years and Over: Male.1,ACS09_5yr_B08007006
Workers 16 Years and Over: Male: Worked in State of Residence,ACS09_5yr_B08007007
Workers 16 Years and Over: Male: Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08007008
Workers 16 Years and Over: Male: Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08007009
Workers 16 Years and Over: Male: Worked Outside State of Residence,ACS09_5yr_B08007010
Workers 16 Years and Over: Female.1,ACS09_5yr_B08007011
Workers 16 Years and Over: Female: Worked in State of Residence,ACS09_5yr_B08007012
Workers 16 Years and Over: Female: Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08007013
Workers 16 Years and Over: Female: Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08007014
Workers 16 Years and Over: Female: Worked Outside State of Residence,ACS09_5yr_B08007015
Std. Error: Workers 16 Years and Over.1,ACS09_5yr_B08007001s
Std. Error: Workers 16 Years and Over: Worked in State of Residence,ACS09_5yr_B08007002s
Std. Error: Workers 16 Years and Over: Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08007003s
Std. Error: Workers 16 Years and Over: Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08007004s
Std. Error: Workers 16 Years and Over: Worked in State of Residence: Worked Outside State of Residence,ACS09_5yr_B08007005s
Std. Error: Workers 16 Years and Over: Male.1,ACS09_5yr_B08007006s
Std. Error: Workers 16 Years and Over: Male: Worked in State of Residence,ACS09_5yr_B08007007s
Std. Error: Workers 16 Years and Over: Male: Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08007008s
Std. Error: Workers 16 Years and Over: Male: Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08007009s
Std. Error: Workers 16 Years and Over: Male: Worked Outside State of Residence,ACS09_5yr_B08007010s
Std. Error: Workers 16 Years and Over: Female.1,ACS09_5yr_B08007011s
Std. Error: Workers 16 Years and Over: Female: Worked in State of Residence,ACS09_5yr_B08007012s
Std. Error: Workers 16 Years and Over: Female: Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08007013s
Std. Error: Workers 16 Years and Over: Female: Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08007014s
Std. Error: Workers 16 Years and Over: Female: Worked Outside State of Residence,ACS09_5yr_B08007015s
% Workers 16 Years and Over: Worked in State of Residence,PCT_ACS09_5yr_B08007002
% Workers 16 Years and Over: Worked in State of Residence: Worked in County of Residence,PCT_ACS09_5yr_B08007003
% Workers 16 Years and Over: Worked in State of Residence: Worked Outside County of Residence,PCT_ACS09_5yr_B08007004
% Workers 16 Years and Over: Worked in State of Residence: Worked Outside State of Residence,PCT_ACS09_5yr_B08007005
% Workers 16 Years and Over: Male.1,PCT_ACS09_5yr_B08007006
% Workers 16 Years and Over: Male: Worked in State of Residence,PCT_ACS09_5yr_B08007007
% Workers 16 Years and Over: Male: Worked in State of Residence: Worked in County of Residence,PCT_ACS09_5yr_B08007008
% Workers 16 Years and Over: Male: Worked in State of Residence: Worked Outside County of Residence,PCT_ACS09_5yr_B08007009
% Workers 16 Years and Over: Male: Worked Outside State of Residence,PCT_ACS09_5yr_B08007010
% Workers 16 Years and Over: Female.1,PCT_ACS09_5yr_B08007011
% Workers 16 Years and Over: Female: Worked in State of Residence,PCT_ACS09_5yr_B08007012
% Workers 16 Years and Over: Female: Worked in State of Residence: Worked in County of Residence,PCT_ACS09_5yr_B08007013
% Workers 16 Years and Over: Female: Worked in State of Residence: Worked Outside County of Residence,PCT_ACS09_5yr_B08007014
% Workers 16 Years and Over: Female: Worked Outside State of Residence,PCT_ACS09_5yr_B08007015
Workers 16 Years and Over.2,ACS09_5yr_B08008001
Workers 16 Years and Over: Living in a Place,ACS09_5yr_B08008002
Workers 16 Years and Over: Living in a Place: Worked in Place of Residence,ACS09_5yr_B08008003
Workers 16 Years and Over: Living in a Place: Worked Outside Place of Residence,ACS09_5yr_B08008004
Workers 16 Years and Over: Living in a Place: Not Living in a Place,ACS09_5yr_B08008005
Workers 16 Years and Over: Male.2,ACS09_5yr_B08008006
Workers 16 Years and Over: Male: Living in a Place,ACS09_5yr_B08008007
Workers 16 Years and Over: Male: Living in a Place: Worked in Place of Residence,ACS09_5yr_B08008008
Workers 16 Years and Over: Male: Living in a Place: Worked Outside Place of Residence,ACS09_5yr_B08008009
Workers 16 Years and Over: Male: Not Living in a Place,ACS09_5yr_B08008010
Workers 16 Years and Over: Female.2,ACS09_5yr_B08008011
Workers 16 Years and Over: Female: Living in a Place,ACS09_5yr_B08008012
Workers 16 Years and Over: Female: Living in a Place: Worked in Place of Residence,ACS09_5yr_B08008013
Workers 16 Years and Over: Female: Living in a Place: Worked Outside Place of Residence,ACS09_5yr_B08008014
Workers 16 Years and Over: Female: Not Living in a Place,ACS09_5yr_B08008015
Std. Error: Workers 16 Years and Over.2,ACS09_5yr_B08008001s
Std. Error: Workers 16 Years and Over: Living in a Place,ACS09_5yr_B08008002s
Std. Error: Workers 16 Years and Over: Living in a Place: Worked in Place of Residence,ACS09_5yr_B08008003s
Std. Error: Workers 16 Years and Over: Living in a Place: Worked Outside Place of Residence,ACS09_5yr_B08008004s
Std. Error: Workers 16 Years and Over: Living in a Place: Not Living in a Place,ACS09_5yr_B08008005s
Std. Error: Workers 16 Years and Over: Male.2,ACS09_5yr_B08008006s
Std. Error: Workers 16 Years and Over: Male: Living in a Place,ACS09_5yr_B08008007s
Std. Error: Workers 16 Years and Over: Male: Living in a Place: Worked in Place of Residence,ACS09_5yr_B08008008s
Std. Error: Workers 16 Years and Over: Male: Living in a Place: Worked Outside Place of Residence,ACS09_5yr_B08008009s
Std. Error: Workers 16 Years and Over: Male: Not Living in a Place,ACS09_5yr_B08008010s
Std. Error: Workers 16 Years and Over: Female.2,ACS09_5yr_B08008011s
Std. Error: Workers 16 Years and Over: Female: Living in a Place,ACS09_5yr_B08008012s
Std. Error: Workers 16 Years and Over: Female: Living in a Place: Worked in Place of Residence,ACS09_5yr_B08008013s
Std. Error: Workers 16 Years and Over: Female: Living in a Place: Worked Outside Place of Residence,ACS09_5yr_B08008014s
Std. Error: Workers 16 Years and Over: Female: Not Living in a Place,ACS09_5yr_B08008015s
% Workers 16 Years and Over: Living in a Place,PCT_ACS09_5yr_B08008002
% Workers 16 Years and Over: Living in a Place: Worked in Place of Residence,PCT_ACS09_5yr_B08008003
% Workers 16 Years and Over: Living in a Place: Worked Outside Place of Residence,PCT_ACS09_5yr_B08008004
% Workers 16 Years and Over: Living in a Place: Not Living in a Place,PCT_ACS09_5yr_B08008005
% Workers 16 Years and Over: Male.2,PCT_ACS09_5yr_B08008006
% Workers 16 Years and Over: Male: Living in a Place,PCT_ACS09_5yr_B08008007
% Workers 16 Years and Over: Male: Living in a Place: Worked in Place of Residence,PCT_ACS09_5yr_B08008008
% Workers 16 Years and Over: Male: Living in a Place: Worked Outside Place of Residence,PCT_ACS09_5yr_B08008009
% Workers 16 Years and Over: Male: Not Living in a Place,PCT_ACS09_5yr_B08008010
% Workers 16 Years and Over: Female.2,PCT_ACS09_5yr_B08008011
% Workers 16 Years and Over: Female: Living in a Place,PCT_ACS09_5yr_B08008012
% Workers 16 Years and Over: Female: Living in a Place: Worked in Place of Residence,PCT_ACS09_5yr_B08008013
% Workers 16 Years and Over: Female: Living in a Place: Worked Outside Place of Residence,PCT_ACS09_5yr_B08008014
% Workers 16 Years and Over: Female: Not Living in a Place,PCT_ACS09_5yr_B08008015
Workers 16 Years and Over.3,ACS09_5yr_B08009001
Workers 16 Years and Over: Living in the 12 Selected States,ACS09_5yr_B08009002
Workers 16 Years and Over: Living in the 12 Selected States: Worked in Mcd of Residence,ACS09_5yr_B08009003
Workers 16 Years and Over: Living in the 12 Selected States: Worked Outside Mcd of Residence,ACS09_5yr_B08009004
Workers 16 Years and Over: Living in the 12 Selected States: Not Living in the 12 Selected States,ACS09_5yr_B08009005
Workers 16 Years and Over: Male.3,ACS09_5yr_B08009006
Workers 16 Years and Over: Male: Living in the 12 Selected States,ACS09_5yr_B08009007
Workers 16 Years and Over: Male: Living in the 12 Selected States: Worked in Mcd of Residence,ACS09_5yr_B08009008
Workers 16 Years and Over: Male: Living in the 12 Selected States: Worked Outside Mcd of Residence,ACS09_5yr_B08009009
Workers 16 Years and Over: Male: Not Living in the 12 Selected States,ACS09_5yr_B08009010
Workers 16 Years and Over: Female.3,ACS09_5yr_B08009011
Workers 16 Years and Over: Female: Living in the 12 Selected States,ACS09_5yr_B08009012
Workers 16 Years and Over: Female: Living in the 12 Selected States: Worked in Mcd of Residence,ACS09_5yr_B08009013
Workers 16 Years and Over: Female: Living in the 12 Selected States: Worked Outside Mcd of Residence,ACS09_5yr_B08009014
Workers 16 Years and Over: Female: Not Living in the 12 Selected States,ACS09_5yr_B08009015
Std. Error: Workers 16 Years and Over.3,ACS09_5yr_B08009001s
Std. Error: Workers 16 Years and Over: Living in the 12 Selected States,ACS09_5yr_B08009002s
Std. Error: Workers 16 Years and Over: Living in the 12 Selected States: Worked in Mcd of Residence,ACS09_5yr_B08009003s
Std. Error: Workers 16 Years and Over: Living in the 12 Selected States: Worked Outside Mcd of Residence,ACS09_5yr_B08009004s
Std. Error: Workers 16 Years and Over: Living in the 12 Selected States: Not Living in the 12 Selected States,ACS09_5yr_B08009005s
Std. Error: Workers 16 Years and Over: Male.3,ACS09_5yr_B08009006s
Std. Error: Workers 16 Years and Over: Male: Living in the 12 Selected States,ACS09_5yr_B08009007s
Std. Error: Workers 16 Years and Over: Male: Living in the 12 Selected States: Worked in Mcd of Residence,ACS09_5yr_B08009008s
Std. Error: Workers 16 Years and Over: Male: Living in the 12 Selected States: Worked Outside Mcd of Residence,ACS09_5yr_B08009009s
Std. Error: Workers 16 Years and Over: Male: Not Living in the 12 Selected States,ACS09_5yr_B08009010s
Std. Error: Workers 16 Years and Over: Female.3,ACS09_5yr_B08009011s
Std. Error: Workers 16 Years and Over: Female: Living in the 12 Selected States,ACS09_5yr_B08009012s
Std. Error: Workers 16 Years and Over: Female: Living in the 12 Selected States: Worked in Mcd of Residence,ACS09_5yr_B08009013s
Std. Error: Workers 16 Years and Over: Female: Living in the 12 Selected States: Worked Outside Mcd of Residence,ACS09_5yr_B08009014s
Std. Error: Workers 16 Years and Over: Female: Not Living in the 12 Selected States,ACS09_5yr_B08009015s
% Workers 16 Years and Over: Living in the 12 Selected States,PCT_ACS09_5yr_B08009002
% Workers 16 Years and Over: Living in the 12 Selected States: Worked in Mcd of Residence,PCT_ACS09_5yr_B08009003
% Workers 16 Years and Over: Living in the 12 Selected States: Worked Outside Mcd of Residence,PCT_ACS09_5yr_B08009004
% Workers 16 Years and Over: Living in the 12 Selected States: Not Living in the 12 Selected States,PCT_ACS09_5yr_B08009005
% Workers 16 Years and Over: Male.3,PCT_ACS09_5yr_B08009006
% Workers 16 Years and Over: Male: Living in the 12 Selected States,PCT_ACS09_5yr_B08009007
% Workers 16 Years and Over: Male: Living in the 12 Selected States: Worked in Mcd of Residence,PCT_ACS09_5yr_B08009008
% Workers 16 Years and Over: Male: Living in the 12 Selected States: Worked Outside Mcd of Residence,PCT_ACS09_5yr_B08009009
% Workers 16 Years and Over: Male: Not Living in the 12 Selected States,PCT_ACS09_5yr_B08009010
% Workers 16 Years and Over: Female.3,PCT_ACS09_5yr_B08009011
% Workers 16 Years and Over: Female: Living in the 12 Selected States,PCT_ACS09_5yr_B08009012
% Workers 16 Years and Over: Female: Living in the 12 Selected States: Worked in Mcd of Residence,PCT_ACS09_5yr_B08009013
% Workers 16 Years and Over: Female: Living in the 12 Selected States: Worked Outside Mcd of Residence,PCT_ACS09_5yr_B08009014
% Workers 16 Years and Over: Female: Not Living in the 12 Selected States,PCT_ACS09_5yr_B08009015
Workers 16 Years and Over Who Did Not Work At Home,ACS09_5yr_B08011001
Workers 16 Years and Over Who Did Not Work At Home: 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08011002
Workers 16 Years and Over Who Did Not Work At Home: 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08011003
Workers 16 Years and Over Who Did Not Work At Home: 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08011004
Workers 16 Years and Over Who Did Not Work At Home: 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08011005
Workers 16 Years and Over Who Did Not Work At Home: 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08011006
Workers 16 Years and Over Who Did Not Work At Home: 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08011007
Workers 16 Years and Over Who Did Not Work At Home: 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08011008
Workers 16 Years and Over Who Did Not Work At Home: 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08011009
Workers 16 Years and Over Who Did Not Work At Home: 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08011010
Workers 16 Years and Over Who Did Not Work At Home: 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08011011
Workers 16 Years and Over Who Did Not Work At Home: 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08011012
Workers 16 Years and Over Who Did Not Work At Home: 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08011013
Workers 16 Years and Over Who Did Not Work At Home: 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08011014
Workers 16 Years and Over Who Did Not Work At Home: 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08011015
Workers 16 Years and Over Who Did Not Work At Home: Male,ACS09_5yr_B08011016
Workers 16 Years and Over Who Did Not Work At Home: Male: 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08011017
Workers 16 Years and Over Who Did Not Work At Home: Male: 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08011018
Workers 16 Years and Over Who Did Not Work At Home: Male: 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08011019
Workers 16 Years and Over Who Did Not Work At Home: Male: 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08011020
Workers 16 Years and Over Who Did Not Work At Home: Male: 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08011021
Workers 16 Years and Over Who Did Not Work At Home: Male: 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08011022
Workers 16 Years and Over Who Did Not Work At Home: Male: 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08011023
Workers 16 Years and Over Who Did Not Work At Home: Male: 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08011024
Workers 16 Years and Over Who Did Not Work At Home: Male: 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08011025
Workers 16 Years and Over Who Did Not Work At Home: Male: 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08011026
Workers 16 Years and Over Who Did Not Work At Home: Male: 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08011027
Workers 16 Years and Over Who Did Not Work At Home: Male: 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08011028
Workers 16 Years and Over Who Did Not Work At Home: Male: 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08011029
Workers 16 Years and Over Who Did Not Work At Home: Male: 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08011030
Workers 16 Years and Over Who Did Not Work At Home: Female,ACS09_5yr_B08011031
Workers 16 Years and Over Who Did Not Work At Home: Female: 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08011032
Workers 16 Years and Over Who Did Not Work At Home: Female: 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08011033
Workers 16 Years and Over Who Did Not Work At Home: Female: 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08011034
Workers 16 Years and Over Who Did Not Work At Home: Female: 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08011035
Workers 16 Years and Over Who Did Not Work At Home: Female: 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08011036
Workers 16 Years and Over Who Did Not Work At Home: Female: 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08011037
Workers 16 Years and Over Who Did Not Work At Home: Female: 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08011038
Workers 16 Years and Over Who Did Not Work At Home: Female: 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08011039
Workers 16 Years and Over Who Did Not Work At Home: Female: 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08011040
Workers 16 Years and Over Who Did Not Work At Home: Female: 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08011041
Workers 16 Years and Over Who Did Not Work At Home: Female: 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08011042
Workers 16 Years and Over Who Did Not Work At Home: Female: 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08011043
Workers 16 Years and Over Who Did Not Work At Home: Female: 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08011044
Workers 16 Years and Over Who Did Not Work At Home: Female: 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08011045
Std. Error: Workers 16 Years and Over Who Did Not Work At Home,ACS09_5yr_B08011001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08011002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08011003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08011004s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08011005s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08011006s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08011007s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08011008s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08011009s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08011010s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08011011s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08011012s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08011013s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08011014s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08011015s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male,ACS09_5yr_B08011016s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08011017s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08011018s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08011019s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08011020s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08011021s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08011022s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08011023s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08011024s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08011025s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08011026s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08011027s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08011028s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08011029s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08011030s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female,ACS09_5yr_B08011031s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08011032s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08011033s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08011034s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08011035s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08011036s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08011037s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08011038s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08011039s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08011040s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08011041s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08011042s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08011043s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08011044s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08011045s
% Workers 16 Years and Over Who Did Not Work At Home: 12:00 A.m. to 4:59 A.m.,PCT_ACS09_5yr_B08011002
% Workers 16 Years and Over Who Did Not Work At Home: 5:00 A.m. to 5:29 A.m.,PCT_ACS09_5yr_B08011003
% Workers 16 Years and Over Who Did Not Work At Home: 5:30 A.m. to 5:59 A.m.,PCT_ACS09_5yr_B08011004
% Workers 16 Years and Over Who Did Not Work At Home: 6:00 A.m. to 6:29 A.m.,PCT_ACS09_5yr_B08011005
% Workers 16 Years and Over Who Did Not Work At Home: 6:30 A.m. to 6:59 A.m.,PCT_ACS09_5yr_B08011006
% Workers 16 Years and Over Who Did Not Work At Home: 7:00 A.m. to 7:29 A.m.,PCT_ACS09_5yr_B08011007
% Workers 16 Years and Over Who Did Not Work At Home: 7:30 A.m. to 7:59 A.m.,PCT_ACS09_5yr_B08011008
% Workers 16 Years and Over Who Did Not Work At Home: 8:00 A.m. to 8:29 A.m.,PCT_ACS09_5yr_B08011009
% Workers 16 Years and Over Who Did Not Work At Home: 8:30 A.m. to 8:59 A.m.,PCT_ACS09_5yr_B08011010
% Workers 16 Years and Over Who Did Not Work At Home: 9:00 A.m. to 9:59 A.m.,PCT_ACS09_5yr_B08011011
% Workers 16 Years and Over Who Did Not Work At Home: 10:00 A.m. to 10:59 A.m.,PCT_ACS09_5yr_B08011012
% Workers 16 Years and Over Who Did Not Work At Home: 11:00 A.m. to 11:59 A.m.,PCT_ACS09_5yr_B08011013
% Workers 16 Years and Over Who Did Not Work At Home: 12:00 P.m. to 3:59 P.m.,PCT_ACS09_5yr_B08011014
% Workers 16 Years and Over Who Did Not Work At Home: 4:00 P.m. to 11:59 P.m.,PCT_ACS09_5yr_B08011015
% Workers 16 Years and Over Who Did Not Work At Home: Male,PCT_ACS09_5yr_B08011016
% Workers 16 Years and Over Who Did Not Work At Home: Male: 12:00 A.m. to 4:59 A.m.,PCT_ACS09_5yr_B08011017
% Workers 16 Years and Over Who Did Not Work At Home: Male: 5:00 A.m. to 5:29 A.m.,PCT_ACS09_5yr_B08011018
% Workers 16 Years and Over Who Did Not Work At Home: Male: 5:30 A.m. to 5:59 A.m.,PCT_ACS09_5yr_B08011019
% Workers 16 Years and Over Who Did Not Work At Home: Male: 6:00 A.m. to 6:29 A.m.,PCT_ACS09_5yr_B08011020
% Workers 16 Years and Over Who Did Not Work At Home: Male: 6:30 A.m. to 6:59 A.m.,PCT_ACS09_5yr_B08011021
% Workers 16 Years and Over Who Did Not Work At Home: Male: 7:00 A.m. to 7:29 A.m.,PCT_ACS09_5yr_B08011022
% Workers 16 Years and Over Who Did Not Work At Home: Male: 7:30 A.m. to 7:59 A.m.,PCT_ACS09_5yr_B08011023
% Workers 16 Years and Over Who Did Not Work At Home: Male: 8:00 A.m. to 8:29 A.m.,PCT_ACS09_5yr_B08011024
% Workers 16 Years and Over Who Did Not Work At Home: Male: 8:30 A.m. to 8:59 A.m.,PCT_ACS09_5yr_B08011025
% Workers 16 Years and Over Who Did Not Work At Home: Male: 9:00 A.m. to 9:59 A.m.,PCT_ACS09_5yr_B08011026
% Workers 16 Years and Over Who Did Not Work At Home: Male: 10:00 A.m. to 10:59 A.m.,PCT_ACS09_5yr_B08011027
% Workers 16 Years and Over Who Did Not Work At Home: Male: 11:00 A.m. to 11:59 A.m.,PCT_ACS09_5yr_B08011028
% Workers 16 Years and Over Who Did Not Work At Home: Male: 12:00 P.m. to 3:59 P.m.,PCT_ACS09_5yr_B08011029
% Workers 16 Years and Over Who Did Not Work At Home: Male: 4:00 P.m. to 11:59 P.m.,PCT_ACS09_5yr_B08011030
% Workers 16 Years and Over Who Did Not Work At Home: Female,PCT_ACS09_5yr_B08011031
% Workers 16 Years and Over Who Did Not Work At Home: Female: 12:00 A.m. to 4:59 A.m.,PCT_ACS09_5yr_B08011032
% Workers 16 Years and Over Who Did Not Work At Home: Female: 5:00 A.m. to 5:29 A.m.,PCT_ACS09_5yr_B08011033
% Workers 16 Years and Over Who Did Not Work At Home: Female: 5:30 A.m. to 5:59 A.m.,PCT_ACS09_5yr_B08011034
% Workers 16 Years and Over Who Did Not Work At Home: Female: 6:00 A.m. to 6:29 A.m.,PCT_ACS09_5yr_B08011035
% Workers 16 Years and Over Who Did Not Work At Home: Female: 6:30 A.m. to 6:59 A.m.,PCT_ACS09_5yr_B08011036
% Workers 16 Years and Over Who Did Not Work At Home: Female: 7:00 A.m. to 7:29 A.m.,PCT_ACS09_5yr_B08011037
% Workers 16 Years and Over Who Did Not Work At Home: Female: 7:30 A.m. to 7:59 A.m.,PCT_ACS09_5yr_B08011038
% Workers 16 Years and Over Who Did Not Work At Home: Female: 8:00 A.m. to 8:29 A.m.,PCT_ACS09_5yr_B08011039
% Workers 16 Years and Over Who Did Not Work At Home: Female: 8:30 A.m. to 8:59 A.m.,PCT_ACS09_5yr_B08011040
% Workers 16 Years and Over Who Did Not Work At Home: Female: 9:00 A.m. to 9:59 A.m.,PCT_ACS09_5yr_B08011041
% Workers 16 Years and Over Who Did Not Work At Home: Female: 10:00 A.m. to 10:59 A.m.,PCT_ACS09_5yr_B08011042
% Workers 16 Years and Over Who Did Not Work At Home: Female: 11:00 A.m. to 11:59 A.m.,PCT_ACS09_5yr_B08011043
% Workers 16 Years and Over Who Did Not Work At Home: Female: 12:00 P.m. to 3:59 P.m.,PCT_ACS09_5yr_B08011044
% Workers 16 Years and Over Who Did Not Work At Home: Female: 4:00 P.m. to 11:59 P.m.,PCT_ACS09_5yr_B08011045
Workers 16 Years and Over Who Did Not Work At Home.1,ACS09_5yr_B08012001
Workers 16 Years and Over Who Did Not Work At Home: Less than 5 Minutes,ACS09_5yr_B08012002
Workers 16 Years and Over Who Did Not Work At Home: 5 to 9 Minutes,ACS09_5yr_B08012003
Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes,ACS09_5yr_B08012004
Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes,ACS09_5yr_B08012005
Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes,ACS09_5yr_B08012006
Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes,ACS09_5yr_B08012007
Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes,ACS09_5yr_B08012008
Workers 16 Years and Over Who Did Not Work At Home: 35 to 39 Minutes,ACS09_5yr_B08012009
Workers 16 Years and Over Who Did Not Work At Home: 40 to 44 Minutes,ACS09_5yr_B08012010
Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes,ACS09_5yr_B08012011
Workers 16 Years and Over Who Did Not Work At Home: 60 to 89 Minutes,ACS09_5yr_B08012012
Workers 16 Years and Over Who Did Not Work At Home: 90 or More Minutes,ACS09_5yr_B08012013
Workers 16 Years and Over Who Did Not Work At Home: Male.1,ACS09_5yr_B08012014
Workers 16 Years and Over Who Did Not Work At Home: Male: Less than 5 Minutes,ACS09_5yr_B08012015
Workers 16 Years and Over Who Did Not Work At Home: Male: 5 to 9 Minutes,ACS09_5yr_B08012016
Workers 16 Years and Over Who Did Not Work At Home: Male: 10 to 14 Minutes,ACS09_5yr_B08012017
Workers 16 Years and Over Who Did Not Work At Home: Male: 15 to 19 Minutes,ACS09_5yr_B08012018
Workers 16 Years and Over Who Did Not Work At Home: Male: 20 to 24 Minutes,ACS09_5yr_B08012019
Workers 16 Years and Over Who Did Not Work At Home: Male: 25 to 29 Minutes,ACS09_5yr_B08012020
Workers 16 Years and Over Who Did Not Work At Home: Male: 30 to 34 Minutes,ACS09_5yr_B08012021
Workers 16 Years and Over Who Did Not Work At Home: Male: 35 to 39 Minutes,ACS09_5yr_B08012022
Workers 16 Years and Over Who Did Not Work At Home: Male: 40 to 44 Minutes,ACS09_5yr_B08012023
Workers 16 Years and Over Who Did Not Work At Home: Male: 45 to 59 Minutes,ACS09_5yr_B08012024
Workers 16 Years and Over Who Did Not Work At Home: Male: 60 to 89 Minutes,ACS09_5yr_B08012025
Workers 16 Years and Over Who Did Not Work At Home: Male: 90 or More Minutes,ACS09_5yr_B08012026
Workers 16 Years and Over Who Did Not Work At Home: Female.1,ACS09_5yr_B08012027
Workers 16 Years and Over Who Did Not Work At Home: Female: Less than 5 Minutes,ACS09_5yr_B08012028
Workers 16 Years and Over Who Did Not Work At Home: Female: 5 to 9 Minutes,ACS09_5yr_B08012029
Workers 16 Years and Over Who Did Not Work At Home: Female: 10 to 14 Minutes,ACS09_5yr_B08012030
Workers 16 Years and Over Who Did Not Work At Home: Female: 15 to 19 Minutes,ACS09_5yr_B08012031
Workers 16 Years and Over Who Did Not Work At Home: Female: 20 to 24 Minutes,ACS09_5yr_B08012032
Workers 16 Years and Over Who Did Not Work At Home: Female: 25 to 29 Minutes,ACS09_5yr_B08012033
Workers 16 Years and Over Who Did Not Work At Home: Female: 30 to 34 Minutes,ACS09_5yr_B08012034
Workers 16 Years and Over Who Did Not Work At Home: Female: 35 to 39 Minutes,ACS09_5yr_B08012035
Workers 16 Years and Over Who Did Not Work At Home: Female: 40 to 44 Minutes,ACS09_5yr_B08012036
Workers 16 Years and Over Who Did Not Work At Home: Female: 45 to 59 Minutes,ACS09_5yr_B08012037
Workers 16 Years and Over Who Did Not Work At Home: Female: 60 to 89 Minutes,ACS09_5yr_B08012038
Workers 16 Years and Over Who Did Not Work At Home: Female: 90 or More Minutes,ACS09_5yr_B08012039
Std. Error: Workers 16 Years and Over Who Did Not Work At Home.1,ACS09_5yr_B08012001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Less than 5 Minutes,ACS09_5yr_B08012002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 5 to 9 Minutes,ACS09_5yr_B08012003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes,ACS09_5yr_B08012004s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes,ACS09_5yr_B08012005s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes,ACS09_5yr_B08012006s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes,ACS09_5yr_B08012007s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes,ACS09_5yr_B08012008s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 35 to 39 Minutes,ACS09_5yr_B08012009s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 40 to 44 Minutes,ACS09_5yr_B08012010s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes,ACS09_5yr_B08012011s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 60 to 89 Minutes,ACS09_5yr_B08012012s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 90 or More Minutes,ACS09_5yr_B08012013s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male.1,ACS09_5yr_B08012014s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: Less than 5 Minutes,ACS09_5yr_B08012015s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 5 to 9 Minutes,ACS09_5yr_B08012016s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 10 to 14 Minutes,ACS09_5yr_B08012017s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 15 to 19 Minutes,ACS09_5yr_B08012018s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 20 to 24 Minutes,ACS09_5yr_B08012019s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 25 to 29 Minutes,ACS09_5yr_B08012020s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 30 to 34 Minutes,ACS09_5yr_B08012021s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 35 to 39 Minutes,ACS09_5yr_B08012022s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 40 to 44 Minutes,ACS09_5yr_B08012023s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 45 to 59 Minutes,ACS09_5yr_B08012024s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 60 to 89 Minutes,ACS09_5yr_B08012025s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 90 or More Minutes,ACS09_5yr_B08012026s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female.1,ACS09_5yr_B08012027s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: Less than 5 Minutes,ACS09_5yr_B08012028s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 5 to 9 Minutes,ACS09_5yr_B08012029s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 10 to 14 Minutes,ACS09_5yr_B08012030s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 15 to 19 Minutes,ACS09_5yr_B08012031s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 20 to 24 Minutes,ACS09_5yr_B08012032s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 25 to 29 Minutes,ACS09_5yr_B08012033s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 30 to 34 Minutes,ACS09_5yr_B08012034s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 35 to 39 Minutes,ACS09_5yr_B08012035s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 40 to 44 Minutes,ACS09_5yr_B08012036s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 45 to 59 Minutes,ACS09_5yr_B08012037s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 60 to 89 Minutes,ACS09_5yr_B08012038s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 90 or More Minutes,ACS09_5yr_B08012039s
% Workers 16 Years and Over Who Did Not Work At Home: Less than 5 Minutes,PCT_ACS09_5yr_B08012002
% Workers 16 Years and Over Who Did Not Work At Home: 5 to 9 Minutes,PCT_ACS09_5yr_B08012003
% Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes,PCT_ACS09_5yr_B08012004
% Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes,PCT_ACS09_5yr_B08012005
% Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes,PCT_ACS09_5yr_B08012006
% Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes,PCT_ACS09_5yr_B08012007
% Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes,PCT_ACS09_5yr_B08012008
% Workers 16 Years and Over Who Did Not Work At Home: 35 to 39 Minutes,PCT_ACS09_5yr_B08012009
% Workers 16 Years and Over Who Did Not Work At Home: 40 to 44 Minutes,PCT_ACS09_5yr_B08012010
% Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes,PCT_ACS09_5yr_B08012011
% Workers 16 Years and Over Who Did Not Work At Home: 60 to 89 Minutes,PCT_ACS09_5yr_B08012012
% Workers 16 Years and Over Who Did Not Work At Home: 90 or More Minutes,PCT_ACS09_5yr_B08012013
% Workers 16 Years and Over Who Did Not Work At Home: Male.1,PCT_ACS09_5yr_B08012014
% Workers 16 Years and Over Who Did Not Work At Home: Male: Less than 5 Minutes,PCT_ACS09_5yr_B08012015
% Workers 16 Years and Over Who Did Not Work At Home: Male: 5 to 9 Minutes,PCT_ACS09_5yr_B08012016
% Workers 16 Years and Over Who Did Not Work At Home: Male: 10 to 14 Minutes,PCT_ACS09_5yr_B08012017
% Workers 16 Years and Over Who Did Not Work At Home: Male: 15 to 19 Minutes,PCT_ACS09_5yr_B08012018
% Workers 16 Years and Over Who Did Not Work At Home: Male: 20 to 24 Minutes,PCT_ACS09_5yr_B08012019
% Workers 16 Years and Over Who Did Not Work At Home: Male: 25 to 29 Minutes,PCT_ACS09_5yr_B08012020
% Workers 16 Years and Over Who Did Not Work At Home: Male: 30 to 34 Minutes,PCT_ACS09_5yr_B08012021
% Workers 16 Years and Over Who Did Not Work At Home: Male: 35 to 39 Minutes,PCT_ACS09_5yr_B08012022
% Workers 16 Years and Over Who Did Not Work At Home: Male: 40 to 44 Minutes,PCT_ACS09_5yr_B08012023
% Workers 16 Years and Over Who Did Not Work At Home: Male: 45 to 59 Minutes,PCT_ACS09_5yr_B08012024
% Workers 16 Years and Over Who Did Not Work At Home: Male: 60 to 89 Minutes,PCT_ACS09_5yr_B08012025
% Workers 16 Years and Over Who Did Not Work At Home: Male: 90 or More Minutes,PCT_ACS09_5yr_B08012026
% Workers 16 Years and Over Who Did Not Work At Home: Female.1,PCT_ACS09_5yr_B08012027
% Workers 16 Years and Over Who Did Not Work At Home: Female: Less than 5 Minutes,PCT_ACS09_5yr_B08012028
% Workers 16 Years and Over Who Did Not Work At Home: Female: 5 to 9 Minutes,PCT_ACS09_5yr_B08012029
% Workers 16 Years and Over Who Did Not Work At Home: Female: 10 to 14 Minutes,PCT_ACS09_5yr_B08012030
% Workers 16 Years and Over Who Did Not Work At Home: Female: 15 to 19 Minutes,PCT_ACS09_5yr_B08012031
% Workers 16 Years and Over Who Did Not Work At Home: Female: 20 to 24 Minutes,PCT_ACS09_5yr_B08012032
% Workers 16 Years and Over Who Did Not Work At Home: Female: 25 to 29 Minutes,PCT_ACS09_5yr_B08012033
% Workers 16 Years and Over Who Did Not Work At Home: Female: 30 to 34 Minutes,PCT_ACS09_5yr_B08012034
% Workers 16 Years and Over Who Did Not Work At Home: Female: 35 to 39 Minutes,PCT_ACS09_5yr_B08012035
% Workers 16 Years and Over Who Did Not Work At Home: Female: 40 to 44 Minutes,PCT_ACS09_5yr_B08012036
% Workers 16 Years and Over Who Did Not Work At Home: Female: 45 to 59 Minutes,PCT_ACS09_5yr_B08012037
% Workers 16 Years and Over Who Did Not Work At Home: Female: 60 to 89 Minutes,PCT_ACS09_5yr_B08012038
% Workers 16 Years and Over Who Did Not Work At Home: Female: 90 or More Minutes,PCT_ACS09_5yr_B08012039
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes),ACS09_5yr_B08013001
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Male,ACS09_5yr_B08013002
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Female,ACS09_5yr_B08013003
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes),ACS09_5yr_B08013001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Male,ACS09_5yr_B08013002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Female,ACS09_5yr_B08013003s
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Male,PCT_ACS09_5yr_B08013002
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Female,PCT_ACS09_5yr_B08013003
Workers 16 Years and Over in Households,ACS09_5yr_B08014001
Workers 16 Years and Over in Households: No Vehicle Available,ACS09_5yr_B08014002
Workers 16 Years and Over in Households: 1 Vehicle Available,ACS09_5yr_B08014003
Workers 16 Years and Over in Households: 2 Vehicles Available,ACS09_5yr_B08014004
Workers 16 Years and Over in Households: 3 Vehicles Available,ACS09_5yr_B08014005
Workers 16 Years and Over in Households: 4 Vehicles Available,ACS09_5yr_B08014006
Workers 16 Years and Over in Households: 5 or More Vehicles Available,ACS09_5yr_B08014007
Workers 16 Years and Over in Households: Male,ACS09_5yr_B08014008
Workers 16 Years and Over in Households: Male: No Vehicle Available,ACS09_5yr_B08014009
Workers 16 Years and Over in Households: Male: 1 Vehicle Available,ACS09_5yr_B08014010
Workers 16 Years and Over in Households: Male: 2 Vehicles Available,ACS09_5yr_B08014011
Workers 16 Years and Over in Households: Male: 3 Vehicles Available,ACS09_5yr_B08014012
Workers 16 Years and Over in Households: Male: 4 Vehicles Available,ACS09_5yr_B08014013
Workers 16 Years and Over in Households: Male: 5 or More Vehicles Available,ACS09_5yr_B08014014
Workers 16 Years and Over in Households: Female,ACS09_5yr_B08014015
Workers 16 Years and Over in Households: Female: No Vehicle Available,ACS09_5yr_B08014016
Workers 16 Years and Over in Households: Female: 1 Vehicle Available,ACS09_5yr_B08014017
Workers 16 Years and Over in Households: Female: 2 Vehicles Available,ACS09_5yr_B08014018
Workers 16 Years and Over in Households: Female: 3 Vehicles Available,ACS09_5yr_B08014019
Workers 16 Years and Over in Households: Female: 4 Vehicles Available,ACS09_5yr_B08014020
Workers 16 Years and Over in Households: Female: 5 or More Vehicles Available,ACS09_5yr_B08014021
Std. Error: Workers 16 Years and Over in Households,ACS09_5yr_B08014001s
Std. Error: Workers 16 Years and Over in Households: No Vehicle Available,ACS09_5yr_B08014002s
Std. Error: Workers 16 Years and Over in Households: 1 Vehicle Available,ACS09_5yr_B08014003s
Std. Error: Workers 16 Years and Over in Households: 2 Vehicles Available,ACS09_5yr_B08014004s
Std. Error: Workers 16 Years and Over in Households: 3 Vehicles Available,ACS09_5yr_B08014005s
Std. Error: Workers 16 Years and Over in Households: 4 Vehicles Available,ACS09_5yr_B08014006s
Std. Error: Workers 16 Years and Over in Households: 5 or More Vehicles Available,ACS09_5yr_B08014007s
Std. Error: Workers 16 Years and Over in Households: Male,ACS09_5yr_B08014008s
Std. Error: Workers 16 Years and Over in Households: Male: No Vehicle Available,ACS09_5yr_B08014009s
Std. Error: Workers 16 Years and Over in Households: Male: 1 Vehicle Available,ACS09_5yr_B08014010s
Std. Error: Workers 16 Years and Over in Households: Male: 2 Vehicles Available,ACS09_5yr_B08014011s
Std. Error: Workers 16 Years and Over in Households: Male: 3 Vehicles Available,ACS09_5yr_B08014012s
Std. Error: Workers 16 Years and Over in Households: Male: 4 Vehicles Available,ACS09_5yr_B08014013s
Std. Error: Workers 16 Years and Over in Households: Male: 5 or More Vehicles Available,ACS09_5yr_B08014014s
Std. Error: Workers 16 Years and Over in Households: Female,ACS09_5yr_B08014015s
Std. Error: Workers 16 Years and Over in Households: Female: No Vehicle Available,ACS09_5yr_B08014016s
Std. Error: Workers 16 Years and Over in Households: Female: 1 Vehicle Available,ACS09_5yr_B08014017s
Std. Error: Workers 16 Years and Over in Households: Female: 2 Vehicles Available,ACS09_5yr_B08014018s
Std. Error: Workers 16 Years and Over in Households: Female: 3 Vehicles Available,ACS09_5yr_B08014019s
Std. Error: Workers 16 Years and Over in Households: Female: 4 Vehicles Available,ACS09_5yr_B08014020s
Std. Error: Workers 16 Years and Over in Households: Female: 5 or More Vehicles Available,ACS09_5yr_B08014021s
% Workers 16 Years and Over in Households: No Vehicle Available,PCT_ACS09_5yr_B08014002
% Workers 16 Years and Over in Households: 1 Vehicle Available,PCT_ACS09_5yr_B08014003
% Workers 16 Years and Over in Households: 2 Vehicles Available,PCT_ACS09_5yr_B08014004
% Workers 16 Years and Over in Households: 3 Vehicles Available,PCT_ACS09_5yr_B08014005
% Workers 16 Years and Over in Households: 4 Vehicles Available,PCT_ACS09_5yr_B08014006
% Workers 16 Years and Over in Households: 5 or More Vehicles Available,PCT_ACS09_5yr_B08014007
% Workers 16 Years and Over in Households: Male,PCT_ACS09_5yr_B08014008
% Workers 16 Years and Over in Households: Male: No Vehicle Available,PCT_ACS09_5yr_B08014009
% Workers 16 Years and Over in Households: Male: 1 Vehicle Available,PCT_ACS09_5yr_B08014010
% Workers 16 Years and Over in Households: Male: 2 Vehicles Available,PCT_ACS09_5yr_B08014011
% Workers 16 Years and Over in Households: Male: 3 Vehicles Available,PCT_ACS09_5yr_B08014012
% Workers 16 Years and Over in Households: Male: 4 Vehicles Available,PCT_ACS09_5yr_B08014013
% Workers 16 Years and Over in Households: Male: 5 or More Vehicles Available,PCT_ACS09_5yr_B08014014
% Workers 16 Years and Over in Households: Female,PCT_ACS09_5yr_B08014015
% Workers 16 Years and Over in Households: Female: No Vehicle Available,PCT_ACS09_5yr_B08014016
% Workers 16 Years and Over in Households: Female: 1 Vehicle Available,PCT_ACS09_5yr_B08014017
% Workers 16 Years and Over in Households: Female: 2 Vehicles Available,PCT_ACS09_5yr_B08014018
% Workers 16 Years and Over in Households: Female: 3 Vehicles Available,PCT_ACS09_5yr_B08014019
% Workers 16 Years and Over in Households: Female: 4 Vehicles Available,PCT_ACS09_5yr_B08014020
% Workers 16 Years and Over in Households: Female: 5 or More Vehicles Available,PCT_ACS09_5yr_B08014021
"Workers Whose Means of Transportation Is Car, Truck, or Van: Aggregate Number of Vehicles (Car, Truck, or Van) Used in Commuting",ACS09_5yr_B08015001
"Workers Whose Means of Transportation Is Car, Truck, or Van: Aggregate Number of Vehicles (Car, Truck, or Van) Used in Commuting: Male",ACS09_5yr_B08015002
"Workers Whose Means of Transportation Is Car, Truck, or Van: Aggregate Number of Vehicles (Car, Truck, or Van) Used in Commuting: Female",ACS09_5yr_B08015003
"Std. Error: Workers Whose Means of Transportation Is Car, Truck, or Van: Aggregate Number of Vehicles (Car, Truck, or Van) Used in Commuting",ACS09_5yr_B08015001s
"Std. Error: Workers Whose Means of Transportation Is Car, Truck, or Van: Aggregate Number of Vehicles (Car, Truck, or Van) Used in Commuting: Male",ACS09_5yr_B08015002s
"Std. Error: Workers Whose Means of Transportation Is Car, Truck, or Van: Aggregate Number of Vehicles (Car, Truck, or Van) Used in Commuting: Female",ACS09_5yr_B08015003s
"% Workers Whose Means of Transportation Is Car, Truck, or Van: Aggregate Number of Vehicles (Car, Truck, or Van) Used in Commuting: Male",PCT_ACS09_5yr_B08015002
"% Workers Whose Means of Transportation Is Car, Truck, or Van: Aggregate Number of Vehicles (Car, Truck, or Van) Used in Commuting: Female",PCT_ACS09_5yr_B08015003
Workers 16 Years and Over Living in a Metropolitan Statistical Area,ACS09_5yr_B08016001
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City,ACS09_5yr_B08016002
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in Metropolitan Statistical Area of Residence,ACS09_5yr_B08016003
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in Metropolitan Statistical Area of Residence: Worked in a Principal City,ACS09_5yr_B08016004
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in Metropolitan Statistical Area of Residence: Worked Outside Any Principal City,ACS09_5yr_B08016005
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Different Metropolitan Statistical Area,ACS09_5yr_B08016006
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Different Metropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08016007
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Different Metropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08016008
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Micropolitan Statistical Area,ACS09_5yr_B08016009
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Micropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08016010
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Micropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08016011
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08016012
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City,ACS09_5yr_B08016013
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in Metropolitan Statistical Area of Residence,ACS09_5yr_B08016014
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in Metropolitan Statistical Area of Residence: Worked in a Principal City,ACS09_5yr_B08016015
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in Metropolitan Statistical Area of Residence: Worked Outside Any Principal City,ACS09_5yr_B08016016
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Metropolitan Statistical Area,ACS09_5yr_B08016017
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Metropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08016018
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Metropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08016019
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Micropolitan Statistical Area,ACS09_5yr_B08016020
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Micropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08016021
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Micropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08016022
Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08016023
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area,ACS09_5yr_B08016001s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City,ACS09_5yr_B08016002s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in Metropolitan Statistical Area of Residence,ACS09_5yr_B08016003s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in Metropolitan Statistical Area of Residence: Worked in a Principal City,ACS09_5yr_B08016004s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in Metropolitan Statistical Area of Residence: Worked Outside Any Principal City,ACS09_5yr_B08016005s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Different Metropolitan Statistical Area,ACS09_5yr_B08016006s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Different Metropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08016007s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Different Metropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08016008s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Micropolitan Statistical Area,ACS09_5yr_B08016009s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Micropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08016010s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Micropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08016011s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08016012s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City,ACS09_5yr_B08016013s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in Metropolitan Statistical Area of Residence,ACS09_5yr_B08016014s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in Metropolitan Statistical Area of Residence: Worked in a Principal City,ACS09_5yr_B08016015s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in Metropolitan Statistical Area of Residence: Worked Outside Any Principal City,ACS09_5yr_B08016016s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Metropolitan Statistical Area,ACS09_5yr_B08016017s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Metropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08016018s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Metropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08016019s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Micropolitan Statistical Area,ACS09_5yr_B08016020s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Micropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08016021s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Micropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08016022s
Std. Error: Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08016023s
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City,PCT_ACS09_5yr_B08016002
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in Metropolitan Statistical Area of Residence,PCT_ACS09_5yr_B08016003
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in Metropolitan Statistical Area of Residence: Worked in a Principal City,PCT_ACS09_5yr_B08016004
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in Metropolitan Statistical Area of Residence: Worked Outside Any Principal City,PCT_ACS09_5yr_B08016005
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Different Metropolitan Statistical Area,PCT_ACS09_5yr_B08016006
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Different Metropolitan Statistical Area: Worked in a Principal City,PCT_ACS09_5yr_B08016007
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Different Metropolitan Statistical Area: Worked Outside Any Principal City,PCT_ACS09_5yr_B08016008
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Micropolitan Statistical Area,PCT_ACS09_5yr_B08016009
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Micropolitan Statistical Area: Worked in a Principal City,PCT_ACS09_5yr_B08016010
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked in a Micropolitan Statistical Area: Worked Outside Any Principal City,PCT_ACS09_5yr_B08016011
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living in a Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,PCT_ACS09_5yr_B08016012
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City,PCT_ACS09_5yr_B08016013
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in Metropolitan Statistical Area of Residence,PCT_ACS09_5yr_B08016014
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in Metropolitan Statistical Area of Residence: Worked in a Principal City,PCT_ACS09_5yr_B08016015
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in Metropolitan Statistical Area of Residence: Worked Outside Any Principal City,PCT_ACS09_5yr_B08016016
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Metropolitan Statistical Area,PCT_ACS09_5yr_B08016017
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Metropolitan Statistical Area: Worked in a Principal City,PCT_ACS09_5yr_B08016018
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Metropolitan Statistical Area: Worked Outside Any Principal City,PCT_ACS09_5yr_B08016019
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Micropolitan Statistical Area,PCT_ACS09_5yr_B08016020
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Micropolitan Statistical Area: Worked in a Principal City,PCT_ACS09_5yr_B08016021
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked in a Micropolitan Statistical Area: Worked Outside Any Principal City,PCT_ACS09_5yr_B08016022
% Workers 16 Years and Over Living in a Metropolitan Statistical Area: Living Outside Any Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,PCT_ACS09_5yr_B08016023
Workers 16 Years and Over Living in a Micropolitan Statistical Area,ACS09_5yr_B08017001
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City,ACS09_5yr_B08017002
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in Micropolitan Statistical Area of Residence,ACS09_5yr_B08017003
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in Micropolitan Statistical Area of Residence: Worked in a Principal City,ACS09_5yr_B08017004
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in Micropolitan Statistical Area of Residence: Worked Outside Any Principal City,ACS09_5yr_B08017005
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Different Micropolitan Statistical Area,ACS09_5yr_B08017006
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Different Micropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08017007
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Different Micropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08017008
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Metropolitan Statistical Area,ACS09_5yr_B08017009
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Metropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08017010
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Metropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08017011
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08017012
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City,ACS09_5yr_B08017013
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in Micropolitan Statistical Area of Residence,ACS09_5yr_B08017014
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in Micropolitan Statistical Area of Residence: Worked in a Principal City,ACS09_5yr_B08017015
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in Micropolitan Statistical Area of Residence: Worked Outside Any Principal City,ACS09_5yr_B08017016
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Micropolitan Statistical Area,ACS09_5yr_B08017017
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Micropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08017018
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Micropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08017019
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Metropolitan Statistical Area,ACS09_5yr_B08017020
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Metropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08017021
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Metropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08017022
Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08017023
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area,ACS09_5yr_B08017001s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City,ACS09_5yr_B08017002s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in Micropolitan Statistical Area of Residence,ACS09_5yr_B08017003s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in Micropolitan Statistical Area of Residence: Worked in a Principal City,ACS09_5yr_B08017004s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in Micropolitan Statistical Area of Residence: Worked Outside Any Principal City,ACS09_5yr_B08017005s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Different Micropolitan Statistical Area,ACS09_5yr_B08017006s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Different Micropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08017007s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Different Micropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08017008s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Metropolitan Statistical Area,ACS09_5yr_B08017009s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Metropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08017010s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Metropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08017011s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08017012s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City,ACS09_5yr_B08017013s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in Micropolitan Statistical Area of Residence,ACS09_5yr_B08017014s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in Micropolitan Statistical Area of Residence: Worked in a Principal City,ACS09_5yr_B08017015s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in Micropolitan Statistical Area of Residence: Worked Outside Any Principal City,ACS09_5yr_B08017016s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Micropolitan Statistical Area,ACS09_5yr_B08017017s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Micropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08017018s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Micropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08017019s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Metropolitan Statistical Area,ACS09_5yr_B08017020s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Metropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08017021s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Metropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08017022s
Std. Error: Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08017023s
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City,PCT_ACS09_5yr_B08017002
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in Micropolitan Statistical Area of Residence,PCT_ACS09_5yr_B08017003
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in Micropolitan Statistical Area of Residence: Worked in a Principal City,PCT_ACS09_5yr_B08017004
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in Micropolitan Statistical Area of Residence: Worked Outside Any Principal City,PCT_ACS09_5yr_B08017005
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Different Micropolitan Statistical Area,PCT_ACS09_5yr_B08017006
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Different Micropolitan Statistical Area: Worked in a Principal City,PCT_ACS09_5yr_B08017007
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Different Micropolitan Statistical Area: Worked Outside Any Principal City,PCT_ACS09_5yr_B08017008
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Metropolitan Statistical Area,PCT_ACS09_5yr_B08017009
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Metropolitan Statistical Area: Worked in a Principal City,PCT_ACS09_5yr_B08017010
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked in a Metropolitan Statistical Area: Worked Outside Any Principal City,PCT_ACS09_5yr_B08017011
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living in a Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,PCT_ACS09_5yr_B08017012
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City,PCT_ACS09_5yr_B08017013
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in Micropolitan Statistical Area of Residence,PCT_ACS09_5yr_B08017014
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in Micropolitan Statistical Area of Residence: Worked in a Principal City,PCT_ACS09_5yr_B08017015
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in Micropolitan Statistical Area of Residence: Worked Outside Any Principal City,PCT_ACS09_5yr_B08017016
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Micropolitan Statistical Area,PCT_ACS09_5yr_B08017017
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Micropolitan Statistical Area: Worked in a Principal City,PCT_ACS09_5yr_B08017018
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Different Micropolitan Statistical Area: Worked Outside Any Principal City,PCT_ACS09_5yr_B08017019
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Metropolitan Statistical Area,PCT_ACS09_5yr_B08017020
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Metropolitan Statistical Area: Worked in a Principal City,PCT_ACS09_5yr_B08017021
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked in a Metropolitan Statistical Area: Worked Outside Any Principal City,PCT_ACS09_5yr_B08017022
% Workers 16 Years and Over Living in a Micropolitan Statistical Area: Living Outside Any Principal City: Worked Outside Any Metropolitan or Micropolitan Statistical Area,PCT_ACS09_5yr_B08017023
Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08018001
Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Metropolitan Statistical Area,ACS09_5yr_B08018002
Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Metropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08018003
Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Metropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08018004
Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Micropolitan Statistical Area,ACS09_5yr_B08018005
Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Micropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08018006
Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Micropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08018007
Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked Outside Any Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08018008
Std. Error: Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08018001s
Std. Error: Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Metropolitan Statistical Area,ACS09_5yr_B08018002s
Std. Error: Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Metropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08018003s
Std. Error: Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Metropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08018004s
Std. Error: Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Micropolitan Statistical Area,ACS09_5yr_B08018005s
Std. Error: Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Micropolitan Statistical Area: Worked in a Principal City,ACS09_5yr_B08018006s
Std. Error: Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Micropolitan Statistical Area: Worked Outside Any Principal City,ACS09_5yr_B08018007s
Std. Error: Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked Outside Any Metropolitan or Micropolitan Statistical Area,ACS09_5yr_B08018008s
% Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Metropolitan Statistical Area,PCT_ACS09_5yr_B08018002
% Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Metropolitan Statistical Area: Worked in a Principal City,PCT_ACS09_5yr_B08018003
% Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Metropolitan Statistical Area: Worked Outside Any Principal City,PCT_ACS09_5yr_B08018004
% Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Micropolitan Statistical Area,PCT_ACS09_5yr_B08018005
% Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Micropolitan Statistical Area: Worked in a Principal City,PCT_ACS09_5yr_B08018006
% Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked in a Micropolitan Statistical Area: Worked Outside Any Principal City,PCT_ACS09_5yr_B08018007
% Workers 16 Years and Over Not Living in a Metropolitan or Micropolitan Statistical Area: Worked Outside Any Metropolitan or Micropolitan Statistical Area,PCT_ACS09_5yr_B08018008
Workers 16 Years and Over.4,ACS09_5yr_B08101001
Workers 16 Years and Over: 16 to 19 Years,ACS09_5yr_B08101002
Workers 16 Years and Over: 20 to 24 Years,ACS09_5yr_B08101003
Workers 16 Years and Over: 25 to 44 Years,ACS09_5yr_B08101004
Workers 16 Years and Over: 45 to 54 Years,ACS09_5yr_B08101005
Workers 16 Years and Over: 55 to 59 Years,ACS09_5yr_B08101006
Workers 16 Years and Over: 60 to 64 Years,ACS09_5yr_B08101007
Workers 16 Years and Over: 65 Years and Over,ACS09_5yr_B08101008
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08101009
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 16 to 19 Years",ACS09_5yr_B08101010
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 20 to 24 Years",ACS09_5yr_B08101011
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 25 to 44 Years",ACS09_5yr_B08101012
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 45 to 54 Years",ACS09_5yr_B08101013
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 55 to 59 Years",ACS09_5yr_B08101014
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 60 to 64 Years",ACS09_5yr_B08101015
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 65 Years and Over",ACS09_5yr_B08101016
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08101017
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 16 to 19 Years",ACS09_5yr_B08101018
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 20 to 24 Years",ACS09_5yr_B08101019
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 25 to 44 Years",ACS09_5yr_B08101020
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 45 to 54 Years",ACS09_5yr_B08101021
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 55 to 59 Years",ACS09_5yr_B08101022
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 60 to 64 Years",ACS09_5yr_B08101023
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 65 Years and Over",ACS09_5yr_B08101024
Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08101025
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 16 to 19 Years,ACS09_5yr_B08101026
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 20 to 24 Years,ACS09_5yr_B08101027
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 25 to 44 Years,ACS09_5yr_B08101028
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 45 to 54 Years,ACS09_5yr_B08101029
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 55 to 59 Years,ACS09_5yr_B08101030
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 60 to 64 Years,ACS09_5yr_B08101031
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 65 Years and Over,ACS09_5yr_B08101032
Workers 16 Years and Over: Walked,ACS09_5yr_B08101033
Workers 16 Years and Over: Walked: 16 to 19 Years,ACS09_5yr_B08101034
Workers 16 Years and Over: Walked: 20 to 24 Years,ACS09_5yr_B08101035
Workers 16 Years and Over: Walked: 25 to 44 Years,ACS09_5yr_B08101036
Workers 16 Years and Over: Walked: 45 to 54 Years,ACS09_5yr_B08101037
Workers 16 Years and Over: Walked: 55 to 59 Years,ACS09_5yr_B08101038
Workers 16 Years and Over: Walked: 60 to 64 Years,ACS09_5yr_B08101039
Workers 16 Years and Over: Walked: 65 Years and Over,ACS09_5yr_B08101040
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08101041
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 16 to 19 Years",ACS09_5yr_B08101042
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 20 to 24 Years",ACS09_5yr_B08101043
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 25 to 44 Years",ACS09_5yr_B08101044
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 45 to 54 Years",ACS09_5yr_B08101045
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 55 to 59 Years",ACS09_5yr_B08101046
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 60 to 64 Years",ACS09_5yr_B08101047
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 65 Years and Over",ACS09_5yr_B08101048
Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08101049
Workers 16 Years and Over: Worked At Home: 16 to 19 Years,ACS09_5yr_B08101050
Workers 16 Years and Over: Worked At Home: 20 to 24 Years,ACS09_5yr_B08101051
Workers 16 Years and Over: Worked At Home: 25 to 44 Years,ACS09_5yr_B08101052
Workers 16 Years and Over: Worked At Home: 45 to 54 Years,ACS09_5yr_B08101053
Workers 16 Years and Over: Worked At Home: 55 to 59 Years,ACS09_5yr_B08101054
Workers 16 Years and Over: Worked At Home: 60 to 64 Years,ACS09_5yr_B08101055
Workers 16 Years and Over: Worked At Home: 65 Years and Over,ACS09_5yr_B08101056
Std. Error: Workers 16 Years and Over.4,ACS09_5yr_B08101001s
Std. Error: Workers 16 Years and Over: 16 to 19 Years,ACS09_5yr_B08101002s
Std. Error: Workers 16 Years and Over: 20 to 24 Years,ACS09_5yr_B08101003s
Std. Error: Workers 16 Years and Over: 25 to 44 Years,ACS09_5yr_B08101004s
Std. Error: Workers 16 Years and Over: 45 to 54 Years,ACS09_5yr_B08101005s
Std. Error: Workers 16 Years and Over: 55 to 59 Years,ACS09_5yr_B08101006s
Std. Error: Workers 16 Years and Over: 60 to 64 Years,ACS09_5yr_B08101007s
Std. Error: Workers 16 Years and Over: 65 Years and Over,ACS09_5yr_B08101008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08101009s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 16 to 19 Years",ACS09_5yr_B08101010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 20 to 24 Years",ACS09_5yr_B08101011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 25 to 44 Years",ACS09_5yr_B08101012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 45 to 54 Years",ACS09_5yr_B08101013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 55 to 59 Years",ACS09_5yr_B08101014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 60 to 64 Years",ACS09_5yr_B08101015s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 65 Years and Over",ACS09_5yr_B08101016s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08101017s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 16 to 19 Years",ACS09_5yr_B08101018s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 20 to 24 Years",ACS09_5yr_B08101019s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 25 to 44 Years",ACS09_5yr_B08101020s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 45 to 54 Years",ACS09_5yr_B08101021s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 55 to 59 Years",ACS09_5yr_B08101022s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 60 to 64 Years",ACS09_5yr_B08101023s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 65 Years and Over",ACS09_5yr_B08101024s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08101025s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 16 to 19 Years,ACS09_5yr_B08101026s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 20 to 24 Years,ACS09_5yr_B08101027s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 25 to 44 Years,ACS09_5yr_B08101028s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 45 to 54 Years,ACS09_5yr_B08101029s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 55 to 59 Years,ACS09_5yr_B08101030s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 60 to 64 Years,ACS09_5yr_B08101031s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 65 Years and Over,ACS09_5yr_B08101032s
Std. Error: Workers 16 Years and Over: Walked,ACS09_5yr_B08101033s
Std. Error: Workers 16 Years and Over: Walked: 16 to 19 Years,ACS09_5yr_B08101034s
Std. Error: Workers 16 Years and Over: Walked: 20 to 24 Years,ACS09_5yr_B08101035s
Std. Error: Workers 16 Years and Over: Walked: 25 to 44 Years,ACS09_5yr_B08101036s
Std. Error: Workers 16 Years and Over: Walked: 45 to 54 Years,ACS09_5yr_B08101037s
Std. Error: Workers 16 Years and Over: Walked: 55 to 59 Years,ACS09_5yr_B08101038s
Std. Error: Workers 16 Years and Over: Walked: 60 to 64 Years,ACS09_5yr_B08101039s
Std. Error: Workers 16 Years and Over: Walked: 65 Years and Over,ACS09_5yr_B08101040s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08101041s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 16 to 19 Years",ACS09_5yr_B08101042s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 20 to 24 Years",ACS09_5yr_B08101043s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 25 to 44 Years",ACS09_5yr_B08101044s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 45 to 54 Years",ACS09_5yr_B08101045s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 55 to 59 Years",ACS09_5yr_B08101046s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 60 to 64 Years",ACS09_5yr_B08101047s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 65 Years and Over",ACS09_5yr_B08101048s
Std. Error: Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08101049s
Std. Error: Workers 16 Years and Over: Worked At Home: 16 to 19 Years,ACS09_5yr_B08101050s
Std. Error: Workers 16 Years and Over: Worked At Home: 20 to 24 Years,ACS09_5yr_B08101051s
Std. Error: Workers 16 Years and Over: Worked At Home: 25 to 44 Years,ACS09_5yr_B08101052s
Std. Error: Workers 16 Years and Over: Worked At Home: 45 to 54 Years,ACS09_5yr_B08101053s
Std. Error: Workers 16 Years and Over: Worked At Home: 55 to 59 Years,ACS09_5yr_B08101054s
Std. Error: Workers 16 Years and Over: Worked At Home: 60 to 64 Years,ACS09_5yr_B08101055s
Std. Error: Workers 16 Years and Over: Worked At Home: 65 Years and Over,ACS09_5yr_B08101056s
% Workers 16 Years and Over: 16 to 19 Years,PCT_ACS09_5yr_B08101002
% Workers 16 Years and Over: 20 to 24 Years,PCT_ACS09_5yr_B08101003
% Workers 16 Years and Over: 25 to 44 Years,PCT_ACS09_5yr_B08101004
% Workers 16 Years and Over: 45 to 54 Years,PCT_ACS09_5yr_B08101005
% Workers 16 Years and Over: 55 to 59 Years,PCT_ACS09_5yr_B08101006
% Workers 16 Years and Over: 60 to 64 Years,PCT_ACS09_5yr_B08101007
% Workers 16 Years and Over: 65 Years and Over,PCT_ACS09_5yr_B08101008
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08101009
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 16 to 19 Years",PCT_ACS09_5yr_B08101010
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 20 to 24 Years",PCT_ACS09_5yr_B08101011
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 25 to 44 Years",PCT_ACS09_5yr_B08101012
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 45 to 54 Years",PCT_ACS09_5yr_B08101013
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 55 to 59 Years",PCT_ACS09_5yr_B08101014
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 60 to 64 Years",PCT_ACS09_5yr_B08101015
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 65 Years and Over",PCT_ACS09_5yr_B08101016
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08101017
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 16 to 19 Years",PCT_ACS09_5yr_B08101018
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 20 to 24 Years",PCT_ACS09_5yr_B08101019
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 25 to 44 Years",PCT_ACS09_5yr_B08101020
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 45 to 54 Years",PCT_ACS09_5yr_B08101021
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 55 to 59 Years",PCT_ACS09_5yr_B08101022
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 60 to 64 Years",PCT_ACS09_5yr_B08101023
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 65 Years and Over",PCT_ACS09_5yr_B08101024
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08101025
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 16 to 19 Years,PCT_ACS09_5yr_B08101026
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 20 to 24 Years,PCT_ACS09_5yr_B08101027
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 25 to 44 Years,PCT_ACS09_5yr_B08101028
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 45 to 54 Years,PCT_ACS09_5yr_B08101029
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 55 to 59 Years,PCT_ACS09_5yr_B08101030
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 60 to 64 Years,PCT_ACS09_5yr_B08101031
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 65 Years and Over,PCT_ACS09_5yr_B08101032
% Workers 16 Years and Over: Walked,PCT_ACS09_5yr_B08101033
% Workers 16 Years and Over: Walked: 16 to 19 Years,PCT_ACS09_5yr_B08101034
% Workers 16 Years and Over: Walked: 20 to 24 Years,PCT_ACS09_5yr_B08101035
% Workers 16 Years and Over: Walked: 25 to 44 Years,PCT_ACS09_5yr_B08101036
% Workers 16 Years and Over: Walked: 45 to 54 Years,PCT_ACS09_5yr_B08101037
% Workers 16 Years and Over: Walked: 55 to 59 Years,PCT_ACS09_5yr_B08101038
% Workers 16 Years and Over: Walked: 60 to 64 Years,PCT_ACS09_5yr_B08101039
% Workers 16 Years and Over: Walked: 65 Years and Over,PCT_ACS09_5yr_B08101040
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08101041
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 16 to 19 Years",PCT_ACS09_5yr_B08101042
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 20 to 24 Years",PCT_ACS09_5yr_B08101043
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 25 to 44 Years",PCT_ACS09_5yr_B08101044
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 45 to 54 Years",PCT_ACS09_5yr_B08101045
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 55 to 59 Years",PCT_ACS09_5yr_B08101046
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 60 to 64 Years",PCT_ACS09_5yr_B08101047
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 65 Years and Over",PCT_ACS09_5yr_B08101048
% Workers 16 Years and Over: Worked At Home,PCT_ACS09_5yr_B08101049
% Workers 16 Years and Over: Worked At Home: 16 to 19 Years,PCT_ACS09_5yr_B08101050
% Workers 16 Years and Over: Worked At Home: 20 to 24 Years,PCT_ACS09_5yr_B08101051
% Workers 16 Years and Over: Worked At Home: 25 to 44 Years,PCT_ACS09_5yr_B08101052
% Workers 16 Years and Over: Worked At Home: 45 to 54 Years,PCT_ACS09_5yr_B08101053
% Workers 16 Years and Over: Worked At Home: 55 to 59 Years,PCT_ACS09_5yr_B08101054
% Workers 16 Years and Over: Worked At Home: 60 to 64 Years,PCT_ACS09_5yr_B08101055
% Workers 16 Years and Over: Worked At Home: 65 Years and Over,PCT_ACS09_5yr_B08101056
Workers 16 Years and Over: Median Age -- Total,ACS09_5yr_B08103001
"Workers 16 Years and Over: Median Age -- Car, Truck, or Van - Drove Alone",ACS09_5yr_B08103002
"Workers 16 Years and Over: Median Age -- Car, Truck, or Van - Carpooled",ACS09_5yr_B08103003
Workers 16 Years and Over: Median Age -- Public Transportation (Excluding Taxicab),ACS09_5yr_B08103004
Workers 16 Years and Over: Median Age -- Walked,ACS09_5yr_B08103005
"Workers 16 Years and Over: Median Age -- Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08103006
Workers 16 Years and Over: Median Age -- Worked At Home,ACS09_5yr_B08103007
Std. Error: Workers 16 Years and Over: Median Age -- Total,ACS09_5yr_B08103001s
"Std. Error: Workers 16 Years and Over: Median Age -- Car, Truck, or Van - Drove Alone",ACS09_5yr_B08103002s
"Std. Error: Workers 16 Years and Over: Median Age -- Car, Truck, or Van - Carpooled",ACS09_5yr_B08103003s
Std. Error: Workers 16 Years and Over: Median Age -- Public Transportation (Excluding Taxicab),ACS09_5yr_B08103004s
Std. Error: Workers 16 Years and Over: Median Age -- Walked,ACS09_5yr_B08103005s
"Std. Error: Workers 16 Years and Over: Median Age -- Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08103006s
Std. Error: Workers 16 Years and Over: Median Age -- Worked At Home,ACS09_5yr_B08103007s
White Alone Workers 16 Years and Over,ACS09_5yr_B08105A001
"White Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105A002
"White Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105A003
White Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105A004
White Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105A005
"White Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105A006
White Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105A007
Std. Error: White Alone Workers 16 Years and Over,ACS09_5yr_B08105A001s
"Std. Error: White Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105A002s
"Std. Error: White Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105A003s
Std. Error: White Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105A004s
Std. Error: White Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105A005s
"Std. Error: White Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105A006s
Std. Error: White Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105A007s
"% White Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08105A002
"% White Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08105A003
% White Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08105A004
% White Alone Workers 16 Years and Over: Walked,PCT_ACS09_5yr_B08105A005
"% White Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08105A006
% White Alone Workers 16 Years and Over: Worked At Home,PCT_ACS09_5yr_B08105A007
Black or African American Alone Workers 16 Years and Over,ACS09_5yr_B08105B001
"Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105B002
"Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105B003
Black or African American Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105B004
Black or African American Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105B005
"Black or African American Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105B006
Black or African American Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105B007
Std. Error: Black or African American Alone Workers 16 Years and Over,ACS09_5yr_B08105B001s
"Std. Error: Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105B002s
"Std. Error: Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105B003s
Std. Error: Black or African American Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105B004s
Std. Error: Black or African American Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105B005s
"Std. Error: Black or African American Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105B006s
Std. Error: Black or African American Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105B007s
"% Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08105B002
"% Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08105B003
% Black or African American Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08105B004
% Black or African American Alone Workers 16 Years and Over: Walked,PCT_ACS09_5yr_B08105B005
"% Black or African American Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08105B006
% Black or African American Alone Workers 16 Years and Over: Worked At Home,PCT_ACS09_5yr_B08105B007
American Indian and Alaska Native Alone Workers 16 Years and Over,ACS09_5yr_B08105C001
"American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105C002
"American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105C003
American Indian and Alaska Native Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105C004
American Indian and Alaska Native Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105C005
"American Indian and Alaska Native Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105C006
American Indian and Alaska Native Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105C007
Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over,ACS09_5yr_B08105C001s
"Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105C002s
"Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105C003s
Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105C004s
Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105C005s
"Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105C006s
Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105C007s
"% American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08105C002
"% American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08105C003
% American Indian and Alaska Native Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08105C004
% American Indian and Alaska Native Alone Workers 16 Years and Over: Walked,PCT_ACS09_5yr_B08105C005
"% American Indian and Alaska Native Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08105C006
% American Indian and Alaska Native Alone Workers 16 Years and Over: Worked At Home,PCT_ACS09_5yr_B08105C007
Asian Alone Workers 16 Years and Over,ACS09_5yr_B08105D001
"Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105D002
"Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105D003
Asian Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105D004
Asian Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105D005
"Asian Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105D006
Asian Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105D007
Std. Error: Asian Alone Workers 16 Years and Over,ACS09_5yr_B08105D001s
"Std. Error: Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105D002s
"Std. Error: Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105D003s
Std. Error: Asian Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105D004s
Std. Error: Asian Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105D005s
"Std. Error: Asian Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105D006s
Std. Error: Asian Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105D007s
"% Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08105D002
"% Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08105D003
% Asian Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08105D004
% Asian Alone Workers 16 Years and Over: Walked,PCT_ACS09_5yr_B08105D005
"% Asian Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08105D006
% Asian Alone Workers 16 Years and Over: Worked At Home,PCT_ACS09_5yr_B08105D007
Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over,ACS09_5yr_B08105E001
"Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105E002
"Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105E003
Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105E004
Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105E005
"Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105E006
Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105E007
Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over,ACS09_5yr_B08105E001s
"Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105E002s
"Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105E003s
Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105E004s
Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105E005s
"Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105E006s
Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105E007s
"% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08105E002
"% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08105E003
% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08105E004
% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Walked,PCT_ACS09_5yr_B08105E005
"% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08105E006
% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Worked At Home,PCT_ACS09_5yr_B08105E007
Some Other Race Alone Workers 16 Years and Over,ACS09_5yr_B08105F001
"Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105F002
"Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105F003
Some Other Race Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105F004
Some Other Race Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105F005
"Some Other Race Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105F006
Some Other Race Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105F007
Std. Error: Some Other Race Alone Workers 16 Years and Over,ACS09_5yr_B08105F001s
"Std. Error: Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105F002s
"Std. Error: Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105F003s
Std. Error: Some Other Race Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105F004s
Std. Error: Some Other Race Alone Workers 16 Years and Over: Walked,ACS09_5yr_B08105F005s
"Std. Error: Some Other Race Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105F006s
Std. Error: Some Other Race Alone Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105F007s
"% Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08105F002
"% Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08105F003
% Some Other Race Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08105F004
% Some Other Race Alone Workers 16 Years and Over: Walked,PCT_ACS09_5yr_B08105F005
"% Some Other Race Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08105F006
% Some Other Race Alone Workers 16 Years and Over: Worked At Home,PCT_ACS09_5yr_B08105F007
Two or More Races Workers 16 Years and Over,ACS09_5yr_B08105G001
"Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105G002
"Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105G003
Two or More Races Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105G004
Two or More Races Workers 16 Years and Over: Walked,ACS09_5yr_B08105G005
"Two or More Races Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105G006
Two or More Races Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105G007
Std. Error: Two or More Races Workers 16 Years and Over,ACS09_5yr_B08105G001s
"Std. Error: Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105G002s
"Std. Error: Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105G003s
Std. Error: Two or More Races Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105G004s
Std. Error: Two or More Races Workers 16 Years and Over: Walked,ACS09_5yr_B08105G005s
"Std. Error: Two or More Races Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105G006s
Std. Error: Two or More Races Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105G007s
"% Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08105G002
"% Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08105G003
% Two or More Races Workers 16 Years and Over: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08105G004
% Two or More Races Workers 16 Years and Over: Walked,PCT_ACS09_5yr_B08105G005
"% Two or More Races Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08105G006
% Two or More Races Workers 16 Years and Over: Worked At Home,PCT_ACS09_5yr_B08105G007
"White Alone, Not Hispanic or Latino Workers 16 Years and Over",ACS09_5yr_B08105H001
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105H002
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105H003
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab)",ACS09_5yr_B08105H004
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Walked",ACS09_5yr_B08105H005
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105H006
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Worked At Home",ACS09_5yr_B08105H007
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over",ACS09_5yr_B08105H001s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105H002s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105H003s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab)",ACS09_5yr_B08105H004s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Walked",ACS09_5yr_B08105H005s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105H006s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Worked At Home",ACS09_5yr_B08105H007s
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08105H002
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08105H003
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab)",PCT_ACS09_5yr_B08105H004
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Walked",PCT_ACS09_5yr_B08105H005
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08105H006
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Worked At Home",PCT_ACS09_5yr_B08105H007
Hispanic or Latino Workers 16 Years and Over,ACS09_5yr_B08105I001
"Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105I002
"Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105I003
Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105I004
Hispanic or Latino Workers 16 Years and Over: Walked,ACS09_5yr_B08105I005
"Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105I006
Hispanic or Latino Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105I007
Std. Error: Hispanic or Latino Workers 16 Years and Over,ACS09_5yr_B08105I001s
"Std. Error: Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08105I002s
"Std. Error: Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled",ACS09_5yr_B08105I003s
Std. Error: Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab),ACS09_5yr_B08105I004s
Std. Error: Hispanic or Latino Workers 16 Years and Over: Walked,ACS09_5yr_B08105I005s
"Std. Error: Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08105I006s
Std. Error: Hispanic or Latino Workers 16 Years and Over: Worked At Home,ACS09_5yr_B08105I007s
"% Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08105I002
"% Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08105I003
% Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08105I004
% Hispanic or Latino Workers 16 Years and Over: Walked,PCT_ACS09_5yr_B08105I005
"% Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08105I006
% Hispanic or Latino Workers 16 Years and Over: Worked At Home,PCT_ACS09_5yr_B08105I007
Workers 16 Years and Over.5,ACS09_5yr_B08111001
Workers 16 Years and Over: Native,ACS09_5yr_B08111002
Workers 16 Years and Over: Foreign Born,ACS09_5yr_B08111003
Workers 16 Years and Over: Foreign Born: Naturalized U.s. Citizen,ACS09_5yr_B08111004
Workers 16 Years and Over: Foreign Born: Not a U.s. Citizen,ACS09_5yr_B08111005
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08111006
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Native",ACS09_5yr_B08111007
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born",ACS09_5yr_B08111008
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Naturalized U.s. Citizen",ACS09_5yr_B08111009
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Not a U.s. Citizen",ACS09_5yr_B08111010
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08111011
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Native",ACS09_5yr_B08111012
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born",ACS09_5yr_B08111013
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Naturalized U.s. Citizen",ACS09_5yr_B08111014
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Not a U.s. Citizen",ACS09_5yr_B08111015
Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08111016
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Native,ACS09_5yr_B08111017
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born,ACS09_5yr_B08111018
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Naturalized U.s. Citizen,ACS09_5yr_B08111019
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Not a U.s. Citizen,ACS09_5yr_B08111020
Workers 16 Years and Over: Walked.1,ACS09_5yr_B08111021
Workers 16 Years and Over: Walked: Native,ACS09_5yr_B08111022
Workers 16 Years and Over: Walked: Foreign Born,ACS09_5yr_B08111023
Workers 16 Years and Over: Walked: Foreign Born: Naturalized U.s. Citizen,ACS09_5yr_B08111024
Workers 16 Years and Over: Walked: Foreign Born: Not a U.s. Citizen,ACS09_5yr_B08111025
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08111026
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Native",ACS09_5yr_B08111027
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born",ACS09_5yr_B08111028
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Naturalized U.s. Citizen",ACS09_5yr_B08111029
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Not a U.s. Citizen",ACS09_5yr_B08111030
Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08111031
Workers 16 Years and Over: Worked At Home: Native,ACS09_5yr_B08111032
Workers 16 Years and Over: Worked At Home: Foreign Born,ACS09_5yr_B08111033
Workers 16 Years and Over: Worked At Home: Foreign Born: Naturalized U.s. Citizen,ACS09_5yr_B08111034
Workers 16 Years and Over: Worked At Home: Foreign Born: Not a U.s. Citizen,ACS09_5yr_B08111035
Std. Error: Workers 16 Years and Over.5,ACS09_5yr_B08111001s
Std. Error: Workers 16 Years and Over: Native,ACS09_5yr_B08111002s
Std. Error: Workers 16 Years and Over: Foreign Born,ACS09_5yr_B08111003s
Std. Error: Workers 16 Years and Over: Foreign Born: Naturalized U.s. Citizen,ACS09_5yr_B08111004s
Std. Error: Workers 16 Years and Over: Foreign Born: Not a U.s. Citizen,ACS09_5yr_B08111005s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08111006s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Native",ACS09_5yr_B08111007s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born",ACS09_5yr_B08111008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Naturalized U.s. Citizen",ACS09_5yr_B08111009s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Not a U.s. Citizen",ACS09_5yr_B08111010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08111011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Native",ACS09_5yr_B08111012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born",ACS09_5yr_B08111013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Naturalized U.s. Citizen",ACS09_5yr_B08111014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Not a U.s. Citizen",ACS09_5yr_B08111015s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08111016s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Native,ACS09_5yr_B08111017s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born,ACS09_5yr_B08111018s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Naturalized U.s. Citizen,ACS09_5yr_B08111019s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Not a U.s. Citizen,ACS09_5yr_B08111020s
Std. Error: Workers 16 Years and Over: Walked.1,ACS09_5yr_B08111021s
Std. Error: Workers 16 Years and Over: Walked: Native,ACS09_5yr_B08111022s
Std. Error: Workers 16 Years and Over: Walked: Foreign Born,ACS09_5yr_B08111023s
Std. Error: Workers 16 Years and Over: Walked: Foreign Born: Naturalized U.s. Citizen,ACS09_5yr_B08111024s
Std. Error: Workers 16 Years and Over: Walked: Foreign Born: Not a U.s. Citizen,ACS09_5yr_B08111025s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08111026s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Native",ACS09_5yr_B08111027s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born",ACS09_5yr_B08111028s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Naturalized U.s. Citizen",ACS09_5yr_B08111029s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Not a U.s. Citizen",ACS09_5yr_B08111030s
Std. Error: Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08111031s
Std. Error: Workers 16 Years and Over: Worked At Home: Native,ACS09_5yr_B08111032s
Std. Error: Workers 16 Years and Over: Worked At Home: Foreign Born,ACS09_5yr_B08111033s
Std. Error: Workers 16 Years and Over: Worked At Home: Foreign Born: Naturalized U.s. Citizen,ACS09_5yr_B08111034s
Std. Error: Workers 16 Years and Over: Worked At Home: Foreign Born: Not a U.s. Citizen,ACS09_5yr_B08111035s
% Workers 16 Years and Over: Native,PCT_ACS09_5yr_B08111002
% Workers 16 Years and Over: Foreign Born,PCT_ACS09_5yr_B08111003
% Workers 16 Years and Over: Foreign Born: Naturalized U.s. Citizen,PCT_ACS09_5yr_B08111004
% Workers 16 Years and Over: Foreign Born: Not a U.s. Citizen,PCT_ACS09_5yr_B08111005
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08111006
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Native",PCT_ACS09_5yr_B08111007
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born",PCT_ACS09_5yr_B08111008
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Naturalized U.s. Citizen",PCT_ACS09_5yr_B08111009
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Not a U.s. Citizen",PCT_ACS09_5yr_B08111010
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08111011
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Native",PCT_ACS09_5yr_B08111012
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born",PCT_ACS09_5yr_B08111013
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Naturalized U.s. Citizen",PCT_ACS09_5yr_B08111014
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Not a U.s. Citizen",PCT_ACS09_5yr_B08111015
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08111016
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Native,PCT_ACS09_5yr_B08111017
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born,PCT_ACS09_5yr_B08111018
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Naturalized U.s. Citizen,PCT_ACS09_5yr_B08111019
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Not a U.s. Citizen,PCT_ACS09_5yr_B08111020
% Workers 16 Years and Over: Walked.1,PCT_ACS09_5yr_B08111021
% Workers 16 Years and Over: Walked: Native,PCT_ACS09_5yr_B08111022
% Workers 16 Years and Over: Walked: Foreign Born,PCT_ACS09_5yr_B08111023
% Workers 16 Years and Over: Walked: Foreign Born: Naturalized U.s. Citizen,PCT_ACS09_5yr_B08111024
% Workers 16 Years and Over: Walked: Foreign Born: Not a U.s. Citizen,PCT_ACS09_5yr_B08111025
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08111026
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Native",PCT_ACS09_5yr_B08111027
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born",PCT_ACS09_5yr_B08111028
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Naturalized U.s. Citizen",PCT_ACS09_5yr_B08111029
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Not a U.s. Citizen",PCT_ACS09_5yr_B08111030
% Workers 16 Years and Over: Worked At Home.1,PCT_ACS09_5yr_B08111031
% Workers 16 Years and Over: Worked At Home: Native,PCT_ACS09_5yr_B08111032
% Workers 16 Years and Over: Worked At Home: Foreign Born,PCT_ACS09_5yr_B08111033
% Workers 16 Years and Over: Worked At Home: Foreign Born: Naturalized U.s. Citizen,PCT_ACS09_5yr_B08111034
% Workers 16 Years and Over: Worked At Home: Foreign Born: Not a U.s. Citizen,PCT_ACS09_5yr_B08111035
Workers 16 Years and Over.6,ACS09_5yr_B08113001
Workers 16 Years and Over: Speak Only English,ACS09_5yr_B08113002
Workers 16 Years and Over: Speak Spanish,ACS09_5yr_B08113003
"Workers 16 Years and Over: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113004
"Workers 16 Years and Over: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113005
Workers 16 Years and Over: Speak Spanish: Speak Other Languages,ACS09_5yr_B08113006
"Workers 16 Years and Over: Speak Spanish: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113007
"Workers 16 Years and Over: Speak Spanish: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113008
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.2",ACS09_5yr_B08113009
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Only English",ACS09_5yr_B08113010
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish",ACS09_5yr_B08113011
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113012
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113013
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages",ACS09_5yr_B08113014
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113015
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113016
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled.2",ACS09_5yr_B08113017
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Only English",ACS09_5yr_B08113018
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish",ACS09_5yr_B08113019
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113020
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113021
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages",ACS09_5yr_B08113022
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113023
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113024
Workers 16 Years and Over: Public Transportation (Excluding Taxicab).2,ACS09_5yr_B08113025
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Only English,ACS09_5yr_B08113026
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish,ACS09_5yr_B08113027
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113028
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113029
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages,ACS09_5yr_B08113030
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113031
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113032
Workers 16 Years and Over: Walked.2,ACS09_5yr_B08113033
Workers 16 Years and Over: Walked: Speak Only English,ACS09_5yr_B08113034
Workers 16 Years and Over: Walked: Speak Spanish,ACS09_5yr_B08113035
"Workers 16 Years and Over: Walked: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113036
"Workers 16 Years and Over: Walked: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113037
Workers 16 Years and Over: Walked: Speak Other Languages,ACS09_5yr_B08113038
"Workers 16 Years and Over: Walked: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113039
"Workers 16 Years and Over: Walked: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113040
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.2",ACS09_5yr_B08113041
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Only English",ACS09_5yr_B08113042
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish",ACS09_5yr_B08113043
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113044
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113045
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages",ACS09_5yr_B08113046
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113047
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113048
Workers 16 Years and Over: Worked At Home.2,ACS09_5yr_B08113049
Workers 16 Years and Over: Worked At Home: Speak Only English,ACS09_5yr_B08113050
Workers 16 Years and Over: Worked At Home: Speak Spanish,ACS09_5yr_B08113051
"Workers 16 Years and Over: Worked At Home: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113052
"Workers 16 Years and Over: Worked At Home: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113053
Workers 16 Years and Over: Worked At Home: Speak Other Languages,ACS09_5yr_B08113054
"Workers 16 Years and Over: Worked At Home: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113055
"Workers 16 Years and Over: Worked At Home: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113056
Std. Error: Workers 16 Years and Over.6,ACS09_5yr_B08113001s
Std. Error: Workers 16 Years and Over: Speak Only English,ACS09_5yr_B08113002s
Std. Error: Workers 16 Years and Over: Speak Spanish,ACS09_5yr_B08113003s
"Std. Error: Workers 16 Years and Over: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113004s
"Std. Error: Workers 16 Years and Over: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113005s
Std. Error: Workers 16 Years and Over: Speak Spanish: Speak Other Languages,ACS09_5yr_B08113006s
"Std. Error: Workers 16 Years and Over: Speak Spanish: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113007s
"Std. Error: Workers 16 Years and Over: Speak Spanish: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.2",ACS09_5yr_B08113009s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Only English",ACS09_5yr_B08113010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish",ACS09_5yr_B08113011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages",ACS09_5yr_B08113014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113015s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113016s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled.2",ACS09_5yr_B08113017s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Only English",ACS09_5yr_B08113018s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish",ACS09_5yr_B08113019s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113020s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113021s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages",ACS09_5yr_B08113022s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113023s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113024s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab).2,ACS09_5yr_B08113025s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Only English,ACS09_5yr_B08113026s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish,ACS09_5yr_B08113027s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113028s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113029s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages,ACS09_5yr_B08113030s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113031s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113032s
Std. Error: Workers 16 Years and Over: Walked.2,ACS09_5yr_B08113033s
Std. Error: Workers 16 Years and Over: Walked: Speak Only English,ACS09_5yr_B08113034s
Std. Error: Workers 16 Years and Over: Walked: Speak Spanish,ACS09_5yr_B08113035s
"Std. Error: Workers 16 Years and Over: Walked: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113036s
"Std. Error: Workers 16 Years and Over: Walked: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113037s
Std. Error: Workers 16 Years and Over: Walked: Speak Other Languages,ACS09_5yr_B08113038s
"Std. Error: Workers 16 Years and Over: Walked: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113039s
"Std. Error: Workers 16 Years and Over: Walked: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113040s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.2",ACS09_5yr_B08113041s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Only English",ACS09_5yr_B08113042s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish",ACS09_5yr_B08113043s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113044s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113045s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages",ACS09_5yr_B08113046s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113047s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113048s
Std. Error: Workers 16 Years and Over: Worked At Home.2,ACS09_5yr_B08113049s
Std. Error: Workers 16 Years and Over: Worked At Home: Speak Only English,ACS09_5yr_B08113050s
Std. Error: Workers 16 Years and Over: Worked At Home: Speak Spanish,ACS09_5yr_B08113051s
"Std. Error: Workers 16 Years and Over: Worked At Home: Speak Spanish: Speak English ""very Well""",ACS09_5yr_B08113052s
"Std. Error: Workers 16 Years and Over: Worked At Home: Speak Spanish: Speak English Less than ""very Well""",ACS09_5yr_B08113053s
Std. Error: Workers 16 Years and Over: Worked At Home: Speak Other Languages,ACS09_5yr_B08113054s
"Std. Error: Workers 16 Years and Over: Worked At Home: Speak Other Languages: Speak English ""very Well""",ACS09_5yr_B08113055s
"Std. Error: Workers 16 Years and Over: Worked At Home: Speak Other Languages: Speak English Less than ""very Well""",ACS09_5yr_B08113056s
% Workers 16 Years and Over: Speak Only English,PCT_ACS09_5yr_B08113002
% Workers 16 Years and Over: Speak Spanish,PCT_ACS09_5yr_B08113003
"% Workers 16 Years and Over: Speak Spanish: Speak English ""very Well""",PCT_ACS09_5yr_B08113004
"% Workers 16 Years and Over: Speak Spanish: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113005
% Workers 16 Years and Over: Speak Spanish: Speak Other Languages,PCT_ACS09_5yr_B08113006
"% Workers 16 Years and Over: Speak Spanish: Speak Other Languages: Speak English ""very Well""",PCT_ACS09_5yr_B08113007
"% Workers 16 Years and Over: Speak Spanish: Speak Other Languages: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113008
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.2",PCT_ACS09_5yr_B08113009
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Only English",PCT_ACS09_5yr_B08113010
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish",PCT_ACS09_5yr_B08113011
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish: Speak English ""very Well""",PCT_ACS09_5yr_B08113012
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113013
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages",PCT_ACS09_5yr_B08113014
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages: Speak English ""very Well""",PCT_ACS09_5yr_B08113015
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113016
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled.2",PCT_ACS09_5yr_B08113017
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Only English",PCT_ACS09_5yr_B08113018
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish",PCT_ACS09_5yr_B08113019
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish: Speak English ""very Well""",PCT_ACS09_5yr_B08113020
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113021
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages",PCT_ACS09_5yr_B08113022
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages: Speak English ""very Well""",PCT_ACS09_5yr_B08113023
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113024
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab).2,PCT_ACS09_5yr_B08113025
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Only English,PCT_ACS09_5yr_B08113026
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish,PCT_ACS09_5yr_B08113027
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish: Speak English ""very Well""",PCT_ACS09_5yr_B08113028
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113029
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages,PCT_ACS09_5yr_B08113030
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages: Speak English ""very Well""",PCT_ACS09_5yr_B08113031
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113032
% Workers 16 Years and Over: Walked.2,PCT_ACS09_5yr_B08113033
% Workers 16 Years and Over: Walked: Speak Only English,PCT_ACS09_5yr_B08113034
% Workers 16 Years and Over: Walked: Speak Spanish,PCT_ACS09_5yr_B08113035
"% Workers 16 Years and Over: Walked: Speak Spanish: Speak English ""very Well""",PCT_ACS09_5yr_B08113036
"% Workers 16 Years and Over: Walked: Speak Spanish: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113037
% Workers 16 Years and Over: Walked: Speak Other Languages,PCT_ACS09_5yr_B08113038
"% Workers 16 Years and Over: Walked: Speak Other Languages: Speak English ""very Well""",PCT_ACS09_5yr_B08113039
"% Workers 16 Years and Over: Walked: Speak Other Languages: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113040
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.2",PCT_ACS09_5yr_B08113041
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Only English",PCT_ACS09_5yr_B08113042
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish",PCT_ACS09_5yr_B08113043
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish: Speak English ""very Well""",PCT_ACS09_5yr_B08113044
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113045
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages",PCT_ACS09_5yr_B08113046
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages: Speak English ""very Well""",PCT_ACS09_5yr_B08113047
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113048
% Workers 16 Years and Over: Worked At Home.2,PCT_ACS09_5yr_B08113049
% Workers 16 Years and Over: Worked At Home: Speak Only English,PCT_ACS09_5yr_B08113050
% Workers 16 Years and Over: Worked At Home: Speak Spanish,PCT_ACS09_5yr_B08113051
"% Workers 16 Years and Over: Worked At Home: Speak Spanish: Speak English ""very Well""",PCT_ACS09_5yr_B08113052
"% Workers 16 Years and Over: Worked At Home: Speak Spanish: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113053
% Workers 16 Years and Over: Worked At Home: Speak Other Languages,PCT_ACS09_5yr_B08113054
"% Workers 16 Years and Over: Worked At Home: Speak Other Languages: Speak English ""very Well""",PCT_ACS09_5yr_B08113055
"% Workers 16 Years and Over: Worked At Home: Speak Other Languages: Speak English Less than ""very Well""",PCT_ACS09_5yr_B08113056
Workers 16 Years and Over with Earnings [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08119001
"Workers 16 Years and Over with Earnings: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119002
"Workers 16 Years and Over with Earnings: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119003
"Workers 16 Years and Over with Earnings: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119004
"Workers 16 Years and Over with Earnings: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119005
"Workers 16 Years and Over with Earnings: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119006
"Workers 16 Years and Over with Earnings: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119007
"Workers 16 Years and Over with Earnings: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119008
"Workers 16 Years and Over with Earnings: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119009
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119010
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119011
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119012
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119013
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119014
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119015
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119016
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119017
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119018
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119019
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119020
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119021
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119022
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119023
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119024
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119025
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119026
"Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119027
Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab) [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08119028
"Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119029
"Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119030
"Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119031
"Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119032
"Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119033
"Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119034
"Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119035
"Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119036
Workers 16 Years and Over with Earnings: Walked [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08119037
"Workers 16 Years and Over with Earnings: Walked: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119038
"Workers 16 Years and Over with Earnings: Walked: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119039
"Workers 16 Years and Over with Earnings: Walked: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119040
"Workers 16 Years and Over with Earnings: Walked: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119041
"Workers 16 Years and Over with Earnings: Walked: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119042
"Workers 16 Years and Over with Earnings: Walked: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119043
"Workers 16 Years and Over with Earnings: Walked: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119044
"Workers 16 Years and Over with Earnings: Walked: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119045
"Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119046
"Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119047
"Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119048
"Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119049
"Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119050
"Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119051
"Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119052
"Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119053
"Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119054
Workers 16 Years and Over with Earnings: Worked At Home [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08119055
"Workers 16 Years and Over with Earnings: Worked At Home: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119056
"Workers 16 Years and Over with Earnings: Worked At Home: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119057
"Workers 16 Years and Over with Earnings: Worked At Home: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119058
"Workers 16 Years and Over with Earnings: Worked At Home: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119059
"Workers 16 Years and Over with Earnings: Worked At Home: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119060
"Workers 16 Years and Over with Earnings: Worked At Home: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119061
"Workers 16 Years and Over with Earnings: Worked At Home: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119062
"Workers 16 Years and Over with Earnings: Worked At Home: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119063
Std. Error: Workers 16 Years and Over with Earnings [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08119001s
"Std. Error: Workers 16 Years and Over with Earnings: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119002s
"Std. Error: Workers 16 Years and Over with Earnings: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119003s
"Std. Error: Workers 16 Years and Over with Earnings: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119004s
"Std. Error: Workers 16 Years and Over with Earnings: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119005s
"Std. Error: Workers 16 Years and Over with Earnings: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119006s
"Std. Error: Workers 16 Years and Over with Earnings: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119007s
"Std. Error: Workers 16 Years and Over with Earnings: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119008s
"Std. Error: Workers 16 Years and Over with Earnings: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119009s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119010s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119011s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119012s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119013s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119014s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119015s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119016s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119017s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119018s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119019s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119020s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119021s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119022s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119023s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119024s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119025s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119026s
"Std. Error: Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119027s
Std. Error: Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab) [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08119028s
"Std. Error: Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119029s
"Std. Error: Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119030s
"Std. Error: Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119031s
"Std. Error: Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119032s
"Std. Error: Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119033s
"Std. Error: Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119034s
"Std. Error: Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119035s
"Std. Error: Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119036s
Std. Error: Workers 16 Years and Over with Earnings: Walked [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08119037s
"Std. Error: Workers 16 Years and Over with Earnings: Walked: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119038s
"Std. Error: Workers 16 Years and Over with Earnings: Walked: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119039s
"Std. Error: Workers 16 Years and Over with Earnings: Walked: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119040s
"Std. Error: Workers 16 Years and Over with Earnings: Walked: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119041s
"Std. Error: Workers 16 Years and Over with Earnings: Walked: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119042s
"Std. Error: Workers 16 Years and Over with Earnings: Walked: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119043s
"Std. Error: Workers 16 Years and Over with Earnings: Walked: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119044s
"Std. Error: Workers 16 Years and Over with Earnings: Walked: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119045s
"Std. Error: Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119046s
"Std. Error: Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119047s
"Std. Error: Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119048s
"Std. Error: Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119049s
"Std. Error: Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119050s
"Std. Error: Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119051s
"Std. Error: Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119052s
"Std. Error: Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119053s
"Std. Error: Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119054s
Std. Error: Workers 16 Years and Over with Earnings: Worked At Home [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08119055s
"Std. Error: Workers 16 Years and Over with Earnings: Worked At Home: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119056s
"Std. Error: Workers 16 Years and Over with Earnings: Worked At Home: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119057s
"Std. Error: Workers 16 Years and Over with Earnings: Worked At Home: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119058s
"Std. Error: Workers 16 Years and Over with Earnings: Worked At Home: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119059s
"Std. Error: Workers 16 Years and Over with Earnings: Worked At Home: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119060s
"Std. Error: Workers 16 Years and Over with Earnings: Worked At Home: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119061s
"Std. Error: Workers 16 Years and Over with Earnings: Worked At Home: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119062s
"Std. Error: Workers 16 Years and Over with Earnings: Worked At Home: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08119063s
"% Workers 16 Years and Over with Earnings: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119002
"% Workers 16 Years and Over with Earnings: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119003
"% Workers 16 Years and Over with Earnings: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119004
"% Workers 16 Years and Over with Earnings: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119005
"% Workers 16 Years and Over with Earnings: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119006
"% Workers 16 Years and Over with Earnings: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119007
"% Workers 16 Years and Over with Earnings: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119008
"% Workers 16 Years and Over with Earnings: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119009
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119010
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119011
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119012
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119013
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119014
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119015
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119016
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119017
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Drove Alone: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119018
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119019
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119020
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119021
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119022
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119023
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119024
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119025
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119026
"% Workers 16 Years and Over with Earnings: Car, Truck, or Van - Carpooled: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119027
% Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab) [Dollars adjusted for inflation to match value in 2019],PCT_ACS09_5yr_B08119028
"% Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119029
"% Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119030
"% Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119031
"% Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119032
"% Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119033
"% Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119034
"% Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119035
"% Workers 16 Years and Over with Earnings: Public Transportation (Excluding Taxicab): $75,000 or More [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119036
% Workers 16 Years and Over with Earnings: Walked [Dollars adjusted for inflation to match value in 2019],PCT_ACS09_5yr_B08119037
"% Workers 16 Years and Over with Earnings: Walked: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119038
"% Workers 16 Years and Over with Earnings: Walked: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119039
"% Workers 16 Years and Over with Earnings: Walked: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119040
"% Workers 16 Years and Over with Earnings: Walked: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119041
"% Workers 16 Years and Over with Earnings: Walked: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119042
"% Workers 16 Years and Over with Earnings: Walked: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119043
"% Workers 16 Years and Over with Earnings: Walked: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119044
"% Workers 16 Years and Over with Earnings: Walked: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119045
"% Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119046
"% Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119047
"% Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119048
"% Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119049
"% Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119050
"% Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119051
"% Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119052
"% Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119053
"% Workers 16 Years and Over with Earnings: Taxicab, Motorcycle, Bicycle, or Other Means: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119054
% Workers 16 Years and Over with Earnings: Worked At Home [Dollars adjusted for inflation to match value in 2019],PCT_ACS09_5yr_B08119055
"% Workers 16 Years and Over with Earnings: Worked At Home: $1 to $9,999 or Loss [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119056
"% Workers 16 Years and Over with Earnings: Worked At Home: $10,000 to $14,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119057
"% Workers 16 Years and Over with Earnings: Worked At Home: $15,000 to $24,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119058
"% Workers 16 Years and Over with Earnings: Worked At Home: $25,000 to $34,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119059
"% Workers 16 Years and Over with Earnings: Worked At Home: $35,000 to $49,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119060
"% Workers 16 Years and Over with Earnings: Worked At Home: $50,000 to $64,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119061
"% Workers 16 Years and Over with Earnings: Worked At Home: $65,000 to $74,999 [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119062
"% Workers 16 Years and Over with Earnings: Worked At Home: $75,000 or More [Dollars adjusted for inflation to match value in 2019]",PCT_ACS09_5yr_B08119063
Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Total [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121001
"Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Car, Truck, or Van - Drove Alone [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08121002
"Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Car, Truck, or Van - Carpooled [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08121003
Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Public Transportation (Excluding Taxicab) [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121004
Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Walked [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121005
"Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Taxicab, Motorcycle, Bicycle, or Other Means [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08121006
Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Worked At Home [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121007
Std. Error: Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Total [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121001s
"Std. Error: Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Car, Truck, or Van - Drove Alone [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08121002s
"Std. Error: Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Car, Truck, or Van - Carpooled [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08121003s
Std. Error: Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Public Transportation (Excluding Taxicab) [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121004s
Std. Error: Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Walked [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121005s
"Std. Error: Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Taxicab, Motorcycle, Bicycle, or Other Means [Dollars adjusted for inflation to match value in 2019]",ACS09_5yr_B08121006s
Std. Error: Workers 16 Years and Over with Earnings: Median Earnings in the Past 12 Months -- Worked At Home [Dollars adjusted for inflation to match value in 2019],ACS09_5yr_B08121007s
Workers 16 Years and Over for Whom Poverty Status Is Determined,ACS09_5yr_B08122001
Workers 16 Years and Over for Whom Poverty Status Is Determined: Below 100 Percent of the Poverty Level,ACS09_5yr_B08122002
Workers 16 Years and Over for Whom Poverty Status Is Determined: 100 to 149 Percent of the Poverty Level,ACS09_5yr_B08122003
Workers 16 Years and Over for Whom Poverty Status Is Determined: At or Above 150 Percent of the Poverty Level,ACS09_5yr_B08122004
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08122005
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone: Below 100 Percent of the Poverty Level",ACS09_5yr_B08122006
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone: 100 to 149 Percent of the Poverty Level",ACS09_5yr_B08122007
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone: At or Above 150 Percent of the Poverty Level",ACS09_5yr_B08122008
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled",ACS09_5yr_B08122009
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled: Below 100 Percent of the Poverty Level",ACS09_5yr_B08122010
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled: 100 to 149 Percent of the Poverty Level",ACS09_5yr_B08122011
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled: At or Above 150 Percent of the Poverty Level",ACS09_5yr_B08122012
Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab),ACS09_5yr_B08122013
Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab): Below 100 Percent of the Poverty Level,ACS09_5yr_B08122014
Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab): 100 to 149 Percent of the Poverty Level,ACS09_5yr_B08122015
Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab): At or Above 150 Percent of the Poverty Level,ACS09_5yr_B08122016
Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked,ACS09_5yr_B08122017
Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked: Below 100 Percent of the Poverty Level,ACS09_5yr_B08122018
Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked: 100 to 149 Percent of the Poverty Level,ACS09_5yr_B08122019
Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked: At or Above 150 Percent of the Poverty Level,ACS09_5yr_B08122020
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08122021
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means: Below 100 Percent of the Poverty Level",ACS09_5yr_B08122022
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means: 100 to 149 Percent of the Poverty Level",ACS09_5yr_B08122023
"Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means: At or Above 150 Percent of the Poverty Level",ACS09_5yr_B08122024
Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home,ACS09_5yr_B08122025
Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home: Below 100 Percent of the Poverty Level,ACS09_5yr_B08122026
Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home: 100 to 149 Percent of the Poverty Level,ACS09_5yr_B08122027
Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home: At or Above 150 Percent of the Poverty Level,ACS09_5yr_B08122028
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined,ACS09_5yr_B08122001s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Below 100 Percent of the Poverty Level,ACS09_5yr_B08122002s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: 100 to 149 Percent of the Poverty Level,ACS09_5yr_B08122003s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: At or Above 150 Percent of the Poverty Level,ACS09_5yr_B08122004s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08122005s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone: Below 100 Percent of the Poverty Level",ACS09_5yr_B08122006s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone: 100 to 149 Percent of the Poverty Level",ACS09_5yr_B08122007s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone: At or Above 150 Percent of the Poverty Level",ACS09_5yr_B08122008s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled",ACS09_5yr_B08122009s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled: Below 100 Percent of the Poverty Level",ACS09_5yr_B08122010s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled: 100 to 149 Percent of the Poverty Level",ACS09_5yr_B08122011s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled: At or Above 150 Percent of the Poverty Level",ACS09_5yr_B08122012s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab),ACS09_5yr_B08122013s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab): Below 100 Percent of the Poverty Level,ACS09_5yr_B08122014s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab): 100 to 149 Percent of the Poverty Level,ACS09_5yr_B08122015s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab): At or Above 150 Percent of the Poverty Level,ACS09_5yr_B08122016s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked,ACS09_5yr_B08122017s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked: Below 100 Percent of the Poverty Level,ACS09_5yr_B08122018s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked: 100 to 149 Percent of the Poverty Level,ACS09_5yr_B08122019s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked: At or Above 150 Percent of the Poverty Level,ACS09_5yr_B08122020s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08122021s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means: Below 100 Percent of the Poverty Level",ACS09_5yr_B08122022s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means: 100 to 149 Percent of the Poverty Level",ACS09_5yr_B08122023s
"Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means: At or Above 150 Percent of the Poverty Level",ACS09_5yr_B08122024s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home,ACS09_5yr_B08122025s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home: Below 100 Percent of the Poverty Level,ACS09_5yr_B08122026s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home: 100 to 149 Percent of the Poverty Level,ACS09_5yr_B08122027s
Std. Error: Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home: At or Above 150 Percent of the Poverty Level,ACS09_5yr_B08122028s
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Below 100 Percent of the Poverty Level,PCT_ACS09_5yr_B08122002
% Workers 16 Years and Over for Whom Poverty Status Is Determined: 100 to 149 Percent of the Poverty Level,PCT_ACS09_5yr_B08122003
% Workers 16 Years and Over for Whom Poverty Status Is Determined: At or Above 150 Percent of the Poverty Level,PCT_ACS09_5yr_B08122004
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08122005
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone: Below 100 Percent of the Poverty Level",PCT_ACS09_5yr_B08122006
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone: 100 to 149 Percent of the Poverty Level",PCT_ACS09_5yr_B08122007
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Drove Alone: At or Above 150 Percent of the Poverty Level",PCT_ACS09_5yr_B08122008
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08122009
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled: Below 100 Percent of the Poverty Level",PCT_ACS09_5yr_B08122010
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled: 100 to 149 Percent of the Poverty Level",PCT_ACS09_5yr_B08122011
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Car, Truck, or Van - Carpooled: At or Above 150 Percent of the Poverty Level",PCT_ACS09_5yr_B08122012
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08122013
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab): Below 100 Percent of the Poverty Level,PCT_ACS09_5yr_B08122014
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab): 100 to 149 Percent of the Poverty Level,PCT_ACS09_5yr_B08122015
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Public Transportation (Excluding Taxicab): At or Above 150 Percent of the Poverty Level,PCT_ACS09_5yr_B08122016
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked,PCT_ACS09_5yr_B08122017
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked: Below 100 Percent of the Poverty Level,PCT_ACS09_5yr_B08122018
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked: 100 to 149 Percent of the Poverty Level,PCT_ACS09_5yr_B08122019
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Walked: At or Above 150 Percent of the Poverty Level,PCT_ACS09_5yr_B08122020
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08122021
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means: Below 100 Percent of the Poverty Level",PCT_ACS09_5yr_B08122022
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means: 100 to 149 Percent of the Poverty Level",PCT_ACS09_5yr_B08122023
"% Workers 16 Years and Over for Whom Poverty Status Is Determined: Taxicab, Motorcycle, Bicycle, or Other Means: At or Above 150 Percent of the Poverty Level",PCT_ACS09_5yr_B08122024
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home,PCT_ACS09_5yr_B08122025
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home: Below 100 Percent of the Poverty Level,PCT_ACS09_5yr_B08122026
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home: 100 to 149 Percent of the Poverty Level,PCT_ACS09_5yr_B08122027
% Workers 16 Years and Over for Whom Poverty Status Is Determined: Worked At Home: At or Above 150 Percent of the Poverty Level,PCT_ACS09_5yr_B08122028
Workers 16 Years and Over.7,ACS09_5yr_B08124001
"Workers 16 Years and Over: Management, Professional, and Related Occupations",ACS09_5yr_B08124002
Workers 16 Years and Over: Service Occupations,ACS09_5yr_B08124003
Workers 16 Years and Over: Sales and Office Occupations,ACS09_5yr_B08124004
"Workers 16 Years and Over: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124005
"Workers 16 Years and Over: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124006
"Workers 16 Years and Over: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124007
Workers 16 Years and Over: Armed Forces,ACS09_5yr_B08124008
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.3",ACS09_5yr_B08124009
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Management, Professional, and Related Occupations",ACS09_5yr_B08124010
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Service Occupations",ACS09_5yr_B08124011
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Sales and Office Occupations",ACS09_5yr_B08124012
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124013
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124014
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124015
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Armed Forces",ACS09_5yr_B08124016
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled.3",ACS09_5yr_B08124017
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Management, Professional, and Related Occupations",ACS09_5yr_B08124018
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Service Occupations",ACS09_5yr_B08124019
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Sales and Office Occupations",ACS09_5yr_B08124020
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124021
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124022
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124023
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Armed Forces",ACS09_5yr_B08124024
Workers 16 Years and Over: Public Transportation (Excluding Taxicab).3,ACS09_5yr_B08124025
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Management, Professional, and Related Occupations",ACS09_5yr_B08124026
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Service Occupations,ACS09_5yr_B08124027
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Sales and Office Occupations,ACS09_5yr_B08124028
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124029
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124030
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124031
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Armed Forces,ACS09_5yr_B08124032
Workers 16 Years and Over: Walked.3,ACS09_5yr_B08124033
"Workers 16 Years and Over: Walked: Management, Professional, and Related Occupations",ACS09_5yr_B08124034
Workers 16 Years and Over: Walked: Service Occupations,ACS09_5yr_B08124035
Workers 16 Years and Over: Walked: Sales and Office Occupations,ACS09_5yr_B08124036
"Workers 16 Years and Over: Walked: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124037
"Workers 16 Years and Over: Walked: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124038
"Workers 16 Years and Over: Walked: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124039
Workers 16 Years and Over: Walked: Armed Forces,ACS09_5yr_B08124040
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.3",ACS09_5yr_B08124041
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Management, Professional, and Related Occupations",ACS09_5yr_B08124042
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Service Occupations",ACS09_5yr_B08124043
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Sales and Office Occupations",ACS09_5yr_B08124044
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124045
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124046
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124047
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Armed Forces",ACS09_5yr_B08124048
Workers 16 Years and Over: Worked At Home.3,ACS09_5yr_B08124049
"Workers 16 Years and Over: Worked At Home: Management, Professional, and Related Occupations",ACS09_5yr_B08124050
Workers 16 Years and Over: Worked At Home: Service Occupations,ACS09_5yr_B08124051
Workers 16 Years and Over: Worked At Home: Sales and Office Occupations,ACS09_5yr_B08124052
"Workers 16 Years and Over: Worked At Home: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124053
"Workers 16 Years and Over: Worked At Home: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124054
"Workers 16 Years and Over: Worked At Home: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124055
Workers 16 Years and Over: Worked At Home: Armed Forces,ACS09_5yr_B08124056
Std. Error: Workers 16 Years and Over.7,ACS09_5yr_B08124001s
"Std. Error: Workers 16 Years and Over: Management, Professional, and Related Occupations",ACS09_5yr_B08124002s
Std. Error: Workers 16 Years and Over: Service Occupations,ACS09_5yr_B08124003s
Std. Error: Workers 16 Years and Over: Sales and Office Occupations,ACS09_5yr_B08124004s
"Std. Error: Workers 16 Years and Over: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124005s
"Std. Error: Workers 16 Years and Over: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124006s
"Std. Error: Workers 16 Years and Over: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124007s
Std. Error: Workers 16 Years and Over: Armed Forces,ACS09_5yr_B08124008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.3",ACS09_5yr_B08124009s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Management, Professional, and Related Occupations",ACS09_5yr_B08124010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Service Occupations",ACS09_5yr_B08124011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Sales and Office Occupations",ACS09_5yr_B08124012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124015s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Armed Forces",ACS09_5yr_B08124016s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled.3",ACS09_5yr_B08124017s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Management, Professional, and Related Occupations",ACS09_5yr_B08124018s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Service Occupations",ACS09_5yr_B08124019s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Sales and Office Occupations",ACS09_5yr_B08124020s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124021s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124022s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124023s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Armed Forces",ACS09_5yr_B08124024s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab).3,ACS09_5yr_B08124025s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Management, Professional, and Related Occupations",ACS09_5yr_B08124026s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Service Occupations,ACS09_5yr_B08124027s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Sales and Office Occupations,ACS09_5yr_B08124028s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124029s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124030s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124031s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Armed Forces,ACS09_5yr_B08124032s
Std. Error: Workers 16 Years and Over: Walked.3,ACS09_5yr_B08124033s
"Std. Error: Workers 16 Years and Over: Walked: Management, Professional, and Related Occupations",ACS09_5yr_B08124034s
Std. Error: Workers 16 Years and Over: Walked: Service Occupations,ACS09_5yr_B08124035s
Std. Error: Workers 16 Years and Over: Walked: Sales and Office Occupations,ACS09_5yr_B08124036s
"Std. Error: Workers 16 Years and Over: Walked: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124037s
"Std. Error: Workers 16 Years and Over: Walked: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124038s
"Std. Error: Workers 16 Years and Over: Walked: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124039s
Std. Error: Workers 16 Years and Over: Walked: Armed Forces,ACS09_5yr_B08124040s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.3",ACS09_5yr_B08124041s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Management, Professional, and Related Occupations",ACS09_5yr_B08124042s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Service Occupations",ACS09_5yr_B08124043s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Sales and Office Occupations",ACS09_5yr_B08124044s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124045s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124046s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124047s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Armed Forces",ACS09_5yr_B08124048s
Std. Error: Workers 16 Years and Over: Worked At Home.3,ACS09_5yr_B08124049s
"Std. Error: Workers 16 Years and Over: Worked At Home: Management, Professional, and Related Occupations",ACS09_5yr_B08124050s
Std. Error: Workers 16 Years and Over: Worked At Home: Service Occupations,ACS09_5yr_B08124051s
Std. Error: Workers 16 Years and Over: Worked At Home: Sales and Office Occupations,ACS09_5yr_B08124052s
"Std. Error: Workers 16 Years and Over: Worked At Home: Farming, Fishing, and Forestry Occupations",ACS09_5yr_B08124053s
"Std. Error: Workers 16 Years and Over: Worked At Home: Construction and Extraction, and Maintenance Occupations",ACS09_5yr_B08124054s
"Std. Error: Workers 16 Years and Over: Worked At Home: Production, Transportation, and Material Moving Occupations",ACS09_5yr_B08124055s
Std. Error: Workers 16 Years and Over: Worked At Home: Armed Forces,ACS09_5yr_B08124056s
"% Workers 16 Years and Over: Management, Professional, and Related Occupations",PCT_ACS09_5yr_B08124002
% Workers 16 Years and Over: Service Occupations,PCT_ACS09_5yr_B08124003
% Workers 16 Years and Over: Sales and Office Occupations,PCT_ACS09_5yr_B08124004
"% Workers 16 Years and Over: Farming, Fishing, and Forestry Occupations",PCT_ACS09_5yr_B08124005
"% Workers 16 Years and Over: Construction and Extraction, and Maintenance Occupations",PCT_ACS09_5yr_B08124006
"% Workers 16 Years and Over: Production, Transportation, and Material Moving Occupations",PCT_ACS09_5yr_B08124007
% Workers 16 Years and Over: Armed Forces,PCT_ACS09_5yr_B08124008
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.3",PCT_ACS09_5yr_B08124009
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Management, Professional, and Related Occupations",PCT_ACS09_5yr_B08124010
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Service Occupations",PCT_ACS09_5yr_B08124011
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Sales and Office Occupations",PCT_ACS09_5yr_B08124012
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Farming, Fishing, and Forestry Occupations",PCT_ACS09_5yr_B08124013
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Construction and Extraction, and Maintenance Occupations",PCT_ACS09_5yr_B08124014
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Production, Transportation, and Material Moving Occupations",PCT_ACS09_5yr_B08124015
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Armed Forces",PCT_ACS09_5yr_B08124016
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled.3",PCT_ACS09_5yr_B08124017
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Management, Professional, and Related Occupations",PCT_ACS09_5yr_B08124018
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Service Occupations",PCT_ACS09_5yr_B08124019
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Sales and Office Occupations",PCT_ACS09_5yr_B08124020
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Farming, Fishing, and Forestry Occupations",PCT_ACS09_5yr_B08124021
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Construction and Extraction, and Maintenance Occupations",PCT_ACS09_5yr_B08124022
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Production, Transportation, and Material Moving Occupations",PCT_ACS09_5yr_B08124023
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Armed Forces",PCT_ACS09_5yr_B08124024
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab).3,PCT_ACS09_5yr_B08124025
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Management, Professional, and Related Occupations",PCT_ACS09_5yr_B08124026
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Service Occupations,PCT_ACS09_5yr_B08124027
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Sales and Office Occupations,PCT_ACS09_5yr_B08124028
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Farming, Fishing, and Forestry Occupations",PCT_ACS09_5yr_B08124029
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Construction and Extraction, and Maintenance Occupations",PCT_ACS09_5yr_B08124030
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Production, Transportation, and Material Moving Occupations",PCT_ACS09_5yr_B08124031
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Armed Forces,PCT_ACS09_5yr_B08124032
% Workers 16 Years and Over: Walked.3,PCT_ACS09_5yr_B08124033
"% Workers 16 Years and Over: Walked: Management, Professional, and Related Occupations",PCT_ACS09_5yr_B08124034
% Workers 16 Years and Over: Walked: Service Occupations,PCT_ACS09_5yr_B08124035
% Workers 16 Years and Over: Walked: Sales and Office Occupations,PCT_ACS09_5yr_B08124036
"% Workers 16 Years and Over: Walked: Farming, Fishing, and Forestry Occupations",PCT_ACS09_5yr_B08124037
"% Workers 16 Years and Over: Walked: Construction and Extraction, and Maintenance Occupations",PCT_ACS09_5yr_B08124038
"% Workers 16 Years and Over: Walked: Production, Transportation, and Material Moving Occupations",PCT_ACS09_5yr_B08124039
% Workers 16 Years and Over: Walked: Armed Forces,PCT_ACS09_5yr_B08124040
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.3",PCT_ACS09_5yr_B08124041
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Management, Professional, and Related Occupations",PCT_ACS09_5yr_B08124042
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Service Occupations",PCT_ACS09_5yr_B08124043
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Sales and Office Occupations",PCT_ACS09_5yr_B08124044
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Farming, Fishing, and Forestry Occupations",PCT_ACS09_5yr_B08124045
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Construction and Extraction, and Maintenance Occupations",PCT_ACS09_5yr_B08124046
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Production, Transportation, and Material Moving Occupations",PCT_ACS09_5yr_B08124047
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Armed Forces",PCT_ACS09_5yr_B08124048
% Workers 16 Years and Over: Worked At Home.3,PCT_ACS09_5yr_B08124049
"% Workers 16 Years and Over: Worked At Home: Management, Professional, and Related Occupations",PCT_ACS09_5yr_B08124050
% Workers 16 Years and Over: Worked At Home: Service Occupations,PCT_ACS09_5yr_B08124051
% Workers 16 Years and Over: Worked At Home: Sales and Office Occupations,PCT_ACS09_5yr_B08124052
"% Workers 16 Years and Over: Worked At Home: Farming, Fishing, and Forestry Occupations",PCT_ACS09_5yr_B08124053
"% Workers 16 Years and Over: Worked At Home: Construction and Extraction, and Maintenance Occupations",PCT_ACS09_5yr_B08124054
"% Workers 16 Years and Over: Worked At Home: Production, Transportation, and Material Moving Occupations",PCT_ACS09_5yr_B08124055
% Workers 16 Years and Over: Worked At Home: Armed Forces,PCT_ACS09_5yr_B08124056
Workers 16 Years and Over.8,ACS09_5yr_B08126001
"Workers 16 Years and Over: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126002
Workers 16 Years and Over: Construction,ACS09_5yr_B08126003
Workers 16 Years and Over: Manufacturing,ACS09_5yr_B08126004
Workers 16 Years and Over: Wholesale Trade,ACS09_5yr_B08126005
Workers 16 Years and Over: Retail Trade,ACS09_5yr_B08126006
"Workers 16 Years and Over: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126007
Workers 16 Years and Over: Information,ACS09_5yr_B08126008
"Workers 16 Years and Over: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126009
"Workers 16 Years and Over: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126010
"Workers 16 Years and Over: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126011
"Workers 16 Years and Over: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126012
Workers 16 Years and Over: Other Services (Except Public Administration),ACS09_5yr_B08126013
Workers 16 Years and Over: Public Administration,ACS09_5yr_B08126014
Workers 16 Years and Over: Armed Forces.1,ACS09_5yr_B08126015
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.4",ACS09_5yr_B08126016
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126017
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Construction",ACS09_5yr_B08126018
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Manufacturing",ACS09_5yr_B08126019
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Wholesale Trade",ACS09_5yr_B08126020
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Retail Trade",ACS09_5yr_B08126021
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126022
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Information",ACS09_5yr_B08126023
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126024
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126025
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126026
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126027
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Other Services (Except Public Administration)",ACS09_5yr_B08126028
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Public Administration",ACS09_5yr_B08126029
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Armed Forces.1",ACS09_5yr_B08126030
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled.4",ACS09_5yr_B08126031
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126032
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Construction",ACS09_5yr_B08126033
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Manufacturing",ACS09_5yr_B08126034
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Wholesale Trade",ACS09_5yr_B08126035
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Retail Trade",ACS09_5yr_B08126036
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126037
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Information",ACS09_5yr_B08126038
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126039
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126040
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126041
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126042
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Other Services (Except Public Administration)",ACS09_5yr_B08126043
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Public Administration",ACS09_5yr_B08126044
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Armed Forces.1",ACS09_5yr_B08126045
Workers 16 Years and Over: Public Transportation (Excluding Taxicab).4,ACS09_5yr_B08126046
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126047
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Construction,ACS09_5yr_B08126048
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Manufacturing,ACS09_5yr_B08126049
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Wholesale Trade,ACS09_5yr_B08126050
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Retail Trade,ACS09_5yr_B08126051
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Transportation and Warehousing, and Utilities",ACS09_5yr_B08126052
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Information,ACS09_5yr_B08126053
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126054
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126055
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126056
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126057
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Other Services (Except Public Administration),ACS09_5yr_B08126058
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Public Administration,ACS09_5yr_B08126059
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Armed Forces.1,ACS09_5yr_B08126060
Workers 16 Years and Over: Walked.4,ACS09_5yr_B08126061
"Workers 16 Years and Over: Walked: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126062
Workers 16 Years and Over: Walked: Construction,ACS09_5yr_B08126063
Workers 16 Years and Over: Walked: Manufacturing,ACS09_5yr_B08126064
Workers 16 Years and Over: Walked: Wholesale Trade,ACS09_5yr_B08126065
Workers 16 Years and Over: Walked: Retail Trade,ACS09_5yr_B08126066
"Workers 16 Years and Over: Walked: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126067
Workers 16 Years and Over: Walked: Information,ACS09_5yr_B08126068
"Workers 16 Years and Over: Walked: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126069
"Workers 16 Years and Over: Walked: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126070
"Workers 16 Years and Over: Walked: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126071
"Workers 16 Years and Over: Walked: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126072
Workers 16 Years and Over: Walked: Other Services (Except Public Administration),ACS09_5yr_B08126073
Workers 16 Years and Over: Walked: Public Administration,ACS09_5yr_B08126074
Workers 16 Years and Over: Walked: Armed Forces.1,ACS09_5yr_B08126075
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.4",ACS09_5yr_B08126076
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126077
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Construction",ACS09_5yr_B08126078
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Manufacturing",ACS09_5yr_B08126079
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Wholesale Trade",ACS09_5yr_B08126080
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Retail Trade",ACS09_5yr_B08126081
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126082
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Information",ACS09_5yr_B08126083
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126084
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126085
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126086
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126087
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Other Services (Except Public Administration)",ACS09_5yr_B08126088
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Public Administration",ACS09_5yr_B08126089
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Armed Forces.1",ACS09_5yr_B08126090
Workers 16 Years and Over: Worked At Home.4,ACS09_5yr_B08126091
"Workers 16 Years and Over: Worked At Home: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126092
Workers 16 Years and Over: Worked At Home: Construction,ACS09_5yr_B08126093
Workers 16 Years and Over: Worked At Home: Manufacturing,ACS09_5yr_B08126094
Workers 16 Years and Over: Worked At Home: Wholesale Trade,ACS09_5yr_B08126095
Workers 16 Years and Over: Worked At Home: Retail Trade,ACS09_5yr_B08126096
"Workers 16 Years and Over: Worked At Home: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126097
Workers 16 Years and Over: Worked At Home: Information,ACS09_5yr_B08126098
"Workers 16 Years and Over: Worked At Home: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126099
"Workers 16 Years and Over: Worked At Home: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126100
"Workers 16 Years and Over: Worked At Home: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126101
"Workers 16 Years and Over: Worked At Home: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126102
Workers 16 Years and Over: Worked At Home: Other Services (Except Public Administration),ACS09_5yr_B08126103
Workers 16 Years and Over: Worked At Home: Public Administration,ACS09_5yr_B08126104
Workers 16 Years and Over: Worked At Home: Armed Forces.1,ACS09_5yr_B08126105
Std. Error: Workers 16 Years and Over.8,ACS09_5yr_B08126001s
"Std. Error: Workers 16 Years and Over: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126002s
Std. Error: Workers 16 Years and Over: Construction,ACS09_5yr_B08126003s
Std. Error: Workers 16 Years and Over: Manufacturing,ACS09_5yr_B08126004s
Std. Error: Workers 16 Years and Over: Wholesale Trade,ACS09_5yr_B08126005s
Std. Error: Workers 16 Years and Over: Retail Trade,ACS09_5yr_B08126006s
"Std. Error: Workers 16 Years and Over: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126007s
Std. Error: Workers 16 Years and Over: Information,ACS09_5yr_B08126008s
"Std. Error: Workers 16 Years and Over: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126009s
"Std. Error: Workers 16 Years and Over: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126010s
"Std. Error: Workers 16 Years and Over: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126011s
"Std. Error: Workers 16 Years and Over: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126012s
Std. Error: Workers 16 Years and Over: Other Services (Except Public Administration),ACS09_5yr_B08126013s
Std. Error: Workers 16 Years and Over: Public Administration,ACS09_5yr_B08126014s
Std. Error: Workers 16 Years and Over: Armed Forces.1,ACS09_5yr_B08126015s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.4",ACS09_5yr_B08126016s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126017s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Construction",ACS09_5yr_B08126018s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Manufacturing",ACS09_5yr_B08126019s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Wholesale Trade",ACS09_5yr_B08126020s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Retail Trade",ACS09_5yr_B08126021s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126022s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Information",ACS09_5yr_B08126023s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126024s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126025s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126026s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126027s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Other Services (Except Public Administration)",ACS09_5yr_B08126028s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Public Administration",ACS09_5yr_B08126029s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Armed Forces.1",ACS09_5yr_B08126030s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled.4",ACS09_5yr_B08126031s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126032s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Construction",ACS09_5yr_B08126033s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Manufacturing",ACS09_5yr_B08126034s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Wholesale Trade",ACS09_5yr_B08126035s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Retail Trade",ACS09_5yr_B08126036s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126037s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Information",ACS09_5yr_B08126038s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126039s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126040s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126041s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126042s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Other Services (Except Public Administration)",ACS09_5yr_B08126043s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Public Administration",ACS09_5yr_B08126044s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Armed Forces.1",ACS09_5yr_B08126045s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab).4,ACS09_5yr_B08126046s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126047s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Construction,ACS09_5yr_B08126048s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Manufacturing,ACS09_5yr_B08126049s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Wholesale Trade,ACS09_5yr_B08126050s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Retail Trade,ACS09_5yr_B08126051s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Transportation and Warehousing, and Utilities",ACS09_5yr_B08126052s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Information,ACS09_5yr_B08126053s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126054s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126055s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126056s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126057s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Other Services (Except Public Administration),ACS09_5yr_B08126058s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Public Administration,ACS09_5yr_B08126059s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Armed Forces.1,ACS09_5yr_B08126060s
Std. Error: Workers 16 Years and Over: Walked.4,ACS09_5yr_B08126061s
"Std. Error: Workers 16 Years and Over: Walked: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126062s
Std. Error: Workers 16 Years and Over: Walked: Construction,ACS09_5yr_B08126063s
Std. Error: Workers 16 Years and Over: Walked: Manufacturing,ACS09_5yr_B08126064s
Std. Error: Workers 16 Years and Over: Walked: Wholesale Trade,ACS09_5yr_B08126065s
Std. Error: Workers 16 Years and Over: Walked: Retail Trade,ACS09_5yr_B08126066s
"Std. Error: Workers 16 Years and Over: Walked: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126067s
Std. Error: Workers 16 Years and Over: Walked: Information,ACS09_5yr_B08126068s
"Std. Error: Workers 16 Years and Over: Walked: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126069s
"Std. Error: Workers 16 Years and Over: Walked: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126070s
"Std. Error: Workers 16 Years and Over: Walked: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126071s
"Std. Error: Workers 16 Years and Over: Walked: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126072s
Std. Error: Workers 16 Years and Over: Walked: Other Services (Except Public Administration),ACS09_5yr_B08126073s
Std. Error: Workers 16 Years and Over: Walked: Public Administration,ACS09_5yr_B08126074s
Std. Error: Workers 16 Years and Over: Walked: Armed Forces.1,ACS09_5yr_B08126075s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.4",ACS09_5yr_B08126076s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126077s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Construction",ACS09_5yr_B08126078s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Manufacturing",ACS09_5yr_B08126079s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Wholesale Trade",ACS09_5yr_B08126080s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Retail Trade",ACS09_5yr_B08126081s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126082s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Information",ACS09_5yr_B08126083s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126084s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126085s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126086s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126087s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Other Services (Except Public Administration)",ACS09_5yr_B08126088s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Public Administration",ACS09_5yr_B08126089s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Armed Forces.1",ACS09_5yr_B08126090s
Std. Error: Workers 16 Years and Over: Worked At Home.4,ACS09_5yr_B08126091s
"Std. Error: Workers 16 Years and Over: Worked At Home: Agriculture, Forestry, Fishing and Hunting, and Mining",ACS09_5yr_B08126092s
Std. Error: Workers 16 Years and Over: Worked At Home: Construction,ACS09_5yr_B08126093s
Std. Error: Workers 16 Years and Over: Worked At Home: Manufacturing,ACS09_5yr_B08126094s
Std. Error: Workers 16 Years and Over: Worked At Home: Wholesale Trade,ACS09_5yr_B08126095s
Std. Error: Workers 16 Years and Over: Worked At Home: Retail Trade,ACS09_5yr_B08126096s
"Std. Error: Workers 16 Years and Over: Worked At Home: Transportation and Warehousing, and Utilities",ACS09_5yr_B08126097s
Std. Error: Workers 16 Years and Over: Worked At Home: Information,ACS09_5yr_B08126098s
"Std. Error: Workers 16 Years and Over: Worked At Home: Finance and Insurance, and Real Estate and Rental and Leasing",ACS09_5yr_B08126099s
"Std. Error: Workers 16 Years and Over: Worked At Home: Professional, Scientific, and Management, and Administrative and Waste Management Services",ACS09_5yr_B08126100s
"Std. Error: Workers 16 Years and Over: Worked At Home: Educational Services, and Health Care and Social Assistance",ACS09_5yr_B08126101s
"Std. Error: Workers 16 Years and Over: Worked At Home: Arts, Entertainment, and Recreation, and Accommodation and Food Services",ACS09_5yr_B08126102s
Std. Error: Workers 16 Years and Over: Worked At Home: Other Services (Except Public Administration),ACS09_5yr_B08126103s
Std. Error: Workers 16 Years and Over: Worked At Home: Public Administration,ACS09_5yr_B08126104s
Std. Error: Workers 16 Years and Over: Worked At Home: Armed Forces.1,ACS09_5yr_B08126105s
"% Workers 16 Years and Over: Agriculture, Forestry, Fishing and Hunting, and Mining",PCT_ACS09_5yr_B08126002
% Workers 16 Years and Over: Construction,PCT_ACS09_5yr_B08126003
% Workers 16 Years and Over: Manufacturing,PCT_ACS09_5yr_B08126004
% Workers 16 Years and Over: Wholesale Trade,PCT_ACS09_5yr_B08126005
% Workers 16 Years and Over: Retail Trade,PCT_ACS09_5yr_B08126006
"% Workers 16 Years and Over: Transportation and Warehousing, and Utilities",PCT_ACS09_5yr_B08126007
% Workers 16 Years and Over: Information,PCT_ACS09_5yr_B08126008
"% Workers 16 Years and Over: Finance and Insurance, and Real Estate and Rental and Leasing",PCT_ACS09_5yr_B08126009
"% Workers 16 Years and Over: Professional, Scientific, and Management, and Administrative and Waste Management Services",PCT_ACS09_5yr_B08126010
"% Workers 16 Years and Over: Educational Services, and Health Care and Social Assistance",PCT_ACS09_5yr_B08126011
"% Workers 16 Years and Over: Arts, Entertainment, and Recreation, and Accommodation and Food Services",PCT_ACS09_5yr_B08126012
% Workers 16 Years and Over: Other Services (Except Public Administration),PCT_ACS09_5yr_B08126013
% Workers 16 Years and Over: Public Administration,PCT_ACS09_5yr_B08126014
% Workers 16 Years and Over: Armed Forces.1,PCT_ACS09_5yr_B08126015
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.4",PCT_ACS09_5yr_B08126016
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Agriculture, Forestry, Fishing and Hunting, and Mining",PCT_ACS09_5yr_B08126017
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Construction",PCT_ACS09_5yr_B08126018
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Manufacturing",PCT_ACS09_5yr_B08126019
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Wholesale Trade",PCT_ACS09_5yr_B08126020
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Retail Trade",PCT_ACS09_5yr_B08126021
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Transportation and Warehousing, and Utilities",PCT_ACS09_5yr_B08126022
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Information",PCT_ACS09_5yr_B08126023
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Finance and Insurance, and Real Estate and Rental and Leasing",PCT_ACS09_5yr_B08126024
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Professional, Scientific, and Management, and Administrative and Waste Management Services",PCT_ACS09_5yr_B08126025
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Educational Services, and Health Care and Social Assistance",PCT_ACS09_5yr_B08126026
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Arts, Entertainment, and Recreation, and Accommodation and Food Services",PCT_ACS09_5yr_B08126027
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Other Services (Except Public Administration)",PCT_ACS09_5yr_B08126028
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Public Administration",PCT_ACS09_5yr_B08126029
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Armed Forces.1",PCT_ACS09_5yr_B08126030
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled.4",PCT_ACS09_5yr_B08126031
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Agriculture, Forestry, Fishing and Hunting, and Mining",PCT_ACS09_5yr_B08126032
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Construction",PCT_ACS09_5yr_B08126033
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Manufacturing",PCT_ACS09_5yr_B08126034
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Wholesale Trade",PCT_ACS09_5yr_B08126035
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Retail Trade",PCT_ACS09_5yr_B08126036
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Transportation and Warehousing, and Utilities",PCT_ACS09_5yr_B08126037
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Information",PCT_ACS09_5yr_B08126038
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Finance and Insurance, and Real Estate and Rental and Leasing",PCT_ACS09_5yr_B08126039
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Professional, Scientific, and Management, and Administrative and Waste Management Services",PCT_ACS09_5yr_B08126040
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Educational Services, and Health Care and Social Assistance",PCT_ACS09_5yr_B08126041
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Arts, Entertainment, and Recreation, and Accommodation and Food Services",PCT_ACS09_5yr_B08126042
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Other Services (Except Public Administration)",PCT_ACS09_5yr_B08126043
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Public Administration",PCT_ACS09_5yr_B08126044
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Armed Forces.1",PCT_ACS09_5yr_B08126045
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab).4,PCT_ACS09_5yr_B08126046
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Agriculture, Forestry, Fishing and Hunting, and Mining",PCT_ACS09_5yr_B08126047
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Construction,PCT_ACS09_5yr_B08126048
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Manufacturing,PCT_ACS09_5yr_B08126049
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Wholesale Trade,PCT_ACS09_5yr_B08126050
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Retail Trade,PCT_ACS09_5yr_B08126051
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Transportation and Warehousing, and Utilities",PCT_ACS09_5yr_B08126052
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Information,PCT_ACS09_5yr_B08126053
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Finance and Insurance, and Real Estate and Rental and Leasing",PCT_ACS09_5yr_B08126054
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Professional, Scientific, and Management, and Administrative and Waste Management Services",PCT_ACS09_5yr_B08126055
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Educational Services, and Health Care and Social Assistance",PCT_ACS09_5yr_B08126056
"% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Arts, Entertainment, and Recreation, and Accommodation and Food Services",PCT_ACS09_5yr_B08126057
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Other Services (Except Public Administration),PCT_ACS09_5yr_B08126058
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Public Administration,PCT_ACS09_5yr_B08126059
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Armed Forces.1,PCT_ACS09_5yr_B08126060
% Workers 16 Years and Over: Walked.4,PCT_ACS09_5yr_B08126061
"% Workers 16 Years and Over: Walked: Agriculture, Forestry, Fishing and Hunting, and Mining",PCT_ACS09_5yr_B08126062
% Workers 16 Years and Over: Walked: Construction,PCT_ACS09_5yr_B08126063
% Workers 16 Years and Over: Walked: Manufacturing,PCT_ACS09_5yr_B08126064
% Workers 16 Years and Over: Walked: Wholesale Trade,PCT_ACS09_5yr_B08126065
% Workers 16 Years and Over: Walked: Retail Trade,PCT_ACS09_5yr_B08126066
"% Workers 16 Years and Over: Walked: Transportation and Warehousing, and Utilities",PCT_ACS09_5yr_B08126067
% Workers 16 Years and Over: Walked: Information,PCT_ACS09_5yr_B08126068
"% Workers 16 Years and Over: Walked: Finance and Insurance, and Real Estate and Rental and Leasing",PCT_ACS09_5yr_B08126069
"% Workers 16 Years and Over: Walked: Professional, Scientific, and Management, and Administrative and Waste Management Services",PCT_ACS09_5yr_B08126070
"% Workers 16 Years and Over: Walked: Educational Services, and Health Care and Social Assistance",PCT_ACS09_5yr_B08126071
"% Workers 16 Years and Over: Walked: Arts, Entertainment, and Recreation, and Accommodation and Food Services",PCT_ACS09_5yr_B08126072
% Workers 16 Years and Over: Walked: Other Services (Except Public Administration),PCT_ACS09_5yr_B08126073
% Workers 16 Years and Over: Walked: Public Administration,PCT_ACS09_5yr_B08126074
% Workers 16 Years and Over: Walked: Armed Forces.1,PCT_ACS09_5yr_B08126075
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.4",PCT_ACS09_5yr_B08126076
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Agriculture, Forestry, Fishing and Hunting, and Mining",PCT_ACS09_5yr_B08126077
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Construction",PCT_ACS09_5yr_B08126078
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Manufacturing",PCT_ACS09_5yr_B08126079
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Wholesale Trade",PCT_ACS09_5yr_B08126080
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Retail Trade",PCT_ACS09_5yr_B08126081
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Transportation and Warehousing, and Utilities",PCT_ACS09_5yr_B08126082
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Information",PCT_ACS09_5yr_B08126083
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Finance and Insurance, and Real Estate and Rental and Leasing",PCT_ACS09_5yr_B08126084
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Professional, Scientific, and Management, and Administrative and Waste Management Services",PCT_ACS09_5yr_B08126085
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Educational Services, and Health Care and Social Assistance",PCT_ACS09_5yr_B08126086
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Arts, Entertainment, and Recreation, and Accommodation and Food Services",PCT_ACS09_5yr_B08126087
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Other Services (Except Public Administration)",PCT_ACS09_5yr_B08126088
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Public Administration",PCT_ACS09_5yr_B08126089
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Armed Forces.1",PCT_ACS09_5yr_B08126090
% Workers 16 Years and Over: Worked At Home.4,PCT_ACS09_5yr_B08126091
"% Workers 16 Years and Over: Worked At Home: Agriculture, Forestry, Fishing and Hunting, and Mining",PCT_ACS09_5yr_B08126092
% Workers 16 Years and Over: Worked At Home: Construction,PCT_ACS09_5yr_B08126093
% Workers 16 Years and Over: Worked At Home: Manufacturing,PCT_ACS09_5yr_B08126094
% Workers 16 Years and Over: Worked At Home: Wholesale Trade,PCT_ACS09_5yr_B08126095
% Workers 16 Years and Over: Worked At Home: Retail Trade,PCT_ACS09_5yr_B08126096
"% Workers 16 Years and Over: Worked At Home: Transportation and Warehousing, and Utilities",PCT_ACS09_5yr_B08126097
% Workers 16 Years and Over: Worked At Home: Information,PCT_ACS09_5yr_B08126098
"% Workers 16 Years and Over: Worked At Home: Finance and Insurance, and Real Estate and Rental and Leasing",PCT_ACS09_5yr_B08126099
"% Workers 16 Years and Over: Worked At Home: Professional, Scientific, and Management, and Administrative and Waste Management Services",PCT_ACS09_5yr_B08126100
"% Workers 16 Years and Over: Worked At Home: Educational Services, and Health Care and Social Assistance",PCT_ACS09_5yr_B08126101
"% Workers 16 Years and Over: Worked At Home: Arts, Entertainment, and Recreation, and Accommodation and Food Services",PCT_ACS09_5yr_B08126102
% Workers 16 Years and Over: Worked At Home: Other Services (Except Public Administration),PCT_ACS09_5yr_B08126103
% Workers 16 Years and Over: Worked At Home: Public Administration,PCT_ACS09_5yr_B08126104
% Workers 16 Years and Over: Worked At Home: Armed Forces.1,PCT_ACS09_5yr_B08126105
Workers 16 Years and Over.9,ACS09_5yr_B08128001
Workers 16 Years and Over: Private for-Profit Wage and Salary Workers,ACS09_5yr_B08128002
Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,ACS09_5yr_B08128003
Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,ACS09_5yr_B08128004
Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Private Not-for-Profit Wage and Salary Workers,ACS09_5yr_B08128005
Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Local Government Workers,ACS09_5yr_B08128006
Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: State Government Workers,ACS09_5yr_B08128007
Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Federal Government Workers,ACS09_5yr_B08128008
Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Self-Employed in Own Not Incorporated Business Workers,ACS09_5yr_B08128009
Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Unpaid Family Workers,ACS09_5yr_B08128010
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.5",ACS09_5yr_B08128011
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private for-Profit Wage and Salary Workers",ACS09_5yr_B08128012
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers",ACS09_5yr_B08128013
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers",ACS09_5yr_B08128014
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private Not-for-Profit Wage and Salary Workers",ACS09_5yr_B08128015
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Local Government Workers",ACS09_5yr_B08128016
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: State Government Workers",ACS09_5yr_B08128017
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Federal Government Workers",ACS09_5yr_B08128018
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Self-Employed in Own Not Incorporated Business Workers",ACS09_5yr_B08128019
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Unpaid Family Workers",ACS09_5yr_B08128020
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled.5",ACS09_5yr_B08128021
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private for-Profit Wage and Salary Workers",ACS09_5yr_B08128022
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers",ACS09_5yr_B08128023
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers",ACS09_5yr_B08128024
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private Not-for-Profit Wage and Salary Workers",ACS09_5yr_B08128025
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Local Government Workers",ACS09_5yr_B08128026
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: State Government Workers",ACS09_5yr_B08128027
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Federal Government Workers",ACS09_5yr_B08128028
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Self-Employed in Own Not Incorporated Business Workers",ACS09_5yr_B08128029
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Unpaid Family Workers",ACS09_5yr_B08128030
Workers 16 Years and Over: Public Transportation (Excluding Taxicab).5,ACS09_5yr_B08128031
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private for-Profit Wage and Salary Workers,ACS09_5yr_B08128032
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,ACS09_5yr_B08128033
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,ACS09_5yr_B08128034
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private Not-for-Profit Wage and Salary Workers,ACS09_5yr_B08128035
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Local Government Workers,ACS09_5yr_B08128036
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): State Government Workers,ACS09_5yr_B08128037
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Federal Government Workers,ACS09_5yr_B08128038
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Self-Employed in Own Not Incorporated Business Workers,ACS09_5yr_B08128039
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Unpaid Family Workers,ACS09_5yr_B08128040
Workers 16 Years and Over: Walked.5,ACS09_5yr_B08128041
Workers 16 Years and Over: Walked: Private for-Profit Wage and Salary Workers,ACS09_5yr_B08128042
Workers 16 Years and Over: Walked: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,ACS09_5yr_B08128043
Workers 16 Years and Over: Walked: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,ACS09_5yr_B08128044
Workers 16 Years and Over: Walked: Private Not-for-Profit Wage and Salary Workers,ACS09_5yr_B08128045
Workers 16 Years and Over: Walked: Local Government Workers,ACS09_5yr_B08128046
Workers 16 Years and Over: Walked: State Government Workers,ACS09_5yr_B08128047
Workers 16 Years and Over: Walked: Federal Government Workers,ACS09_5yr_B08128048
Workers 16 Years and Over: Walked: Self-Employed in Own Not Incorporated Business Workers,ACS09_5yr_B08128049
Workers 16 Years and Over: Walked: Unpaid Family Workers,ACS09_5yr_B08128050
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.5",ACS09_5yr_B08128051
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private for-Profit Wage and Salary Workers",ACS09_5yr_B08128052
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers",ACS09_5yr_B08128053
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers",ACS09_5yr_B08128054
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private Not-for-Profit Wage and Salary Workers",ACS09_5yr_B08128055
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Local Government Workers",ACS09_5yr_B08128056
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: State Government Workers",ACS09_5yr_B08128057
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Federal Government Workers",ACS09_5yr_B08128058
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Self-Employed in Own Not Incorporated Business Workers",ACS09_5yr_B08128059
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Unpaid Family Workers",ACS09_5yr_B08128060
Workers 16 Years and Over: Worked At Home.5,ACS09_5yr_B08128061
Workers 16 Years and Over: Worked At Home: Private for-Profit Wage and Salary Workers,ACS09_5yr_B08128062
Workers 16 Years and Over: Worked At Home: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,ACS09_5yr_B08128063
Workers 16 Years and Over: Worked At Home: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,ACS09_5yr_B08128064
Workers 16 Years and Over: Worked At Home: Private Not-for-Profit Wage and Salary Workers,ACS09_5yr_B08128065
Workers 16 Years and Over: Worked At Home: Local Government Workers,ACS09_5yr_B08128066
Workers 16 Years and Over: Worked At Home: State Government Workers,ACS09_5yr_B08128067
Workers 16 Years and Over: Worked At Home: Federal Government Workers,ACS09_5yr_B08128068
Workers 16 Years and Over: Worked At Home: Self-Employed in Own Not Incorporated Business Workers,ACS09_5yr_B08128069
Workers 16 Years and Over: Worked At Home: Unpaid Family Workers,ACS09_5yr_B08128070
Std. Error: Workers 16 Years and Over.9,ACS09_5yr_B08128001s
Std. Error: Workers 16 Years and Over: Private for-Profit Wage and Salary Workers,ACS09_5yr_B08128002s
Std. Error: Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,ACS09_5yr_B08128003s
Std. Error: Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,ACS09_5yr_B08128004s
Std. Error: Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Private Not-for-Profit Wage and Salary Workers,ACS09_5yr_B08128005s
Std. Error: Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Local Government Workers,ACS09_5yr_B08128006s
Std. Error: Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: State Government Workers,ACS09_5yr_B08128007s
Std. Error: Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Federal Government Workers,ACS09_5yr_B08128008s
Std. Error: Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Self-Employed in Own Not Incorporated Business Workers,ACS09_5yr_B08128009s
Std. Error: Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Unpaid Family Workers,ACS09_5yr_B08128010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.5",ACS09_5yr_B08128011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private for-Profit Wage and Salary Workers",ACS09_5yr_B08128012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers",ACS09_5yr_B08128013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers",ACS09_5yr_B08128014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private Not-for-Profit Wage and Salary Workers",ACS09_5yr_B08128015s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Local Government Workers",ACS09_5yr_B08128016s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: State Government Workers",ACS09_5yr_B08128017s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Federal Government Workers",ACS09_5yr_B08128018s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Self-Employed in Own Not Incorporated Business Workers",ACS09_5yr_B08128019s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Unpaid Family Workers",ACS09_5yr_B08128020s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled.5",ACS09_5yr_B08128021s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private for-Profit Wage and Salary Workers",ACS09_5yr_B08128022s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers",ACS09_5yr_B08128023s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers",ACS09_5yr_B08128024s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private Not-for-Profit Wage and Salary Workers",ACS09_5yr_B08128025s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Local Government Workers",ACS09_5yr_B08128026s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: State Government Workers",ACS09_5yr_B08128027s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Federal Government Workers",ACS09_5yr_B08128028s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Self-Employed in Own Not Incorporated Business Workers",ACS09_5yr_B08128029s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Unpaid Family Workers",ACS09_5yr_B08128030s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab).5,ACS09_5yr_B08128031s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private for-Profit Wage and Salary Workers,ACS09_5yr_B08128032s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,ACS09_5yr_B08128033s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,ACS09_5yr_B08128034s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private Not-for-Profit Wage and Salary Workers,ACS09_5yr_B08128035s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Local Government Workers,ACS09_5yr_B08128036s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): State Government Workers,ACS09_5yr_B08128037s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Federal Government Workers,ACS09_5yr_B08128038s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Self-Employed in Own Not Incorporated Business Workers,ACS09_5yr_B08128039s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Unpaid Family Workers,ACS09_5yr_B08128040s
Std. Error: Workers 16 Years and Over: Walked.5,ACS09_5yr_B08128041s
Std. Error: Workers 16 Years and Over: Walked: Private for-Profit Wage and Salary Workers,ACS09_5yr_B08128042s
Std. Error: Workers 16 Years and Over: Walked: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,ACS09_5yr_B08128043s
Std. Error: Workers 16 Years and Over: Walked: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,ACS09_5yr_B08128044s
Std. Error: Workers 16 Years and Over: Walked: Private Not-for-Profit Wage and Salary Workers,ACS09_5yr_B08128045s
Std. Error: Workers 16 Years and Over: Walked: Local Government Workers,ACS09_5yr_B08128046s
Std. Error: Workers 16 Years and Over: Walked: State Government Workers,ACS09_5yr_B08128047s
Std. Error: Workers 16 Years and Over: Walked: Federal Government Workers,ACS09_5yr_B08128048s
Std. Error: Workers 16 Years and Over: Walked: Self-Employed in Own Not Incorporated Business Workers,ACS09_5yr_B08128049s
Std. Error: Workers 16 Years and Over: Walked: Unpaid Family Workers,ACS09_5yr_B08128050s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.5",ACS09_5yr_B08128051s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private for-Profit Wage and Salary Workers",ACS09_5yr_B08128052s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers",ACS09_5yr_B08128053s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers",ACS09_5yr_B08128054s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private Not-for-Profit Wage and Salary Workers",ACS09_5yr_B08128055s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Local Government Workers",ACS09_5yr_B08128056s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: State Government Workers",ACS09_5yr_B08128057s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Federal Government Workers",ACS09_5yr_B08128058s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Self-Employed in Own Not Incorporated Business Workers",ACS09_5yr_B08128059s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Unpaid Family Workers",ACS09_5yr_B08128060s
Std. Error: Workers 16 Years and Over: Worked At Home.5,ACS09_5yr_B08128061s
Std. Error: Workers 16 Years and Over: Worked At Home: Private for-Profit Wage and Salary Workers,ACS09_5yr_B08128062s
Std. Error: Workers 16 Years and Over: Worked At Home: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,ACS09_5yr_B08128063s
Std. Error: Workers 16 Years and Over: Worked At Home: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,ACS09_5yr_B08128064s
Std. Error: Workers 16 Years and Over: Worked At Home: Private Not-for-Profit Wage and Salary Workers,ACS09_5yr_B08128065s
Std. Error: Workers 16 Years and Over: Worked At Home: Local Government Workers,ACS09_5yr_B08128066s
Std. Error: Workers 16 Years and Over: Worked At Home: State Government Workers,ACS09_5yr_B08128067s
Std. Error: Workers 16 Years and Over: Worked At Home: Federal Government Workers,ACS09_5yr_B08128068s
Std. Error: Workers 16 Years and Over: Worked At Home: Self-Employed in Own Not Incorporated Business Workers,ACS09_5yr_B08128069s
Std. Error: Workers 16 Years and Over: Worked At Home: Unpaid Family Workers,ACS09_5yr_B08128070s
% Workers 16 Years and Over: Private for-Profit Wage and Salary Workers,PCT_ACS09_5yr_B08128002
% Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,PCT_ACS09_5yr_B08128003
% Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,PCT_ACS09_5yr_B08128004
% Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Private Not-for-Profit Wage and Salary Workers,PCT_ACS09_5yr_B08128005
% Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Local Government Workers,PCT_ACS09_5yr_B08128006
% Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: State Government Workers,PCT_ACS09_5yr_B08128007
% Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Federal Government Workers,PCT_ACS09_5yr_B08128008
% Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Self-Employed in Own Not Incorporated Business Workers,PCT_ACS09_5yr_B08128009
% Workers 16 Years and Over: Private for-Profit Wage and Salary Workers: Unpaid Family Workers,PCT_ACS09_5yr_B08128010
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.5",PCT_ACS09_5yr_B08128011
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private for-Profit Wage and Salary Workers",PCT_ACS09_5yr_B08128012
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers",PCT_ACS09_5yr_B08128013
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers",PCT_ACS09_5yr_B08128014
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Private Not-for-Profit Wage and Salary Workers",PCT_ACS09_5yr_B08128015
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Local Government Workers",PCT_ACS09_5yr_B08128016
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: State Government Workers",PCT_ACS09_5yr_B08128017
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Federal Government Workers",PCT_ACS09_5yr_B08128018
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Self-Employed in Own Not Incorporated Business Workers",PCT_ACS09_5yr_B08128019
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Unpaid Family Workers",PCT_ACS09_5yr_B08128020
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled.5",PCT_ACS09_5yr_B08128021
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private for-Profit Wage and Salary Workers",PCT_ACS09_5yr_B08128022
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers",PCT_ACS09_5yr_B08128023
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers",PCT_ACS09_5yr_B08128024
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Private Not-for-Profit Wage and Salary Workers",PCT_ACS09_5yr_B08128025
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Local Government Workers",PCT_ACS09_5yr_B08128026
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: State Government Workers",PCT_ACS09_5yr_B08128027
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Federal Government Workers",PCT_ACS09_5yr_B08128028
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Self-Employed in Own Not Incorporated Business Workers",PCT_ACS09_5yr_B08128029
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Unpaid Family Workers",PCT_ACS09_5yr_B08128030
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab).5,PCT_ACS09_5yr_B08128031
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private for-Profit Wage and Salary Workers,PCT_ACS09_5yr_B08128032
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,PCT_ACS09_5yr_B08128033
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,PCT_ACS09_5yr_B08128034
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Private Not-for-Profit Wage and Salary Workers,PCT_ACS09_5yr_B08128035
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Local Government Workers,PCT_ACS09_5yr_B08128036
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): State Government Workers,PCT_ACS09_5yr_B08128037
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Federal Government Workers,PCT_ACS09_5yr_B08128038
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Self-Employed in Own Not Incorporated Business Workers,PCT_ACS09_5yr_B08128039
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Unpaid Family Workers,PCT_ACS09_5yr_B08128040
% Workers 16 Years and Over: Walked.5,PCT_ACS09_5yr_B08128041
% Workers 16 Years and Over: Walked: Private for-Profit Wage and Salary Workers,PCT_ACS09_5yr_B08128042
% Workers 16 Years and Over: Walked: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,PCT_ACS09_5yr_B08128043
% Workers 16 Years and Over: Walked: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,PCT_ACS09_5yr_B08128044
% Workers 16 Years and Over: Walked: Private Not-for-Profit Wage and Salary Workers,PCT_ACS09_5yr_B08128045
% Workers 16 Years and Over: Walked: Local Government Workers,PCT_ACS09_5yr_B08128046
% Workers 16 Years and Over: Walked: State Government Workers,PCT_ACS09_5yr_B08128047
% Workers 16 Years and Over: Walked: Federal Government Workers,PCT_ACS09_5yr_B08128048
% Workers 16 Years and Over: Walked: Self-Employed in Own Not Incorporated Business Workers,PCT_ACS09_5yr_B08128049
% Workers 16 Years and Over: Walked: Unpaid Family Workers,PCT_ACS09_5yr_B08128050
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.5",PCT_ACS09_5yr_B08128051
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private for-Profit Wage and Salary Workers",PCT_ACS09_5yr_B08128052
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers",PCT_ACS09_5yr_B08128053
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers",PCT_ACS09_5yr_B08128054
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Private Not-for-Profit Wage and Salary Workers",PCT_ACS09_5yr_B08128055
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Local Government Workers",PCT_ACS09_5yr_B08128056
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: State Government Workers",PCT_ACS09_5yr_B08128057
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Federal Government Workers",PCT_ACS09_5yr_B08128058
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Self-Employed in Own Not Incorporated Business Workers",PCT_ACS09_5yr_B08128059
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Unpaid Family Workers",PCT_ACS09_5yr_B08128060
% Workers 16 Years and Over: Worked At Home.5,PCT_ACS09_5yr_B08128061
% Workers 16 Years and Over: Worked At Home: Private for-Profit Wage and Salary Workers,PCT_ACS09_5yr_B08128062
% Workers 16 Years and Over: Worked At Home: Private for-Profit Wage and Salary Workers: Employee of Private Company Workers,PCT_ACS09_5yr_B08128063
% Workers 16 Years and Over: Worked At Home: Private for-Profit Wage and Salary Workers: Self-Employed in Own Incorporated Business Workers,PCT_ACS09_5yr_B08128064
% Workers 16 Years and Over: Worked At Home: Private Not-for-Profit Wage and Salary Workers,PCT_ACS09_5yr_B08128065
% Workers 16 Years and Over: Worked At Home: Local Government Workers,PCT_ACS09_5yr_B08128066
% Workers 16 Years and Over: Worked At Home: State Government Workers,PCT_ACS09_5yr_B08128067
% Workers 16 Years and Over: Worked At Home: Federal Government Workers,PCT_ACS09_5yr_B08128068
% Workers 16 Years and Over: Worked At Home: Self-Employed in Own Not Incorporated Business Workers,PCT_ACS09_5yr_B08128069
% Workers 16 Years and Over: Worked At Home: Unpaid Family Workers,PCT_ACS09_5yr_B08128070
Workers 16 Years and Over.10,ACS09_5yr_B08130001
Workers 16 Years and Over: Worked in State of Residence.1,ACS09_5yr_B08130002
Workers 16 Years and Over: Worked in State of Residence: Worked in County of Residence.1,ACS09_5yr_B08130003
Workers 16 Years and Over: Worked in State of Residence: Worked Outside County of Residence.1,ACS09_5yr_B08130004
Workers 16 Years and Over: Worked in State of Residence: Worked Outside State of Residence.1,ACS09_5yr_B08130005
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.6",ACS09_5yr_B08130006
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked in State of Residence",ACS09_5yr_B08130007
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked in State of Residence: Worked in County of Residence",ACS09_5yr_B08130008
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked in State of Residence: Worked Outside County of Residence",ACS09_5yr_B08130009
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked Outside State of Residence",ACS09_5yr_B08130010
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled.6",ACS09_5yr_B08130011
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked in State of Residence",ACS09_5yr_B08130012
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked in State of Residence: Worked in County of Residence",ACS09_5yr_B08130013
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked in State of Residence: Worked Outside County of Residence",ACS09_5yr_B08130014
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked Outside State of Residence",ACS09_5yr_B08130015
Workers 16 Years and Over: Public Transportation (Excluding Taxicab).6,ACS09_5yr_B08130016
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked in State of Residence,ACS09_5yr_B08130017
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08130018
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08130019
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked Outside State of Residence,ACS09_5yr_B08130020
Workers 16 Years and Over: Walked.6,ACS09_5yr_B08130021
Workers 16 Years and Over: Walked: Worked in State of Residence,ACS09_5yr_B08130022
Workers 16 Years and Over: Walked: Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08130023
Workers 16 Years and Over: Walked: Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08130024
Workers 16 Years and Over: Walked: Worked Outside State of Residence,ACS09_5yr_B08130025
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.6",ACS09_5yr_B08130026
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked in State of Residence",ACS09_5yr_B08130027
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked in State of Residence: Worked in County of Residence",ACS09_5yr_B08130028
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked in State of Residence: Worked Outside County of Residence",ACS09_5yr_B08130029
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked Outside State of Residence",ACS09_5yr_B08130030
Workers 16 Years and Over: Worked At Home.6,ACS09_5yr_B08130031
Std. Error: Workers 16 Years and Over.10,ACS09_5yr_B08130001s
Std. Error: Workers 16 Years and Over: Worked in State of Residence.1,ACS09_5yr_B08130002s
Std. Error: Workers 16 Years and Over: Worked in State of Residence: Worked in County of Residence.1,ACS09_5yr_B08130003s
Std. Error: Workers 16 Years and Over: Worked in State of Residence: Worked Outside County of Residence.1,ACS09_5yr_B08130004s
Std. Error: Workers 16 Years and Over: Worked in State of Residence: Worked Outside State of Residence.1,ACS09_5yr_B08130005s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.6",ACS09_5yr_B08130006s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked in State of Residence",ACS09_5yr_B08130007s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked in State of Residence: Worked in County of Residence",ACS09_5yr_B08130008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked in State of Residence: Worked Outside County of Residence",ACS09_5yr_B08130009s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked Outside State of Residence",ACS09_5yr_B08130010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled.6",ACS09_5yr_B08130011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked in State of Residence",ACS09_5yr_B08130012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked in State of Residence: Worked in County of Residence",ACS09_5yr_B08130013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked in State of Residence: Worked Outside County of Residence",ACS09_5yr_B08130014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked Outside State of Residence",ACS09_5yr_B08130015s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab).6,ACS09_5yr_B08130016s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked in State of Residence,ACS09_5yr_B08130017s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08130018s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08130019s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked Outside State of Residence,ACS09_5yr_B08130020s
Std. Error: Workers 16 Years and Over: Walked.6,ACS09_5yr_B08130021s
Std. Error: Workers 16 Years and Over: Walked: Worked in State of Residence,ACS09_5yr_B08130022s
Std. Error: Workers 16 Years and Over: Walked: Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08130023s
Std. Error: Workers 16 Years and Over: Walked: Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08130024s
Std. Error: Workers 16 Years and Over: Walked: Worked Outside State of Residence,ACS09_5yr_B08130025s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.6",ACS09_5yr_B08130026s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked in State of Residence",ACS09_5yr_B08130027s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked in State of Residence: Worked in County of Residence",ACS09_5yr_B08130028s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked in State of Residence: Worked Outside County of Residence",ACS09_5yr_B08130029s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked Outside State of Residence",ACS09_5yr_B08130030s
Std. Error: Workers 16 Years and Over: Worked At Home.6,ACS09_5yr_B08130031s
% Workers 16 Years and Over: Worked in State of Residence.1,PCT_ACS09_5yr_B08130002
% Workers 16 Years and Over: Worked in State of Residence: Worked in County of Residence.1,PCT_ACS09_5yr_B08130003
% Workers 16 Years and Over: Worked in State of Residence: Worked Outside County of Residence.1,PCT_ACS09_5yr_B08130004
% Workers 16 Years and Over: Worked in State of Residence: Worked Outside State of Residence.1,PCT_ACS09_5yr_B08130005
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.6",PCT_ACS09_5yr_B08130006
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked in State of Residence",PCT_ACS09_5yr_B08130007
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked in State of Residence: Worked in County of Residence",PCT_ACS09_5yr_B08130008
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked in State of Residence: Worked Outside County of Residence",PCT_ACS09_5yr_B08130009
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Worked Outside State of Residence",PCT_ACS09_5yr_B08130010
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled.6",PCT_ACS09_5yr_B08130011
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked in State of Residence",PCT_ACS09_5yr_B08130012
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked in State of Residence: Worked in County of Residence",PCT_ACS09_5yr_B08130013
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked in State of Residence: Worked Outside County of Residence",PCT_ACS09_5yr_B08130014
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Worked Outside State of Residence",PCT_ACS09_5yr_B08130015
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab).6,PCT_ACS09_5yr_B08130016
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked in State of Residence,PCT_ACS09_5yr_B08130017
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked in State of Residence: Worked in County of Residence,PCT_ACS09_5yr_B08130018
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked in State of Residence: Worked Outside County of Residence,PCT_ACS09_5yr_B08130019
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Worked Outside State of Residence,PCT_ACS09_5yr_B08130020
% Workers 16 Years and Over: Walked.6,PCT_ACS09_5yr_B08130021
% Workers 16 Years and Over: Walked: Worked in State of Residence,PCT_ACS09_5yr_B08130022
% Workers 16 Years and Over: Walked: Worked in State of Residence: Worked in County of Residence,PCT_ACS09_5yr_B08130023
% Workers 16 Years and Over: Walked: Worked in State of Residence: Worked Outside County of Residence,PCT_ACS09_5yr_B08130024
% Workers 16 Years and Over: Walked: Worked Outside State of Residence,PCT_ACS09_5yr_B08130025
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.6",PCT_ACS09_5yr_B08130026
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked in State of Residence",PCT_ACS09_5yr_B08130027
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked in State of Residence: Worked in County of Residence",PCT_ACS09_5yr_B08130028
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked in State of Residence: Worked Outside County of Residence",PCT_ACS09_5yr_B08130029
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Worked Outside State of Residence",PCT_ACS09_5yr_B08130030
% Workers 16 Years and Over: Worked At Home.6,PCT_ACS09_5yr_B08130031
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes).1,ACS09_5yr_B08131001
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked in State of Residence,ACS09_5yr_B08131002
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08131003
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08131004
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked Outside State of Residence,ACS09_5yr_B08131005
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes).1,ACS09_5yr_B08131001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked in State of Residence,ACS09_5yr_B08131002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked in State of Residence: Worked in County of Residence,ACS09_5yr_B08131003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked in State of Residence: Worked Outside County of Residence,ACS09_5yr_B08131004s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked Outside State of Residence,ACS09_5yr_B08131005s
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked in State of Residence,PCT_ACS09_5yr_B08131002
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked in State of Residence: Worked in County of Residence,PCT_ACS09_5yr_B08131003
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked in State of Residence: Worked Outside County of Residence,PCT_ACS09_5yr_B08131004
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Worked Outside State of Residence,PCT_ACS09_5yr_B08131005
Workers 16 Years and Over Who Did Not Work At Home.2,ACS09_5yr_B08132001
Workers 16 Years and Over Who Did Not Work At Home: 12:00 A.m. to 4:59 A.m..1,ACS09_5yr_B08132002
Workers 16 Years and Over Who Did Not Work At Home: 5:00 A.m. to 5:29 A.m..1,ACS09_5yr_B08132003
Workers 16 Years and Over Who Did Not Work At Home: 5:30 A.m. to 5:59 A.m..1,ACS09_5yr_B08132004
Workers 16 Years and Over Who Did Not Work At Home: 6:00 A.m. to 6:29 A.m..1,ACS09_5yr_B08132005
Workers 16 Years and Over Who Did Not Work At Home: 6:30 A.m. to 6:59 A.m..1,ACS09_5yr_B08132006
Workers 16 Years and Over Who Did Not Work At Home: 7:00 A.m. to 7:29 A.m..1,ACS09_5yr_B08132007
Workers 16 Years and Over Who Did Not Work At Home: 7:30 A.m. to 7:59 A.m..1,ACS09_5yr_B08132008
Workers 16 Years and Over Who Did Not Work At Home: 8:00 A.m. to 8:29 A.m..1,ACS09_5yr_B08132009
Workers 16 Years and Over Who Did Not Work At Home: 8:30 A.m. to 8:59 A.m..1,ACS09_5yr_B08132010
Workers 16 Years and Over Who Did Not Work At Home: 9:00 A.m. to 9:59 A.m..1,ACS09_5yr_B08132011
Workers 16 Years and Over Who Did Not Work At Home: 10:00 A.m. to 10:59 A.m..1,ACS09_5yr_B08132012
Workers 16 Years and Over Who Did Not Work At Home: 11:00 A.m. to 11:59 A.m..1,ACS09_5yr_B08132013
Workers 16 Years and Over Who Did Not Work At Home: 12:00 P.m. to 3:59 P.m..1,ACS09_5yr_B08132014
Workers 16 Years and Over Who Did Not Work At Home: 4:00 P.m. to 11:59 P.m..1,ACS09_5yr_B08132015
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08132016
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 12:00 A.m. to 4:59 A.m.",ACS09_5yr_B08132017
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 5:00 A.m. to 5:29 A.m.",ACS09_5yr_B08132018
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 5:30 A.m. to 5:59 A.m.",ACS09_5yr_B08132019
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 6:00 A.m. to 6:29 A.m.",ACS09_5yr_B08132020
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 6:30 A.m. to 6:59 A.m.",ACS09_5yr_B08132021
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 7:00 A.m. to 7:29 A.m.",ACS09_5yr_B08132022
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 7:30 A.m. to 7:59 A.m.",ACS09_5yr_B08132023
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 8:00 A.m. to 8:29 A.m.",ACS09_5yr_B08132024
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 8:30 A.m. to 8:59 A.m.",ACS09_5yr_B08132025
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 9:00 A.m. to 9:59 A.m.",ACS09_5yr_B08132026
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 10:00 A.m. to 10:59 A.m.",ACS09_5yr_B08132027
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 11:00 A.m. to 11:59 A.m.",ACS09_5yr_B08132028
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 12:00 P.m. to 3:59 P.m.",ACS09_5yr_B08132029
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 4:00 P.m. to 11:59 P.m.",ACS09_5yr_B08132030
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled",ACS09_5yr_B08132031
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 12:00 A.m. to 4:59 A.m.",ACS09_5yr_B08132032
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 5:00 A.m. to 5:29 A.m.",ACS09_5yr_B08132033
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 5:30 A.m. to 5:59 A.m.",ACS09_5yr_B08132034
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 6:00 A.m. to 6:29 A.m.",ACS09_5yr_B08132035
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 6:30 A.m. to 6:59 A.m.",ACS09_5yr_B08132036
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 7:00 A.m. to 7:29 A.m.",ACS09_5yr_B08132037
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 7:30 A.m. to 7:59 A.m.",ACS09_5yr_B08132038
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 8:00 A.m. to 8:29 A.m.",ACS09_5yr_B08132039
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 8:30 A.m. to 8:59 A.m.",ACS09_5yr_B08132040
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 9:00 A.m. to 9:59 A.m.",ACS09_5yr_B08132041
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 10:00 A.m. to 10:59 A.m.",ACS09_5yr_B08132042
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 11:00 A.m. to 11:59 A.m.",ACS09_5yr_B08132043
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 12:00 P.m. to 3:59 P.m.",ACS09_5yr_B08132044
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 4:00 P.m. to 11:59 P.m.",ACS09_5yr_B08132045
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab),ACS09_5yr_B08132046
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08132047
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08132048
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08132049
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08132050
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08132051
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08132052
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08132053
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08132054
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08132055
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08132056
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08132057
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08132058
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08132059
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08132060
Workers 16 Years and Over Who Did Not Work At Home: Walked,ACS09_5yr_B08132061
Workers 16 Years and Over Who Did Not Work At Home: Walked: 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08132062
Workers 16 Years and Over Who Did Not Work At Home: Walked: 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08132063
Workers 16 Years and Over Who Did Not Work At Home: Walked: 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08132064
Workers 16 Years and Over Who Did Not Work At Home: Walked: 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08132065
Workers 16 Years and Over Who Did Not Work At Home: Walked: 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08132066
Workers 16 Years and Over Who Did Not Work At Home: Walked: 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08132067
Workers 16 Years and Over Who Did Not Work At Home: Walked: 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08132068
Workers 16 Years and Over Who Did Not Work At Home: Walked: 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08132069
Workers 16 Years and Over Who Did Not Work At Home: Walked: 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08132070
Workers 16 Years and Over Who Did Not Work At Home: Walked: 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08132071
Workers 16 Years and Over Who Did Not Work At Home: Walked: 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08132072
Workers 16 Years and Over Who Did Not Work At Home: Walked: 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08132073
Workers 16 Years and Over Who Did Not Work At Home: Walked: 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08132074
Workers 16 Years and Over Who Did Not Work At Home: Walked: 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08132075
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08132076
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 12:00 A.m. to 4:59 A.m.",ACS09_5yr_B08132077
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 5:00 A.m. to 5:29 A.m.",ACS09_5yr_B08132078
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 5:30 A.m. to 5:59 A.m.",ACS09_5yr_B08132079
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 6:00 A.m. to 6:29 A.m.",ACS09_5yr_B08132080
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 6:30 A.m. to 6:59 A.m.",ACS09_5yr_B08132081
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 7:00 A.m. to 7:29 A.m.",ACS09_5yr_B08132082
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 7:30 A.m. to 7:59 A.m.",ACS09_5yr_B08132083
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 8:00 A.m. to 8:29 A.m.",ACS09_5yr_B08132084
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 8:30 A.m. to 8:59 A.m.",ACS09_5yr_B08132085
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 9:00 A.m. to 9:59 A.m.",ACS09_5yr_B08132086
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 10:00 A.m. to 10:59 A.m.",ACS09_5yr_B08132087
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 11:00 A.m. to 11:59 A.m.",ACS09_5yr_B08132088
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 12:00 P.m. to 3:59 P.m.",ACS09_5yr_B08132089
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 4:00 P.m. to 11:59 P.m.",ACS09_5yr_B08132090
Std. Error: Workers 16 Years and Over Who Did Not Work At Home.2,ACS09_5yr_B08132001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 12:00 A.m. to 4:59 A.m..1,ACS09_5yr_B08132002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 5:00 A.m. to 5:29 A.m..1,ACS09_5yr_B08132003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 5:30 A.m. to 5:59 A.m..1,ACS09_5yr_B08132004s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 6:00 A.m. to 6:29 A.m..1,ACS09_5yr_B08132005s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 6:30 A.m. to 6:59 A.m..1,ACS09_5yr_B08132006s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 7:00 A.m. to 7:29 A.m..1,ACS09_5yr_B08132007s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 7:30 A.m. to 7:59 A.m..1,ACS09_5yr_B08132008s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 8:00 A.m. to 8:29 A.m..1,ACS09_5yr_B08132009s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 8:30 A.m. to 8:59 A.m..1,ACS09_5yr_B08132010s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 9:00 A.m. to 9:59 A.m..1,ACS09_5yr_B08132011s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 10:00 A.m. to 10:59 A.m..1,ACS09_5yr_B08132012s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 11:00 A.m. to 11:59 A.m..1,ACS09_5yr_B08132013s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 12:00 P.m. to 3:59 P.m..1,ACS09_5yr_B08132014s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 4:00 P.m. to 11:59 P.m..1,ACS09_5yr_B08132015s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08132016s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 12:00 A.m. to 4:59 A.m.",ACS09_5yr_B08132017s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 5:00 A.m. to 5:29 A.m.",ACS09_5yr_B08132018s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 5:30 A.m. to 5:59 A.m.",ACS09_5yr_B08132019s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 6:00 A.m. to 6:29 A.m.",ACS09_5yr_B08132020s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 6:30 A.m. to 6:59 A.m.",ACS09_5yr_B08132021s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 7:00 A.m. to 7:29 A.m.",ACS09_5yr_B08132022s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 7:30 A.m. to 7:59 A.m.",ACS09_5yr_B08132023s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 8:00 A.m. to 8:29 A.m.",ACS09_5yr_B08132024s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 8:30 A.m. to 8:59 A.m.",ACS09_5yr_B08132025s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 9:00 A.m. to 9:59 A.m.",ACS09_5yr_B08132026s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 10:00 A.m. to 10:59 A.m.",ACS09_5yr_B08132027s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 11:00 A.m. to 11:59 A.m.",ACS09_5yr_B08132028s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 12:00 P.m. to 3:59 P.m.",ACS09_5yr_B08132029s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 4:00 P.m. to 11:59 P.m.",ACS09_5yr_B08132030s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled",ACS09_5yr_B08132031s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 12:00 A.m. to 4:59 A.m.",ACS09_5yr_B08132032s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 5:00 A.m. to 5:29 A.m.",ACS09_5yr_B08132033s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 5:30 A.m. to 5:59 A.m.",ACS09_5yr_B08132034s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 6:00 A.m. to 6:29 A.m.",ACS09_5yr_B08132035s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 6:30 A.m. to 6:59 A.m.",ACS09_5yr_B08132036s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 7:00 A.m. to 7:29 A.m.",ACS09_5yr_B08132037s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 7:30 A.m. to 7:59 A.m.",ACS09_5yr_B08132038s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 8:00 A.m. to 8:29 A.m.",ACS09_5yr_B08132039s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 8:30 A.m. to 8:59 A.m.",ACS09_5yr_B08132040s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 9:00 A.m. to 9:59 A.m.",ACS09_5yr_B08132041s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 10:00 A.m. to 10:59 A.m.",ACS09_5yr_B08132042s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 11:00 A.m. to 11:59 A.m.",ACS09_5yr_B08132043s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 12:00 P.m. to 3:59 P.m.",ACS09_5yr_B08132044s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 4:00 P.m. to 11:59 P.m.",ACS09_5yr_B08132045s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab),ACS09_5yr_B08132046s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08132047s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08132048s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08132049s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08132050s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08132051s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08132052s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08132053s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08132054s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08132055s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08132056s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08132057s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08132058s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08132059s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08132060s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked,ACS09_5yr_B08132061s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08132062s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08132063s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08132064s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08132065s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08132066s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08132067s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08132068s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08132069s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08132070s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08132071s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08132072s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08132073s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08132074s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Walked: 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08132075s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08132076s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 12:00 A.m. to 4:59 A.m.",ACS09_5yr_B08132077s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 5:00 A.m. to 5:29 A.m.",ACS09_5yr_B08132078s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 5:30 A.m. to 5:59 A.m.",ACS09_5yr_B08132079s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 6:00 A.m. to 6:29 A.m.",ACS09_5yr_B08132080s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 6:30 A.m. to 6:59 A.m.",ACS09_5yr_B08132081s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 7:00 A.m. to 7:29 A.m.",ACS09_5yr_B08132082s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 7:30 A.m. to 7:59 A.m.",ACS09_5yr_B08132083s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 8:00 A.m. to 8:29 A.m.",ACS09_5yr_B08132084s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 8:30 A.m. to 8:59 A.m.",ACS09_5yr_B08132085s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 9:00 A.m. to 9:59 A.m.",ACS09_5yr_B08132086s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 10:00 A.m. to 10:59 A.m.",ACS09_5yr_B08132087s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 11:00 A.m. to 11:59 A.m.",ACS09_5yr_B08132088s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 12:00 P.m. to 3:59 P.m.",ACS09_5yr_B08132089s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 4:00 P.m. to 11:59 P.m.",ACS09_5yr_B08132090s
% Workers 16 Years and Over Who Did Not Work At Home: 12:00 A.m. to 4:59 A.m..1,PCT_ACS09_5yr_B08132002
% Workers 16 Years and Over Who Did Not Work At Home: 5:00 A.m. to 5:29 A.m..1,PCT_ACS09_5yr_B08132003
% Workers 16 Years and Over Who Did Not Work At Home: 5:30 A.m. to 5:59 A.m..1,PCT_ACS09_5yr_B08132004
% Workers 16 Years and Over Who Did Not Work At Home: 6:00 A.m. to 6:29 A.m..1,PCT_ACS09_5yr_B08132005
% Workers 16 Years and Over Who Did Not Work At Home: 6:30 A.m. to 6:59 A.m..1,PCT_ACS09_5yr_B08132006
% Workers 16 Years and Over Who Did Not Work At Home: 7:00 A.m. to 7:29 A.m..1,PCT_ACS09_5yr_B08132007
% Workers 16 Years and Over Who Did Not Work At Home: 7:30 A.m. to 7:59 A.m..1,PCT_ACS09_5yr_B08132008
% Workers 16 Years and Over Who Did Not Work At Home: 8:00 A.m. to 8:29 A.m..1,PCT_ACS09_5yr_B08132009
% Workers 16 Years and Over Who Did Not Work At Home: 8:30 A.m. to 8:59 A.m..1,PCT_ACS09_5yr_B08132010
% Workers 16 Years and Over Who Did Not Work At Home: 9:00 A.m. to 9:59 A.m..1,PCT_ACS09_5yr_B08132011
% Workers 16 Years and Over Who Did Not Work At Home: 10:00 A.m. to 10:59 A.m..1,PCT_ACS09_5yr_B08132012
% Workers 16 Years and Over Who Did Not Work At Home: 11:00 A.m. to 11:59 A.m..1,PCT_ACS09_5yr_B08132013
% Workers 16 Years and Over Who Did Not Work At Home: 12:00 P.m. to 3:59 P.m..1,PCT_ACS09_5yr_B08132014
% Workers 16 Years and Over Who Did Not Work At Home: 4:00 P.m. to 11:59 P.m..1,PCT_ACS09_5yr_B08132015
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08132016
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 12:00 A.m. to 4:59 A.m.",PCT_ACS09_5yr_B08132017
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 5:00 A.m. to 5:29 A.m.",PCT_ACS09_5yr_B08132018
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 5:30 A.m. to 5:59 A.m.",PCT_ACS09_5yr_B08132019
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 6:00 A.m. to 6:29 A.m.",PCT_ACS09_5yr_B08132020
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 6:30 A.m. to 6:59 A.m.",PCT_ACS09_5yr_B08132021
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 7:00 A.m. to 7:29 A.m.",PCT_ACS09_5yr_B08132022
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 7:30 A.m. to 7:59 A.m.",PCT_ACS09_5yr_B08132023
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 8:00 A.m. to 8:29 A.m.",PCT_ACS09_5yr_B08132024
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 8:30 A.m. to 8:59 A.m.",PCT_ACS09_5yr_B08132025
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 9:00 A.m. to 9:59 A.m.",PCT_ACS09_5yr_B08132026
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 10:00 A.m. to 10:59 A.m.",PCT_ACS09_5yr_B08132027
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 11:00 A.m. to 11:59 A.m.",PCT_ACS09_5yr_B08132028
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 12:00 P.m. to 3:59 P.m.",PCT_ACS09_5yr_B08132029
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 4:00 P.m. to 11:59 P.m.",PCT_ACS09_5yr_B08132030
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08132031
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 12:00 A.m. to 4:59 A.m.",PCT_ACS09_5yr_B08132032
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 5:00 A.m. to 5:29 A.m.",PCT_ACS09_5yr_B08132033
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 5:30 A.m. to 5:59 A.m.",PCT_ACS09_5yr_B08132034
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 6:00 A.m. to 6:29 A.m.",PCT_ACS09_5yr_B08132035
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 6:30 A.m. to 6:59 A.m.",PCT_ACS09_5yr_B08132036
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 7:00 A.m. to 7:29 A.m.",PCT_ACS09_5yr_B08132037
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 7:30 A.m. to 7:59 A.m.",PCT_ACS09_5yr_B08132038
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 8:00 A.m. to 8:29 A.m.",PCT_ACS09_5yr_B08132039
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 8:30 A.m. to 8:59 A.m.",PCT_ACS09_5yr_B08132040
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 9:00 A.m. to 9:59 A.m.",PCT_ACS09_5yr_B08132041
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 10:00 A.m. to 10:59 A.m.",PCT_ACS09_5yr_B08132042
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 11:00 A.m. to 11:59 A.m.",PCT_ACS09_5yr_B08132043
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 12:00 P.m. to 3:59 P.m.",PCT_ACS09_5yr_B08132044
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 4:00 P.m. to 11:59 P.m.",PCT_ACS09_5yr_B08132045
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08132046
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 12:00 A.m. to 4:59 A.m.,PCT_ACS09_5yr_B08132047
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 5:00 A.m. to 5:29 A.m.,PCT_ACS09_5yr_B08132048
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 5:30 A.m. to 5:59 A.m.,PCT_ACS09_5yr_B08132049
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 6:00 A.m. to 6:29 A.m.,PCT_ACS09_5yr_B08132050
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 6:30 A.m. to 6:59 A.m.,PCT_ACS09_5yr_B08132051
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 7:00 A.m. to 7:29 A.m.,PCT_ACS09_5yr_B08132052
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 7:30 A.m. to 7:59 A.m.,PCT_ACS09_5yr_B08132053
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 8:00 A.m. to 8:29 A.m.,PCT_ACS09_5yr_B08132054
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 8:30 A.m. to 8:59 A.m.,PCT_ACS09_5yr_B08132055
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 9:00 A.m. to 9:59 A.m.,PCT_ACS09_5yr_B08132056
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 10:00 A.m. to 10:59 A.m.,PCT_ACS09_5yr_B08132057
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 11:00 A.m. to 11:59 A.m.,PCT_ACS09_5yr_B08132058
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 12:00 P.m. to 3:59 P.m.,PCT_ACS09_5yr_B08132059
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 4:00 P.m. to 11:59 P.m.,PCT_ACS09_5yr_B08132060
% Workers 16 Years and Over Who Did Not Work At Home: Walked,PCT_ACS09_5yr_B08132061
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 12:00 A.m. to 4:59 A.m.,PCT_ACS09_5yr_B08132062
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 5:00 A.m. to 5:29 A.m.,PCT_ACS09_5yr_B08132063
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 5:30 A.m. to 5:59 A.m.,PCT_ACS09_5yr_B08132064
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 6:00 A.m. to 6:29 A.m.,PCT_ACS09_5yr_B08132065
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 6:30 A.m. to 6:59 A.m.,PCT_ACS09_5yr_B08132066
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 7:00 A.m. to 7:29 A.m.,PCT_ACS09_5yr_B08132067
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 7:30 A.m. to 7:59 A.m.,PCT_ACS09_5yr_B08132068
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 8:00 A.m. to 8:29 A.m.,PCT_ACS09_5yr_B08132069
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 8:30 A.m. to 8:59 A.m.,PCT_ACS09_5yr_B08132070
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 9:00 A.m. to 9:59 A.m.,PCT_ACS09_5yr_B08132071
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 10:00 A.m. to 10:59 A.m.,PCT_ACS09_5yr_B08132072
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 11:00 A.m. to 11:59 A.m.,PCT_ACS09_5yr_B08132073
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 12:00 P.m. to 3:59 P.m.,PCT_ACS09_5yr_B08132074
% Workers 16 Years and Over Who Did Not Work At Home: Walked: 4:00 P.m. to 11:59 P.m.,PCT_ACS09_5yr_B08132075
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08132076
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 12:00 A.m. to 4:59 A.m.",PCT_ACS09_5yr_B08132077
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 5:00 A.m. to 5:29 A.m.",PCT_ACS09_5yr_B08132078
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 5:30 A.m. to 5:59 A.m.",PCT_ACS09_5yr_B08132079
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 6:00 A.m. to 6:29 A.m.",PCT_ACS09_5yr_B08132080
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 6:30 A.m. to 6:59 A.m.",PCT_ACS09_5yr_B08132081
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 7:00 A.m. to 7:29 A.m.",PCT_ACS09_5yr_B08132082
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 7:30 A.m. to 7:59 A.m.",PCT_ACS09_5yr_B08132083
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 8:00 A.m. to 8:29 A.m.",PCT_ACS09_5yr_B08132084
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 8:30 A.m. to 8:59 A.m.",PCT_ACS09_5yr_B08132085
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 9:00 A.m. to 9:59 A.m.",PCT_ACS09_5yr_B08132086
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 10:00 A.m. to 10:59 A.m.",PCT_ACS09_5yr_B08132087
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 11:00 A.m. to 11:59 A.m.",PCT_ACS09_5yr_B08132088
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 12:00 P.m. to 3:59 P.m.",PCT_ACS09_5yr_B08132089
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle, or Other Means: 4:00 P.m. to 11:59 P.m.",PCT_ACS09_5yr_B08132090
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes).2,ACS09_5yr_B08133001
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08133002
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08133003
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08133004
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08133005
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08133006
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08133007
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08133008
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08133009
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08133010
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08133011
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08133012
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08133013
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08133014
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08133015
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes).2,ACS09_5yr_B08133001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 12:00 A.m. to 4:59 A.m.,ACS09_5yr_B08133002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 5:00 A.m. to 5:29 A.m.,ACS09_5yr_B08133003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 5:30 A.m. to 5:59 A.m.,ACS09_5yr_B08133004s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 6:00 A.m. to 6:29 A.m.,ACS09_5yr_B08133005s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 6:30 A.m. to 6:59 A.m.,ACS09_5yr_B08133006s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 7:00 A.m. to 7:29 A.m.,ACS09_5yr_B08133007s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 7:30 A.m. to 7:59 A.m.,ACS09_5yr_B08133008s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 8:00 A.m. to 8:29 A.m.,ACS09_5yr_B08133009s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 8:30 A.m. to 8:59 A.m.,ACS09_5yr_B08133010s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 9:00 A.m. to 9:59 A.m.,ACS09_5yr_B08133011s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 10:00 A.m. to 10:59 A.m.,ACS09_5yr_B08133012s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 11:00 A.m. to 11:59 A.m.,ACS09_5yr_B08133013s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 12:00 P.m. to 3:59 P.m.,ACS09_5yr_B08133014s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 4:00 P.m. to 11:59 P.m.,ACS09_5yr_B08133015s
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 12:00 A.m. to 4:59 A.m.,PCT_ACS09_5yr_B08133002
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 5:00 A.m. to 5:29 A.m.,PCT_ACS09_5yr_B08133003
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 5:30 A.m. to 5:59 A.m.,PCT_ACS09_5yr_B08133004
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 6:00 A.m. to 6:29 A.m.,PCT_ACS09_5yr_B08133005
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 6:30 A.m. to 6:59 A.m.,PCT_ACS09_5yr_B08133006
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 7:00 A.m. to 7:29 A.m.,PCT_ACS09_5yr_B08133007
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 7:30 A.m. to 7:59 A.m.,PCT_ACS09_5yr_B08133008
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 8:00 A.m. to 8:29 A.m.,PCT_ACS09_5yr_B08133009
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 8:30 A.m. to 8:59 A.m.,PCT_ACS09_5yr_B08133010
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 9:00 A.m. to 9:59 A.m.,PCT_ACS09_5yr_B08133011
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 10:00 A.m. to 10:59 A.m.,PCT_ACS09_5yr_B08133012
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 11:00 A.m. to 11:59 A.m.,PCT_ACS09_5yr_B08133013
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 12:00 P.m. to 3:59 P.m.,PCT_ACS09_5yr_B08133014
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 4:00 P.m. to 11:59 P.m.,PCT_ACS09_5yr_B08133015
Workers 16 Years and Over Who Did Not Work At Home.3,ACS09_5yr_C08134001
Workers 16 Years and Over Who Did Not Work At Home: Less than 10 Minutes,ACS09_5yr_C08134002
Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.1,ACS09_5yr_C08134003
Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.1,ACS09_5yr_C08134004
Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.1,ACS09_5yr_C08134005
Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.1,ACS09_5yr_C08134006
Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.1,ACS09_5yr_C08134007
Workers 16 Years and Over Who Did Not Work At Home: 35 to 44 Minutes,ACS09_5yr_C08134008
Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.1,ACS09_5yr_C08134009
Workers 16 Years and Over Who Did Not Work At Home: 60 or More Minutes,ACS09_5yr_C08134010
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_C08134011
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: Less than 10 Minutes",ACS09_5yr_C08134012
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 10 to 14 Minutes",ACS09_5yr_C08134013
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 15 to 19 Minutes",ACS09_5yr_C08134014
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 20 to 24 Minutes",ACS09_5yr_C08134015
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 25 to 29 Minutes",ACS09_5yr_C08134016
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 30 to 34 Minutes",ACS09_5yr_C08134017
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 35 to 44 Minutes",ACS09_5yr_C08134018
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 45 to 59 Minutes",ACS09_5yr_C08134019
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 60 or More Minutes",ACS09_5yr_C08134020
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled.1",ACS09_5yr_C08134021
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: Less than 10 Minutes",ACS09_5yr_C08134022
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 10 to 14 Minutes",ACS09_5yr_C08134023
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 15 to 19 Minutes",ACS09_5yr_C08134024
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 20 to 24 Minutes",ACS09_5yr_C08134025
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 25 to 29 Minutes",ACS09_5yr_C08134026
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 30 to 34 Minutes",ACS09_5yr_C08134027
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 35 to 44 Minutes",ACS09_5yr_C08134028
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 45 to 59 Minutes",ACS09_5yr_C08134029
"Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 60 or More Minutes",ACS09_5yr_C08134030
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab).1,ACS09_5yr_C08134031
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): Less than 10 Minutes,ACS09_5yr_C08134032
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 10 to 14 Minutes,ACS09_5yr_C08134033
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 15 to 19 Minutes,ACS09_5yr_C08134034
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 20 to 24 Minutes,ACS09_5yr_C08134035
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 25 to 29 Minutes,ACS09_5yr_C08134036
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 30 to 34 Minutes,ACS09_5yr_C08134037
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 35 to 44 Minutes,ACS09_5yr_C08134038
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 45 to 59 Minutes,ACS09_5yr_C08134039
Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 60 or More Minutes,ACS09_5yr_C08134040
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means",ACS09_5yr_C08134041
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: Less than 10 Minutes",ACS09_5yr_C08134042
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 10 to 14 Minutes",ACS09_5yr_C08134043
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 15 to 19 Minutes",ACS09_5yr_C08134044
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 20 to 24 Minutes",ACS09_5yr_C08134045
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 25 to 29 Minutes",ACS09_5yr_C08134046
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 30 to 34 Minutes",ACS09_5yr_C08134047
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 35 to 44 Minutes",ACS09_5yr_C08134048
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 45 to 59 Minutes",ACS09_5yr_C08134049
"Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 60 or More Minutes",ACS09_5yr_C08134050
Std. Error: Workers 16 Years and Over Who Did Not Work At Home.3,ACS09_5yr_C08134001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Less than 10 Minutes,ACS09_5yr_C08134002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.1,ACS09_5yr_C08134003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.1,ACS09_5yr_C08134004s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.1,ACS09_5yr_C08134005s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.1,ACS09_5yr_C08134006s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.1,ACS09_5yr_C08134007s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 35 to 44 Minutes,ACS09_5yr_C08134008s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.1,ACS09_5yr_C08134009s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 60 or More Minutes,ACS09_5yr_C08134010s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_C08134011s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: Less than 10 Minutes",ACS09_5yr_C08134012s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 10 to 14 Minutes",ACS09_5yr_C08134013s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 15 to 19 Minutes",ACS09_5yr_C08134014s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 20 to 24 Minutes",ACS09_5yr_C08134015s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 25 to 29 Minutes",ACS09_5yr_C08134016s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 30 to 34 Minutes",ACS09_5yr_C08134017s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 35 to 44 Minutes",ACS09_5yr_C08134018s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 45 to 59 Minutes",ACS09_5yr_C08134019s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 60 or More Minutes",ACS09_5yr_C08134020s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled.1",ACS09_5yr_C08134021s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: Less than 10 Minutes",ACS09_5yr_C08134022s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 10 to 14 Minutes",ACS09_5yr_C08134023s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 15 to 19 Minutes",ACS09_5yr_C08134024s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 20 to 24 Minutes",ACS09_5yr_C08134025s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 25 to 29 Minutes",ACS09_5yr_C08134026s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 30 to 34 Minutes",ACS09_5yr_C08134027s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 35 to 44 Minutes",ACS09_5yr_C08134028s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 45 to 59 Minutes",ACS09_5yr_C08134029s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 60 or More Minutes",ACS09_5yr_C08134030s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab).1,ACS09_5yr_C08134031s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): Less than 10 Minutes,ACS09_5yr_C08134032s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 10 to 14 Minutes,ACS09_5yr_C08134033s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 15 to 19 Minutes,ACS09_5yr_C08134034s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 20 to 24 Minutes,ACS09_5yr_C08134035s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 25 to 29 Minutes,ACS09_5yr_C08134036s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 30 to 34 Minutes,ACS09_5yr_C08134037s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 35 to 44 Minutes,ACS09_5yr_C08134038s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 45 to 59 Minutes,ACS09_5yr_C08134039s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 60 or More Minutes,ACS09_5yr_C08134040s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means",ACS09_5yr_C08134041s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: Less than 10 Minutes",ACS09_5yr_C08134042s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 10 to 14 Minutes",ACS09_5yr_C08134043s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 15 to 19 Minutes",ACS09_5yr_C08134044s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 20 to 24 Minutes",ACS09_5yr_C08134045s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 25 to 29 Minutes",ACS09_5yr_C08134046s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 30 to 34 Minutes",ACS09_5yr_C08134047s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 35 to 44 Minutes",ACS09_5yr_C08134048s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 45 to 59 Minutes",ACS09_5yr_C08134049s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 60 or More Minutes",ACS09_5yr_C08134050s
% Workers 16 Years and Over Who Did Not Work At Home: Less than 10 Minutes,PCT_ACS09_5yr_C08134002
% Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.1,PCT_ACS09_5yr_C08134003
% Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.1,PCT_ACS09_5yr_C08134004
% Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.1,PCT_ACS09_5yr_C08134005
% Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.1,PCT_ACS09_5yr_C08134006
% Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.1,PCT_ACS09_5yr_C08134007
% Workers 16 Years and Over Who Did Not Work At Home: 35 to 44 Minutes,PCT_ACS09_5yr_C08134008
% Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.1,PCT_ACS09_5yr_C08134009
% Workers 16 Years and Over Who Did Not Work At Home: 60 or More Minutes,PCT_ACS09_5yr_C08134010
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_C08134011
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: Less than 10 Minutes",PCT_ACS09_5yr_C08134012
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 10 to 14 Minutes",PCT_ACS09_5yr_C08134013
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 15 to 19 Minutes",PCT_ACS09_5yr_C08134014
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 20 to 24 Minutes",PCT_ACS09_5yr_C08134015
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 25 to 29 Minutes",PCT_ACS09_5yr_C08134016
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 30 to 34 Minutes",PCT_ACS09_5yr_C08134017
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 35 to 44 Minutes",PCT_ACS09_5yr_C08134018
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 45 to 59 Minutes",PCT_ACS09_5yr_C08134019
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Drove Alone: 60 or More Minutes",PCT_ACS09_5yr_C08134020
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_C08134021
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: Less than 10 Minutes",PCT_ACS09_5yr_C08134022
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 10 to 14 Minutes",PCT_ACS09_5yr_C08134023
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 15 to 19 Minutes",PCT_ACS09_5yr_C08134024
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 20 to 24 Minutes",PCT_ACS09_5yr_C08134025
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 25 to 29 Minutes",PCT_ACS09_5yr_C08134026
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 30 to 34 Minutes",PCT_ACS09_5yr_C08134027
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 35 to 44 Minutes",PCT_ACS09_5yr_C08134028
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 45 to 59 Minutes",PCT_ACS09_5yr_C08134029
"% Workers 16 Years and Over Who Did Not Work At Home: Car, Truck, or Van - Carpooled: 60 or More Minutes",PCT_ACS09_5yr_C08134030
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_C08134031
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): Less than 10 Minutes,PCT_ACS09_5yr_C08134032
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 10 to 14 Minutes,PCT_ACS09_5yr_C08134033
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 15 to 19 Minutes,PCT_ACS09_5yr_C08134034
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 20 to 24 Minutes,PCT_ACS09_5yr_C08134035
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 25 to 29 Minutes,PCT_ACS09_5yr_C08134036
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 30 to 34 Minutes,PCT_ACS09_5yr_C08134037
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 35 to 44 Minutes,PCT_ACS09_5yr_C08134038
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 45 to 59 Minutes,PCT_ACS09_5yr_C08134039
% Workers 16 Years and Over Who Did Not Work At Home: Public Transportation (Excluding Taxicab): 60 or More Minutes,PCT_ACS09_5yr_C08134040
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means",PCT_ACS09_5yr_C08134041
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: Less than 10 Minutes",PCT_ACS09_5yr_C08134042
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 10 to 14 Minutes",PCT_ACS09_5yr_C08134043
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 15 to 19 Minutes",PCT_ACS09_5yr_C08134044
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 20 to 24 Minutes",PCT_ACS09_5yr_C08134045
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 25 to 29 Minutes",PCT_ACS09_5yr_C08134046
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 30 to 34 Minutes",PCT_ACS09_5yr_C08134047
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 35 to 44 Minutes",PCT_ACS09_5yr_C08134048
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 45 to 59 Minutes",PCT_ACS09_5yr_C08134049
"% Workers 16 Years and Over Who Did Not Work At Home: Taxicab, Motorcycle, Bicycle,  Walked, or Other Means: 60 or More Minutes",PCT_ACS09_5yr_C08134050
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes).3,ACS09_5yr_B08135001
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Less than 10 Minutes,ACS09_5yr_B08135002
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 10 to 14 Minutes,ACS09_5yr_B08135003
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 15 to 19 Minutes,ACS09_5yr_B08135004
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 20 to 24 Minutes,ACS09_5yr_B08135005
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 25 to 29 Minutes,ACS09_5yr_B08135006
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 30 to 34 Minutes,ACS09_5yr_B08135007
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 35 to 44 Minutes,ACS09_5yr_B08135008
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 45 to 59 Minutes,ACS09_5yr_B08135009
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 60 or More Minutes,ACS09_5yr_B08135010
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes).3,ACS09_5yr_B08135001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Less than 10 Minutes,ACS09_5yr_B08135002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 10 to 14 Minutes,ACS09_5yr_B08135003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 15 to 19 Minutes,ACS09_5yr_B08135004s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 20 to 24 Minutes,ACS09_5yr_B08135005s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 25 to 29 Minutes,ACS09_5yr_B08135006s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 30 to 34 Minutes,ACS09_5yr_B08135007s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 35 to 44 Minutes,ACS09_5yr_B08135008s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 45 to 59 Minutes,ACS09_5yr_B08135009s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 60 or More Minutes,ACS09_5yr_B08135010s
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Less than 10 Minutes,PCT_ACS09_5yr_B08135002
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 10 to 14 Minutes,PCT_ACS09_5yr_B08135003
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 15 to 19 Minutes,PCT_ACS09_5yr_B08135004
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 20 to 24 Minutes,PCT_ACS09_5yr_B08135005
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 25 to 29 Minutes,PCT_ACS09_5yr_B08135006
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 30 to 34 Minutes,PCT_ACS09_5yr_B08135007
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 35 to 44 Minutes,PCT_ACS09_5yr_B08135008
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 45 to 59 Minutes,PCT_ACS09_5yr_B08135009
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): 60 or More Minutes,PCT_ACS09_5yr_B08135010
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes).4,ACS09_5yr_C08136001
"Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Car, Truck, or Van - Drove Alone",ACS09_5yr_C08136002
"Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Car, Truck, or Van - Carpooled",ACS09_5yr_C08136003
Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Public Transportation (Excluding Taxicab),ACS09_5yr_C08136004
"Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Taxicab, Motorcycle, Bicycle, Walked, or Other Means",ACS09_5yr_C08136005
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes).4,ACS09_5yr_C08136001s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Car, Truck, or Van - Drove Alone",ACS09_5yr_C08136002s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Car, Truck, or Van - Carpooled",ACS09_5yr_C08136003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Public Transportation (Excluding Taxicab),ACS09_5yr_C08136004s
"Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Taxicab, Motorcycle, Bicycle, Walked, or Other Means",ACS09_5yr_C08136005s
"% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_C08136002
"% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_C08136003
% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_C08136004
"% Workers 16 Years and Over Who Did Not Work At Home: Aggregate Travel Time to Work (in Minutes): Taxicab, Motorcycle, Bicycle, Walked, or Other Means",PCT_ACS09_5yr_C08136005
Workers 16 Years and Over in Households.1,ACS09_5yr_B08137001
Workers 16 Years and Over in Households: Householder Lived in Owner-Occupied Housing Units,ACS09_5yr_B08137002
Workers 16 Years and Over in Households: Householder Lived in Renter-Occupied Housing Units,ACS09_5yr_B08137003
"Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08137004
"Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: Householder Lived in Owner-Occupied Housing Units",ACS09_5yr_B08137005
"Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: Householder Lived in Renter-Occupied Housing Units",ACS09_5yr_B08137006
"Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled",ACS09_5yr_B08137007
"Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: Householder Lived in Owner-Occupied Housing Units",ACS09_5yr_B08137008
"Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: Householder Lived in Renter-Occupied Housing Units",ACS09_5yr_B08137009
Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab),ACS09_5yr_B08137010
Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): Householder Lived in Owner-Occupied Housing Units,ACS09_5yr_B08137011
Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): Householder Lived in Renter-Occupied Housing Units,ACS09_5yr_B08137012
Workers 16 Years and Over in Households: Walked,ACS09_5yr_B08137013
Workers 16 Years and Over in Households: Walked: Householder Lived in Owner-Occupied Housing Units,ACS09_5yr_B08137014
Workers 16 Years and Over in Households: Walked: Householder Lived in Renter-Occupied Housing Units,ACS09_5yr_B08137015
"Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08137016
"Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: Householder Lived in Owner-Occupied Housing Units",ACS09_5yr_B08137017
"Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: Householder Lived in Renter-Occupied Housing Units",ACS09_5yr_B08137018
Workers 16 Years and Over in Households: Worked At Home,ACS09_5yr_B08137019
Workers 16 Years and Over in Households: Worked At Home: Householder Lived in Owner-Occupied Housing Units,ACS09_5yr_B08137020
Workers 16 Years and Over in Households: Worked At Home: Householder Lived in Renter-Occupied Housing Units,ACS09_5yr_B08137021
Std. Error: Workers 16 Years and Over in Households.1,ACS09_5yr_B08137001s
Std. Error: Workers 16 Years and Over in Households: Householder Lived in Owner-Occupied Housing Units,ACS09_5yr_B08137002s
Std. Error: Workers 16 Years and Over in Households: Householder Lived in Renter-Occupied Housing Units,ACS09_5yr_B08137003s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone",ACS09_5yr_B08137004s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: Householder Lived in Owner-Occupied Housing Units",ACS09_5yr_B08137005s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: Householder Lived in Renter-Occupied Housing Units",ACS09_5yr_B08137006s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled",ACS09_5yr_B08137007s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: Householder Lived in Owner-Occupied Housing Units",ACS09_5yr_B08137008s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: Householder Lived in Renter-Occupied Housing Units",ACS09_5yr_B08137009s
Std. Error: Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab),ACS09_5yr_B08137010s
Std. Error: Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): Householder Lived in Owner-Occupied Housing Units,ACS09_5yr_B08137011s
Std. Error: Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): Householder Lived in Renter-Occupied Housing Units,ACS09_5yr_B08137012s
Std. Error: Workers 16 Years and Over in Households: Walked,ACS09_5yr_B08137013s
Std. Error: Workers 16 Years and Over in Households: Walked: Householder Lived in Owner-Occupied Housing Units,ACS09_5yr_B08137014s
Std. Error: Workers 16 Years and Over in Households: Walked: Householder Lived in Renter-Occupied Housing Units,ACS09_5yr_B08137015s
"Std. Error: Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means",ACS09_5yr_B08137016s
"Std. Error: Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: Householder Lived in Owner-Occupied Housing Units",ACS09_5yr_B08137017s
"Std. Error: Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: Householder Lived in Renter-Occupied Housing Units",ACS09_5yr_B08137018s
Std. Error: Workers 16 Years and Over in Households: Worked At Home,ACS09_5yr_B08137019s
Std. Error: Workers 16 Years and Over in Households: Worked At Home: Householder Lived in Owner-Occupied Housing Units,ACS09_5yr_B08137020s
Std. Error: Workers 16 Years and Over in Households: Worked At Home: Householder Lived in Renter-Occupied Housing Units,ACS09_5yr_B08137021s
% Workers 16 Years and Over in Households: Householder Lived in Owner-Occupied Housing Units,PCT_ACS09_5yr_B08137002
% Workers 16 Years and Over in Households: Householder Lived in Renter-Occupied Housing Units,PCT_ACS09_5yr_B08137003
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone",PCT_ACS09_5yr_B08137004
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: Householder Lived in Owner-Occupied Housing Units",PCT_ACS09_5yr_B08137005
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: Householder Lived in Renter-Occupied Housing Units",PCT_ACS09_5yr_B08137006
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled",PCT_ACS09_5yr_B08137007
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: Householder Lived in Owner-Occupied Housing Units",PCT_ACS09_5yr_B08137008
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: Householder Lived in Renter-Occupied Housing Units",PCT_ACS09_5yr_B08137009
% Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab),PCT_ACS09_5yr_B08137010
% Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): Householder Lived in Owner-Occupied Housing Units,PCT_ACS09_5yr_B08137011
% Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): Householder Lived in Renter-Occupied Housing Units,PCT_ACS09_5yr_B08137012
% Workers 16 Years and Over in Households: Walked,PCT_ACS09_5yr_B08137013
% Workers 16 Years and Over in Households: Walked: Householder Lived in Owner-Occupied Housing Units,PCT_ACS09_5yr_B08137014
% Workers 16 Years and Over in Households: Walked: Householder Lived in Renter-Occupied Housing Units,PCT_ACS09_5yr_B08137015
"% Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means",PCT_ACS09_5yr_B08137016
"% Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: Householder Lived in Owner-Occupied Housing Units",PCT_ACS09_5yr_B08137017
"% Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: Householder Lived in Renter-Occupied Housing Units",PCT_ACS09_5yr_B08137018
% Workers 16 Years and Over in Households: Worked At Home,PCT_ACS09_5yr_B08137019
% Workers 16 Years and Over in Households: Worked At Home: Householder Lived in Owner-Occupied Housing Units,PCT_ACS09_5yr_B08137020
% Workers 16 Years and Over in Households: Worked At Home: Householder Lived in Renter-Occupied Housing Units,PCT_ACS09_5yr_B08137021
Workers 16 Years and Over in Households.2,ACS09_5yr_B08141001
Workers 16 Years and Over in Households: No Vehicle Available.1,ACS09_5yr_B08141002
Workers 16 Years and Over in Households: 1 Vehicle Available.1,ACS09_5yr_B08141003
Workers 16 Years and Over in Households: 2 Vehicles Available.1,ACS09_5yr_B08141004
Workers 16 Years and Over in Households: 3 or More Vehicles Available,ACS09_5yr_B08141005
"Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08141006
"Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: No Vehicle Available",ACS09_5yr_B08141007
"Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: 1 Vehicle Available",ACS09_5yr_B08141008
"Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: 2 Vehicles Available",ACS09_5yr_B08141009
"Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: 3 or More Vehicles Available",ACS09_5yr_B08141010
"Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08141011
"Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: No Vehicle Available",ACS09_5yr_B08141012
"Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: 1 Vehicle Available",ACS09_5yr_B08141013
"Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: 2 Vehicles Available",ACS09_5yr_B08141014
"Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: 3 or More Vehicles Available",ACS09_5yr_B08141015
Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08141016
Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): No Vehicle Available,ACS09_5yr_B08141017
Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): 1 Vehicle Available,ACS09_5yr_B08141018
Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): 2 Vehicles Available,ACS09_5yr_B08141019
Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): 3 or More Vehicles Available,ACS09_5yr_B08141020
Workers 16 Years and Over in Households: Walked.1,ACS09_5yr_B08141021
Workers 16 Years and Over in Households: Walked: No Vehicle Available,ACS09_5yr_B08141022
Workers 16 Years and Over in Households: Walked: 1 Vehicle Available,ACS09_5yr_B08141023
Workers 16 Years and Over in Households: Walked: 2 Vehicles Available,ACS09_5yr_B08141024
Workers 16 Years and Over in Households: Walked: 3 or More Vehicles Available,ACS09_5yr_B08141025
"Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08141026
"Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: No Vehicle Available",ACS09_5yr_B08141027
"Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: 1 Vehicle Available",ACS09_5yr_B08141028
"Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: 2 Vehicles Available",ACS09_5yr_B08141029
"Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: 3 or More Vehicles Available",ACS09_5yr_B08141030
Workers 16 Years and Over in Households: Worked At Home.1,ACS09_5yr_B08141031
Workers 16 Years and Over in Households: Worked At Home: No Vehicle Available,ACS09_5yr_B08141032
Workers 16 Years and Over in Households: Worked At Home: 1 Vehicle Available,ACS09_5yr_B08141033
Workers 16 Years and Over in Households: Worked At Home: 2 Vehicles Available,ACS09_5yr_B08141034
Workers 16 Years and Over in Households: Worked At Home: 3 or More Vehicles Available,ACS09_5yr_B08141035
Std. Error: Workers 16 Years and Over in Households.2,ACS09_5yr_B08141001s
Std. Error: Workers 16 Years and Over in Households: No Vehicle Available.1,ACS09_5yr_B08141002s
Std. Error: Workers 16 Years and Over in Households: 1 Vehicle Available.1,ACS09_5yr_B08141003s
Std. Error: Workers 16 Years and Over in Households: 2 Vehicles Available.1,ACS09_5yr_B08141004s
Std. Error: Workers 16 Years and Over in Households: 3 or More Vehicles Available,ACS09_5yr_B08141005s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08141006s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: No Vehicle Available",ACS09_5yr_B08141007s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: 1 Vehicle Available",ACS09_5yr_B08141008s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: 2 Vehicles Available",ACS09_5yr_B08141009s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: 3 or More Vehicles Available",ACS09_5yr_B08141010s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08141011s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: No Vehicle Available",ACS09_5yr_B08141012s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: 1 Vehicle Available",ACS09_5yr_B08141013s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: 2 Vehicles Available",ACS09_5yr_B08141014s
"Std. Error: Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: 3 or More Vehicles Available",ACS09_5yr_B08141015s
Std. Error: Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08141016s
Std. Error: Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): No Vehicle Available,ACS09_5yr_B08141017s
Std. Error: Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): 1 Vehicle Available,ACS09_5yr_B08141018s
Std. Error: Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): 2 Vehicles Available,ACS09_5yr_B08141019s
Std. Error: Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): 3 or More Vehicles Available,ACS09_5yr_B08141020s
Std. Error: Workers 16 Years and Over in Households: Walked.1,ACS09_5yr_B08141021s
Std. Error: Workers 16 Years and Over in Households: Walked: No Vehicle Available,ACS09_5yr_B08141022s
Std. Error: Workers 16 Years and Over in Households: Walked: 1 Vehicle Available,ACS09_5yr_B08141023s
Std. Error: Workers 16 Years and Over in Households: Walked: 2 Vehicles Available,ACS09_5yr_B08141024s
Std. Error: Workers 16 Years and Over in Households: Walked: 3 or More Vehicles Available,ACS09_5yr_B08141025s
"Std. Error: Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08141026s
"Std. Error: Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: No Vehicle Available",ACS09_5yr_B08141027s
"Std. Error: Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: 1 Vehicle Available",ACS09_5yr_B08141028s
"Std. Error: Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: 2 Vehicles Available",ACS09_5yr_B08141029s
"Std. Error: Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: 3 or More Vehicles Available",ACS09_5yr_B08141030s
Std. Error: Workers 16 Years and Over in Households: Worked At Home.1,ACS09_5yr_B08141031s
Std. Error: Workers 16 Years and Over in Households: Worked At Home: No Vehicle Available,ACS09_5yr_B08141032s
Std. Error: Workers 16 Years and Over in Households: Worked At Home: 1 Vehicle Available,ACS09_5yr_B08141033s
Std. Error: Workers 16 Years and Over in Households: Worked At Home: 2 Vehicles Available,ACS09_5yr_B08141034s
Std. Error: Workers 16 Years and Over in Households: Worked At Home: 3 or More Vehicles Available,ACS09_5yr_B08141035s
% Workers 16 Years and Over in Households: No Vehicle Available.1,PCT_ACS09_5yr_B08141002
% Workers 16 Years and Over in Households: 1 Vehicle Available.1,PCT_ACS09_5yr_B08141003
% Workers 16 Years and Over in Households: 2 Vehicles Available.1,PCT_ACS09_5yr_B08141004
% Workers 16 Years and Over in Households: 3 or More Vehicles Available,PCT_ACS09_5yr_B08141005
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08141006
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: No Vehicle Available",PCT_ACS09_5yr_B08141007
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: 1 Vehicle Available",PCT_ACS09_5yr_B08141008
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: 2 Vehicles Available",PCT_ACS09_5yr_B08141009
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Drove Alone: 3 or More Vehicles Available",PCT_ACS09_5yr_B08141010
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08141011
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: No Vehicle Available",PCT_ACS09_5yr_B08141012
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: 1 Vehicle Available",PCT_ACS09_5yr_B08141013
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: 2 Vehicles Available",PCT_ACS09_5yr_B08141014
"% Workers 16 Years and Over in Households: Car, Truck, or Van - Carpooled: 3 or More Vehicles Available",PCT_ACS09_5yr_B08141015
% Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08141016
% Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): No Vehicle Available,PCT_ACS09_5yr_B08141017
% Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): 1 Vehicle Available,PCT_ACS09_5yr_B08141018
% Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): 2 Vehicles Available,PCT_ACS09_5yr_B08141019
% Workers 16 Years and Over in Households: Public Transportation (Excluding Taxicab): 3 or More Vehicles Available,PCT_ACS09_5yr_B08141020
% Workers 16 Years and Over in Households: Walked.1,PCT_ACS09_5yr_B08141021
% Workers 16 Years and Over in Households: Walked: No Vehicle Available,PCT_ACS09_5yr_B08141022
% Workers 16 Years and Over in Households: Walked: 1 Vehicle Available,PCT_ACS09_5yr_B08141023
% Workers 16 Years and Over in Households: Walked: 2 Vehicles Available,PCT_ACS09_5yr_B08141024
% Workers 16 Years and Over in Households: Walked: 3 or More Vehicles Available,PCT_ACS09_5yr_B08141025
"% Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08141026
"% Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: No Vehicle Available",PCT_ACS09_5yr_B08141027
"% Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: 1 Vehicle Available",PCT_ACS09_5yr_B08141028
"% Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: 2 Vehicles Available",PCT_ACS09_5yr_B08141029
"% Workers 16 Years and Over in Households: Taxicab, Motorcycle, Bicycle, or Other Means: 3 or More Vehicles Available",PCT_ACS09_5yr_B08141030
% Workers 16 Years and Over in Households: Worked At Home.1,PCT_ACS09_5yr_B08141031
% Workers 16 Years and Over in Households: Worked At Home: No Vehicle Available,PCT_ACS09_5yr_B08141032
% Workers 16 Years and Over in Households: Worked At Home: 1 Vehicle Available,PCT_ACS09_5yr_B08141033
% Workers 16 Years and Over in Households: Worked At Home: 2 Vehicles Available,PCT_ACS09_5yr_B08141034
% Workers 16 Years and Over in Households: Worked At Home: 3 or More Vehicles Available,PCT_ACS09_5yr_B08141035
Households,ACS09_5yr_B08201001
Households: No Vehicle Available,ACS09_5yr_B08201002
Households: 1 Vehicle Available,ACS09_5yr_B08201003
Households: 2 Vehicles Available,ACS09_5yr_B08201004
Households: 3 Vehicles Available,ACS09_5yr_B08201005
Households: 4 or More Vehicles Available,ACS09_5yr_B08201006
Households: 1-Person Household,ACS09_5yr_B08201007
Households: 1-Person Household: No Vehicle Available,ACS09_5yr_B08201008
Households: 1-Person Household: 1 Vehicle Available,ACS09_5yr_B08201009
Households: 1-Person Household: 2 Vehicles Available,ACS09_5yr_B08201010
Households: 1-Person Household: 3 Vehicles Available,ACS09_5yr_B08201011
Households: 1-Person Household: 4 or More Vehicles Available,ACS09_5yr_B08201012
Households: 2-Person Household,ACS09_5yr_B08201013
Households: 2-Person Household: No Vehicle Available,ACS09_5yr_B08201014
Households: 2-Person Household: 1 Vehicle Available,ACS09_5yr_B08201015
Households: 2-Person Household: 2 Vehicles Available,ACS09_5yr_B08201016
Households: 2-Person Household: 3 Vehicles Available,ACS09_5yr_B08201017
Households: 2-Person Household: 4 or More Vehicles Available,ACS09_5yr_B08201018
Households: 3-Person Household,ACS09_5yr_B08201019
Households: 3-Person Household: No Vehicle Available,ACS09_5yr_B08201020
Households: 3-Person Household: 1 Vehicle Available,ACS09_5yr_B08201021
Households: 3-Person Household: 2 Vehicles Available,ACS09_5yr_B08201022
Households: 3-Person Household: 3 Vehicles Available,ACS09_5yr_B08201023
Households: 3-Person Household: 4 or More Vehicles Available,ACS09_5yr_B08201024
Households: 4-or-More-Person Household,ACS09_5yr_B08201025
Households: 4-or-More-Person Household: No Vehicle Available,ACS09_5yr_B08201026
Households: 4-or-More-Person Household: 1 Vehicle Available,ACS09_5yr_B08201027
Households: 4-or-More-Person Household: 2 Vehicles Available,ACS09_5yr_B08201028
Households: 4-or-More-Person Household: 3 Vehicles Available,ACS09_5yr_B08201029
Households: 4-or-More-Person Household: 4 or More Vehicles Available,ACS09_5yr_B08201030
Std. Error: Households,ACS09_5yr_B08201001s
Std. Error: Households: No Vehicle Available,ACS09_5yr_B08201002s
Std. Error: Households: 1 Vehicle Available,ACS09_5yr_B08201003s
Std. Error: Households: 2 Vehicles Available,ACS09_5yr_B08201004s
Std. Error: Households: 3 Vehicles Available,ACS09_5yr_B08201005s
Std. Error: Households: 4 or More Vehicles Available,ACS09_5yr_B08201006s
Std. Error: Households: 1-Person Household,ACS09_5yr_B08201007s
Std. Error: Households: 1-Person Household: No Vehicle Available,ACS09_5yr_B08201008s
Std. Error: Households: 1-Person Household: 1 Vehicle Available,ACS09_5yr_B08201009s
Std. Error: Households: 1-Person Household: 2 Vehicles Available,ACS09_5yr_B08201010s
Std. Error: Households: 1-Person Household: 3 Vehicles Available,ACS09_5yr_B08201011s
Std. Error: Households: 1-Person Household: 4 or More Vehicles Available,ACS09_5yr_B08201012s
Std. Error: Households: 2-Person Household,ACS09_5yr_B08201013s
Std. Error: Households: 2-Person Household: No Vehicle Available,ACS09_5yr_B08201014s
Std. Error: Households: 2-Person Household: 1 Vehicle Available,ACS09_5yr_B08201015s
Std. Error: Households: 2-Person Household: 2 Vehicles Available,ACS09_5yr_B08201016s
Std. Error: Households: 2-Person Household: 3 Vehicles Available,ACS09_5yr_B08201017s
Std. Error: Households: 2-Person Household: 4 or More Vehicles Available,ACS09_5yr_B08201018s
Std. Error: Households: 3-Person Household,ACS09_5yr_B08201019s
Std. Error: Households: 3-Person Household: No Vehicle Available,ACS09_5yr_B08201020s
Std. Error: Households: 3-Person Household: 1 Vehicle Available,ACS09_5yr_B08201021s
Std. Error: Households: 3-Person Household: 2 Vehicles Available,ACS09_5yr_B08201022s
Std. Error: Households: 3-Person Household: 3 Vehicles Available,ACS09_5yr_B08201023s
Std. Error: Households: 3-Person Household: 4 or More Vehicles Available,ACS09_5yr_B08201024s
Std. Error: Households: 4-or-More-Person Household,ACS09_5yr_B08201025s
Std. Error: Households: 4-or-More-Person Household: No Vehicle Available,ACS09_5yr_B08201026s
Std. Error: Households: 4-or-More-Person Household: 1 Vehicle Available,ACS09_5yr_B08201027s
Std. Error: Households: 4-or-More-Person Household: 2 Vehicles Available,ACS09_5yr_B08201028s
Std. Error: Households: 4-or-More-Person Household: 3 Vehicles Available,ACS09_5yr_B08201029s
Std. Error: Households: 4-or-More-Person Household: 4 or More Vehicles Available,ACS09_5yr_B08201030s
% Households: No Vehicle Available,PCT_ACS09_5yr_B08201002
% Households: 1 Vehicle Available,PCT_ACS09_5yr_B08201003
% Households: 2 Vehicles Available,PCT_ACS09_5yr_B08201004
% Households: 3 Vehicles Available,PCT_ACS09_5yr_B08201005
% Households: 4 or More Vehicles Available,PCT_ACS09_5yr_B08201006
% Households: 1-Person Household,PCT_ACS09_5yr_B08201007
% Households: 1-Person Household: No Vehicle Available,PCT_ACS09_5yr_B08201008
% Households: 1-Person Household: 1 Vehicle Available,PCT_ACS09_5yr_B08201009
% Households: 1-Person Household: 2 Vehicles Available,PCT_ACS09_5yr_B08201010
% Households: 1-Person Household: 3 Vehicles Available,PCT_ACS09_5yr_B08201011
% Households: 1-Person Household: 4 or More Vehicles Available,PCT_ACS09_5yr_B08201012
% Households: 2-Person Household,PCT_ACS09_5yr_B08201013
% Households: 2-Person Household: No Vehicle Available,PCT_ACS09_5yr_B08201014
% Households: 2-Person Household: 1 Vehicle Available,PCT_ACS09_5yr_B08201015
% Households: 2-Person Household: 2 Vehicles Available,PCT_ACS09_5yr_B08201016
% Households: 2-Person Household: 3 Vehicles Available,PCT_ACS09_5yr_B08201017
% Households: 2-Person Household: 4 or More Vehicles Available,PCT_ACS09_5yr_B08201018
% Households: 3-Person Household,PCT_ACS09_5yr_B08201019
% Households: 3-Person Household: No Vehicle Available,PCT_ACS09_5yr_B08201020
% Households: 3-Person Household: 1 Vehicle Available,PCT_ACS09_5yr_B08201021
% Households: 3-Person Household: 2 Vehicles Available,PCT_ACS09_5yr_B08201022
% Households: 3-Person Household: 3 Vehicles Available,PCT_ACS09_5yr_B08201023
% Households: 3-Person Household: 4 or More Vehicles Available,PCT_ACS09_5yr_B08201024
% Households: 4-or-More-Person Household,PCT_ACS09_5yr_B08201025
% Households: 4-or-More-Person Household: No Vehicle Available,PCT_ACS09_5yr_B08201026
% Households: 4-or-More-Person Household: 1 Vehicle Available,PCT_ACS09_5yr_B08201027
% Households: 4-or-More-Person Household: 2 Vehicles Available,PCT_ACS09_5yr_B08201028
% Households: 4-or-More-Person Household: 3 Vehicles Available,PCT_ACS09_5yr_B08201029
% Households: 4-or-More-Person Household: 4 or More Vehicles Available,PCT_ACS09_5yr_B08201030
Households.1,ACS09_5yr_B08202001
Households: No Workers,ACS09_5yr_B08202002
Households: 1 Worker,ACS09_5yr_B08202003
Households: 2 Workers,ACS09_5yr_B08202004
Households: 3 or More Workers,ACS09_5yr_B08202005
Households: 1-Person Household.1,ACS09_5yr_B08202006
Households: 1-Person Household: No Workers,ACS09_5yr_B08202007
Households: 1-Person Household: 1 Worker,ACS09_5yr_B08202008
Households: 2-Person Household.1,ACS09_5yr_B08202009
Households: 2-Person Household: No Workers,ACS09_5yr_B08202010
Households: 2-Person Household: 1 Worker,ACS09_5yr_B08202011
Households: 2-Person Household: 2 Workers,ACS09_5yr_B08202012
Households: 3-Person Household.1,ACS09_5yr_B08202013
Households: 3-Person Household: No Workers,ACS09_5yr_B08202014
Households: 3-Person Household: 1 Worker,ACS09_5yr_B08202015
Households: 3-Person Household: 2 Workers,ACS09_5yr_B08202016
Households: 3-Person Household: 3 Workers,ACS09_5yr_B08202017
Households: 4-or-More-Person Household.1,ACS09_5yr_B08202018
Households: 4-or-More-Person Household: No Workers,ACS09_5yr_B08202019
Households: 4-or-More-Person Household: 1 Worker,ACS09_5yr_B08202020
Households: 4-or-More-Person Household: 2 Workers,ACS09_5yr_B08202021
Households: 4-or-More-Person Household: 3 or More Workers,ACS09_5yr_B08202022
Std. Error: Households.1,ACS09_5yr_B08202001s
Std. Error: Households: No Workers,ACS09_5yr_B08202002s
Std. Error: Households: 1 Worker,ACS09_5yr_B08202003s
Std. Error: Households: 2 Workers,ACS09_5yr_B08202004s
Std. Error: Households: 3 or More Workers,ACS09_5yr_B08202005s
Std. Error: Households: 1-Person Household.1,ACS09_5yr_B08202006s
Std. Error: Households: 1-Person Household: No Workers,ACS09_5yr_B08202007s
Std. Error: Households: 1-Person Household: 1 Worker,ACS09_5yr_B08202008s
Std. Error: Households: 2-Person Household.1,ACS09_5yr_B08202009s
Std. Error: Households: 2-Person Household: No Workers,ACS09_5yr_B08202010s
Std. Error: Households: 2-Person Household: 1 Worker,ACS09_5yr_B08202011s
Std. Error: Households: 2-Person Household: 2 Workers,ACS09_5yr_B08202012s
Std. Error: Households: 3-Person Household.1,ACS09_5yr_B08202013s
Std. Error: Households: 3-Person Household: No Workers,ACS09_5yr_B08202014s
Std. Error: Households: 3-Person Household: 1 Worker,ACS09_5yr_B08202015s
Std. Error: Households: 3-Person Household: 2 Workers,ACS09_5yr_B08202016s
Std. Error: Households: 3-Person Household: 3 Workers,ACS09_5yr_B08202017s
Std. Error: Households: 4-or-More-Person Household.1,ACS09_5yr_B08202018s
Std. Error: Households: 4-or-More-Person Household: No Workers,ACS09_5yr_B08202019s
Std. Error: Households: 4-or-More-Person Household: 1 Worker,ACS09_5yr_B08202020s
Std. Error: Households: 4-or-More-Person Household: 2 Workers,ACS09_5yr_B08202021s
Std. Error: Households: 4-or-More-Person Household: 3 or More Workers,ACS09_5yr_B08202022s
% Households: No Workers,PCT_ACS09_5yr_B08202002
% Households: 1 Worker,PCT_ACS09_5yr_B08202003
% Households: 2 Workers,PCT_ACS09_5yr_B08202004
% Households: 3 or More Workers,PCT_ACS09_5yr_B08202005
% Households: 1-Person Household.1,PCT_ACS09_5yr_B08202006
% Households: 1-Person Household: No Workers,PCT_ACS09_5yr_B08202007
% Households: 1-Person Household: 1 Worker,PCT_ACS09_5yr_B08202008
% Households: 2-Person Household.1,PCT_ACS09_5yr_B08202009
% Households: 2-Person Household: No Workers,PCT_ACS09_5yr_B08202010
% Households: 2-Person Household: 1 Worker,PCT_ACS09_5yr_B08202011
% Households: 2-Person Household: 2 Workers,PCT_ACS09_5yr_B08202012
% Households: 3-Person Household.1,PCT_ACS09_5yr_B08202013
% Households: 3-Person Household: No Workers,PCT_ACS09_5yr_B08202014
% Households: 3-Person Household: 1 Worker,PCT_ACS09_5yr_B08202015
% Households: 3-Person Household: 2 Workers,PCT_ACS09_5yr_B08202016
% Households: 3-Person Household: 3 Workers,PCT_ACS09_5yr_B08202017
% Households: 4-or-More-Person Household.1,PCT_ACS09_5yr_B08202018
% Households: 4-or-More-Person Household: No Workers,PCT_ACS09_5yr_B08202019
% Households: 4-or-More-Person Household: 1 Worker,PCT_ACS09_5yr_B08202020
% Households: 4-or-More-Person Household: 2 Workers,PCT_ACS09_5yr_B08202021
% Households: 4-or-More-Person Household: 3 or More Workers,PCT_ACS09_5yr_B08202022
Households.2,ACS09_5yr_B08203001
Households: No Vehicle Available.1,ACS09_5yr_B08203002
Households: 1 Vehicle Available.1,ACS09_5yr_B08203003
Households: 2 Vehicles Available.1,ACS09_5yr_B08203004
Households: 3 Vehicles Available.1,ACS09_5yr_B08203005
Households: 4 or More Vehicles Available.1,ACS09_5yr_B08203006
Households: No Workers.1,ACS09_5yr_B08203007
Households: No Workers: No Vehicle Available,ACS09_5yr_B08203008
Households: No Workers: 1 Vehicle Available,ACS09_5yr_B08203009
Households: No Workers: 2 Vehicles Available,ACS09_5yr_B08203010
Households: No Workers: 3 Vehicles Available,ACS09_5yr_B08203011
Households: No Workers: 4 or More Vehicles Available,ACS09_5yr_B08203012
Households: 1 Worker.1,ACS09_5yr_B08203013
Households: 1 Worker: No Vehicle Available,ACS09_5yr_B08203014
Households: 1 Worker: 1 Vehicle Available,ACS09_5yr_B08203015
Households: 1 Worker: 2 Vehicles Available,ACS09_5yr_B08203016
Households: 1 Worker: 3 Vehicles Available,ACS09_5yr_B08203017
Households: 1 Worker: 4 or More Vehicles Available,ACS09_5yr_B08203018
Households: 2 Workers.1,ACS09_5yr_B08203019
Households: 2 Workers: No Vehicle Available,ACS09_5yr_B08203020
Households: 2 Workers: 1 Vehicle Available,ACS09_5yr_B08203021
Households: 2 Workers: 2 Vehicles Available,ACS09_5yr_B08203022
Households: 2 Workers: 3 Vehicles Available,ACS09_5yr_B08203023
Households: 2 Workers: 4 or More Vehicles Available,ACS09_5yr_B08203024
Households: 3 or More Workers.1,ACS09_5yr_B08203025
Households: 3 or More Workers: No Vehicle Available,ACS09_5yr_B08203026
Households: 3 or More Workers: 1 Vehicle Available,ACS09_5yr_B08203027
Households: 3 or More Workers: 2 Vehicles Available,ACS09_5yr_B08203028
Households: 3 or More Workers: 3 Vehicles Available,ACS09_5yr_B08203029
Households: 3 or More Workers: 4 or More Vehicles Available,ACS09_5yr_B08203030
Std. Error: Households.2,ACS09_5yr_B08203001s
Std. Error: Households: No Vehicle Available.1,ACS09_5yr_B08203002s
Std. Error: Households: 1 Vehicle Available.1,ACS09_5yr_B08203003s
Std. Error: Households: 2 Vehicles Available.1,ACS09_5yr_B08203004s
Std. Error: Households: 3 Vehicles Available.1,ACS09_5yr_B08203005s
Std. Error: Households: 4 or More Vehicles Available.1,ACS09_5yr_B08203006s
Std. Error: Households: No Workers.1,ACS09_5yr_B08203007s
Std. Error: Households: No Workers: No Vehicle Available,ACS09_5yr_B08203008s
Std. Error: Households: No Workers: 1 Vehicle Available,ACS09_5yr_B08203009s
Std. Error: Households: No Workers: 2 Vehicles Available,ACS09_5yr_B08203010s
Std. Error: Households: No Workers: 3 Vehicles Available,ACS09_5yr_B08203011s
Std. Error: Households: No Workers: 4 or More Vehicles Available,ACS09_5yr_B08203012s
Std. Error: Households: 1 Worker.1,ACS09_5yr_B08203013s
Std. Error: Households: 1 Worker: No Vehicle Available,ACS09_5yr_B08203014s
Std. Error: Households: 1 Worker: 1 Vehicle Available,ACS09_5yr_B08203015s
Std. Error: Households: 1 Worker: 2 Vehicles Available,ACS09_5yr_B08203016s
Std. Error: Households: 1 Worker: 3 Vehicles Available,ACS09_5yr_B08203017s
Std. Error: Households: 1 Worker: 4 or More Vehicles Available,ACS09_5yr_B08203018s
Std. Error: Households: 2 Workers.1,ACS09_5yr_B08203019s
Std. Error: Households: 2 Workers: No Vehicle Available,ACS09_5yr_B08203020s
Std. Error: Households: 2 Workers: 1 Vehicle Available,ACS09_5yr_B08203021s
Std. Error: Households: 2 Workers: 2 Vehicles Available,ACS09_5yr_B08203022s
Std. Error: Households: 2 Workers: 3 Vehicles Available,ACS09_5yr_B08203023s
Std. Error: Households: 2 Workers: 4 or More Vehicles Available,ACS09_5yr_B08203024s
Std. Error: Households: 3 or More Workers.1,ACS09_5yr_B08203025s
Std. Error: Households: 3 or More Workers: No Vehicle Available,ACS09_5yr_B08203026s
Std. Error: Households: 3 or More Workers: 1 Vehicle Available,ACS09_5yr_B08203027s
Std. Error: Households: 3 or More Workers: 2 Vehicles Available,ACS09_5yr_B08203028s
Std. Error: Households: 3 or More Workers: 3 Vehicles Available,ACS09_5yr_B08203029s
Std. Error: Households: 3 or More Workers: 4 or More Vehicles Available,ACS09_5yr_B08203030s
% Households: No Vehicle Available.1,PCT_ACS09_5yr_B08203002
% Households: 1 Vehicle Available.1,PCT_ACS09_5yr_B08203003
% Households: 2 Vehicles Available.1,PCT_ACS09_5yr_B08203004
% Households: 3 Vehicles Available.1,PCT_ACS09_5yr_B08203005
% Households: 4 or More Vehicles Available.1,PCT_ACS09_5yr_B08203006
% Households: No Workers.1,PCT_ACS09_5yr_B08203007
% Households: No Workers: No Vehicle Available,PCT_ACS09_5yr_B08203008
% Households: No Workers: 1 Vehicle Available,PCT_ACS09_5yr_B08203009
% Households: No Workers: 2 Vehicles Available,PCT_ACS09_5yr_B08203010
% Households: No Workers: 3 Vehicles Available,PCT_ACS09_5yr_B08203011
% Households: No Workers: 4 or More Vehicles Available,PCT_ACS09_5yr_B08203012
% Households: 1 Worker.1,PCT_ACS09_5yr_B08203013
% Households: 1 Worker: No Vehicle Available,PCT_ACS09_5yr_B08203014
% Households: 1 Worker: 1 Vehicle Available,PCT_ACS09_5yr_B08203015
% Households: 1 Worker: 2 Vehicles Available,PCT_ACS09_5yr_B08203016
% Households: 1 Worker: 3 Vehicles Available,PCT_ACS09_5yr_B08203017
% Households: 1 Worker: 4 or More Vehicles Available,PCT_ACS09_5yr_B08203018
% Households: 2 Workers.1,PCT_ACS09_5yr_B08203019
% Households: 2 Workers: No Vehicle Available,PCT_ACS09_5yr_B08203020
% Households: 2 Workers: 1 Vehicle Available,PCT_ACS09_5yr_B08203021
% Households: 2 Workers: 2 Vehicles Available,PCT_ACS09_5yr_B08203022
% Households: 2 Workers: 3 Vehicles Available,PCT_ACS09_5yr_B08203023
% Households: 2 Workers: 4 or More Vehicles Available,PCT_ACS09_5yr_B08203024
% Households: 3 or More Workers.1,PCT_ACS09_5yr_B08203025
% Households: 3 or More Workers: No Vehicle Available,PCT_ACS09_5yr_B08203026
% Households: 3 or More Workers: 1 Vehicle Available,PCT_ACS09_5yr_B08203027
% Households: 3 or More Workers: 2 Vehicles Available,PCT_ACS09_5yr_B08203028
% Households: 3 or More Workers: 3 Vehicles Available,PCT_ACS09_5yr_B08203029
% Households: 3 or More Workers: 4 or More Vehicles Available,PCT_ACS09_5yr_B08203030
Workers 16 Years and Over.11,ACS09_5yr_B08301001
"Workers 16 Years and Over: Car, Truck, or Van.1",ACS09_5yr_B08301002
"Workers 16 Years and Over: Car, Truck, or Van: Drove Alone.1",ACS09_5yr_B08301003
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled.1",ACS09_5yr_B08301004
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 2-Person Carpool.1",ACS09_5yr_B08301005
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 3-Person Carpool.1",ACS09_5yr_B08301006
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 4-Person Carpool",ACS09_5yr_B08301007
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 5- or 6-Person Carpool",ACS09_5yr_B08301008
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 7-or-More-Person Carpool",ACS09_5yr_B08301009
Workers 16 Years and Over: Public Transportation (Excluding Taxicab).7,ACS09_5yr_B08301010
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Bus or Trolley Bus,ACS09_5yr_B08301011
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico),ACS09_5yr_B08301012
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Subway or Elevated,ACS09_5yr_B08301013
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Railroad,ACS09_5yr_B08301014
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Ferryboat,ACS09_5yr_B08301015
Workers 16 Years and Over: Taxicab,ACS09_5yr_B08301016
Workers 16 Years and Over: Motorcycle,ACS09_5yr_B08301017
Workers 16 Years and Over: Bicycle,ACS09_5yr_B08301018
Workers 16 Years and Over: Walked.7,ACS09_5yr_B08301019
Workers 16 Years and Over: Other Means,ACS09_5yr_B08301020
Workers 16 Years and Over: Worked At Home.7,ACS09_5yr_B08301021
Std. Error: Workers 16 Years and Over.11,ACS09_5yr_B08301001s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van.1",ACS09_5yr_B08301002s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Drove Alone.1",ACS09_5yr_B08301003s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled.1",ACS09_5yr_B08301004s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 2-Person Carpool.1",ACS09_5yr_B08301005s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 3-Person Carpool.1",ACS09_5yr_B08301006s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 4-Person Carpool",ACS09_5yr_B08301007s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 5- or 6-Person Carpool",ACS09_5yr_B08301008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 7-or-More-Person Carpool",ACS09_5yr_B08301009s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab).7,ACS09_5yr_B08301010s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Bus or Trolley Bus,ACS09_5yr_B08301011s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico),ACS09_5yr_B08301012s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Subway or Elevated,ACS09_5yr_B08301013s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Railroad,ACS09_5yr_B08301014s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Ferryboat,ACS09_5yr_B08301015s
Std. Error: Workers 16 Years and Over: Taxicab,ACS09_5yr_B08301016s
Std. Error: Workers 16 Years and Over: Motorcycle,ACS09_5yr_B08301017s
Std. Error: Workers 16 Years and Over: Bicycle,ACS09_5yr_B08301018s
Std. Error: Workers 16 Years and Over: Walked.7,ACS09_5yr_B08301019s
Std. Error: Workers 16 Years and Over: Other Means,ACS09_5yr_B08301020s
Std. Error: Workers 16 Years and Over: Worked At Home.7,ACS09_5yr_B08301021s
"% Workers 16 Years and Over: Car, Truck, or Van.1",PCT_ACS09_5yr_B08301002
"% Workers 16 Years and Over: Car, Truck, or Van: Drove Alone.1",PCT_ACS09_5yr_B08301003
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled.1",PCT_ACS09_5yr_B08301004
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 2-Person Carpool.1",PCT_ACS09_5yr_B08301005
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 3-Person Carpool.1",PCT_ACS09_5yr_B08301006
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 4-Person Carpool",PCT_ACS09_5yr_B08301007
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 5- or 6-Person Carpool",PCT_ACS09_5yr_B08301008
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 7-or-More-Person Carpool",PCT_ACS09_5yr_B08301009
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab).7,PCT_ACS09_5yr_B08301010
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Bus or Trolley Bus,PCT_ACS09_5yr_B08301011
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico),PCT_ACS09_5yr_B08301012
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Subway or Elevated,PCT_ACS09_5yr_B08301013
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Railroad,PCT_ACS09_5yr_B08301014
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Ferryboat,PCT_ACS09_5yr_B08301015
% Workers 16 Years and Over: Taxicab,PCT_ACS09_5yr_B08301016
% Workers 16 Years and Over: Motorcycle,PCT_ACS09_5yr_B08301017
% Workers 16 Years and Over: Bicycle,PCT_ACS09_5yr_B08301018
% Workers 16 Years and Over: Walked.7,PCT_ACS09_5yr_B08301019
% Workers 16 Years and Over: Other Means,PCT_ACS09_5yr_B08301020
% Workers 16 Years and Over: Worked At Home.7,PCT_ACS09_5yr_B08301021
Workers 16 Years and Over Who Did Not Work At Home.4,ACS09_5yr_B08302001
Workers 16 Years and Over Who Did Not Work At Home: 12:00 A.m. to 4:59 A.m..2,ACS09_5yr_B08302002
Workers 16 Years and Over Who Did Not Work At Home: 5:00 A.m. to 5:29 A.m..2,ACS09_5yr_B08302003
Workers 16 Years and Over Who Did Not Work At Home: 5:30 A.m. to 5:59 A.m..2,ACS09_5yr_B08302004
Workers 16 Years and Over Who Did Not Work At Home: 6:00 A.m. to 6:29 A.m..2,ACS09_5yr_B08302005
Workers 16 Years and Over Who Did Not Work At Home: 6:30 A.m. to 6:59 A.m..2,ACS09_5yr_B08302006
Workers 16 Years and Over Who Did Not Work At Home: 7:00 A.m. to 7:29 A.m..2,ACS09_5yr_B08302007
Workers 16 Years and Over Who Did Not Work At Home: 7:30 A.m. to 7:59 A.m..2,ACS09_5yr_B08302008
Workers 16 Years and Over Who Did Not Work At Home: 8:00 A.m. to 8:29 A.m..2,ACS09_5yr_B08302009
Workers 16 Years and Over Who Did Not Work At Home: 8:30 A.m. to 8:59 A.m..2,ACS09_5yr_B08302010
Workers 16 Years and Over Who Did Not Work At Home: 9:00 A.m. to 9:59 A.m..2,ACS09_5yr_B08302011
Workers 16 Years and Over Who Did Not Work At Home: 10:00 A.m. to 10:59 A.m..2,ACS09_5yr_B08302012
Workers 16 Years and Over Who Did Not Work At Home: 11:00 A.m. to 11:59 A.m..2,ACS09_5yr_B08302013
Workers 16 Years and Over Who Did Not Work At Home: 12:00 P.m. to 3:59 P.m..2,ACS09_5yr_B08302014
Workers 16 Years and Over Who Did Not Work At Home: 4:00 P.m. to 11:59 P.m..2,ACS09_5yr_B08302015
Std. Error: Workers 16 Years and Over Who Did Not Work At Home.4,ACS09_5yr_B08302001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 12:00 A.m. to 4:59 A.m..2,ACS09_5yr_B08302002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 5:00 A.m. to 5:29 A.m..2,ACS09_5yr_B08302003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 5:30 A.m. to 5:59 A.m..2,ACS09_5yr_B08302004s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 6:00 A.m. to 6:29 A.m..2,ACS09_5yr_B08302005s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 6:30 A.m. to 6:59 A.m..2,ACS09_5yr_B08302006s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 7:00 A.m. to 7:29 A.m..2,ACS09_5yr_B08302007s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 7:30 A.m. to 7:59 A.m..2,ACS09_5yr_B08302008s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 8:00 A.m. to 8:29 A.m..2,ACS09_5yr_B08302009s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 8:30 A.m. to 8:59 A.m..2,ACS09_5yr_B08302010s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 9:00 A.m. to 9:59 A.m..2,ACS09_5yr_B08302011s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 10:00 A.m. to 10:59 A.m..2,ACS09_5yr_B08302012s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 11:00 A.m. to 11:59 A.m..2,ACS09_5yr_B08302013s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 12:00 P.m. to 3:59 P.m..2,ACS09_5yr_B08302014s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 4:00 P.m. to 11:59 P.m..2,ACS09_5yr_B08302015s
% Workers 16 Years and Over Who Did Not Work At Home: 12:00 A.m. to 4:59 A.m..2,PCT_ACS09_5yr_B08302002
% Workers 16 Years and Over Who Did Not Work At Home: 5:00 A.m. to 5:29 A.m..2,PCT_ACS09_5yr_B08302003
% Workers 16 Years and Over Who Did Not Work At Home: 5:30 A.m. to 5:59 A.m..2,PCT_ACS09_5yr_B08302004
% Workers 16 Years and Over Who Did Not Work At Home: 6:00 A.m. to 6:29 A.m..2,PCT_ACS09_5yr_B08302005
% Workers 16 Years and Over Who Did Not Work At Home: 6:30 A.m. to 6:59 A.m..2,PCT_ACS09_5yr_B08302006
% Workers 16 Years and Over Who Did Not Work At Home: 7:00 A.m. to 7:29 A.m..2,PCT_ACS09_5yr_B08302007
% Workers 16 Years and Over Who Did Not Work At Home: 7:30 A.m. to 7:59 A.m..2,PCT_ACS09_5yr_B08302008
% Workers 16 Years and Over Who Did Not Work At Home: 8:00 A.m. to 8:29 A.m..2,PCT_ACS09_5yr_B08302009
% Workers 16 Years and Over Who Did Not Work At Home: 8:30 A.m. to 8:59 A.m..2,PCT_ACS09_5yr_B08302010
% Workers 16 Years and Over Who Did Not Work At Home: 9:00 A.m. to 9:59 A.m..2,PCT_ACS09_5yr_B08302011
% Workers 16 Years and Over Who Did Not Work At Home: 10:00 A.m. to 10:59 A.m..2,PCT_ACS09_5yr_B08302012
% Workers 16 Years and Over Who Did Not Work At Home: 11:00 A.m. to 11:59 A.m..2,PCT_ACS09_5yr_B08302013
% Workers 16 Years and Over Who Did Not Work At Home: 12:00 P.m. to 3:59 P.m..2,PCT_ACS09_5yr_B08302014
% Workers 16 Years and Over Who Did Not Work At Home: 4:00 P.m. to 11:59 P.m..2,PCT_ACS09_5yr_B08302015
Workers 16 Years and Over Who Did Not Work At Home.5,ACS09_5yr_B08303001
Workers 16 Years and Over Who Did Not Work At Home: Less than 5 Minutes.1,ACS09_5yr_B08303002
Workers 16 Years and Over Who Did Not Work At Home: 5 to 9 Minutes.1,ACS09_5yr_B08303003
Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.2,ACS09_5yr_B08303004
Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.2,ACS09_5yr_B08303005
Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.2,ACS09_5yr_B08303006
Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.2,ACS09_5yr_B08303007
Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.2,ACS09_5yr_B08303008
Workers 16 Years and Over Who Did Not Work At Home: 35 to 39 Minutes.1,ACS09_5yr_B08303009
Workers 16 Years and Over Who Did Not Work At Home: 40 to 44 Minutes.1,ACS09_5yr_B08303010
Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.2,ACS09_5yr_B08303011
Workers 16 Years and Over Who Did Not Work At Home: 60 to 89 Minutes.1,ACS09_5yr_B08303012
Workers 16 Years and Over Who Did Not Work At Home: 90 or More Minutes.1,ACS09_5yr_B08303013
Std. Error: Workers 16 Years and Over Who Did Not Work At Home.5,ACS09_5yr_B08303001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Less than 5 Minutes.1,ACS09_5yr_B08303002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 5 to 9 Minutes.1,ACS09_5yr_B08303003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.2,ACS09_5yr_B08303004s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.2,ACS09_5yr_B08303005s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.2,ACS09_5yr_B08303006s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.2,ACS09_5yr_B08303007s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.2,ACS09_5yr_B08303008s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 35 to 39 Minutes.1,ACS09_5yr_B08303009s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 40 to 44 Minutes.1,ACS09_5yr_B08303010s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.2,ACS09_5yr_B08303011s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 60 to 89 Minutes.1,ACS09_5yr_B08303012s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 90 or More Minutes.1,ACS09_5yr_B08303013s
% Workers 16 Years and Over Who Did Not Work At Home: Less than 5 Minutes.1,PCT_ACS09_5yr_B08303002
% Workers 16 Years and Over Who Did Not Work At Home: 5 to 9 Minutes.1,PCT_ACS09_5yr_B08303003
% Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.2,PCT_ACS09_5yr_B08303004
% Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.2,PCT_ACS09_5yr_B08303005
% Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.2,PCT_ACS09_5yr_B08303006
% Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.2,PCT_ACS09_5yr_B08303007
% Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.2,PCT_ACS09_5yr_B08303008
% Workers 16 Years and Over Who Did Not Work At Home: 35 to 39 Minutes.1,PCT_ACS09_5yr_B08303009
% Workers 16 Years and Over Who Did Not Work At Home: 40 to 44 Minutes.1,PCT_ACS09_5yr_B08303010
% Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.2,PCT_ACS09_5yr_B08303011
% Workers 16 Years and Over Who Did Not Work At Home: 60 to 89 Minutes.1,PCT_ACS09_5yr_B08303012
% Workers 16 Years and Over Who Did Not Work At Home: 90 or More Minutes.1,PCT_ACS09_5yr_B08303013
Workers 16 Years and Over.12,ACS09_5yr_B08406001
"Workers 16 Years and Over: Car, Truck, or Van.2",ACS09_5yr_B08406002
"Workers 16 Years and Over: Car, Truck, or Van: Drove Alone.2",ACS09_5yr_B08406003
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled.2",ACS09_5yr_B08406004
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 2-Person Carpool.2",ACS09_5yr_B08406005
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 3-Person Carpool.2",ACS09_5yr_B08406006
"Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool.1",ACS09_5yr_B08406007
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab).1",ACS09_5yr_B08406008
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Bus or Trolley Bus.1",ACS09_5yr_B08406009
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico).1",ACS09_5yr_B08406010
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Subway or Elevated.1",ACS09_5yr_B08406011
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Railroad.1",ACS09_5yr_B08406012
"Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Ferryboat.1",ACS09_5yr_B08406013
"Workers 16 Years and Over: Car, Truck, or Van: Bicycle.1",ACS09_5yr_B08406014
"Workers 16 Years and Over: Car, Truck, or Van: Walked.1",ACS09_5yr_B08406015
"Workers 16 Years and Over: Car, Truck, or Van: Taxicab, Motorcycle, or Other Means.1",ACS09_5yr_B08406016
"Workers 16 Years and Over: Car, Truck, or Van: Worked At Home.1",ACS09_5yr_B08406017
Workers 16 Years and Over: Male.4,ACS09_5yr_B08406018
"Workers 16 Years and Over: Male: Car, Truck, or Van.1",ACS09_5yr_B08406019
"Workers 16 Years and Over: Male: Car, Truck, or Van: Drove Alone.1",ACS09_5yr_B08406020
"Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled.1",ACS09_5yr_B08406021
"Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 2-Person Carpool.1",ACS09_5yr_B08406022
"Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 3-Person Carpool.1",ACS09_5yr_B08406023
"Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool.1",ACS09_5yr_B08406024
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08406025
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Bus or Trolley Bus.1,ACS09_5yr_B08406026
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico).1,ACS09_5yr_B08406027
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Subway or Elevated.1,ACS09_5yr_B08406028
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Railroad.1,ACS09_5yr_B08406029
Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Ferryboat.1,ACS09_5yr_B08406030
Workers 16 Years and Over: Male: Bicycle.1,ACS09_5yr_B08406031
Workers 16 Years and Over: Male: Walked.1,ACS09_5yr_B08406032
"Workers 16 Years and Over: Male: Taxicab, Motorcycle, or Other Means.1",ACS09_5yr_B08406033
Workers 16 Years and Over: Male: Worked At Home.1,ACS09_5yr_B08406034
Workers 16 Years and Over: Female.4,ACS09_5yr_B08406035
"Workers 16 Years and Over: Female: Car, Truck, or Van.1",ACS09_5yr_B08406036
"Workers 16 Years and Over: Female: Car, Truck, or Van: Drove Alone.1",ACS09_5yr_B08406037
"Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled.1",ACS09_5yr_B08406038
"Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 2-Person Carpool.1",ACS09_5yr_B08406039
"Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 3-Person Carpool.1",ACS09_5yr_B08406040
"Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool.1",ACS09_5yr_B08406041
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08406042
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Bus or Trolley Bus.1,ACS09_5yr_B08406043
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico).1,ACS09_5yr_B08406044
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Subway or Elevated.1,ACS09_5yr_B08406045
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Railroad.1,ACS09_5yr_B08406046
Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Ferryboat.1,ACS09_5yr_B08406047
Workers 16 Years and Over: Female: Bicycle.1,ACS09_5yr_B08406048
Workers 16 Years and Over: Female: Walked.1,ACS09_5yr_B08406049
"Workers 16 Years and Over: Female: Taxicab, Motorcycle, or Other Means.1",ACS09_5yr_B08406050
Workers 16 Years and Over: Female: Worked At Home.1,ACS09_5yr_B08406051
Std. Error: Workers 16 Years and Over.12,ACS09_5yr_B08406001s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van.2",ACS09_5yr_B08406002s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Drove Alone.2",ACS09_5yr_B08406003s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled.2",ACS09_5yr_B08406004s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 2-Person Carpool.2",ACS09_5yr_B08406005s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 3-Person Carpool.2",ACS09_5yr_B08406006s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool.1",ACS09_5yr_B08406007s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab).1",ACS09_5yr_B08406008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Bus or Trolley Bus.1",ACS09_5yr_B08406009s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico).1",ACS09_5yr_B08406010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Subway or Elevated.1",ACS09_5yr_B08406011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Railroad.1",ACS09_5yr_B08406012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Ferryboat.1",ACS09_5yr_B08406013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Bicycle.1",ACS09_5yr_B08406014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Walked.1",ACS09_5yr_B08406015s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Taxicab, Motorcycle, or Other Means.1",ACS09_5yr_B08406016s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van: Worked At Home.1",ACS09_5yr_B08406017s
Std. Error: Workers 16 Years and Over: Male.4,ACS09_5yr_B08406018s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van.1",ACS09_5yr_B08406019s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van: Drove Alone.1",ACS09_5yr_B08406020s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled.1",ACS09_5yr_B08406021s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 2-Person Carpool.1",ACS09_5yr_B08406022s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 3-Person Carpool.1",ACS09_5yr_B08406023s
"Std. Error: Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool.1",ACS09_5yr_B08406024s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08406025s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Bus or Trolley Bus.1,ACS09_5yr_B08406026s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico).1,ACS09_5yr_B08406027s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Subway or Elevated.1,ACS09_5yr_B08406028s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Railroad.1,ACS09_5yr_B08406029s
Std. Error: Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Ferryboat.1,ACS09_5yr_B08406030s
Std. Error: Workers 16 Years and Over: Male: Bicycle.1,ACS09_5yr_B08406031s
Std. Error: Workers 16 Years and Over: Male: Walked.1,ACS09_5yr_B08406032s
"Std. Error: Workers 16 Years and Over: Male: Taxicab, Motorcycle, or Other Means.1",ACS09_5yr_B08406033s
Std. Error: Workers 16 Years and Over: Male: Worked At Home.1,ACS09_5yr_B08406034s
Std. Error: Workers 16 Years and Over: Female.4,ACS09_5yr_B08406035s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van.1",ACS09_5yr_B08406036s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van: Drove Alone.1",ACS09_5yr_B08406037s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled.1",ACS09_5yr_B08406038s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 2-Person Carpool.1",ACS09_5yr_B08406039s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 3-Person Carpool.1",ACS09_5yr_B08406040s
"Std. Error: Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool.1",ACS09_5yr_B08406041s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08406042s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Bus or Trolley Bus.1,ACS09_5yr_B08406043s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico).1,ACS09_5yr_B08406044s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Subway or Elevated.1,ACS09_5yr_B08406045s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Railroad.1,ACS09_5yr_B08406046s
Std. Error: Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Ferryboat.1,ACS09_5yr_B08406047s
Std. Error: Workers 16 Years and Over: Female: Bicycle.1,ACS09_5yr_B08406048s
Std. Error: Workers 16 Years and Over: Female: Walked.1,ACS09_5yr_B08406049s
"Std. Error: Workers 16 Years and Over: Female: Taxicab, Motorcycle, or Other Means.1",ACS09_5yr_B08406050s
Std. Error: Workers 16 Years and Over: Female: Worked At Home.1,ACS09_5yr_B08406051s
"% Workers 16 Years and Over: Car, Truck, or Van.2",PCT_ACS09_5yr_B08406002
"% Workers 16 Years and Over: Car, Truck, or Van: Drove Alone.2",PCT_ACS09_5yr_B08406003
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled.2",PCT_ACS09_5yr_B08406004
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 2-Person Carpool.2",PCT_ACS09_5yr_B08406005
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 3-Person Carpool.2",PCT_ACS09_5yr_B08406006
"% Workers 16 Years and Over: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool.1",PCT_ACS09_5yr_B08406007
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab).1",PCT_ACS09_5yr_B08406008
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Bus or Trolley Bus.1",PCT_ACS09_5yr_B08406009
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico).1",PCT_ACS09_5yr_B08406010
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Subway or Elevated.1",PCT_ACS09_5yr_B08406011
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Railroad.1",PCT_ACS09_5yr_B08406012
"% Workers 16 Years and Over: Car, Truck, or Van: Public Transportation (Excluding Taxicab): Ferryboat.1",PCT_ACS09_5yr_B08406013
"% Workers 16 Years and Over: Car, Truck, or Van: Bicycle.1",PCT_ACS09_5yr_B08406014
"% Workers 16 Years and Over: Car, Truck, or Van: Walked.1",PCT_ACS09_5yr_B08406015
"% Workers 16 Years and Over: Car, Truck, or Van: Taxicab, Motorcycle, or Other Means.1",PCT_ACS09_5yr_B08406016
"% Workers 16 Years and Over: Car, Truck, or Van: Worked At Home.1",PCT_ACS09_5yr_B08406017
% Workers 16 Years and Over: Male.4,PCT_ACS09_5yr_B08406018
"% Workers 16 Years and Over: Male: Car, Truck, or Van.1",PCT_ACS09_5yr_B08406019
"% Workers 16 Years and Over: Male: Car, Truck, or Van: Drove Alone.1",PCT_ACS09_5yr_B08406020
"% Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled.1",PCT_ACS09_5yr_B08406021
"% Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 2-Person Carpool.1",PCT_ACS09_5yr_B08406022
"% Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 3-Person Carpool.1",PCT_ACS09_5yr_B08406023
"% Workers 16 Years and Over: Male: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool.1",PCT_ACS09_5yr_B08406024
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08406025
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Bus or Trolley Bus.1,PCT_ACS09_5yr_B08406026
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico).1,PCT_ACS09_5yr_B08406027
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Subway or Elevated.1,PCT_ACS09_5yr_B08406028
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Railroad.1,PCT_ACS09_5yr_B08406029
% Workers 16 Years and Over: Male: Public Transportation (Excluding Taxicab): Ferryboat.1,PCT_ACS09_5yr_B08406030
% Workers 16 Years and Over: Male: Bicycle.1,PCT_ACS09_5yr_B08406031
% Workers 16 Years and Over: Male: Walked.1,PCT_ACS09_5yr_B08406032
"% Workers 16 Years and Over: Male: Taxicab, Motorcycle, or Other Means.1",PCT_ACS09_5yr_B08406033
% Workers 16 Years and Over: Male: Worked At Home.1,PCT_ACS09_5yr_B08406034
% Workers 16 Years and Over: Female.4,PCT_ACS09_5yr_B08406035
"% Workers 16 Years and Over: Female: Car, Truck, or Van.1",PCT_ACS09_5yr_B08406036
"% Workers 16 Years and Over: Female: Car, Truck, or Van: Drove Alone.1",PCT_ACS09_5yr_B08406037
"% Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled.1",PCT_ACS09_5yr_B08406038
"% Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 2-Person Carpool.1",PCT_ACS09_5yr_B08406039
"% Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 3-Person Carpool.1",PCT_ACS09_5yr_B08406040
"% Workers 16 Years and Over: Female: Car, Truck, or Van: Carpooled: in 4-or-More-Person Carpool.1",PCT_ACS09_5yr_B08406041
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08406042
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Bus or Trolley Bus.1,PCT_ACS09_5yr_B08406043
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Streetcar or Trolley Car (Carro Publico in Puerto Rico).1,PCT_ACS09_5yr_B08406044
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Subway or Elevated.1,PCT_ACS09_5yr_B08406045
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Railroad.1,PCT_ACS09_5yr_B08406046
% Workers 16 Years and Over: Female: Public Transportation (Excluding Taxicab): Ferryboat.1,PCT_ACS09_5yr_B08406047
% Workers 16 Years and Over: Female: Bicycle.1,PCT_ACS09_5yr_B08406048
% Workers 16 Years and Over: Female: Walked.1,PCT_ACS09_5yr_B08406049
"% Workers 16 Years and Over: Female: Taxicab, Motorcycle, or Other Means.1",PCT_ACS09_5yr_B08406050
% Workers 16 Years and Over: Female: Worked At Home.1,PCT_ACS09_5yr_B08406051
Workers 16 Years and Over Who Did Not Work At Home.6,ACS09_5yr_B08412001
Workers 16 Years and Over Who Did Not Work At Home: Less than 5 Minutes.2,ACS09_5yr_B08412002
Workers 16 Years and Over Who Did Not Work At Home: 5 to 9 Minutes.2,ACS09_5yr_B08412003
Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.3,ACS09_5yr_B08412004
Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.3,ACS09_5yr_B08412005
Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.3,ACS09_5yr_B08412006
Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.3,ACS09_5yr_B08412007
Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.3,ACS09_5yr_B08412008
Workers 16 Years and Over Who Did Not Work At Home: 35 to 39 Minutes.2,ACS09_5yr_B08412009
Workers 16 Years and Over Who Did Not Work At Home: 40 to 44 Minutes.2,ACS09_5yr_B08412010
Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.3,ACS09_5yr_B08412011
Workers 16 Years and Over Who Did Not Work At Home: 60 to 89 Minutes.2,ACS09_5yr_B08412012
Workers 16 Years and Over Who Did Not Work At Home: 90 or More Minutes.2,ACS09_5yr_B08412013
Workers 16 Years and Over Who Did Not Work At Home: Male.2,ACS09_5yr_B08412014
Workers 16 Years and Over Who Did Not Work At Home: Male: Less than 5 Minutes.1,ACS09_5yr_B08412015
Workers 16 Years and Over Who Did Not Work At Home: Male: 5 to 9 Minutes.1,ACS09_5yr_B08412016
Workers 16 Years and Over Who Did Not Work At Home: Male: 10 to 14 Minutes.1,ACS09_5yr_B08412017
Workers 16 Years and Over Who Did Not Work At Home: Male: 15 to 19 Minutes.1,ACS09_5yr_B08412018
Workers 16 Years and Over Who Did Not Work At Home: Male: 20 to 24 Minutes.1,ACS09_5yr_B08412019
Workers 16 Years and Over Who Did Not Work At Home: Male: 25 to 29 Minutes.1,ACS09_5yr_B08412020
Workers 16 Years and Over Who Did Not Work At Home: Male: 30 to 34 Minutes.1,ACS09_5yr_B08412021
Workers 16 Years and Over Who Did Not Work At Home: Male: 35 to 39 Minutes.1,ACS09_5yr_B08412022
Workers 16 Years and Over Who Did Not Work At Home: Male: 40 to 44 Minutes.1,ACS09_5yr_B08412023
Workers 16 Years and Over Who Did Not Work At Home: Male: 45 to 59 Minutes.1,ACS09_5yr_B08412024
Workers 16 Years and Over Who Did Not Work At Home: Male: 60 to 89 Minutes.1,ACS09_5yr_B08412025
Workers 16 Years and Over Who Did Not Work At Home: Male: 90 or More Minutes.1,ACS09_5yr_B08412026
Workers 16 Years and Over Who Did Not Work At Home: Female.2,ACS09_5yr_B08412027
Workers 16 Years and Over Who Did Not Work At Home: Female: Less than 5 Minutes.1,ACS09_5yr_B08412028
Workers 16 Years and Over Who Did Not Work At Home: Female: 5 to 9 Minutes.1,ACS09_5yr_B08412029
Workers 16 Years and Over Who Did Not Work At Home: Female: 10 to 14 Minutes.1,ACS09_5yr_B08412030
Workers 16 Years and Over Who Did Not Work At Home: Female: 15 to 19 Minutes.1,ACS09_5yr_B08412031
Workers 16 Years and Over Who Did Not Work At Home: Female: 20 to 24 Minutes.1,ACS09_5yr_B08412032
Workers 16 Years and Over Who Did Not Work At Home: Female: 25 to 29 Minutes.1,ACS09_5yr_B08412033
Workers 16 Years and Over Who Did Not Work At Home: Female: 30 to 34 Minutes.1,ACS09_5yr_B08412034
Workers 16 Years and Over Who Did Not Work At Home: Female: 35 to 39 Minutes.1,ACS09_5yr_B08412035
Workers 16 Years and Over Who Did Not Work At Home: Female: 40 to 44 Minutes.1,ACS09_5yr_B08412036
Workers 16 Years and Over Who Did Not Work At Home: Female: 45 to 59 Minutes.1,ACS09_5yr_B08412037
Workers 16 Years and Over Who Did Not Work At Home: Female: 60 to 89 Minutes.1,ACS09_5yr_B08412038
Workers 16 Years and Over Who Did Not Work At Home: Female: 90 or More Minutes.1,ACS09_5yr_B08412039
Std. Error: Workers 16 Years and Over Who Did Not Work At Home.6,ACS09_5yr_B08412001s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Less than 5 Minutes.2,ACS09_5yr_B08412002s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 5 to 9 Minutes.2,ACS09_5yr_B08412003s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.3,ACS09_5yr_B08412004s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.3,ACS09_5yr_B08412005s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.3,ACS09_5yr_B08412006s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.3,ACS09_5yr_B08412007s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.3,ACS09_5yr_B08412008s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 35 to 39 Minutes.2,ACS09_5yr_B08412009s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 40 to 44 Minutes.2,ACS09_5yr_B08412010s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.3,ACS09_5yr_B08412011s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 60 to 89 Minutes.2,ACS09_5yr_B08412012s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: 90 or More Minutes.2,ACS09_5yr_B08412013s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male.2,ACS09_5yr_B08412014s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: Less than 5 Minutes.1,ACS09_5yr_B08412015s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 5 to 9 Minutes.1,ACS09_5yr_B08412016s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 10 to 14 Minutes.1,ACS09_5yr_B08412017s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 15 to 19 Minutes.1,ACS09_5yr_B08412018s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 20 to 24 Minutes.1,ACS09_5yr_B08412019s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 25 to 29 Minutes.1,ACS09_5yr_B08412020s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 30 to 34 Minutes.1,ACS09_5yr_B08412021s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 35 to 39 Minutes.1,ACS09_5yr_B08412022s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 40 to 44 Minutes.1,ACS09_5yr_B08412023s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 45 to 59 Minutes.1,ACS09_5yr_B08412024s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 60 to 89 Minutes.1,ACS09_5yr_B08412025s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Male: 90 or More Minutes.1,ACS09_5yr_B08412026s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female.2,ACS09_5yr_B08412027s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: Less than 5 Minutes.1,ACS09_5yr_B08412028s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 5 to 9 Minutes.1,ACS09_5yr_B08412029s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 10 to 14 Minutes.1,ACS09_5yr_B08412030s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 15 to 19 Minutes.1,ACS09_5yr_B08412031s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 20 to 24 Minutes.1,ACS09_5yr_B08412032s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 25 to 29 Minutes.1,ACS09_5yr_B08412033s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 30 to 34 Minutes.1,ACS09_5yr_B08412034s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 35 to 39 Minutes.1,ACS09_5yr_B08412035s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 40 to 44 Minutes.1,ACS09_5yr_B08412036s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 45 to 59 Minutes.1,ACS09_5yr_B08412037s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 60 to 89 Minutes.1,ACS09_5yr_B08412038s
Std. Error: Workers 16 Years and Over Who Did Not Work At Home: Female: 90 or More Minutes.1,ACS09_5yr_B08412039s
% Workers 16 Years and Over Who Did Not Work At Home: Less than 5 Minutes.2,PCT_ACS09_5yr_B08412002
% Workers 16 Years and Over Who Did Not Work At Home: 5 to 9 Minutes.2,PCT_ACS09_5yr_B08412003
% Workers 16 Years and Over Who Did Not Work At Home: 10 to 14 Minutes.3,PCT_ACS09_5yr_B08412004
% Workers 16 Years and Over Who Did Not Work At Home: 15 to 19 Minutes.3,PCT_ACS09_5yr_B08412005
% Workers 16 Years and Over Who Did Not Work At Home: 20 to 24 Minutes.3,PCT_ACS09_5yr_B08412006
% Workers 16 Years and Over Who Did Not Work At Home: 25 to 29 Minutes.3,PCT_ACS09_5yr_B08412007
% Workers 16 Years and Over Who Did Not Work At Home: 30 to 34 Minutes.3,PCT_ACS09_5yr_B08412008
% Workers 16 Years and Over Who Did Not Work At Home: 35 to 39 Minutes.2,PCT_ACS09_5yr_B08412009
% Workers 16 Years and Over Who Did Not Work At Home: 40 to 44 Minutes.2,PCT_ACS09_5yr_B08412010
% Workers 16 Years and Over Who Did Not Work At Home: 45 to 59 Minutes.3,PCT_ACS09_5yr_B08412011
% Workers 16 Years and Over Who Did Not Work At Home: 60 to 89 Minutes.2,PCT_ACS09_5yr_B08412012
% Workers 16 Years and Over Who Did Not Work At Home: 90 or More Minutes.2,PCT_ACS09_5yr_B08412013
% Workers 16 Years and Over Who Did Not Work At Home: Male.2,PCT_ACS09_5yr_B08412014
% Workers 16 Years and Over Who Did Not Work At Home: Male: Less than 5 Minutes.1,PCT_ACS09_5yr_B08412015
% Workers 16 Years and Over Who Did Not Work At Home: Male: 5 to 9 Minutes.1,PCT_ACS09_5yr_B08412016
% Workers 16 Years and Over Who Did Not Work At Home: Male: 10 to 14 Minutes.1,PCT_ACS09_5yr_B08412017
% Workers 16 Years and Over Who Did Not Work At Home: Male: 15 to 19 Minutes.1,PCT_ACS09_5yr_B08412018
% Workers 16 Years and Over Who Did Not Work At Home: Male: 20 to 24 Minutes.1,PCT_ACS09_5yr_B08412019
% Workers 16 Years and Over Who Did Not Work At Home: Male: 25 to 29 Minutes.1,PCT_ACS09_5yr_B08412020
% Workers 16 Years and Over Who Did Not Work At Home: Male: 30 to 34 Minutes.1,PCT_ACS09_5yr_B08412021
% Workers 16 Years and Over Who Did Not Work At Home: Male: 35 to 39 Minutes.1,PCT_ACS09_5yr_B08412022
% Workers 16 Years and Over Who Did Not Work At Home: Male: 40 to 44 Minutes.1,PCT_ACS09_5yr_B08412023
% Workers 16 Years and Over Who Did Not Work At Home: Male: 45 to 59 Minutes.1,PCT_ACS09_5yr_B08412024
% Workers 16 Years and Over Who Did Not Work At Home: Male: 60 to 89 Minutes.1,PCT_ACS09_5yr_B08412025
% Workers 16 Years and Over Who Did Not Work At Home: Male: 90 or More Minutes.1,PCT_ACS09_5yr_B08412026
% Workers 16 Years and Over Who Did Not Work At Home: Female.2,PCT_ACS09_5yr_B08412027
% Workers 16 Years and Over Who Did Not Work At Home: Female: Less than 5 Minutes.1,PCT_ACS09_5yr_B08412028
% Workers 16 Years and Over Who Did Not Work At Home: Female: 5 to 9 Minutes.1,PCT_ACS09_5yr_B08412029
% Workers 16 Years and Over Who Did Not Work At Home: Female: 10 to 14 Minutes.1,PCT_ACS09_5yr_B08412030
% Workers 16 Years and Over Who Did Not Work At Home: Female: 15 to 19 Minutes.1,PCT_ACS09_5yr_B08412031
% Workers 16 Years and Over Who Did Not Work At Home: Female: 20 to 24 Minutes.1,PCT_ACS09_5yr_B08412032
% Workers 16 Years and Over Who Did Not Work At Home: Female: 25 to 29 Minutes.1,PCT_ACS09_5yr_B08412033
% Workers 16 Years and Over Who Did Not Work At Home: Female: 30 to 34 Minutes.1,PCT_ACS09_5yr_B08412034
% Workers 16 Years and Over Who Did Not Work At Home: Female: 35 to 39 Minutes.1,PCT_ACS09_5yr_B08412035
% Workers 16 Years and Over Who Did Not Work At Home: Female: 40 to 44 Minutes.1,PCT_ACS09_5yr_B08412036
% Workers 16 Years and Over Who Did Not Work At Home: Female: 45 to 59 Minutes.1,PCT_ACS09_5yr_B08412037
% Workers 16 Years and Over Who Did Not Work At Home: Female: 60 to 89 Minutes.1,PCT_ACS09_5yr_B08412038
% Workers 16 Years and Over Who Did Not Work At Home: Female: 90 or More Minutes.1,PCT_ACS09_5yr_B08412039
Workers 16 Years and Over.13,ACS09_5yr_B08501001
Workers 16 Years and Over: 16 to 19 Years.1,ACS09_5yr_B08501002
Workers 16 Years and Over: 20 to 24 Years.1,ACS09_5yr_B08501003
Workers 16 Years and Over: 25 to 44 Years.1,ACS09_5yr_B08501004
Workers 16 Years and Over: 45 to 54 Years.1,ACS09_5yr_B08501005
Workers 16 Years and Over: 55 to 59 Years.1,ACS09_5yr_B08501006
Workers 16 Years and Over: 60 to 64 Years.1,ACS09_5yr_B08501007
Workers 16 Years and Over: 65 Years and Over.1,ACS09_5yr_B08501008
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.7",ACS09_5yr_B08501009
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 16 to 19 Years.1",ACS09_5yr_B08501010
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 20 to 24 Years.1",ACS09_5yr_B08501011
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 25 to 44 Years.1",ACS09_5yr_B08501012
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 45 to 54 Years.1",ACS09_5yr_B08501013
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 55 to 59 Years.1",ACS09_5yr_B08501014
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 60 to 64 Years.1",ACS09_5yr_B08501015
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 65 Years and Over.1",ACS09_5yr_B08501016
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled.7",ACS09_5yr_B08501017
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 16 to 19 Years.1",ACS09_5yr_B08501018
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 20 to 24 Years.1",ACS09_5yr_B08501019
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 25 to 44 Years.1",ACS09_5yr_B08501020
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 45 to 54 Years.1",ACS09_5yr_B08501021
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 55 to 59 Years.1",ACS09_5yr_B08501022
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 60 to 64 Years.1",ACS09_5yr_B08501023
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 65 Years and Over.1",ACS09_5yr_B08501024
Workers 16 Years and Over: Public Transportation (Excluding Taxicab).8,ACS09_5yr_B08501025
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 16 to 19 Years.1,ACS09_5yr_B08501026
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 20 to 24 Years.1,ACS09_5yr_B08501027
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 25 to 44 Years.1,ACS09_5yr_B08501028
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 45 to 54 Years.1,ACS09_5yr_B08501029
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 55 to 59 Years.1,ACS09_5yr_B08501030
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 60 to 64 Years.1,ACS09_5yr_B08501031
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 65 Years and Over.1,ACS09_5yr_B08501032
Workers 16 Years and Over: Walked.8,ACS09_5yr_B08501033
Workers 16 Years and Over: Walked: 16 to 19 Years.1,ACS09_5yr_B08501034
Workers 16 Years and Over: Walked: 20 to 24 Years.1,ACS09_5yr_B08501035
Workers 16 Years and Over: Walked: 25 to 44 Years.1,ACS09_5yr_B08501036
Workers 16 Years and Over: Walked: 45 to 54 Years.1,ACS09_5yr_B08501037
Workers 16 Years and Over: Walked: 55 to 59 Years.1,ACS09_5yr_B08501038
Workers 16 Years and Over: Walked: 60 to 64 Years.1,ACS09_5yr_B08501039
Workers 16 Years and Over: Walked: 65 Years and Over.1,ACS09_5yr_B08501040
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.7",ACS09_5yr_B08501041
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 16 to 19 Years.1",ACS09_5yr_B08501042
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 20 to 24 Years.1",ACS09_5yr_B08501043
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 25 to 44 Years.1",ACS09_5yr_B08501044
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 45 to 54 Years.1",ACS09_5yr_B08501045
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 55 to 59 Years.1",ACS09_5yr_B08501046
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 60 to 64 Years.1",ACS09_5yr_B08501047
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 65 Years and Over.1",ACS09_5yr_B08501048
Workers 16 Years and Over: Worked At Home.8,ACS09_5yr_B08501049
Workers 16 Years and Over: Worked At Home: 16 to 19 Years.1,ACS09_5yr_B08501050
Workers 16 Years and Over: Worked At Home: 20 to 24 Years.1,ACS09_5yr_B08501051
Workers 16 Years and Over: Worked At Home: 25 to 44 Years.1,ACS09_5yr_B08501052
Workers 16 Years and Over: Worked At Home: 45 to 54 Years.1,ACS09_5yr_B08501053
Workers 16 Years and Over: Worked At Home: 55 to 59 Years.1,ACS09_5yr_B08501054
Workers 16 Years and Over: Worked At Home: 60 to 64 Years.1,ACS09_5yr_B08501055
Workers 16 Years and Over: Worked At Home: 65 Years and Over.1,ACS09_5yr_B08501056
Std. Error: Workers 16 Years and Over.13,ACS09_5yr_B08501001s
Std. Error: Workers 16 Years and Over: 16 to 19 Years.1,ACS09_5yr_B08501002s
Std. Error: Workers 16 Years and Over: 20 to 24 Years.1,ACS09_5yr_B08501003s
Std. Error: Workers 16 Years and Over: 25 to 44 Years.1,ACS09_5yr_B08501004s
Std. Error: Workers 16 Years and Over: 45 to 54 Years.1,ACS09_5yr_B08501005s
Std. Error: Workers 16 Years and Over: 55 to 59 Years.1,ACS09_5yr_B08501006s
Std. Error: Workers 16 Years and Over: 60 to 64 Years.1,ACS09_5yr_B08501007s
Std. Error: Workers 16 Years and Over: 65 Years and Over.1,ACS09_5yr_B08501008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.7",ACS09_5yr_B08501009s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 16 to 19 Years.1",ACS09_5yr_B08501010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 20 to 24 Years.1",ACS09_5yr_B08501011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 25 to 44 Years.1",ACS09_5yr_B08501012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 45 to 54 Years.1",ACS09_5yr_B08501013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 55 to 59 Years.1",ACS09_5yr_B08501014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 60 to 64 Years.1",ACS09_5yr_B08501015s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 65 Years and Over.1",ACS09_5yr_B08501016s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled.7",ACS09_5yr_B08501017s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 16 to 19 Years.1",ACS09_5yr_B08501018s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 20 to 24 Years.1",ACS09_5yr_B08501019s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 25 to 44 Years.1",ACS09_5yr_B08501020s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 45 to 54 Years.1",ACS09_5yr_B08501021s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 55 to 59 Years.1",ACS09_5yr_B08501022s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 60 to 64 Years.1",ACS09_5yr_B08501023s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 65 Years and Over.1",ACS09_5yr_B08501024s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab).8,ACS09_5yr_B08501025s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 16 to 19 Years.1,ACS09_5yr_B08501026s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 20 to 24 Years.1,ACS09_5yr_B08501027s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 25 to 44 Years.1,ACS09_5yr_B08501028s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 45 to 54 Years.1,ACS09_5yr_B08501029s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 55 to 59 Years.1,ACS09_5yr_B08501030s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 60 to 64 Years.1,ACS09_5yr_B08501031s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 65 Years and Over.1,ACS09_5yr_B08501032s
Std. Error: Workers 16 Years and Over: Walked.8,ACS09_5yr_B08501033s
Std. Error: Workers 16 Years and Over: Walked: 16 to 19 Years.1,ACS09_5yr_B08501034s
Std. Error: Workers 16 Years and Over: Walked: 20 to 24 Years.1,ACS09_5yr_B08501035s
Std. Error: Workers 16 Years and Over: Walked: 25 to 44 Years.1,ACS09_5yr_B08501036s
Std. Error: Workers 16 Years and Over: Walked: 45 to 54 Years.1,ACS09_5yr_B08501037s
Std. Error: Workers 16 Years and Over: Walked: 55 to 59 Years.1,ACS09_5yr_B08501038s
Std. Error: Workers 16 Years and Over: Walked: 60 to 64 Years.1,ACS09_5yr_B08501039s
Std. Error: Workers 16 Years and Over: Walked: 65 Years and Over.1,ACS09_5yr_B08501040s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.7",ACS09_5yr_B08501041s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 16 to 19 Years.1",ACS09_5yr_B08501042s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 20 to 24 Years.1",ACS09_5yr_B08501043s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 25 to 44 Years.1",ACS09_5yr_B08501044s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 45 to 54 Years.1",ACS09_5yr_B08501045s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 55 to 59 Years.1",ACS09_5yr_B08501046s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 60 to 64 Years.1",ACS09_5yr_B08501047s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 65 Years and Over.1",ACS09_5yr_B08501048s
Std. Error: Workers 16 Years and Over: Worked At Home.8,ACS09_5yr_B08501049s
Std. Error: Workers 16 Years and Over: Worked At Home: 16 to 19 Years.1,ACS09_5yr_B08501050s
Std. Error: Workers 16 Years and Over: Worked At Home: 20 to 24 Years.1,ACS09_5yr_B08501051s
Std. Error: Workers 16 Years and Over: Worked At Home: 25 to 44 Years.1,ACS09_5yr_B08501052s
Std. Error: Workers 16 Years and Over: Worked At Home: 45 to 54 Years.1,ACS09_5yr_B08501053s
Std. Error: Workers 16 Years and Over: Worked At Home: 55 to 59 Years.1,ACS09_5yr_B08501054s
Std. Error: Workers 16 Years and Over: Worked At Home: 60 to 64 Years.1,ACS09_5yr_B08501055s
Std. Error: Workers 16 Years and Over: Worked At Home: 65 Years and Over.1,ACS09_5yr_B08501056s
% Workers 16 Years and Over: 16 to 19 Years.1,PCT_ACS09_5yr_B08501002
% Workers 16 Years and Over: 20 to 24 Years.1,PCT_ACS09_5yr_B08501003
% Workers 16 Years and Over: 25 to 44 Years.1,PCT_ACS09_5yr_B08501004
% Workers 16 Years and Over: 45 to 54 Years.1,PCT_ACS09_5yr_B08501005
% Workers 16 Years and Over: 55 to 59 Years.1,PCT_ACS09_5yr_B08501006
% Workers 16 Years and Over: 60 to 64 Years.1,PCT_ACS09_5yr_B08501007
% Workers 16 Years and Over: 65 Years and Over.1,PCT_ACS09_5yr_B08501008
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.7",PCT_ACS09_5yr_B08501009
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 16 to 19 Years.1",PCT_ACS09_5yr_B08501010
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 20 to 24 Years.1",PCT_ACS09_5yr_B08501011
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 25 to 44 Years.1",PCT_ACS09_5yr_B08501012
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 45 to 54 Years.1",PCT_ACS09_5yr_B08501013
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 55 to 59 Years.1",PCT_ACS09_5yr_B08501014
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 60 to 64 Years.1",PCT_ACS09_5yr_B08501015
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: 65 Years and Over.1",PCT_ACS09_5yr_B08501016
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled.7",PCT_ACS09_5yr_B08501017
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 16 to 19 Years.1",PCT_ACS09_5yr_B08501018
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 20 to 24 Years.1",PCT_ACS09_5yr_B08501019
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 25 to 44 Years.1",PCT_ACS09_5yr_B08501020
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 45 to 54 Years.1",PCT_ACS09_5yr_B08501021
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 55 to 59 Years.1",PCT_ACS09_5yr_B08501022
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 60 to 64 Years.1",PCT_ACS09_5yr_B08501023
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: 65 Years and Over.1",PCT_ACS09_5yr_B08501024
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab).8,PCT_ACS09_5yr_B08501025
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 16 to 19 Years.1,PCT_ACS09_5yr_B08501026
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 20 to 24 Years.1,PCT_ACS09_5yr_B08501027
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 25 to 44 Years.1,PCT_ACS09_5yr_B08501028
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 45 to 54 Years.1,PCT_ACS09_5yr_B08501029
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 55 to 59 Years.1,PCT_ACS09_5yr_B08501030
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 60 to 64 Years.1,PCT_ACS09_5yr_B08501031
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): 65 Years and Over.1,PCT_ACS09_5yr_B08501032
% Workers 16 Years and Over: Walked.8,PCT_ACS09_5yr_B08501033
% Workers 16 Years and Over: Walked: 16 to 19 Years.1,PCT_ACS09_5yr_B08501034
% Workers 16 Years and Over: Walked: 20 to 24 Years.1,PCT_ACS09_5yr_B08501035
% Workers 16 Years and Over: Walked: 25 to 44 Years.1,PCT_ACS09_5yr_B08501036
% Workers 16 Years and Over: Walked: 45 to 54 Years.1,PCT_ACS09_5yr_B08501037
% Workers 16 Years and Over: Walked: 55 to 59 Years.1,PCT_ACS09_5yr_B08501038
% Workers 16 Years and Over: Walked: 60 to 64 Years.1,PCT_ACS09_5yr_B08501039
% Workers 16 Years and Over: Walked: 65 Years and Over.1,PCT_ACS09_5yr_B08501040
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.7",PCT_ACS09_5yr_B08501041
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 16 to 19 Years.1",PCT_ACS09_5yr_B08501042
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 20 to 24 Years.1",PCT_ACS09_5yr_B08501043
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 25 to 44 Years.1",PCT_ACS09_5yr_B08501044
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 45 to 54 Years.1",PCT_ACS09_5yr_B08501045
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 55 to 59 Years.1",PCT_ACS09_5yr_B08501046
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 60 to 64 Years.1",PCT_ACS09_5yr_B08501047
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: 65 Years and Over.1",PCT_ACS09_5yr_B08501048
% Workers 16 Years and Over: Worked At Home.8,PCT_ACS09_5yr_B08501049
% Workers 16 Years and Over: Worked At Home: 16 to 19 Years.1,PCT_ACS09_5yr_B08501050
% Workers 16 Years and Over: Worked At Home: 20 to 24 Years.1,PCT_ACS09_5yr_B08501051
% Workers 16 Years and Over: Worked At Home: 25 to 44 Years.1,PCT_ACS09_5yr_B08501052
% Workers 16 Years and Over: Worked At Home: 45 to 54 Years.1,PCT_ACS09_5yr_B08501053
% Workers 16 Years and Over: Worked At Home: 55 to 59 Years.1,PCT_ACS09_5yr_B08501054
% Workers 16 Years and Over: Worked At Home: 60 to 64 Years.1,PCT_ACS09_5yr_B08501055
% Workers 16 Years and Over: Worked At Home: 65 Years and Over.1,PCT_ACS09_5yr_B08501056
Workers 16 Years and Over: Median Age -- Total.1,ACS09_5yr_B08503001
"Workers 16 Years and Over: Median Age -- Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08503002
"Workers 16 Years and Over: Median Age -- Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08503003
Workers 16 Years and Over: Median Age -- Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08503004
Workers 16 Years and Over: Median Age -- Walked.1,ACS09_5yr_B08503005
"Workers 16 Years and Over: Median Age -- Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08503006
Workers 16 Years and Over: Median Age -- Worked At Home.1,ACS09_5yr_B08503007
Std. Error: Workers 16 Years and Over: Median Age -- Total.1,ACS09_5yr_B08503001s
"Std. Error: Workers 16 Years and Over: Median Age -- Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08503002s
"Std. Error: Workers 16 Years and Over: Median Age -- Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08503003s
Std. Error: Workers 16 Years and Over: Median Age -- Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08503004s
Std. Error: Workers 16 Years and Over: Median Age -- Walked.1,ACS09_5yr_B08503005s
"Std. Error: Workers 16 Years and Over: Median Age -- Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08503006s
Std. Error: Workers 16 Years and Over: Median Age -- Worked At Home.1,ACS09_5yr_B08503007s
White Alone Workers 16 Years and Over.1,ACS09_5yr_B08505A001
"White Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505A002
"White Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505A003
White Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505A004
White Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505A005
"White Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505A006
White Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505A007
Std. Error: White Alone Workers 16 Years and Over.1,ACS09_5yr_B08505A001s
"Std. Error: White Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505A002s
"Std. Error: White Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505A003s
Std. Error: White Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505A004s
Std. Error: White Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505A005s
"Std. Error: White Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505A006s
Std. Error: White Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505A007s
"% White Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08505A002
"% White Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08505A003
% White Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08505A004
% White Alone Workers 16 Years and Over: Walked.1,PCT_ACS09_5yr_B08505A005
"% White Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08505A006
% White Alone Workers 16 Years and Over: Worked At Home.1,PCT_ACS09_5yr_B08505A007
Black or African American Alone Workers 16 Years and Over.1,ACS09_5yr_B08505B001
"Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505B002
"Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505B003
Black or African American Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505B004
Black or African American Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505B005
"Black or African American Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505B006
Black or African American Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505B007
Std. Error: Black or African American Alone Workers 16 Years and Over.1,ACS09_5yr_B08505B001s
"Std. Error: Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505B002s
"Std. Error: Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505B003s
Std. Error: Black or African American Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505B004s
Std. Error: Black or African American Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505B005s
"Std. Error: Black or African American Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505B006s
Std. Error: Black or African American Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505B007s
"% Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08505B002
"% Black or African American Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08505B003
% Black or African American Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08505B004
% Black or African American Alone Workers 16 Years and Over: Walked.1,PCT_ACS09_5yr_B08505B005
"% Black or African American Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08505B006
% Black or African American Alone Workers 16 Years and Over: Worked At Home.1,PCT_ACS09_5yr_B08505B007
American Indian and Alaska Native Alone Workers 16 Years and Over.1,ACS09_5yr_B08505C001
"American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505C002
"American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505C003
American Indian and Alaska Native Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505C004
American Indian and Alaska Native Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505C005
"American Indian and Alaska Native Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505C006
American Indian and Alaska Native Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505C007
Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over.1,ACS09_5yr_B08505C001s
"Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505C002s
"Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505C003s
Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505C004s
Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505C005s
"Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505C006s
Std. Error: American Indian and Alaska Native Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505C007s
"% American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08505C002
"% American Indian and Alaska Native Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08505C003
% American Indian and Alaska Native Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08505C004
% American Indian and Alaska Native Alone Workers 16 Years and Over: Walked.1,PCT_ACS09_5yr_B08505C005
"% American Indian and Alaska Native Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08505C006
% American Indian and Alaska Native Alone Workers 16 Years and Over: Worked At Home.1,PCT_ACS09_5yr_B08505C007
Asian Alone Workers 16 Years and Over.1,ACS09_5yr_B08505D001
"Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505D002
"Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505D003
Asian Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505D004
Asian Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505D005
"Asian Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505D006
Asian Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505D007
Std. Error: Asian Alone Workers 16 Years and Over.1,ACS09_5yr_B08505D001s
"Std. Error: Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505D002s
"Std. Error: Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505D003s
Std. Error: Asian Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505D004s
Std. Error: Asian Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505D005s
"Std. Error: Asian Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505D006s
Std. Error: Asian Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505D007s
"% Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08505D002
"% Asian Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08505D003
% Asian Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08505D004
% Asian Alone Workers 16 Years and Over: Walked.1,PCT_ACS09_5yr_B08505D005
"% Asian Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08505D006
% Asian Alone Workers 16 Years and Over: Worked At Home.1,PCT_ACS09_5yr_B08505D007
Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over.1,ACS09_5yr_B08505E001
"Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505E002
"Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505E003
Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505E004
Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505E005
"Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505E006
Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505E007
Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over.1,ACS09_5yr_B08505E001s
"Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505E002s
"Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505E003s
Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505E004s
Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505E005s
"Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505E006s
Std. Error: Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505E007s
"% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08505E002
"% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08505E003
% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08505E004
% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Walked.1,PCT_ACS09_5yr_B08505E005
"% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08505E006
% Native Hawaiian and Other Pacific Islander Alone Workers 16 Years and Over: Worked At Home.1,PCT_ACS09_5yr_B08505E007
Some Other Race Alone Workers 16 Years and Over.1,ACS09_5yr_B08505F001
"Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505F002
"Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505F003
Some Other Race Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505F004
Some Other Race Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505F005
"Some Other Race Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505F006
Some Other Race Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505F007
Std. Error: Some Other Race Alone Workers 16 Years and Over.1,ACS09_5yr_B08505F001s
"Std. Error: Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505F002s
"Std. Error: Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505F003s
Std. Error: Some Other Race Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505F004s
Std. Error: Some Other Race Alone Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505F005s
"Std. Error: Some Other Race Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505F006s
Std. Error: Some Other Race Alone Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505F007s
"% Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08505F002
"% Some Other Race Alone Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08505F003
% Some Other Race Alone Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08505F004
% Some Other Race Alone Workers 16 Years and Over: Walked.1,PCT_ACS09_5yr_B08505F005
"% Some Other Race Alone Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08505F006
% Some Other Race Alone Workers 16 Years and Over: Worked At Home.1,PCT_ACS09_5yr_B08505F007
Two or More Races Workers 16 Years and Over.1,ACS09_5yr_B08505G001
"Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505G002
"Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505G003
Two or More Races Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505G004
Two or More Races Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505G005
"Two or More Races Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505G006
Two or More Races Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505G007
Std. Error: Two or More Races Workers 16 Years and Over.1,ACS09_5yr_B08505G001s
"Std. Error: Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505G002s
"Std. Error: Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505G003s
Std. Error: Two or More Races Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505G004s
Std. Error: Two or More Races Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505G005s
"Std. Error: Two or More Races Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505G006s
Std. Error: Two or More Races Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505G007s
"% Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08505G002
"% Two or More Races Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08505G003
% Two or More Races Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08505G004
% Two or More Races Workers 16 Years and Over: Walked.1,PCT_ACS09_5yr_B08505G005
"% Two or More Races Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08505G006
% Two or More Races Workers 16 Years and Over: Worked At Home.1,PCT_ACS09_5yr_B08505G007
"White Alone, Not Hispanic or Latino Workers 16 Years and Over.1",ACS09_5yr_B08505H001
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505H002
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505H003
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1",ACS09_5yr_B08505H004
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Walked.1",ACS09_5yr_B08505H005
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505H006
"White Alone, Not Hispanic or Latino Workers 16 Years and Over: Worked At Home.1",ACS09_5yr_B08505H007
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over.1",ACS09_5yr_B08505H001s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505H002s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505H003s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1",ACS09_5yr_B08505H004s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Walked.1",ACS09_5yr_B08505H005s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505H006s
"Std. Error: White Alone, Not Hispanic or Latino Workers 16 Years and Over: Worked At Home.1",ACS09_5yr_B08505H007s
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08505H002
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08505H003
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1",PCT_ACS09_5yr_B08505H004
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Walked.1",PCT_ACS09_5yr_B08505H005
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08505H006
"% White Alone, Not Hispanic or Latino Workers 16 Years and Over: Worked At Home.1",PCT_ACS09_5yr_B08505H007
Hispanic or Latino Workers 16 Years and Over.1,ACS09_5yr_B08505I001
"Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505I002
"Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505I003
Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505I004
Hispanic or Latino Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505I005
"Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505I006
Hispanic or Latino Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505I007
Std. Error: Hispanic or Latino Workers 16 Years and Over.1,ACS09_5yr_B08505I001s
"Std. Error: Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",ACS09_5yr_B08505I002s
"Std. Error: Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",ACS09_5yr_B08505I003s
Std. Error: Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,ACS09_5yr_B08505I004s
Std. Error: Hispanic or Latino Workers 16 Years and Over: Walked.1,ACS09_5yr_B08505I005s
"Std. Error: Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",ACS09_5yr_B08505I006s
Std. Error: Hispanic or Latino Workers 16 Years and Over: Worked At Home.1,ACS09_5yr_B08505I007s
"% Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.1",PCT_ACS09_5yr_B08505I002
"% Hispanic or Latino Workers 16 Years and Over: Car, Truck, or Van - Carpooled.1",PCT_ACS09_5yr_B08505I003
% Hispanic or Latino Workers 16 Years and Over: Public Transportation (Excluding Taxicab).1,PCT_ACS09_5yr_B08505I004
% Hispanic or Latino Workers 16 Years and Over: Walked.1,PCT_ACS09_5yr_B08505I005
"% Hispanic or Latino Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.1",PCT_ACS09_5yr_B08505I006
% Hispanic or Latino Workers 16 Years and Over: Worked At Home.1,PCT_ACS09_5yr_B08505I007
Workers 16 Years and Over.14,ACS09_5yr_B08511001
Workers 16 Years and Over: Native.1,ACS09_5yr_B08511002
Workers 16 Years and Over: Foreign Born.1,ACS09_5yr_B08511003
Workers 16 Years and Over: Foreign Born: Naturalized U.s. Citizen.1,ACS09_5yr_B08511004
Workers 16 Years and Over: Foreign Born: Not a U.s. Citizen.1,ACS09_5yr_B08511005
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.8",ACS09_5yr_B08511006
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Native.1",ACS09_5yr_B08511007
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born.1",ACS09_5yr_B08511008
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Naturalized U.s. Citizen.1",ACS09_5yr_B08511009
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Not a U.s. Citizen.1",ACS09_5yr_B08511010
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled.8",ACS09_5yr_B08511011
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Native.1",ACS09_5yr_B08511012
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born.1",ACS09_5yr_B08511013
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Naturalized U.s. Citizen.1",ACS09_5yr_B08511014
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Not a U.s. Citizen.1",ACS09_5yr_B08511015
Workers 16 Years and Over: Public Transportation (Excluding Taxicab).9,ACS09_5yr_B08511016
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Native.1,ACS09_5yr_B08511017
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born.1,ACS09_5yr_B08511018
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Naturalized U.s. Citizen.1,ACS09_5yr_B08511019
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Not a U.s. Citizen.1,ACS09_5yr_B08511020
Workers 16 Years and Over: Walked.9,ACS09_5yr_B08511021
Workers 16 Years and Over: Walked: Native.1,ACS09_5yr_B08511022
Workers 16 Years and Over: Walked: Foreign Born.1,ACS09_5yr_B08511023
Workers 16 Years and Over: Walked: Foreign Born: Naturalized U.s. Citizen.1,ACS09_5yr_B08511024
Workers 16 Years and Over: Walked: Foreign Born: Not a U.s. Citizen.1,ACS09_5yr_B08511025
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.8",ACS09_5yr_B08511026
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Native.1",ACS09_5yr_B08511027
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born.1",ACS09_5yr_B08511028
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Naturalized U.s. Citizen.1",ACS09_5yr_B08511029
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Not a U.s. Citizen.1",ACS09_5yr_B08511030
Workers 16 Years and Over: Worked At Home.9,ACS09_5yr_B08511031
Workers 16 Years and Over: Worked At Home: Native.1,ACS09_5yr_B08511032
Workers 16 Years and Over: Worked At Home: Foreign Born.1,ACS09_5yr_B08511033
Workers 16 Years and Over: Worked At Home: Foreign Born: Naturalized U.s. Citizen.1,ACS09_5yr_B08511034
Workers 16 Years and Over: Worked At Home: Foreign Born: Not a U.s. Citizen.1,ACS09_5yr_B08511035
Std. Error: Workers 16 Years and Over.14,ACS09_5yr_B08511001s
Std. Error: Workers 16 Years and Over: Native.1,ACS09_5yr_B08511002s
Std. Error: Workers 16 Years and Over: Foreign Born.1,ACS09_5yr_B08511003s
Std. Error: Workers 16 Years and Over: Foreign Born: Naturalized U.s. Citizen.1,ACS09_5yr_B08511004s
Std. Error: Workers 16 Years and Over: Foreign Born: Not a U.s. Citizen.1,ACS09_5yr_B08511005s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.8",ACS09_5yr_B08511006s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Native.1",ACS09_5yr_B08511007s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born.1",ACS09_5yr_B08511008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Naturalized U.s. Citizen.1",ACS09_5yr_B08511009s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Not a U.s. Citizen.1",ACS09_5yr_B08511010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled.8",ACS09_5yr_B08511011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Native.1",ACS09_5yr_B08511012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born.1",ACS09_5yr_B08511013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Naturalized U.s. Citizen.1",ACS09_5yr_B08511014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Not a U.s. Citizen.1",ACS09_5yr_B08511015s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab).9,ACS09_5yr_B08511016s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Native.1,ACS09_5yr_B08511017s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born.1,ACS09_5yr_B08511018s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Naturalized U.s. Citizen.1,ACS09_5yr_B08511019s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Not a U.s. Citizen.1,ACS09_5yr_B08511020s
Std. Error: Workers 16 Years and Over: Walked.9,ACS09_5yr_B08511021s
Std. Error: Workers 16 Years and Over: Walked: Native.1,ACS09_5yr_B08511022s
Std. Error: Workers 16 Years and Over: Walked: Foreign Born.1,ACS09_5yr_B08511023s
Std. Error: Workers 16 Years and Over: Walked: Foreign Born: Naturalized U.s. Citizen.1,ACS09_5yr_B08511024s
Std. Error: Workers 16 Years and Over: Walked: Foreign Born: Not a U.s. Citizen.1,ACS09_5yr_B08511025s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.8",ACS09_5yr_B08511026s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Native.1",ACS09_5yr_B08511027s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born.1",ACS09_5yr_B08511028s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Naturalized U.s. Citizen.1",ACS09_5yr_B08511029s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Not a U.s. Citizen.1",ACS09_5yr_B08511030s
Std. Error: Workers 16 Years and Over: Worked At Home.9,ACS09_5yr_B08511031s
Std. Error: Workers 16 Years and Over: Worked At Home: Native.1,ACS09_5yr_B08511032s
Std. Error: Workers 16 Years and Over: Worked At Home: Foreign Born.1,ACS09_5yr_B08511033s
Std. Error: Workers 16 Years and Over: Worked At Home: Foreign Born: Naturalized U.s. Citizen.1,ACS09_5yr_B08511034s
Std. Error: Workers 16 Years and Over: Worked At Home: Foreign Born: Not a U.s. Citizen.1,ACS09_5yr_B08511035s
% Workers 16 Years and Over: Native.1,PCT_ACS09_5yr_B08511002
% Workers 16 Years and Over: Foreign Born.1,PCT_ACS09_5yr_B08511003
% Workers 16 Years and Over: Foreign Born: Naturalized U.s. Citizen.1,PCT_ACS09_5yr_B08511004
% Workers 16 Years and Over: Foreign Born: Not a U.s. Citizen.1,PCT_ACS09_5yr_B08511005
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.8",PCT_ACS09_5yr_B08511006
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Native.1",PCT_ACS09_5yr_B08511007
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born.1",PCT_ACS09_5yr_B08511008
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Naturalized U.s. Citizen.1",PCT_ACS09_5yr_B08511009
"% Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Foreign Born: Not a U.s. Citizen.1",PCT_ACS09_5yr_B08511010
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled.8",PCT_ACS09_5yr_B08511011
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Native.1",PCT_ACS09_5yr_B08511012
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born.1",PCT_ACS09_5yr_B08511013
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Naturalized U.s. Citizen.1",PCT_ACS09_5yr_B08511014
"% Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Foreign Born: Not a U.s. Citizen.1",PCT_ACS09_5yr_B08511015
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab).9,PCT_ACS09_5yr_B08511016
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Native.1,PCT_ACS09_5yr_B08511017
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born.1,PCT_ACS09_5yr_B08511018
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Naturalized U.s. Citizen.1,PCT_ACS09_5yr_B08511019
% Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Foreign Born: Not a U.s. Citizen.1,PCT_ACS09_5yr_B08511020
% Workers 16 Years and Over: Walked.9,PCT_ACS09_5yr_B08511021
% Workers 16 Years and Over: Walked: Native.1,PCT_ACS09_5yr_B08511022
% Workers 16 Years and Over: Walked: Foreign Born.1,PCT_ACS09_5yr_B08511023
% Workers 16 Years and Over: Walked: Foreign Born: Naturalized U.s. Citizen.1,PCT_ACS09_5yr_B08511024
% Workers 16 Years and Over: Walked: Foreign Born: Not a U.s. Citizen.1,PCT_ACS09_5yr_B08511025
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.8",PCT_ACS09_5yr_B08511026
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Native.1",PCT_ACS09_5yr_B08511027
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born.1",PCT_ACS09_5yr_B08511028
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Naturalized U.s. Citizen.1",PCT_ACS09_5yr_B08511029
"% Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Foreign Born: Not a U.s. Citizen.1",PCT_ACS09_5yr_B08511030
% Workers 16 Years and Over: Worked At Home.9,PCT_ACS09_5yr_B08511031
% Workers 16 Years and Over: Worked At Home: Native.1,PCT_ACS09_5yr_B08511032
% Workers 16 Years and Over: Worked At Home: Foreign Born.1,PCT_ACS09_5yr_B08511033
% Workers 16 Years and Over: Worked At Home: Foreign Born: Naturalized U.s. Citizen.1,PCT_ACS09_5yr_B08511034
% Workers 16 Years and Over: Worked At Home: Foreign Born: Not a U.s. Citizen.1,PCT_ACS09_5yr_B08511035
Workers 16 Years and Over.15,ACS09_5yr_B08513001
Workers 16 Years and Over: Speak Only English.1,ACS09_5yr_B08513002
Workers 16 Years and Over: Speak Spanish.1,ACS09_5yr_B08513003
"Workers 16 Years and Over: Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513004
"Workers 16 Years and Over: Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513005
Workers 16 Years and Over: Speak Spanish: Speak Other Languages.1,ACS09_5yr_B08513006
"Workers 16 Years and Over: Speak Spanish: Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513007
"Workers 16 Years and Over: Speak Spanish: Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513008
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.9",ACS09_5yr_B08513009
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Only English.1",ACS09_5yr_B08513010
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish.1",ACS09_5yr_B08513011
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513012
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513013
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages.1",ACS09_5yr_B08513014
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513015
"Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513016
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled.9",ACS09_5yr_B08513017
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Only English.1",ACS09_5yr_B08513018
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish.1",ACS09_5yr_B08513019
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513020
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513021
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages.1",ACS09_5yr_B08513022
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513023
"Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513024
Workers 16 Years and Over: Public Transportation (Excluding Taxicab).10,ACS09_5yr_B08513025
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Only English.1,ACS09_5yr_B08513026
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish.1,ACS09_5yr_B08513027
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513028
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513029
Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages.1,ACS09_5yr_B08513030
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513031
"Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513032
Workers 16 Years and Over: Walked.10,ACS09_5yr_B08513033
Workers 16 Years and Over: Walked: Speak Only English.1,ACS09_5yr_B08513034
Workers 16 Years and Over: Walked: Speak Spanish.1,ACS09_5yr_B08513035
"Workers 16 Years and Over: Walked: Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513036
"Workers 16 Years and Over: Walked: Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513037
Workers 16 Years and Over: Walked: Speak Other Languages.1,ACS09_5yr_B08513038
"Workers 16 Years and Over: Walked: Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513039
"Workers 16 Years and Over: Walked: Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513040
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.9",ACS09_5yr_B08513041
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Only English.1",ACS09_5yr_B08513042
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish.1",ACS09_5yr_B08513043
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513044
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513045
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages.1",ACS09_5yr_B08513046
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513047
"Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513048
Workers 16 Years and Over: Worked At Home.10,ACS09_5yr_B08513049
Workers 16 Years and Over: Worked At Home: Speak Only English.1,ACS09_5yr_B08513050
Workers 16 Years and Over: Worked At Home: Speak Spanish.1,ACS09_5yr_B08513051
"Workers 16 Years and Over: Worked At Home: Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513052
"Workers 16 Years and Over: Worked At Home: Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513053
Workers 16 Years and Over: Worked At Home: Speak Other Languages.1,ACS09_5yr_B08513054
"Workers 16 Years and Over: Worked At Home: Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513055
"Workers 16 Years and Over: Worked At Home: Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513056
Std. Error: Workers 16 Years and Over.15,ACS09_5yr_B08513001s
Std. Error: Workers 16 Years and Over: Speak Only English.1,ACS09_5yr_B08513002s
Std. Error: Workers 16 Years and Over: Speak Spanish.1,ACS09_5yr_B08513003s
"Std. Error: Workers 16 Years and Over: Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513004s
"Std. Error: Workers 16 Years and Over: Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513005s
Std. Error: Workers 16 Years and Over: Speak Spanish: Speak Other Languages.1,ACS09_5yr_B08513006s
"Std. Error: Workers 16 Years and Over: Speak Spanish: Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513007s
"Std. Error: Workers 16 Years and Over: Speak Spanish: Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513008s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone.9",ACS09_5yr_B08513009s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Only English.1",ACS09_5yr_B08513010s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish.1",ACS09_5yr_B08513011s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513012s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513013s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages.1",ACS09_5yr_B08513014s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513015s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Drove Alone: Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513016s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled.9",ACS09_5yr_B08513017s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Only English.1",ACS09_5yr_B08513018s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish.1",ACS09_5yr_B08513019s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513020s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513021s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages.1",ACS09_5yr_B08513022s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513023s
"Std. Error: Workers 16 Years and Over: Car, Truck, or Van - Carpooled: Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513024s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab).10,ACS09_5yr_B08513025s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Only English.1,ACS09_5yr_B08513026s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish.1,ACS09_5yr_B08513027s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513028s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513029s
Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages.1,ACS09_5yr_B08513030s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513031s
"Std. Error: Workers 16 Years and Over: Public Transportation (Excluding Taxicab): Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513032s
Std. Error: Workers 16 Years and Over: Walked.10,ACS09_5yr_B08513033s
Std. Error: Workers 16 Years and Over: Walked: Speak Only English.1,ACS09_5yr_B08513034s
Std. Error: Workers 16 Years and Over: Walked: Speak Spanish.1,ACS09_5yr_B08513035s
"Std. Error: Workers 16 Years and Over: Walked: Speak Spanish: Speak English ""very Well"".1",ACS09_5yr_B08513036s
"Std. Error: Workers 16 Years and Over: Walked: Speak Spanish: Speak English Less than ""very Well"".1",ACS09_5yr_B08513037s
Std. Error: Workers 16 Years and Over: Walked: Speak Other Languages.1,ACS09_5yr_B08513038s
"Std. Error: Workers 16 Years and Over: Walked: Speak Other Languages: Speak English ""very Well"".1",ACS09_5yr_B08513039s
"Std. Error: Workers 16 Years and Over: Walked: Speak Other Languages: Speak English Less than ""very Well"".1",ACS09_5yr_B08513040s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means.9",ACS09_5yr_B08513041s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Only English.1",ACS09_5yr_B08513042s
"Std. Error: Workers 16 Years and Over: Taxicab, Motorcycle, Bicycle, or Other Means: Speak Spanish.1",ACS09_5yr_B08513043s
