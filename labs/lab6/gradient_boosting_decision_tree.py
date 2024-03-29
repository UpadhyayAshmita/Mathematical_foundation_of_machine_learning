# gradient_boosting_decision_tree.py
import numpy as np
import pandas as pd
from decision_tree_regression import decisiontree

def RMSE(ypred, ytrue):
    """Calculate the Root Mean Squared Error."""
    return np.sqrt(np.mean((ypred.squeeze() - ytrue.squeeze())**2))

class GradientBoostingDecisionTree:
    def __init__(self, max_depth=8, n_estimators=10, lr=0.01, delta=1.0):
        self.max_depth = max_depth
        self.n_estimators = n_estimators
        self.lr = lr  # Learning rate (shrinkage)
        self.delta = delta  # Huber loss delta parameter

        self.gradient_coeff = []
        self.stop = n_estimators

        self.tree0 = decisiontree(max_depth=self.max_depth)
        self.trees = [decisiontree(max_depth=self.max_depth) for _ in range(n_estimators)]

    def fit(self, X, y):
        # Initial prediction using a single decision tree
        self.tree0.fit(X, y)
        y_pred = self.tree0.predict(X).reshape(-1, 1)
        residue = y - y_pred

        for idx, tree in enumerate(self.trees):
            # Stopping condition based on residue norm
            if np.linalg.norm(residue) < 1e-4:
                self.stop = idx
                break

            tree.fit(X, residue)
            pred = tree.predict(X).reshape(-1, 1)

            
            y_pred += self.lr * pred
            residue = y - y_pred
            
            
            residue = self.huber_loss_gradient(residue)

    def predict(self, X):
        y_pred = self.tree0.predict(X).reshape(-1, 1)
        for idx, tree in enumerate(self.trees[:self.stop]):
            pred = tree.predict(X).reshape(-1, 1)
            y_pred += self.lr * pred
        return y_pred

    def huber_loss_gradient(self, residue):
        """Calculate the gradient of the Huber loss."""
        return np.where(np.abs(residue) <= self.delta, residue, self.delta * np.sign(residue))

if __name__ == '__main__':
    X_train_path = 'datasets/airfoil/airfoil_self_noise_X_train.csv'
    y_train_path = 'datasets/airfoil/airfoil_self_noise_y_train.csv'
    X_test_path = 'datasets/airfoil/airfoil_self_noise_X_test.csv'
    y_test_path = 'datasets/airfoil/airfoil_self_noise_y_test.csv'

    # Load data
    X_train = pd.read_csv(X_train_path).values
    y_train = pd.read_csv(y_train_path).values
    X_test = pd.read_csv(X_test_path).values
    y_test = pd.read_csv(y_test_path).values

    # Initialize and fit the model
    GBDT = GradientBoostingDecisionTree(n_estimators=200, max_depth=15, lr= 0.01)
    GBDT.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = GBDT.predict(X_test)
    print('RMSE:', RMSE(y_pred, y_test))
