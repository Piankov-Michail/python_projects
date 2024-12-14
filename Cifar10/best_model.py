import tensorflow as tf
import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

model = keras.saving.load_model("logs/my_model.h5")

print(model.summary())

model.evaluate(x_test, y_test)