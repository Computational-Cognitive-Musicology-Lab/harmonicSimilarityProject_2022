data <- read.csv("data_top20.csv", header=TRUE, stringsAsFactors = FALSE)
exactlySame <- read.csv("exactlysame.csv", header=TRUE, stringsAsFactors = FALSE)
View(data)

library(ggplot2)
ggplot(data, aes(x = year)) +
  geom_bar()+
  theme(axis.text = element_text(size = 20),
        axis.title = element_text(size = 20))

ggplot(data, aes(x = beat)) +
  geom_bar()+
  xlab("meter")+
  theme(axis.text = element_text(size = 20),
        axis.title = element_text(size = 20))

ggplot(data, aes(x = original_key)) +
  geom_bar()+
  theme(axis.text = element_text(size = 19),
        axis.title = element_text(size = 20))

ggplot(data, aes(x = data_key)) +
  geom_bar()+
  theme(axis.text = element_text(size = 19),
        axis.title = element_text(size = 20))

#non-simplified
ggplot(filter(exactlySame, version == "top20v212"), 
       aes(x = year, y = count, fill = type)) +
  scale_fill_grey()+
  geom_bar(stat='identity', position=position_dodge())+
  theme(axis.text = element_text(size = 15),
        axis.title = element_text(size = 15))

#simplified
ggplot(filter(exactlySame, version == "top20v221"), 
       aes(x = year, y = count, fill = type)) +
  scale_fill_grey()+
  geom_bar(stat='identity', position=position_dodge())+
  theme(axis.text = element_text(size = 15),
        axis.title = element_text(size = 15))

#root
ggplot(filter(exactlySame, version == "top20v231"), 
       aes(x = year, y = count, fill = type)) +
  scale_fill_grey()+
  geom_bar(stat='identity', position=position_dodge())+
  theme(axis.text = element_text(size = 15),
        axis.title = element_text(size = 15))
  

