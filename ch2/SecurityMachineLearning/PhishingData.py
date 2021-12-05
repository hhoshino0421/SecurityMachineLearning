
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

from sklearn.model_selection import cross_val_score


# エントリポイント関数
def phishing_main():

    # データ読み込み
    training_data = np.genfromtxt('dataset.csv', delimiter=',', dtype=np.int)

    # Xには最終列以外のデータをセット
    x = training_data[:, :-1]
    # yには最終列のデータをセット
    y = training_data[:, -1]

    # 訓練用データとテスト用データに分割する
    X_train, X_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.2, shuffle=True, random_state=101)

    # ロジスティック回帰オブジェクトを生成
    classifier = LogisticRegression(solver='lbfgs')

    # 訓練用データを使って訓練を実行
    classifier.fit(X_train, y_train)

    # 予測処理を実行
    predictions = classifier.predict(X_test)

    # フィッシング検出器の正答率を計算
    accuracy = 100.0 * accuracy_score(y_test, predictions)
    # 正答率を出力
    print("accuracy  :{}".format(accuracy) )

    # 交差検証（５分割）による汎化性能の評価
    scores = cross_val_score(classifier, x, y, cv=5)
    # 評価値を計算
    scores_val = 100 * scores.mean()
    # 汎化性能を出力
    print("scores_val:{}".format(scores_val))
    print('')



