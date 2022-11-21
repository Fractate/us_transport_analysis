# options(stringsAsFactors=F, scipen = 999)
# 
# pkg = 'Hmisc'
# if (!require(pkg, character.only = TRUE)) {
#   install.packages(pkg)
#   library(pkg, character.only = TRUE)
# }

library("devtools")
install_version("Hmisc", version = "3.17-2")



brfss <- sasxport.get("CNTY07.xpt")
write.csv(brfss, file = "CNTY07.csv")

brfss <- sasxport.get("CNTY09.xpt")
write.csv(brfss, file = "CNTY09.csv")

brfss <- sasxport.get("MMSA2019.xpt")
write.csv(brfss, file = "MMSA2019.csv")
