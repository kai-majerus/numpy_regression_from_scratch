import numpy as np
import pandas as pd


# Creating Train and Test data
def data_shuffler(X, y, seed=None):
    # randomly shuffling data in X and y
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0]) #creating indices
    np.random.shuffle(idx) #shuffling the indices
    try:
        return X[idx], y[idx]
    except:
        return X.iloc[idx], y.iloc[idx]


def Train_Test_Split(X, y, train_size=0.5, seed=None, shuffle=True):
    # splitting the X and y into train and test set
    if shuffle:
        X, y = data_shuffler(X, y, seed)
    # Split the training data from test data in the ratio specified in test_size
    idx_split = len(y) - int(len(y) // (1 / (1-train_size)))
    X_train, X_test = X[:idx_split], X[idx_split:]
    y_train, y_test = y[:idx_split], y[idx_split:]

    return X_train, X_test, y_train, y_test


def data_preprocessing(csv_path=None):
    X_train, X_test, y_train, y_test = None, None, None, None
    if(csv_path):
        # reading csv as a pandas dataframe
        df = pd.read_csv(csv_path)

        # dropping Null and removing categorical columns
        df.dropna(axis=0, how='all', thresh=None, subset=None, inplace=True)
        df = df.select_dtypes(['number'])

        # Finding correlated features
        X = df.drop(columns=['Score'])  # independent features
        y = df['Score']  # dependent feature

        print("Original Shape of X : ", X.shape)

        correlated_features = set()
        correlation_matrix = X.corr()
        for i in range(len(correlation_matrix.columns)):
            for j in range(i):
                # Finding positively or negatively correlated
                if abs(correlation_matrix.iloc[i, j]) > 0.8:
                    colname = correlation_matrix.columns[i]
                    correlated_features.add(colname)

        print("Correlated Features : ", correlated_features)

        # Dropping the Correlated features from X
        X.drop(columns=correlated_features, axis=1, inplace=True)

        print("Shape of X after dropping correlated features : ", X.shape)

        X_train, X_test, y_train, y_test = Train_Test_Split(X, y, seed=42, train_size=0.8)

    return X_train, X_test, y_train, y_test