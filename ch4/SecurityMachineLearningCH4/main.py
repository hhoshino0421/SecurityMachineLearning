
from vector_data_make import *
from standard_scaler import *


def main():

    # ベクターデータ作成処理
    # vector_data_make_main()

    # 特徴量の標準化
    x_train_standard, x_test_standard, y_train, y_test = standard_scaler_main()

    #


if __name__ == '__main__':
    main()

