
from keras.backend import clear_session
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
# from tensorflow.keras.optimizers import Adam
# import tf.keras.optimizers.Adam
# from keras.optimizers import adam_v2
from keras.optimizer_v2 import adam

from FileDataRead import *


import numpy as np
import gc
import optuna

g_data_dir_g = ""


def read_file_data_self():

    return read_file_data(g_data_dir_g)


# パラメータチューニング処理メイン
def Objective(trial):

    # データ読み込み処理
    x_train, y_train, x_test, y_test = read_file_data_self()

    # データのコピー
    # データコピーするとメモリエラーになるのでコピーせずに使用する方式に変更
    # x_train_copy = np.copy(x_train)
    # y_train_copy = np.copy(y_train)

    # モデルの作成とパラメータ探索の設定
    model = Sequential()
    model.add(Dense(2048, activation='relu', input_dim=2381))
    # model.add(Dropout(rate=dropout_rate))
    dropout_rate = trial.suggest_uniform('dropout_rate', 0, 0.5)
    # model.add(Dropout)
    # model.add(Dropout(rate=0.2))
    model.add(Dropout(rate=dropout_rate))
    model.add(Dense(1024, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    optimizer = adam.Adam(learning_rate=trial.suggest_loguniform("learning_rate", 1e-5, 1e-1),
                          beta_1=trial.suggest_uniform("beta_1", 0.0, 1.0),
                          beta_2=trial.suggest_uniform("beta_2", 0.0, 1.0)
                          )

    model.compile(loss='binary_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])

    history = model.fit(
        x_train
        , y_train
        , batch_size=512
        , epochs=5
        , validation_split=0.2
    )

    eval_value = 1 - history.history["val_accuracy"][-1]

    # 訓練データの削除とメモリの解放
    clear_session()
    # del model, optimizer, history, x_train_copy, y_train_copy
    del model, optimizer, history, x_train, y_train,  x_test, y_test
    gc.collect()

    return eval_value


# パラメータチューニング処理関数(エントリポイント関数)
def tuning_parameter(data_dir):

    # グローバル変数に値をセット
    global g_data_dir_g
    g_data_dir_g = data_dir

    # パラメータチューニング処理
    study_obj = optuna.create_study()
    study_obj.optimize(Objective, n_trials=3, timeout=1200)
    print('Best Params:', study_obj.best_params)

    clear_session()

    # 最適なパラメータを返送
    return study_obj

