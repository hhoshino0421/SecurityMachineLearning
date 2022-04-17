
from MalwareAnalize import *


# メイン関数
def main():

    # 定数定義
    # 検査対象ファイルパス
    file_path_name = "/home/hhoshino/data/file/putty.exe"
    # 学習済モデルファイルパス
    model_file_path = "/home/hhoshino/data/ember2018_model/detect_malware_model.h5"

    # ファイル判定処理
    malware_file_analyze(file_path_name, model_file_path)


# プログラムのエントリポイント関数
if __name__ == '__main__':
    main()

