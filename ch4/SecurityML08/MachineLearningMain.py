
import ember

from sklearn.preprocessing import StandardScaler

from ReadFile import *
from ReadModel import *


def check_malware(check_file_path, model_file_path):

    check_file_obj = read_file(check_file_path)

    #scaler = StandardScaler()
    #sample_data_new = scaler.transform(check_file_obj)
    sample_data_new = StandardScaler.transform(check_file_obj)

    model_obj = read_model(model_file_path)

    extractor = ember.PEFeatureExtractor(2)

    print("end")





