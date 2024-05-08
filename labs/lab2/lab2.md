# Lab2 plot inference<br>
# Regression: California dataset<br>
Inference of plot:
The plot typically includes a curve representing the training score (performance) of the regression model as a function of the training set size. The training score measures how well the model fits the training data. In california housing data,as the training set size increases,the training score is at plateau so we can imply that that the model is unable to benefit from additional data or is overfitting.<br>

The plot also includes a curve representing the cross-validation score (performance) of the regression model as a function of the training set size. The cross-validation score measures how well the model generalizes to unseen data. As the training set size is 2000 there is a gap between training score and cv curve so it suggest that the model is overfitting.  In this case, the model performs well on the training data but fails to generalize to unseen data. By increasing training size from 2000-4000, we were able to reduce overfitting. <br>

The learning curve function splits the dataset into training and validation sets for each specified training set size. It checks the performance of the model on each training set size so that we can know how the size of data effects the model's performance. If we can have a model that perform well on 2000 training data then why to add more data? <br>


# Logistic regression: Iris dataset<br>
Inference of plot:
Prediction accuracy is 1 meaning the performance of model is good. It successfully distinguishes between instances of class "Iris-Setosa" and instances of class "Not Iris-Setosa" based on the features (petal length and width) provided.The black dashed line represents the decision boundary learned by the logistic regression model. This boundary separates the regions where the model predicts "Iris-Setosa" from the regions where it predicts "Not Iris-Setosa".<br>

The predict_proba function is used to compute the predicted probabilities of each sample belonging to class 1 (Iris-Setosa) using a logistic regression model (log_reg).<br>
The predict_proba function is used to predict the probability of each class label, and it returns the probability estimates for each possible class label. This VVis used for multi-class classification problems, where we want to know the probability of each possible outcome.<br>