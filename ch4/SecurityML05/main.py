
from OptunaTuning import *


def main():

    # データディレクトリ定義
    data_file_dir = "/home/hhoshino/data/ember2018"

    # パラメータチューニング
    study_obj = tuning_parameter(data_file_dir)


if __name__ == '__main__':
    main()

