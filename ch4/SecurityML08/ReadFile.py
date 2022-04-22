
import numpy as np


def read_file(check_file_path):

    file_data_obj = np.load(check_file_path).reshape(1,-1)

    return file_data_obj

