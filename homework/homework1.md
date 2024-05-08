## Homework 1 
The first homework is about the basic concepts of machine learning. Questions are selected from the book *An introduction to statistical learning*.
The homework is due on 12th of February.
* For undergraduate students, answer 1-3 and 5. Question 4 is optional.
* For graduate students, answer all questions.

### Question 1 
For the following questions, indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.
The predictor is also known as an independent variable, feature, or input variable. The response is also known as a dependent variable or output variable.

1. The sample size $n$ is extremely large, and the number of predictors $p$ is small.

Since we have large sample size and number of predictors is small. The performance of flexible model will be poor than the inflexible one because the flexible model will try to capture complex pattern resulting more noise and resulting low performance.Furthermore, the data may not be complex enough or include enough information with a small number of predictors $p$ to allow the flexible method to be effectively utilized. In these situations, inflexible that force simpler structures or assumptions on the data could work better because they prevent overfitting and better capture the underlying patterns.

2. The number of predictors $p$ is extremely large, and the number of observations $n$ is small.

Inflexible methods would likely to perform worst like linear regression or logistic regression may struggle when faced with a large number of predictors and a small number of observations. These models often assume linear relationships between predictors and the response variable. With a large number of predictors, inflexible models may not capture the complex, non-linear relationships present in the data adequately.Also, Inflexible models typically have high bias and low variance. With a small number of observations, inflexible models may not have sufficient data to estimate the coefficients accurately, leading to biased parameter estimates. This can result in poor model performance and inaccurate predictions.

3. The relationship between the predictors and response is highly non-linear.

 Inflexible methods would likely to perform worst, like linear regression, assume a linear relationship between predictors and the response variable. They model the relationship using a straight line (or a hyperplane in higher dimensions). When the relationship is highly non-linear, such methods are unable to capture the complex and non-linear patterns in the data effectively.Also,Inflexible models lack the expressiveness and complexity required to model highly non-linear relationships adequately. They may struggle to represent the complex interactions and dependencies among predictors, leading to inadequate model fit and reduced predictive accuracy.

4. The variance of the error terms, i.e. $\sigma^2 = Var(\epsilon)$, is extremely high.

When the variance of the error terms (i.e., $\sigma^2 = \text{Var}(\epsilon)$) is extremely high, models that are sensitive to outliers and noise would typically perform the worst. In this scenario, linear regression models might perform poorly compared to robust regression techniques or models that are less affected by high variance.
Robust regression techniques, such as robust linear regression, ridge regression, or LASSO regression, are less sensitive to outliers and heteroscedasticity. These methods mitigate the impact of high variance in the error terms by downweighting the influence of outliers and imposing regularization on the regression coefficients. As a result, they tend to perform better in the presence of high variance in the error terms.

### Question 2 
Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide $n$ and $p$.

1. We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.

This is regression problem as we have quantitative data for a response and we are interested in inference and $n$ is 500 and $p$ is is 3.

2. We are considering launching a new product and wish to know whether it will be a *success* or a *failure*. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

This is classification problem as the response is in binary distribution and we are interested in predicting whether launching product will be a success or failure . $n$ is 20 and $p$ is 13.

3. We are interested in predicting the % change in the US dollar in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the dollar, the % change in the US market, the % change in the British market, and the % change in the German market.

This is regression problem as the response us dollar change is a quantitative variable and we are interested in predicting the change in dollar  and $n$ is there is weekly data so 7days=1 week now360/7 = 51 observation and $p$ is 3.

### Question 3
You will now think of some real-life applications for machine/statistical learning.

1. Describe three real-life applications in which classification might be useful. Describe the response, as well as the predictors. Is the goal of each application inference or prediction? Explain your answer.

i. Plant Disease Classification:

Response: Presence or absence of a specific plant disease (e.g., powdery mildew, leaf rust).
Predictors: Plant features and environmental factors, such as leaf color, texture, shape, size, humidity, temperature, and soil conditions.
Inference or Prediction: The primary goal is prediction. By analyzing plant features and environmental conditions, classification models can predict whether a plant is infected with a particular disease. This information is valuable for early disease detection, treatment planning, and disease management strategies in agriculture.

ii. Weed Detection in Crop Fields:

Response: Presence or absence of weeds in crop fields.
Predictors: Plant characteristics, color, texture, and spatial distribution in images captured by drones or agricultural robots, as well as environmental factors like soil moisture and temperature.
Inference or Prediction: The primary goal is prediction. Classification models are trained to distinguish between crop plants and weeds based on image data and environmental variables. By accurately detecting weeds in crop fields, farmers can implement targeted weed control strategies, reduce herbicide use, and optimize crop yields. Automated weed detection systems help farmers identify weed-infested areas early, allowing for timely intervention and resource-efficient crop management practices.

iii. Plant Species Identification:

Response: Plant species or genus classification.
Predictors: Morphological characteristics such as leaf shape, size, color, flower structure, stem characteristics, and growth patterns.
Inference or Prediction: The primary goal is prediction. Researchers aim to develop classification models that can accurately identify plant species or genera based on their morphological features. These models can be used for biodiversity studies, ecological monitoring, and conservation efforts. By automating the process of plant species identification, researchers can streamline field surveys, assess species distributions, and monitor changes in plant communities over time.

2. Describe three real-life applications in which regression might be useful. Describe the response, as well as the predictors. Is the goal of each application inference or prediction? Explain your answer.

i. The relationship between adverstising spending and sales is a real life regression where people might fit a regression model using advertising spending as a predictor and sales as a response variable. The goal is to make prediction.

ii. In agriculture scientist often use regression to measure the effect of fertilizer and water on crop yields. Yield is a response whereas fertilizer and water irrigation are predictor.The primary interest is often in understanding how changes in fertilizer application and water irrigation levels affect crop yields (inference).

iii. In plant breeding the primary goal of commonly used GBLUP model (Genomic Best Linear Unbiased Prediction) is prediction. By leveraging genomic data, GBLUP predicts the breeding value of individuals for traits of interest. However, GBLUP can also provide inference by estimating the genetic variance and heritability of traits, helping breeders understand the genetic basis of complex traits and guiding breeding decisions.

Here Response is Breeding value or phenotype of individuals (e.g., yield).
Predictors: Genotypic data, such as single nucleotide polymorphisms (SNPs) or genetic markers.

3. Describe three real-life applications in which cluster analysis might be useful.

In plant breeding research we use cluster often such as:

i. Genetic Diversity Assessment:

Clustering analysis helps assess the genetic diversity present within a plant breeding population.
Utility: By clustering plants based on genetic markers or phenotypic traits, breeders can identify distinct genetic groups or subpopulations within the breeding population. Understanding genetic diversity is crucial for selecting parents for crosses, designing breeding strategies, and conserving genetic resources.

ii.Trait-Based Selection:

Clustering assists in identifying plants with desirable traits for breeding programs.
Utility: Breeders can cluster plants based on phenotypic traits, such as yield, quality, drought tolerance, or disease resistance. By grouping plants with similar trait profiles, breeders can identify promising candidates for further evaluation and selection in breeding programs. Clustering helps streamline the breeding process by focusing efforts on plants with desired characteristics.

iii.Marker-Assisted Selection (MAS):

Clustering facilitates the identification of marker-trait associations for MAS.
Utility: Clustering methods help identify genetic markers associated with target traits of interest, such as disease resistance genes or quantitative trait loci (QTLs) for yield components. By clustering plants based on marker data and trait performance, breeders can detect marker-trait associations, prioritize markers for selection, and accelerate the development of improved cultivars through MAS.

### Question 4 
Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non-parametric approach)? What are its disadvantages?

Parametric method:

Parametric Methods uses a fixed number of parameters to build the model.
Parametric analysis is to test group means.
It is applicable only for variables.
It always considers strong assumptions about data.
Parametric Methods require lesser data than Non-Parametric Methods.
Parametric methods assumed to be a normal distribution.
Parametric methods have more statistical power than Non-Parametric methods.
Examples: Linear regression, Logistic Regression, Naïve Bayes Model, etc.

Non-parametric method:

Non-Parametric Methods use the flexible number of parameters to build the model.
A non-parametric analysis is to test medians.
It is applicable for both – Variable and Attribute.
It generally fewer assumptions about data.
Non-Parametric Methods requires much more data than Parametric Methods.
There is no assumed distribution in non-parametric methods.
Non-parametric methods have less statistical power than Parametric methods.
Examples: KNN, Decision Tree Model, etc.

Advantage of parametric over non paramteric:

More powerful: When the assumptions are met, parametric tests are generally more powerful than non-parametric tests, meaning they are more likely to detect a real effect when it exists.

More efficient: Parametric tests require smaller sample sizes than non-parametric tests to achieve the same level of power.

Provide estimates of population parameters: Parametric methods provide estimates of the population mean, variance, and other parameters, which can be used for further analysis.

Disadvantage of parametric approach:

Sensitive to assumptions: If the assumptions of normality, homogeneity of variance, and independence are not met, parametric tests can be invalid and produce misleading results.

Limited flexibility: Parametric methods are limited to the specific probability distribution they are based on.

May not capture complex relationships: Parametric methods are not well-suited for capturing complex non-linear relationships between variables.



### Question 5 
This exercies involves the `boston` housing dataset. Have a jupyter notebook ready to answer the following questions.
The `boston` dataset is in the folder `datasets` of this repository and describes housing values and other information about Boston census tracts.
1. Load the dataset and explore the variables by `pandas`
2. Use the `matplotlab` to plot the two variables/predictors `indus` vs `nox` by the following code:
```python
import matplotlib.pyplot as plt
plt.scatter(data.loc[:,'indus'], data.loc[:,'nox']) # data = pd.read_csv('datasets/boston.csv')
plt.show()
```
3. Use the `pandas` to list all the variables/predictors (columns).
4. After exploring the dataset, select the `medv` as the response/label 'y' and the rest of the variables as the predictors `X`.
5. Split the dataset into a training set and a testing set. The training set should be 70% of the original dataset and the test set is the rest 30%.
6. Train a linear regression model on the training set and evaluate its performance on the test set.
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)
mean_squared_error(y_test, y_pred)
```
