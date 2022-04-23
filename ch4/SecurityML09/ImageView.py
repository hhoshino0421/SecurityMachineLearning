
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def image_view(image_file_name):

    img = mpimg.imread(image_file_name)
    imgplot = plt.imshow(img)
    plt.show()