options(stringsAsFactors=F, scipen = 999)

pkg = 'Hmisc'
if (!require(pkg, character.only = TRUE)) {
  install.packages(pkg)
  library(pkg, character.only = TRUE)
}


setwd("C:/Users/cjong/Projects/python_projects/us_transportation_and_mental_health/brfss_cdc_data")


brfss <- sasxport.get("MMSA2014.xpt")
write.csv(brfss, file = "MMSA2014.csv")

brfss <- sasxport.get("MMSA2019.xpt")
write.csv(brfss, file = "MMSA2019.csv")
