from PhishingData import *
from TuningParam import *
from PhingDataAfterTuning import *
from DecisionTree import *


# 処理開始関数
def startup_main():

    # フィッシングデータ処理
    phishing_main()

    # パラメータチューニング処理
    study = tuning_exec()

    # フィッシングデータ処理(チューニング後)
    phishing_after_tuning_main(study)

    # 決定木を利用したフィッシングサイト検知 パラメータチューニング処理
    study_obj = decision_tree_parameter_tuning()

    # 決定木を利用したフィッシングサイト検知処理関数
    decision_tree_main(study_obj)


# エントリポイント関数
if __name__ == '__main__':
    startup_main()


