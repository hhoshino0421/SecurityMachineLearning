from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import numpy as np
import optuna
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split


class Objective_DTC:

    # 変数初期化
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, trial):
        # ターゲットのハイパーパラメータの設定
        params = {
            'criterion':
            trial.suggest_categorical('criterion', ['gini', 'entropy']),
            'splitter':
            trial.suggest_categorical('splitter', ['best', 'random']),
            'max_features':
            trial.suggest_categorical('max_features', ['auto', 'sqrt', 'log2']),
            'min_samples_split':
            trial.suggest_int('min_samples_split', 2, 64),
            'max_depth':
            trial.suggest_int('max_depth', 2, 64)
        }

        model = DecisionTreeClassifier(**params)

        # 評価指標として正解の最大化を目指す
        scores = cross_validate(model, X=self.x, y=self.y, scoring='accuracy', n_jobs=-1)

        return scores['test_score'].mean()


# 決定木によるフィッシングサイトパラメータチューニング関数
def decision_tree_parameter_tuning():

    # データ読み込み
    training_data = np.genfromtxt('dataset.csv', delimiter=',', dtype=np.int)

    # Xには最終列以外のデータをセット
    x = training_data[:, :-1]
    # yには最終列のデータをセット
    y = training_data[:, -1]

    # 訓練用データとテスト用データに分割する
    X_train, X_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.2, shuffle=True, random_state=101)

    # ハイパーパラメータのチューニング実行処理
    objective = Objective_DTC(X_train, y_train)
    study = optuna.create_study(direction='maximize')
    # timeoutに60を指定し、最大で1分間探索させる
    study.optimize(objective, timeout=60)
    print('params:', study.best_params)

    # チューニング結果を返送
    return study


# 決定木によるフィッシングサイト検知関数
def decision_tree_main(study_obj):

    # データ読み込み
    training_data = np.genfromtxt('dataset.csv', delimiter=',', dtype=np.int)

    # Xには最終列以外のデータをセット
    x = training_data[:, :-1]
    # yには最終列のデータをセット
    y = training_data[:, -1]

    # 訓練用データとテスト用データに分割する
    X_train, X_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.2, shuffle=True, random_state=101)

    # チューニング結果で得られた推奨パラメータを利用してハイパーパラメータを設定
    model = DecisionTreeClassifier(
        criterion=study_obj.best_params['criterion'],
        splitter=study_obj.best_params['splitter'],
        max_features=study_obj.best_params['max_features'],
        min_samples_split=study_obj.best_params['min_samples_split'],
        max_depth=study_obj.best_params['max_depth']
    )

    # 決定木を利用した機械学習処理を実行
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    # 処理結果を出力
    # 正答率を出力
    print("Accuracy: {:.5f} %".format(100 * accuracy_score(y_test, pred)))
    # 適合率の出力
    print("Precision: {:.5f} %".format(100 * precision_score(y_test, pred)))
    # 再現率の出力
    print("Recall: {:5f} %".format(100 * recall_score(y_test, pred)))
    # 混合行列の出力
    print(confusion_matrix(y_test, pred))
