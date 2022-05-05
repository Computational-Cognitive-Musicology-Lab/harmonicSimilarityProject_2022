CPSIdata <- read.csv("CPSI_data.csv", header=TRUE, stringsAsFactors = FALSE)
CPSIdata$CPSI_total = CPSIdata$CPSI_verse+CPSIdata$CPSI_chorus
#CPSIdata$year <- as.factor(CPSIdata$year)
View(CPSIdata)

##anova test
library(dplyr)
##verse
top20v111data = filter(CPSIdata, version=="top20v111")
aov111 <- aov(CPSI_verse~year,top20v111data)
top20v112data = filter(CPSIdata, version=="top20v112")
aov112 <- aov(CPSI_verse~year,top20v112data)
top20v121data = filter(CPSIdata, version=="top20v121")
aov121 <- aov(CPSI_verse~year,top20v121data)
top20v122data = filter(CPSIdata, version=="top20v122")
aov122 <- aov(CPSI_verse~year,top20v122data)
top20v131data = filter(CPSIdata, version=="top20v131")
aov131 <- aov(CPSI_verse~year,top20v131data)
top20v132data = filter(CPSIdata, version=="top20v132")
aov132 <- aov(CPSI_verse~year,top20v132data)
top20v211data = filter(CPSIdata, version=="top20v211")
aov211 <- aov(CPSI_verse~year,top20v211data)
top20v212data = filter(CPSIdata, version=="top20v212")
aov212 <- aov(CPSI_verse~year,top20v212data)
top20v221data = filter(CPSIdata, version=="top20v221")
aov221 <- aov(CPSI_verse~year,top20v221data)
top20v222data = filter(CPSIdata, version=="top20v222")
aov222 <- aov(CPSI_verse~year,top20v222data)
top20v231data = filter(CPSIdata, version=="top20v231")
aov231 <- aov(CPSI_verse~year,top20v231data)
top20v232data = filter(CPSIdata, version=="top20v232")
aov232 <- aov(CPSI_verse~year,top20v232data)
summary(aov111)#0.00282 **
summary(aov112)#0.0557 .
summary(aov121)#0.00298 **
summary(aov122)#0.0145 *
summary(aov131)#0.00186 **
summary(aov132)#0.467
summary(aov211)#0.00327 **
summary(aov212)#0.0562 .
summary(aov221)#0.00271 **
summary(aov222)#0.0147 *
summary(aov231)#0.00219 **
summary(aov232)#0.565
##chorus
top20v111data = filter(CPSIdata, version=="top20v111")
aov111 <- aov(CPSI_chorus~year,top20v111data)
top20v112data = filter(CPSIdata, version=="top20v112")
aov112 <- aov(CPSI_chorus~year,top20v112data)
top20v121data = filter(CPSIdata, version=="top20v121")
aov121 <- aov(CPSI_chorus~year,top20v121data)
top20v122data = filter(CPSIdata, version=="top20v122")
aov122 <- aov(CPSI_chorus~year,top20v122data)
top20v131data = filter(CPSIdata, version=="top20v131")
aov131 <- aov(CPSI_chorus~year,top20v131data)
top20v132data = filter(CPSIdata, version=="top20v132")
aov132 <- aov(CPSI_chorus~year,top20v132data)
top20v211data = filter(CPSIdata, version=="top20v211")
aov211 <- aov(CPSI_chorus~year,top20v211data)
top20v212data = filter(CPSIdata, version=="top20v212")
aov212 <- aov(CPSI_chorus~year,top20v212data)
top20v221data = filter(CPSIdata, version=="top20v221")
aov221 <- aov(CPSI_chorus~year,top20v221data)
top20v222data = filter(CPSIdata, version=="top20v222")
aov222 <- aov(CPSI_chorus~year,top20v222data)
top20v231data = filter(CPSIdata, version=="top20v231")
aov231 <- aov(CPSI_chorus~year,top20v231data)
top20v232data = filter(CPSIdata, version=="top20v232")
aov232 <- aov(CPSI_chorus~year,top20v232data)
summary(aov111)#0.0141 *
summary(aov112)#0.0128 *
summary(aov121)#0.0575 .
summary(aov122)#0.204
summary(aov131)#0.873
summary(aov132)#0.519
summary(aov211)#0.0122 *
summary(aov212)#0.0113 *
summary(aov221)#0.24
summary(aov222)#0.19
summary(aov231)#0.922
summary(aov232)#0.47
##total
top20v111data = filter(CPSIdata, version=="top20v111")
aov111 <- aov(CPSI_total~year,top20v111data)
top20v112data = filter(CPSIdata, version=="top20v112")
aov112 <- aov(CPSI_total~year,top20v112data)
top20v121data = filter(CPSIdata, version=="top20v121")
aov121 <- aov(CPSI_total~year,top20v121data)
top20v122data = filter(CPSIdata, version=="top20v122")
aov122 <- aov(CPSI_total~year,top20v122data)
top20v131data = filter(CPSIdata, version=="top20v131")
aov131 <- aov(CPSI_total~year,top20v131data)
top20v132data = filter(CPSIdata, version=="top20v132")
aov132 <- aov(CPSI_total~year,top20v132data)
top20v211data = filter(CPSIdata, version=="top20v211")
aov211 <- aov(CPSI_total~year,top20v211data)
top20v212data = filter(CPSIdata, version=="top20v212")
aov212 <- aov(CPSI_total~year,top20v212data)
top20v221data = filter(CPSIdata, version=="top20v221")
aov221 <- aov(CPSI_total~year,top20v221data)
top20v222data = filter(CPSIdata, version=="top20v222")
aov222 <- aov(CPSI_total~year,top20v222data)
top20v231data = filter(CPSIdata, version=="top20v231")
aov231 <- aov(CPSI_total~year,top20v231data)
top20v232data = filter(CPSIdata, version=="top20v232")
aov232 <- aov(CPSI_total~year,top20v232data)
summary(aov111)#0.00205 **
summary(aov112)#0.014 *
summary(aov121)#0.00702 **
summary(aov122)#0.0384 *
summary(aov131)#0.0662 .
summary(aov132)#0.441
summary(aov211)#0.00191 **
summary(aov212)#0.0131 * 
summary(aov221)#0.0338 *
summary(aov222)#0.0365 *
summary(aov231)#0.0775 .
summary(aov232)#0.463

#qualified version: 111,112,211,212
qdata = filter(CPSIdata,version == "top20v111" | version == "top20v112" | 
                 version == "top20v211" | version == "top20v212")
View(qdata)


# plot
##verse data, chorus data: mean and median

versedata = aggregate(CPSIdata$CPSI_verse, 
                      by=list(CPSIdata$version,CPSIdata$year),
                      mean)
chorusdata = aggregate(CPSIdata$CPSI_chorus, 
                       by=list(CPSIdata$version,CPSIdata$year),
                       mean)
totaldata = aggregate(CPSIdata$CPSI_total, 
                      by=list(CPSIdata$version,CPSIdata$year),
                      mean)
versedata$median = aggregate(CPSIdata$CPSI_verse, 
                             by=list(CPSIdata$version,CPSIdata$year),
                             median)$x
chorusdata$median = aggregate(CPSIdata$CPSI_chorus, 
                             by=list(CPSIdata$version,CPSIdata$year),
                             median)$x
totaldata$median = aggregate(CPSIdata$CPSI_total, 
                              by=list(CPSIdata$version,CPSIdata$year),
                              median)$x
colnames(versedata) <- c("version","year","mean","median")
colnames(chorusdata) <- c("version","year","mean","median")
colnames(totaldata) <- c("version","year","mean","median")
View(versedata)

library(ggplot2)
ggplot(filter(totaldata,
              version=="top20v111"|version=="top20v112"
              |version=="top20v211"|version=="top20v212"), 
       aes(x=as.factor(year), y=median)) + 
  geom_boxplot()+
  labs(title = "CPSI(sum) median of v1.1.1, v1.1.2, v2.1.1 and v2.1.2", 
       x = "year", y = "median")+
  theme(plot.title = element_text(hjust = 0.5))

ggplot(filter(totaldata,
              version=="top20v111"|version=="top20v112"
              |version=="top20v211"|version=="top20v212"), 
       aes(x=as.factor(year), y=mean)) + 
  geom_boxplot()+
  labs(title = "CPSI(sum) mean of v1.1.1, v1.1.2, v2.1.1 and v2.1.2", 
       x = "year", y = "mean")+
  theme(plot.title = element_text(hjust = 0.5))