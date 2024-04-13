## Homework 3
This homework is due on 04/15/2024 by 11:59 PM. Homework 3 is about resampling methods and decision trees.

### Question 1 
The bootstrap is one part of the bagging algorithm. 
At its core, bootstrap involves repeatedly resampling, with replacement, from the observed data set and recalculating the statistic of interest on each resample. This process builds an empirical distribution of the statistic, providing insight into its variability without requiring stringent assumptions about the underlying population distribution from which the sample was drawn.

The bootstrap is a statistical technique that allows you to estimate the distribution of a statistic (such as the mean, median, or standard deviation) of a population from a sample of data. Its beauty lies in its simplicity and versatility, making it applicable across a wide range of situations in statistical inference, where understanding the variability of an estimator is crucial. Here's how it works and why it's so powerful:

### Step-by-Step Explanation

1. **Original Sample**: You start with an original sample of \(n\) observations, which serves as a proxy for the larger population. This sample is presumed to contain enough information to model the variability of the population.

2. **Bootstrap Samples**: From this original sample, you generate a large number of bootstrap samples. Each bootstrap sample is the same size as the original and is created by randomly selecting observations from the original data with replacement. This means any observation can appear more than once or not at all in each bootstrap sample.

3. **Calculate Statistics**: For each bootstrap sample, calculate the statistic of interest (e.g., mean, variance). Because you're working with a high number of bootstrap samples, you'll get a wide array of values for the statistic.

4. **Estimate Distribution**: The collection of calculated statistics from all the bootstrap samples forms an empirical distribution. This distribution approximates the sampling distribution of the statistic if you were able to draw infinite samples from the population.

5. **Quantify Uncertainty**: With the empirical distribution, you can now quantify the uncertainty of the estimator. For example, you can estimate the standard error, confidence intervals, or prediction intervals of the statistic, providing a robust measure of its reliability.

### Questions
We will now derive the probability that a given observation is part of a boostrap sample. Suppose that we obtain a boostrap sample from a set of $n$ observations. 

1. What is the probability that the first bootstrap observation is not the $j$th observation from the original sample? Justify your answer.\
Ans: Every observation in the sample has  a 1/n chance of being selected in a single bootstrap draw.
Therefore, the probability of not selecting a particular observation i.e jth one is 1-1/n.
When we bootstrap, each draw from the original sample is independent, and every observation has an equal chance of being selected. Since the bootstrap sample is of the same size as the original sample
(n observations), each draw is likely to picking one observation out of n, with replacement, meaning the same observation can be chosen multiple times across different draws.

2. What is the probability that the second bootstrap observation is not the $j$th observation from the original sample? Justify your answer.\
Ans: Just as with the first observation, each draw from the original sample of n observations is independent and made with replacement. Therefore, the probability that any single observation, including the second observation, is not the jth observation from the original sample is 1-1/n. 
We can justify this with these principles of bootstrap sampling:
Independence of Draws: Each draw is independent of previous draws. The outcome of the first draw does not influence the outcome of the second draw.
Equal Probability for Each Observation: On each draw, every observation from the original sample has an equal chance of being selected, which is 1/n.
Sampling With Replacement: After an observation is selected, it is "replaced" in the pool, meaning it can be selected again. Thus, the selection probabilities remain constant across draws.

3. Argue that the probability that the $j$th observation is not in the bootstrap sample is $(1-1/n)^n$.
The probability that a given jth observation is not included in a bootstrap sample, when the sample is drawn with replacement from an original set of n observations, is calculated using the concept of independent selection. Since each observation has an equal chance of 1/n of being selected in each draw, the probability of not selecting the jth observation in a single draw is 1−1/n. Given that the bootstrap sample consists of n such independent draws, the probability that the jth observation is not included in any of the draws is the product of its probability of not being selected across all n draws, which is (1−1/n)^n.



4. When $n = 5$, what is the probability that the $j$th observation is in the bootstrap sample? 
For n=5, the probability that the jth observation is included in the bootstrap sample is approximately 0.6723.
5. When $n = 100$, what is the probability that the $j$th observation is in the bootstrap sample?
Forn=100, the probability that the jth observation is included in the bootstrap sample is approximately 0.6340.
6. When $n = 10000$, what is the probability that the $j$th observation is in the bootstrap sample?
For n=10,000, the probability that the jth observation is included in the bootstrap sample is approximately 0.6321.
7. Create a plot that shows how the probability that the $j$th observation is in the bootstrap sample changes as $n$ increases from 1 to 10000. Comment on what you observe. (Need coding)
We can observe initial fluctutation i.e for a very small sample size, the probablility shows more significant fluctutations and also each additonal observation in a samll sample significantly changes the selection dynamics. Also, we can observe the probability quickly stabilizes and converges as n increases and this shows the diminishing impact of each observation added on the probability of any observation's inclusion.

## Question 2 
a. Explain how $k$-fold cross-validation is implemented.
first we split the dataset into k- equal sized folds or subsets and for each iteration, one of the $k$ subsets is used as the test set (or validation set), and the remaining $k-1$ subsets are combined to form a training set. Then the model is trained using training set and validated on the test set and we can assess the model accuracy, R2 for each iterations. We further repeat the iterations and model training steps which gives us k different models and their performance. At the end we obtain performance estimates from kth iterations and then we aggregate that to achieve a single performace metric by taking average of metric accross all kth iterations.

b. What are the advantages and disadvantages of $k$-fold cross-validation relative to LOOCV?\
One of the significant advantages of k-fold cross-validation over Leave-One-Out Cross-Validation (LOOCV) is its efficiency in terms of computational resources and time, especially for large datasets or complex models. In k-fold cross-validation, the original dataset is divided into $k$ smaller subsets, and the model is trained and validated $k$ times, each time with a different subset as the validation set and the remaining $k-1$ subsets combined as the training set. This process requires significantly fewer iterations than LOOCV, which trains the model $N$ times for a dataset with $N$ observations. Furthermore, $k$-fold cross-validation tends to provide a more reliable estimate of model performance by reducing the variance associated with the performance measurement. Since LOOCV evaluates the model on $N$ highly similar training datasets (each missing only one observation from the full dataset), it can lead to higher variance in performance estimates due to the high correlation between the training sets used in each iteration. Additionally, $k$-fold cross-validation allows for a more in-depth analysis of the model’s stability by assessing performance across different training and validation splits, offering insights into how the model might perform under varying conditions.

- Leave-one-out cross-validation (LOOCV) is a special case of $k$-fold cross-validation where $k$ is equal to the number of observations in the data set.
The learning method is fit on the $n-1$ training observations and a prediction is made for the excluded observation. This process is repeated $n$ times, with each of the $n$ observations used exactly once as the validation data. The $n$ validation errors are then averaged to obtain the LOOCV estimate of the test error.

## Question 3 
Consider the Gini index, classification error, and entropy in a simple classification setting with two classes. 
Create a single plot that displays each of these quantities as a function of \(\hat{p}_{mk}\). The x-axis should display \(\hat{p}_{mk}\), ranging from 0 to 1, and the y-axis should display the value of the Gini index, classification error, and entropy.

Hint: In a setting with two classes, \(\hat{p}_{m1} = 1 - \hat{p}_{m2}\). The Gini index is given by \(2\hat{p}_{m1}\hat{p}_{m2}\), the classification error is given by \(1 - \max(\hat{p}_{mk}, 1 - \hat{p}_{mk})\), and the entropy is given by \(-\hat{p}_{mk}\log_2(\hat{p}_{mk}) - (1 - \hat{p}_{mk})\log_2(1 - \hat{p}_{mk})\).

## Question 4 
Suppose we produce ten bootstrapped samples from a data set containing red and green classes. We then apply a classification tree to each bootstrapped sample and, for a specific value of $X$, produce 10 estimates of $P(\text{Class} = \text{Green} | X)$

\[0.1, 0.15, 0.2, 0.2, 0.55, 0.6, 0.6, 0.65, 0.7, 0.75\]

There are two common ways to combine these results together to produce a single class prediction. One is the majority vote approach, where the most commonly occurring class is predicted. The other is the average probability approach, where the average of the estimated probabilities is taken.
In this example, what is the final prediction under each of these two approaches?\
Ans: \
Majority Vote Approach:
In the majority vote approach, we look at each probability estimate and classify each one as a vote for "Green" if the probability is greater than 0.5 (since it indicates that the probability of being Green is more likely than not), and as a vote for "Red" if the probability is 0.5 or less.\
Votes for Green: 6 (for probabilities 0.55, 0.6, 0.6, 0.65, 0.7, 0.75)\
Votes for Red: 4 (for probabilities 0.1, 0.15, 0.2, 0.2)\
Since there are more votes for Green, the majority vote prediction is Green.\

Average Probability Approach
Here, we simply calculate the average of the estimated probabilities and compare the average to 0.5. If the average is greater than 0.5, the prediction is "Green"; otherwise, it's "Red".\
The average of the probabilities is calculated as follows:\
Average =(0.1+0.15+0.2+0.2+0.55+0.6+0.6+0.65+0.7+0.75)/ 10 \
Let's calculate this average to determine the final prediction.\
Under the average probability approach, the average of the estimated probabilities is 0.45. Since this average is less than 0.5,the final prediction based on the average probability approach is Red.

## Question 5 
This is a semi report of your project. You need to write a brief summary of your project and the steps you have taken so far.

If you choose the project 1, you need to write 
1. how you have split the data
I have splitted one year 2020 as train and 2021 as a test
2. what models you have used, 
I have fitted linear regression a simple one and then started building for complex which is random forest for my data.
3. what are the results of your models,
The results is accuracy, as in plant breeding even if we have regression data accuracy i.e corelation between predicted estimated breeding value and actual phenotypic observation matters the most to rank the genotype and also I have calculated RMSE to follow standard approach 
4. how you process the grid search,
I have eused grid search function
5. and what are the best parameters you have found.

Also, you need to write what you are planning to do next.

If you choose the project 2, you need to write how you understand the method, what you have done so far, and what you are planning to do next.
