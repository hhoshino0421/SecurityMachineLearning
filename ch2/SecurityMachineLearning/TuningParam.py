from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
import optuna
from sklearn.model_selection import cross_validate


class Objective:
    def __init__(self, X, y):
        # x,y 変数の初期化
        self.X = X
        self.y = y

    def __call__(self, trial):
        # ターゲットのハイパーパラメータの設定
        params = {
            # 最適化に使用するアルゴリズムの候補をカテゴリとして指定
            #'solver': trial.suggest_categorical('solver', ['newton-cg', 'lbfgs', 'liblinear',' sag', 'saga']),
            'solver': trial.suggest_categorical('solver', ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']),
            # 正則化の強さに0.0001から10までを指定
            'C': trial.suggest_loguniform('C', 0.0001, 10),
            # ソルバーが収束するまでの最大反復回数
            'max_iter': trial.suggest_int('max_iter', 100, 1000000)
        }

        model = LogisticRegression(**params)

        # 評価指標として正解数の最大化を目指す
        scores = cross_validate(model, X=self.X, y=self.y, scoring='accuracy', n_jobs=-1)

        return scores['test_score'].mean()


def tuning_exec():
    # データ読み込み
    training_data = np.genfromtxt('dataset.csv', delimiter=',', dtype=np.int)

    # Xには最終列以外のデータをセット
    x = training_data[:, :-1]
    # yには最終列のデータをセット
    y = training_data[:, -1]

    # 訓練用データとテスト用データに分割する
    X_train, X_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.2, shuffle=True, random_state=101)

    # 以下はパラメータチューニング用のロジック
    # ハイパーパラメータの探索
    # objective_obj = Objective(X_train, y_train)
    objective_obj = Objective(X_train, y_train)
    study = optuna.create_study(direction='maximize')
    study.optimize(objective_obj, timeout=60)
    # ベストのパラメータの出力
    print('params:', study.best_params)