
from OptunaTuning import *
from MachineLearningMalware import *


# メイン処理関数
def main():

    # データディレクトリ定義
    data_file_dir = "/home/hhoshino/data/ember2018"

    # パラメータチューニング
    study_obj = tuning_parameter(data_file_dir)

    # 機械学習実行(チューニングされたパラメータを利用)
    machine_learning_malware_data(data_file_dir, study_obj)


if __name__ == '__main__':
    main()

