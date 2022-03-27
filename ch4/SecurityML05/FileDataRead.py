
import ember


# データファイル読み込み処理関数
def read_file_data(data_dir):

    # データ読み込み
    x_train, y_train, x_test, y_test = ember.read_vectorized_features(data_dir)

    return x_train, y_train, x_test, y_test
