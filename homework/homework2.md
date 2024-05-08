## Homework 2
Homework 2 is about K-nearest neighbors, t-SNE, and Gradient Descent.
Homework 2 is due on March 8th, 2024.

For the submission, all your work should be push the repository, `homework/homework2/`. 
As typing math equations is not easy, you can write your answers by hand and scan it.
Otherwise, you will not get the full credits (-5%).

### Question 1
The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.
| Obs. | X1 | X2 | X3 | Y     |
|------|----|----|----|-------|
| 1    | 0  | 3  | 0  | Red   |
| 2    | 2  | 0  | 0  | Red   |
| 3    | 0  | 1  | 3  | Red   |
| 4    | 0  | 1  | 2  | Green |
| 5    | -1 | 0  | 1  | Green |
| 6    | 1  | 1  | 1  | Red   |
Suppose we wish to use this data set to make a prediction for $Y$ when $X1 = X2 = X3 = 0$ using K-nearest neighbors. <br>
(a) Compute the Euclidean distance between each observation and the test point, $X1 = X2 = X3 = 0$. <br>
(b) What is our prediction with K = 1? Why? <br>
- with k=1, we select the observation closest to test point., i.e., the closest observation is obs 5(green). Therefore, our prediction is green.<br>

(c) What is our prediction with K = 3? Why? <br>
- with k=3, we select closest three obs. The closest three obs are 5(green), 2(Red), and 6(red). Among these, red is majority so our prediction is Red.<br>

(d) If the Bayes decision boundary in this problem is highly non-linear, then would we expect the best value for K to be large or small? Why? <br>
- if the bayes decision boundary is non-linear we would expect best value for K to be small. This is because smaller k value results in more flexible decision boundaries, which can capture non-linear relationships.

### Question 2
Carefully explain the differences between the KNN classifier and the KNN regression methods. <br>
- KNN Classifier:<br>
* Used for classification tasks where the output variable is categorical.<br>
* Predicts the class of a data point by finding the majority class among its k nearest neighbors.<br>
* Works well with discrete data and classification problems with non-linear decision boundaries.<br>
* The output is a class label.<br>

KNN Regression:<br>
* Used for regression tasks where the output variable is continuous.<br>
* Predicts the value of a data point by averaging the values of its k nearest neighbors.<br>
* Works well with continuous data and regression problems with non-linear relationships.<br>
* The output is a numerical value representing the predicted target variable.<br>

### Question 3
We cover the SNE, symmetric SNE and t-SNE in the class.
* (a) What does the SNE algorithm try to minimize? <br>
- SNE minimizes the difference between the distances of points in high-dimensional space and their projections in low-dimensional space, aiming to preserve local and global structure within the data.<br>

* (b) Calculate the gradient of the SNE cost function with respect to $y_i$. <br>
* (c) Calculate the gradient of the symmetric SNE cost function with respect to $y_i$. <br>
* (d) Calculate the gradient of the t-SNE cost function with respect to $y_i$. <br>

### Question 4
Consider the fitted values that result from performing linear regression without an intercept. In this setting, the i-th fitted value takes the form

\[ \hat{y}_i = x_i \hat{\beta}, \]

where

\[ \hat{\beta} = \left( \sum_{i=1}^{n} x_i y_i \right) / \left( \sum_{i'=1}^{n} x_{i'}^2 \right). \]

Show that we can write

\[ \hat{y}_i = \sum_{i'=1}^{n} a_{i'} y_{i'}. \]

What is \( a_{i'} \)?

**Note**: We interpret this result by saying that the fitted values from linear regression are linear combinations of the response values.

### Question 5 
The last question is about the gradient descent of logistic regression.
In the gitlab repository, there is a folder `code` including the gradient descent algorithm for linear regression. The task here is to write the gradient descent algorithm for the logistic regression. Requirement: the function is called `LogisticRegression` and is implemented in a class with the following structure.
```python
def sigmoid(z):
    return # the sigmoid function

class LogisticRegression:
    def __init__(self, M, N, lr = 0.1):
        self.M  = M
        self.N  = N
        self.lr = lr
        self.W  = np.zeros((N, 1))
        self.b  = 0.
        self.scaler = StandardScaler()

    def fit(self, X, y, epoch=2000, visual=False):
        self.scaler.fit(X)
        X = self.scaler.transform(X)

        # perform the gradient descent
        for i in range(epoch):

    def predict(self, X_test):
        X_test = self.scaler.transform(X_test)
        y_hat  = sigmoid(np.dot(X_test, self.W)+self.b)
        return np.where(y_hat>0.5, 1, 0)

    def loss_fcn(self, X, y):
        y_hat  = sigmoid(np.dot(X, self.W) + self.b)
        return -np.sum(y*np.log(y_hat)+(1-y)*np.log(1-y_hat))/self.M
```
