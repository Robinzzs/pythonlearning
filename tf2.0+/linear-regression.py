import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

train_X = np.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                      7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = np.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                      2.827,3.465,1.65,2.904,2.42,2.94,1.3])

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(1,)))
model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(0.002), loss='mse')

history = model.fit(train_X, train_Y, epochs=1000)

Y = model.predict(train_X)


plt.plot(train_X, train_Y, 'ro', label='original')
plt.plot(train_X, Y, label='fitted')
plt.legend()
plt.show()
