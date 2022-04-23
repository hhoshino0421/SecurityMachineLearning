import array
import os.path

import numpy as np
import imageio


def file_image(file_name_path):

    file_size = os.path.getsize(file_name_path)

    width_size = 256

    file_obj = open(file_name_path, 'rb')

    rem = file_size % width_size

    array_obj = array.array("B")
    array_obj.fromfile(file_obj, file_size - rem)

    file_obj.close()

    output_imgae_file_name = "putty.png"

    image_obj = np.reshape(array_obj, (len(array_obj)//width_size, width_size) )
    image_obj = np.uint8(image_obj)
    imageio.imwrite(output_imgae_file_name, image_obj)

    return output_imgae_file_name

