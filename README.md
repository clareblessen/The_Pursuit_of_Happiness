# Predicting Happiness around the World
# The Data
The data comes from the World Happiness Report collected from Gallup World Poll. The World Happiness Report is a landmark survey of the state of global happiness. The first report was published in 2012, the second in 2013, the third in 2015, and the fourth in the 2016 Update. The World Happiness 2017, which ranks 155 countries by their happiness levels, was released at the United Nations at an event celebrating International Day of Happiness on March 20th. The report continues to gain global recognition as governments, organizations and civil society increasingly use happiness indicators to inform their policy-making decisions. Leading experts across fields – economics, psychology, survey analysis, national statistics, health, public policy and more – describe how measurements of well-being can be used effectively to assess the progress of nations. The reports review the state of happiness in the world today and show how the new science of happiness explains personal and national variations in happiness.

# Variables
The scores are based on answers to the main life evaluation question asked in the poll. This question, known as the Cantril ladder, asks respondents to think of a ladder/Rank with the best possible life for them being a 10 and the worst possible life being a 0 and to rate their own current lives on that scale. The variables following the happiness score estimate the extent to which each of six factors – economic production/GDP, Family/social support, life expectancy, freedom, absence of corruption, and generosity.

# EDA
We want to first look at how countries and continent played a role on the happiness scale.
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/continentshappiness.png)



![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/map.png)


Looks like Europeans are generally happier than other parts of the world.

See if each variables distributions in histogram.
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/featurescorrelation.png)


# Feature Engineering
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/cor.png)

We decided to drop Health life expectancy because it violated the multicollinearity assumptions. And it was highly correlated with GDP, r>0.8
## Stepwise Selection
we want to use Stepwise selection to get the best variables with the most predcitvator power by automatic selection.
It seems like the selection methods kept all the variables.

# The Model
The model included categorical variable- continents: explained 80% of the variance, AIC is 736.

Happiness ~ 2.87+1.42GDP+0.47Family+1.48Freedom+0.14Trust_GovCorruption+0.62Generosity+0.062continent_Asia+0.78continent_Australia+0.48continent_Europe+0.78continent_North_America+0.85continent_South_America

The model without continent variable : explained 75% of the variance, AIC is 835.

## normality of error 
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/normality of error.png)

## Homoscedasticity assumption
![alt test](https://raw.githubusercontent.com/rockinhumingbird/Mod4_project/master/images/residualplot.png)




# Future Applications and Importance

It seems like the common criticism for "The World Happiness Report" is quite valid. A high focus on GDP and strongly correlated features such as health/ life expectancy.
It goes well with common wisdom that money makes you happy up to a certain threshold. Having good social/family support is extremely important. 
There are multiple external data sources such as world suicide rates, voting behavior data etc to see if certain factors correlates with behavioral patterns. 

