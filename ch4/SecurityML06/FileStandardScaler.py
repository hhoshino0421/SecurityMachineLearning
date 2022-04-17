
import ember
import numpy as np

from sklearn.preprocessing import StandardScaler


# 対象ファイル読み込み処理＆標準スケール化処理
def file_standard_scaler(file_path_name):

    read_file_data = open(file_path_name, "rb").read()

    extractor = ember.PEFeatureExtractor(2)

    # sample_data = np.array(
    #     extractor.feature_vector(read_file_data),
    #     dtype=np.float
    # ).reshape(1, -1)
    sample_data = np.array(
        extractor.feature_vector(read_file_data),
        dtype=np.float
    )


    scaler = StandardScaler()
    sample_data_new = scaler.transform(sample_data)

    # for debug
    print(sample_data_new)

    return sample_data_new
