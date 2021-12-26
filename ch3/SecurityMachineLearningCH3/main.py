
from MalwareProfile import *
from MalwareFutureSelect import *
from MalwareFutureRandomForest import *
from MalwareGradientBoosting import *


# メイン関数
def main_func():

    # マルウェアデータプロファイル
    # malware_profile_main()

    # 特徴量機械学習
    # malware_future_select()

    # ランダムフォレストの処理------------------
    # ランダムフォレストのパラメータチューニング処理
    # study_obj, x_obj, y_obj = malware_future_select_random_forest_tuning()

    # ランダムフォレストでの機械学習処理
    # malware_random_forest_learning(study_obj, x_obj, y_obj)
    # ここまでランダムフォレストの処理-----------

    # 勾配ブースティングの処理------------------
    # 勾配ブースティングのパラメータチューニング処理
    study_obj, x_train, x_test, y_train, y_test = gradient_boosting_classifier_tuning()

    # 勾配ブースティングの機械学習処理
    gradient_boosting_classifier_execute(study_obj, x_train, x_test, y_train, y_test)
    # ここまで勾配ブースティングの処理-----------


# エントリポイント関数
if __name__ == '__main__':
    main_func()
