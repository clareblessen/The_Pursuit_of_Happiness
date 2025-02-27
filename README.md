# Predicting Happiness around the World
# The Data
The data comes from the World Happiness Report collected from Gallup World Poll. The World Happiness Report is a landmark survey of the state of global happiness. The first report was published in 2012. The 2017 World Happiness Report, which ranks 155 countries by their happiness levels, was released at the United Nations. The report continues to gain global recognition as governments, organizations and civil society increasingly use happiness indicators to inform their policy-making decisions. Leading experts across fields – economics, psychology, survey analysis, national statistics, health, public policy and more – describe how measurements of well-being can be used effectively to assess the progress of nations. The reports review the state of happiness in the world today and show how the new science of happiness explains personal and national variations in happiness.

# Variables
The scores are based on answers to the main life evaluation question asked in the poll. This question, known as the Cantril ladder, asks respondents to think of a ladder/Rank with the best possible life for them being a 10 and the worst possible life being a 0 and to rate their own current lives on that scale. The variables following the happiness score estimate the extent to which each of six factors – economic production/GDP, Family/social support, life expectancy, freedom, absence of corruption, and generosity.

# EDA
We want to first look at how countries and continent played a role on the happiness scale.
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/continentshappiness.png)



![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/map.png)


It looks like Europeans are generally happier than other parts of the world.

We then see if the variables are normally distributed and linearly correlated with happiness score.
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/featurescorrelation.png)


# Feature Engineering
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/cor.png)

We decided to drop Health life expectancy because it violated the multicollinearity assumptions as it it was highly correlated with GDP, r > 0.8, and GDP had higher predictive value. 

## Stepwise Selection
We used Stepwise selection based on training data split 70%/30% to get the best variables with the most predictive power by automatic selection.
The selection methods kept all the variables.

# The Model

-- Happiness ~ 3.25 + 1.41GDP + 1.48freedom + 0.42family + 0.14corruption + 0.10generosity + 0.08continent_Asia + 0.82continent_Australia + 0.5continent_Europe + 0.74continent_North_America + 0.84continent_South_America

Since we log transformed some independent variables, we can interpret the IV as follows: we’d say that a one percent increase in the average trust in government would result in a (1.01)exp.14 increase in the averge happiness. 

The model with continent variable : explained 80% of the variance, it also came to the lowest AIC 737.

## Normality of error 
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/normality_of_error.png)

## Homoscedasticity assumption
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/residualpolot.png)
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/qqplot.png)




# Future Applications and Importance
GDP per Capita and Freedom in a country have the greatest impact on its citizens' happiness.
There are multiple external data sources such as world suicide rates, voting behavior data etc we'd like to use in the future to see if certain factors correlates with behavioral patterns. 

