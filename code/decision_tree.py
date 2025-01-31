import numpy as np

def accuracy(ypred, ytrue):
    return np.sum(ypred==ytrue)/float(len(ypred))

class decisiontree():
    def __init__(self, max_depth=5, current_depth=0, max_features=None):
        # tree structure value
        self.left_tree = None
        self.right_tree = None
        self.max_depth = max_depth
        self.current_depth = current_depth

        self.best_feature_id = 0.
        self.best_gain = 0.
        self.best_split_value = 0.
        self.GINI = 0.
        self.label = None

        # feature values
        self.X = None
        self.y = None
        self.M = 0
        self.N = 0

        self.max_features = max_features

    def fit(self, X, y):
        self.X = X
        self.y = y
        self.M = X.shape[0]
        self.N = X.shape[1]

        if self.max_features==None or self.max_features>self.N:
            self.max_features = self.N
        if self.current_depth < self.max_depth:
            self.GINI = self.GINI_calculation(self.y)
            self.best_feature_id, self.best_gain, self.best_split_value = self.find_best_split()
            if self.best_gain > 0.:
                self.split_trees()

    def split_trees(self):
        self.left_tree = decisiontree(self.max_depth, self.current_depth+1)
        self.right_tree = decisiontree(self.max_depth, self.current_depth+1)
        best_feature_values = self.X[:, self.best_feature_id]
        left_indices = np.where(best_feature_values < self.best_split_value)
        right_indices = np.where(best_feature_values >= self.best_split_value)

        left_tree_X = self.X[left_indices]
        left_tree_y = self.y[left_indices]
        right_tree_X = self.X[right_indices]
        right_tree_y = self.y[right_indices]

        self.left_tree.fit(left_tree_X, left_tree_y)
        self.right_tree.fit(right_tree_X, right_tree_y)

    def GINI_calculation(self, y):
        if y.size==0 or y is None:
            return 0.
        unique, counts = np.unique(y, return_counts=True)
        prob = counts/y.size
        return 1.-np.sum(prob*prob)

    def find_best_split(self):
        best_feature_id  = None
        best_gain        = 0.
        best_split_value = None
        n_features = np.random.choice(self.N, self.max_features, replace=False)
        for feature_id in n_features:
            current_gain, current_split_value = self.find_best_split_one_feature(feature_id)
            if best_gain < current_gain:
                best_feature_id = feature_id
                best_gain = current_gain
                best_split_value = current_split_value
        return best_feature_id, best_gain, best_split_value

    def find_best_split_one_feature(self, feature_id):
        feature_values = self.X[:, feature_id]
        unique_feature_values = np.unique(feature_values)
        best_gain = 0.
        best_split_value = None

        if len(unique_feature_values) == 1:
            return best_gain, best_split_value

        for fea_val in unique_feature_values:
            left_indices = np.where(feature_values < fea_val)
            right_indices = np.where(feature_values >= fea_val)

            left_tree_X = self.X[left_indices]
            left_tree_y = self.y[left_indices]

            right_tree_X = self.X[right_indices]
            right_tree_y = self.y[right_indices]

            left_GINI = self.GINI_calculation(left_tree_y)
            right_GINI = self.GINI_calculation(right_tree_y)

            left_n = left_tree_X.shape[0]
            right_n = right_tree_X.shape[0]

            current_gain = self.GINI-left_n/self.M*left_GINI-right_n/self.M*right_GINI
            if best_gain < current_gain:
                best_gain = current_gain
                best_split_value = fea_val
        return best_gain, best_split_value

    def predict(self, X_test):
        n_test = X_test.shape[0]
        y_pred = np.empty(n_test, dtype=int)
        for i in range(n_test):
            y_pred[i] = self.tree_propogation(X_test[i])
        return y_pred

    def tree_propogation(self, feature):
        # this is a leaf
        if self.left_tree is None:
            return self.predict_label()
        # belongs to the left tree
        if feature[self.best_feature_id] < self.best_split_value:
            return self.left_tree.tree_propogation(feature)
        # belongs to the right tree
        else:
            return self.right_tree.tree_propogation(feature)

    def predict_label(self):
        if self.label != None:
            return self.label
        unique, counts = np.unique(self.y, return_counts=True)
        max_count = 0
        #idx = np.argmax(counts)
        #self.label = unique[idx]
        for i in range(unique.size):
            if counts[i] > max_count:
                max_count = counts[i]
                self.label = unique[i]
        return self.label

if __name__ == '__main__':
    import pandas as pd
    X_train = pd.read_csv('Digits_X_train.csv').values
    y_train = pd.read_csv('Digits_y_train.csv').values
    X_test  = pd.read_csv('Digits_X_test.csv').values
    y_test  = pd.read_csv('Digits_y_test.csv').values

    #DT = decisiontree()
    DT = decisiontree(max_depth=25)
    DT.fit(X_train, y_train)

    y_pred = DT.predict(X_test)
    print(accuracy(y_pred, y_test.ravel()))

    from sklearn.tree import DecisionTreeClassifier
    skDT = DecisionTreeClassifier()
    skDT.fit(X_train, y_train)
    y_pred = skDT.predict(X_test)
    print(accuracy(y_pred, y_test.ravel()))
else:
    print('class decisiontree imported from decision_tree.py')
