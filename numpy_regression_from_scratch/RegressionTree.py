import numpy as np
import pandas as pd
from numpy_regression_from_scratch.DataPreparation import data_preprocessing

class RegressionTree:
    def __init__(self, X=None,
                 y=None,
                 min_split=None,
                 maxm_depth=None,
                 depth=None,
                 node_type=None,
                 rule=None):

        #self.csv_path = csv_path
        self.X = X
        self.y = y

        # min samples to be present at each node for splitting
        self.min_split = min_split if min_split else 10
        # maximum depth the tree can grow
        self.maxm_depth = maxm_depth if maxm_depth else 5
        # current node depth
        self.depth = depth if depth else 0
        # node type
        self.node_type = node_type if node_type else "root"
        # features
        self.features = self.X.columns
        # rule for splitting the nodes, feature used for splitting
        self.rule = rule if rule else ""

        # initializing the left and right node
        self.left = None
        self.right = None

        #splitting attributes
        self.best_feature = None
        self.best_value = None

        # No.of samples
        self.n_samples = len(self.y)

        # Calculating mean of y
        self.y_mean = np.mean(self.y)

        # Calculating the impurity (mse) of the node
        self.mse = self.mse_calculator(self.y, self.y_mean)

        # Calculating the residuals of the node
        self.residual = self.y - self.y_mean

    def mse_calculator(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)


    # calculate mean of two consecutive numbers
    def moving_avg_calculator(self, val_array, consecutive_nos):
        return np.convolve(val_array, np.ones(consecutive_nos), "valid") / consecutive_nos

    # Calculating the best features and best value to split the node for decision tree
    def best_split_calculator(self):
        best_feature, best_value = None, None
        # creation of a dataframe combining X and y
        df = self.X.copy()
        df["y"] = self.y

        # gini impurity
        impurity = self.mse

        for feature in self.features:
            X_df = df.dropna().sort_values(feature) #sort to calculate moving avg
            x_mean = self.moving_avg_calculator(X_df[feature].unique(),2)

            # splitting the samples into left and right subtrees
            for value in x_mean:
                left_tree_y = X_df[X_df[feature] < value]["y"].values
                right_tree_y = X_df[X_df[feature] >= value]["y"].values

                # Calculating the mean and residuals for left and right subtrees
                left_tree_mean = np.mean(left_tree_y)
                right_tree_mean = np.mean(right_tree_y)
                left_tree_residual = left_tree_y - left_tree_mean
                right_tree_residual = right_tree_y - right_tree_mean

                # Concatinating the residuals
                total_residual = np.concatenate((left_tree_residual, right_tree_residual), axis=None)

                #calculate impurity to split
                impurity_split = np.mean(total_residual ** 2) #MSE

                # returning the best split
                if(impurity_split < impurity):
                    best_feature = feature
                    best_value = value
                    impurity = impurity_split #update the impurity score

        return best_feature, best_value

    def grow_tree_recursive(self):
        # Grow the regression tree recursively
        # creation of a dataframe combining X and y
        df = self.X.copy()
        df["y"] = self.y

        if(self.depth < self.maxm_depth and self.n_samples >= self.min_split):
            # getting best splitting configs
            current_best_feature, current_best_val = self.best_split_calculator()

            if current_best_feature is not None:
                self.best_feature = current_best_feature
                self.best_value = current_best_val

                # Splitting dataframe into left subtree df and right subtree df
                left_subtree_df = df[df[current_best_feature]<current_best_val].copy()
                right_subtree_df = df[df[current_best_feature] >= current_best_val].copy()

                # Creating the left and right node respectively
                left_node = RegressionTree(
                                 left_subtree_df[self.features],
                                 left_subtree_df["y"].values.tolist(),
                                 depth=self.depth+1,
                                 maxm_depth=self.maxm_depth,
                                 min_split=self.min_split,
                                 node_type="left_node",
                                 rule= f"{self.best_feature} <= {round(self.best_value,4)}")

                self.left = left_node
                self.left.grow_tree_recursive()

                right_node = RegressionTree(
                                 right_subtree_df[self.features],
                                 right_subtree_df["y"].values.tolist(),
                                 depth=self.depth + 1,
                                 maxm_depth=self.maxm_depth,
                                 min_split=self.min_split,
                                 node_type="right_node",
                                 rule=f"{self.best_feature} > {round(self.best_value, 4)}")

                self.right = right_node
                self.right.grow_tree_recursive()


    def display_tree_info(self, tree_width=4):
        # displays the information about the regression tree

        # dynamic space calculation based on depth of the node
        constant = int(self.depth * tree_width ** 1.5)
        total_spaces = "-" * constant

        if self.node_type.lower() =="root":
            print("ROOT")
        else:
            print(f"|{total_spaces} Rule for splitting :  {self.rule}")

        print(f"{'' * constant} | MSE of the current node : {round(self.mse,3)}")
        print(f"{'' * constant} | No. of observation in the node : {self.n_samples}")
        print(f"{'' * constant} | Node Prediction : {round(self.y_mean, 3)}")


    def display_tree(self):
        # main method to display the entire tree recursively
        self.display_tree_info()

        if self.left is not None:
            self.left.display_tree()

        if self.right is not None:
            self.right.display_tree()

    def RT_main(self, csv_path = None):

        if(csv_path):
            X_train, X_test, y_train, y_test = data_preprocessing(csv_path)
            root_node = RegressionTree(X_train, y_train, maxm_depth=2, min_split=3)

        # Growing the regression tree
        self.grow_tree_recursive()

        # Displaying the tree structure
        self.display_tree()


if __name__ == '__main__':
    csv_path = 'raw_data/EPL_Soccer_MLR_LR.csv'

    # Splitting data into train and test
    X_train, X_test, y_train, y_test = data_preprocessing(csv_path)

    # Generating root node
    root_node = RegressionTree(X_train, y_train, maxm_depth=2, min_split=3)
    root_node.RT_main()