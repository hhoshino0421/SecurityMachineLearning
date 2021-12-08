from PhishingData import *
from TuningParam import *
from PhingDataAfterTuning import *


# 処理開始関数
def startup_main():

    # フィッシングデータ処理
    phishing_main()

    # パラメータチューニング処理
    study = tuning_exec()

    # フィッシングデータ処理(チューニング後)
    phishing_after_tuning_main(study)


# エントリポイント関数
if __name__ == '__main__':
    startup_main()


