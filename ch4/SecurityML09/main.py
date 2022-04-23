
# URL
# https://www.kaggle.com/competitions/malware-classification/data
# login:google account
# DataSize:about 35GB over
#


from FileImage import *
from ImageView import *


def main():

    file_name_path = "/home/hhoshino/data/file/putty.exe"

    image_file_name = file_image(file_name_path)

    path_name = "/home/hhoshino/develop/Pychram_workspace/SecurityML09/"
    image_file_path_name = path_name + image_file_name

    image_view(image_file_path_name)


if __name__ == '__main__':
    main()

