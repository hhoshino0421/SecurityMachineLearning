import pandas as pd

from read_data import *
from sklearn.preprocessing import StandardScaler


# 特徴量の標準化
def standard_scaler_main():

    x_train, y_train, x_test, y_test = read_data_main()

    train_rows = (y_train != -1)
    x_train_new = x_train[train_rows]
    y_train_new = y_train[train_rows]

    # orig_data = pd.DataFrame(x_train_new[6, :])
    #
    # orig_data.plot

    scalar_obj = StandardScaler()

    x_train_standard = scalar_obj.fit_transform(x_train_new)
    x_test_standard = scalar_obj.fit_transform(x_test)

    return x_train_standard, x_test_standard, y_train, y_test
