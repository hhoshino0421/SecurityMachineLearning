
# import tf.keras.Model
from keras.models import save_model

from FileDataRead import *


def save_model(data_file_dir, estimator, model_file_save):

    # estimator = buildmodel()

    x_train, y_train, x_test, y_test = read_file_data(data_file_dir)

    estimator.fit(x_train, y_train, epochs=10, batch_size=128)

    estimator.save(model_file_save)

    print("save end.")
