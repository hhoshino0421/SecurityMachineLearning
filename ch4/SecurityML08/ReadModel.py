
from tensorflow import keras


def read_model(model_file_path):
    # read model file
    new_model = keras.models.load_model(model_file_path)

    # for debug
    # モデルのアーキテクチャを表示
    # new_model.summary()

    return new_model
