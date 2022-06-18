from numpy_regression_from_scratch.LinearRegression import LinearRegression
from numpy_regression_from_scratch.LassoRegression import LassoRegression
from numpy_regression_from_scratch.RidgeRegression import RidgeRegression
import pickle as pkl


class EngineClass:
    def __init__(self, csv_path, model_save_path):
        self.csv_path = csv_path
        self.model_save_path = model_save_path

    def main(self, type_="linear"):
        if type_ == "linear":
            linear_model = LinearRegression(
                lr=0.00001, n_iter=100, csv_path=self.csv_path
            )
            linear_model.LR_main()
            # Saving model in Output Folder
            pkl.dump(
                linear_model, open(self.model_save_path + "linear_model.pkl", "wb")
            )

        elif type_ == "lasso":
            lasso_model = LassoRegression(
                alpha=0.03, lr=0.00001, n_iter=100, csv_path=self.csv_path
            )
            lasso_model.LR_main()
            # Saving model in Output Folder
            pkl.dump(lasso_model, open(self.model_save_path + "lasso_model.pkl", "wb"))

        elif type_ == "ridge":
            ridge_model = RidgeRegression(
                alpha=0.03, lr=0.00001, n_iter=100, csv_path=self.csv_path
            )
            ridge_model.RR_main()
            # Saving model in Output Folder
            pkl.dump(ridge_model, open(self.model_save_path + "ridge_model.pkl", "wb"))


if __name__ == "__main__":
    csv_path = "raw_data/EPL_Soccer_MLR_LR.csv"
    model_save_path = "numpy_regression_from_scratch/data/Models/"
    eng_obj = EngineClass(csv_path, model_save_path)
    """    
    regressions = ["linear", "lasso", "ridge"]
    """
    eng_obj.main("ridge")
