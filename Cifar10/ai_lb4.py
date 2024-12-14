import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

import tensorflow
import keras
from matplotlib import pyplot as plt
import numpy as np
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Reshape, Flatten, BatchNormalization, SpatialDropout2D

# Модули для графиков и визуализации
from tensorflow.keras.utils import plot_model
from tensorflow.keras.callbacks import TensorBoard
tensorboard_callback = keras.callbacks.TensorBoard(log_dir='./logs/', histogram_freq=1)

# Модуль для остановки обучения
from tensorflow.keras.callbacks import EarlyStopping

# Загрузка и подготовка данных из cifar10
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

images_to_show = x_train[:16]
labels_to_show = y_train[:16]


fig, axes = plt.subplots(4, 4, figsize=(8, 8))
axes = axes.flatten()

for i in range(16):
    img = images_to_show[i].astype(np.uint8)
    label_index = labels_to_show[i][0]
    class_name = class_names[label_index]

    axes[i].imshow(img)
    axes[i].set_title(class_name)
    axes[i].set_xticks([])
    axes[i].set_yticks([])

plt.tight_layout()
plt.show()

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# Создание нейросети

# Пояснение к слоям:

# Conv2d: filters - количество матриц с весами, kernel_size - размер матриц,
# padding - добавление 0 к оступам (same/valid), чтобы было красиво, strides - (сдвиг в пикселях)
# При распростанении данных, выбираются матрицы размером kernel_size (из данных)
# и производится матричное умножение на матрицы с весами в filters, потом сдвиг на stides, число записывается в выходной тензор

# BatchNormalization - выполняет нормализацию данных после слоя, делает обучение более плавным и устойчивым

# MaxPooling - Из полученного тензора выбираются матрицы размером pool_size и внутри них выбирается максимальный элемент,
# то есть происходит масштабирование, это позволяет сократить число признаков путём выделения главных черт

# SpatialDropout2D - отключает изменение весов у целых матриц с весами (filters), а у не у конкретных связей, как Dropout

model = keras.Sequential([
    Conv2D(filters=128, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 3), padding='same'),
    BatchNormalization(),
    SpatialDropout2D(rate=0.2),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same'),
    BatchNormalization(),
    SpatialDropout2D(rate=0.2),
    Conv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same'),
    BatchNormalization(),
    SpatialDropout2D(rate=0.2),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same'),
    BatchNormalization(),
    SpatialDropout2D(rate=0.2),
    Conv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same'),
    BatchNormalization(),
    SpatialDropout2D(rate=0.2),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(filters=512, kernel_size=(3, 3), activation='relu', padding='same'),
    BatchNormalization(),
    SpatialDropout2D(rate=0.2),
    Conv2D(filters=512, kernel_size=(3, 3), activation='relu', padding='same'),
    BatchNormalization(),
    SpatialDropout2D(rate=0.2),
    Conv2D(filters=512, kernel_size=(3, 3), activation='relu', padding='same'),
    BatchNormalization(),
    SpatialDropout2D(rate=0.2),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),
    Dense(units=1024, activation='relu'),
    Dropout(0.2),
    Dense(units=10, activation='softmax')
])

print(model.summary())

# Компиляция нейросети (выбор оптимизатора, функции ошибки и характеристики точности нейросети)
#my_optimizer = keras.optimizers.SGD(learning_rate = 0.01, nesterov = True)
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Остановка обучения, если точность в выборке валидации долго не изменяется
early_stopping = EarlyStopping(
    monitor='val_accuracy',
    mode='auto',
    patience=5,
    verbose=1
)

# Обучение нейросети
history = model.fit(x_train, y_train, batch_size=60, epochs=40, validation_data = (x_test, y_test), callbacks=[tensorboard_callback, early_stopping])

# Предсказание для тестовой выборки
model.evaluate(x_test, y_test)

# Сохранение
model.save("logs/my_model.keras")