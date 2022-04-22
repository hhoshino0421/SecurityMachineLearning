
import ember

from sklearn.preprocessing import StandardScaler

from ReadFile import *
from ReadModel import *


def check_malware(check_file_path, model_file_path):

    check_file_obj = read_file(check_file_path)

    scaler = StandardScaler()
    scaler.fit(check_file_obj)
    sample_data_new = scaler.transform(check_file_obj)
    #sample_data_new = scaler.transform(check_file_obj)
    #sample_data_new = StandardScaler.transform(check_file_obj)

    model_obj = read_model(model_file_path)

    # extractor = ember.PEFeatureExtractor(2)

    pred = (model_obj.predict(sample_data_new) > 0.5).astype("int32")

    # for debug
    print(pred)

    if pred:
        print("Malware!")
    else:
        print("benign file")

    print("end")





