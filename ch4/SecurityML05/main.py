
from OptunaTuning import *
from MachineLearningMalware import *
from SaveModel import *


# メイン処理関数
def main():

    # データディレクトリ定義
    data_file_dir = "/home/hhoshino/data/ember2018"

    model_file_save = "/home/hhoshino/data/ember2018_model/detect_malware_model.h5"

    # パラメータチューニング
    study_obj = tuning_parameter(data_file_dir)

    # 機械学習実行(チューニングされたパラメータを利用)
    estimator = machine_learning_malware_data(data_file_dir, study_obj)

    # 機械学習モデルを保存
    save_model(data_file_dir, estimator, model_file_save)


if __name__ == '__main__':
    main()

