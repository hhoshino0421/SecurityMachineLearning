
from MachineLearningMain import *


def main():

    check_file_path = "/home/hhoshino/data/file/putty.npy"

    model_file_path = "/home/hhoshino/data/ember2018_model/detect_malware_model.h5"

    check_malware(check_file_path, model_file_path)


if __name__ == '__main__':
    main()
