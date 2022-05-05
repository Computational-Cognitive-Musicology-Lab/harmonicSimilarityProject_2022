CPSIdata <- read.csv("CPSI_data.csv", header=TRUE, stringsAsFactors = FALSE)
#CPSIdata$year <- as.factor(CPSIdata$year)
View(CPSIdata)
library(dplyr)
top20v112data = filter(CPSIdata, version=="top20v212")
aov1 <- aov(CPSI_verse~year,top20v112data)
summary(aov1)

tukey <- TukeyHSD(aov1)
tukey = as.data.frame(tukey$year)
tukey$pair = rownames(tukey)
ggplot(tukey, aes(colour=cut(`p adj`, c(0, 0.01, 0.05, 1), 
                             label=c("p<0.01","p<0.05","Non-Sig")))) +
  theme_bw(base_size = 16)+
  geom_hline(yintercept=0, lty="11", colour="grey30",size = 1) +
  geom_errorbar(aes(pair, ymin=lwr, ymax=upr), width=0.2,size = 1) +
  geom_point(aes(pair, diff),size = 2) +
  labs(colour="")+
  theme(axis.text.x = element_text(size = 14))
Versemean = aggregate(CPSIdata$CPSI_verse, by=list(CPSIdata$version,CPSIdata$year),mean)
Chorusmean = aggregate(CPSIdata$CPSI_chorus, by=list(CPSIdata$version,CPSIdata$year),mean)
colnames(Versemean) <- c("version","year","mean")
colnames(Chorusmean) <- c("version","year","mean")
View(Versemean)
library("trend")
mk.test(filter(Versemean, version=="top20v212")$mean, continuity = TRUE)
#library(DescTools)
#CochranArmitageTest(CAT)
sumverse = aggregate(Versemean$median, by=list(Versemean$year),median)
colnames(sumverse) <- c("year","median")
mk.test(sumverse$median, continuity = TRUE)


ggplot(Totalmean, aes(x=year, y=mean)) + 
  geom_boxplot()
CPSIdata$CPSI_total = CPSIdata$CPSI_verse+CPSIdata$CPSI_chorus
Totalmean = aggregate(CPSIdata$CPSI_total, by=list(CPSIdata$version,CPSIdata$year),mean)
colnames(Totalmean) <- c("version","year","mean")
Totalmean$year <- as.numeric(Totalmean$year)

sumtotal = aggregate(Totalmean$mean, by=list(Totalmean$year),mean)
colnames(sumtotal) <- c("year","mean")
mk.test(filter(sumtotal,year>2018)$mean, continuity = TRUE)
View(sumtotal)
