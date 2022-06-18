import numpy as np

# MSE - Mean Squared Error
# MSE = (1/n) * Σ(y_true - y_pred) ** 2
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


# R2 Score -  It can be calculated by squaring the coefficient of correlation
# coefficient of correlation = corr_matrix[0, 1]
# we take [0,1] because it gives the correlation value between y_true and y_pred
def r2_score(y_true, y_pred):
    corr_matrix = np.corrcoef(y_true, y_pred)
    corr = corr_matrix[0, 1]
    return corr**2
