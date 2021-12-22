
from MalwareProfile import *
from MalwareFutureSelect import *
from MalwareFutureRandomForest import *


# メイン関数
def main_func():

    # マルウェアデータプロファイル
    # malware_profile_main()

    # 特徴量機械学習
    # malware_future_select()

    # ランダムフォレストのパラメータチューニング処理
    study_obj, x_obj, y_obj = malware_future_select_random_forest_tuning()

    # ランダムフォレストでの機械学習処理
    malware_random_forest_learning(study_obj, x_obj, y_obj)


# エントリポイント関数
if __name__ == '__main__':
    main_func()
