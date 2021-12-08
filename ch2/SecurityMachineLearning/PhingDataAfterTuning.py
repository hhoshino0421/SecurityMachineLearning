
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.metrics import precision_score,recall_score

from sklearn.model_selection import cross_val_score


# エントリポイント関数
def phishing_after_tuning_main(study):

    # データ読み込み
    training_data = np.genfromtxt('dataset.csv', delimiter=',', dtype=np.int)

    # Xには最終列以外のデータをセット
    x = training_data[:, :-1]
    # yには最終列のデータをセット
    y = training_data[:, -1]

    # 訓練用データとテスト用データに分割する
    X_train, X_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.2, shuffle=True, random_state=101)

    model = LogisticRegression(solver=study.best_params['solver'],
                               C=study.best_params['C'],
                               max_iter=study.best_params['max_iter']
                               )

    model.fit(X_train,y_train)
    pred = model.predict(X_test)
    # 正解率の出力
    print("Accuracy:{:.5f}".format(100*accuracy_score(y_test, pred)))
    # 混合行列の出力
    print(confusion_matrix(y_test, pred))

    # 適合率の確認
    print("Precision: {:.5f} %".format(100 * precision_score(y_test,pred)))
    # 再現率の確認
    print("Recall: {:.5f} %".format(100 * recall_score(y_test,pred)))

