import numpy as np
import pandas as pd
from termcolor import colored
from numpy_regression_from_scratch.DataPreparation import data_preprocessing
from numpy_regression_from_scratch.metrics import mean_squared_error, r2_score


class RidgeRegression:
    def __init__(self, alpha=1, lr=0.01, n_iter=1000, csv_path=None):
        # hyperparameters initialization
        self.alpha = alpha
        self.lr = lr
        self.n_iter = n_iter
        self.csv_path = csv_path
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # parameter initialization
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iter):
            # prediction
            y_pred = self.predict(X)

            # compute gradients
            dW = (-(2 * np.dot(X.T, (y - y_pred))) + (2 * self.alpha * self.weights)) / n_samples
            db = -2 * np.sum(y_pred - y) / n_samples

            # update parameters
            self.weights -= self.lr * dW
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

    def RR_main(self):
        # Splitting data into train and test
        X_train, X_test, y_train, y_test = data_preprocessing(self.csv_path)

        # model fit and predict
        self.fit(X_train, y_train)
        ridge_predict = self.predict(X_test)

        # Metrics
        print(colored((f"MSE of Ridge Model : {mean_squared_error(y_test, ridge_predict)}"), "red"))
        print(colored((f"R2 Score of Ridge Model: {r2_score(y_test, ridge_predict)}"), "red"))


if __name__ == '__main__':
    csv_path = 'raw_data/EPL_Soccer_MLR_LR.csv'

    # lr = learning rate
    # n_iter = no. of iterations
    ridge_model = RidgeRegression(alpha=0.03, lr=.00001, n_iter=100, csv_path=csv_path)
    ridge_model.RR_main()