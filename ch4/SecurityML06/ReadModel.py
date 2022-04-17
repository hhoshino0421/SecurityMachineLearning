
import tensorflow as tf
from tensorflow import keras


# 学習済モデルファイル読み込み処理
def read_model(model_file_path):

    # read model file
    new_model = keras.models.load_model(model_file_path)

    # # for debug
    # # モデルのアーキテクチャを表示
    # new_model.summary()

    return new_model
    