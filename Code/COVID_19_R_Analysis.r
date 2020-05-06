#Kaggle: Novel Coronavirus 2019 Dataset

#Import the data
library(ggplot2)
options(max.print = 1000000000)
getOption("max.print")
datax = read.csv("C:/Users/admin/Downloads/covid_19_data.csv")
datax
data = datax[(datax$Country.Region=='US'),]
data


##STATISTICAL ANALYSIS##


#Find the Mean of the following: Deaths, Recovered, and Confirmed Cases

#Mean of Deaths:
deaths = data$Deaths
m_death = mean(deaths)
#Mean of Recovered:
recovered = data$Recovered
m_recovered = mean(recovered)
#Mean of Confirmed Cases:
confirmed = data$Confirmed
m_confirmed = mean(confirmed)

#Combine all of the means into a Data Frame: 
Covid_Mean = data.frame(m_death, m_confirmed, m_recovered)
Covid_Mean





#Find the Median of the following: Deaths, Recovered, and Confirmed Cases

#Median of Deaths:
med_death = median(deaths)
#Median of Recovered:
med_recovered = median(recovered)
#Median of Confirmed Cases:
med_confirmed = median(confirmed)

#Combine all of the medians into a Data Frame: 
Covid_Median = data.frame(med_death, med_confirmed, med_recovered)
Covid_Median






#Find the Pearson Correlation of the Compared Groups: 

#Linear Significance of Deaths versus Recovered: 
death_v_recovered = cor(deaths,recovered, method = "pearson")
paste("The pearson correlation of", death_v_recovered, "represents a negative linear correlation")

#Linear Significance of Recovered versus Confirmed: 
recovered_v_confirmed = cor(recovered,confirmed, method = "pearson")
paste("The pearson correlation of", recovered_v_confirmed, "represents a negative linear correlation")

#Linear Significance of Deaths versus Confirmed: 
death_v_confirmed = cor(deaths,confirmed, method = "pearson")
paste("The pearson correlation of", death_v_confirmed, "represents a positive linear correlation")




#Find the p-value via T-test of the Compared Groups: 

#Deaths versus Recovered: T-test 
d_v_r_t = t.test(recovered, deaths, paired = FALSE)
d_v_r_t
paste("The p-value provided of", 0.03726, "shows that the death and recovered data is significant and that the averages are similar.")
#Recovered versus Confirmed: T-test
r_v_c_t = t.test(confirmed, recovered, paired = FALSE)
r_v_c_t
paste("The p-value provided of", "< 2.2e-16", "shows that the death and recovered data is significant and that the averages are similar.")
#Deaths versus Confirmed: T-test
d_v_c_t = t.test(confirmed, deaths, paired = FALSE)
d_v_c_t
paste("The p-value provided of", "< 2.2e-16", "shows that the death and recovered data is significant and that the averages are similar.")




##PLOTTING##



#Scatter Plot: Observing Distribution of COVID-19 by Province/State
ggplot(data) + geom_point(mapping= aes(x= confirmed, y= deaths, color= Province.State)) + geom_smooth(mapping= aes(x= confirmed, y= deaths), method= 'lm',se= FALSE) + theme(legend.position = 'bottom') + ggtitle("                                                                                                                                    United States of America: Distribution of COVID-19 Deaths based on Province/State")





# Line plot: Examining Death Rate of COVID-19 in the United States 
ggplot(data, mapping = aes(x=Confirmed, y=Deaths)) + geom_line() +ggtitle("                                                COVID-19 Deaths (March-April): United States of America")






#Pie Chart 

#COVID-19 Deaths vs Recovered
pizza <- c(sum(deaths), sum(recovered))
labels <-  c('Deaths', 'Recovered')
pct <- round(pizza/sum(pizza)*100)
labels <- paste(paste(labels, pct), "%", sep= " ")
pie(pizza, labels= labels,  main = 'United States of America: COVID-19 Deaths vs Recovered')


#COVID-19 Recovered vs Confirmed
doughnut <- c(sum(recovered), sum(confirmed))
labels <-  c('Recovered', 'Confirmed')
pct <- round(doughnut/sum(doughnut)*100)
labels <- paste(paste(labels, pct), "%", sep= " ")
pie(doughnut, labels= labels,  main = 'United States of America: COVID-19 Recovered vs Confirmed')


#COVID-19 Deaths vs Confirmed
pastry <- c(sum(deaths), sum(confirmed))
labels <-  c('Deaths', 'Confirmed')
pct <- round(pastry/sum(pastry)*100)
labels <- paste(paste(labels, pct), "%", sep= " ")
pie(pastry, labels= labels,  main = 'United States of America: COVID-19 Deaths vs Confirmed')









# Organizing COVID-19 Data: DC, Maryland, & Virginia
zeta <- subset(data, Province.State == c("Maryland", "Virginia"))
zeta
beta <- subset(data, Province.State == c("District of Columbia"))
beta
epsilon <- rbind(zeta, beta)
epsilon
rownames(epsilon) <- c(1:57)
epsilon

#Density Plot of COVID-19 in the DMV area:

alpha <- ggplot(epsilon) + geom_density(mapping = aes(x = Deaths, fill = Province.State), alpha= .6) + ggtitle("                                         Density of COVID-19 Deaths: DC, Maryland, & Virginia")
alpha
deltaz <- ggplot(epsilon)+ geom_density(mapping = aes(x = Recovered, fill = Province.State), alpha= .6) + ggtitle("                                         Density of COVID-19 Recoveries: DC, Maryland, & Virginia")
deltaz
omegaz <- ggplot(epsilon)+ geom_density(mapping = aes(x = Confirmed, fill = Province.State), alpha= .6) + ggtitle("                                         Density of COVID-19 Confirmed: DC, Maryland, & Virginia")
omegaz

