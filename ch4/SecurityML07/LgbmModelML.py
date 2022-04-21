import ember
import lightgbm as lgb


def lgbm_model_test(model_file_path, analyze_file_path):

    lgbm_model = lgb.Booster(model_file=model_file_path)
    putty_data = open(analyze_file_path, "rb").read()

    print(ember.predict_sample(lgbm_model, putty_data))

