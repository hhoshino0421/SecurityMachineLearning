import ember


def read_data_main():

    x_train, y_train, x_test, y_test \
        = ember.read_vectorized_features("/home/hhoshino/data/ember2018")

    return x_train, y_train, x_test, y_test
