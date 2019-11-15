import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#random samples
x_data = np.linspace(-0.5, 0.5, 200)[:, np.newaxis]  #
noise = np.random.normal(0, 0.02, x_data.shape)
y_data = np.square(x_data) + noise

#placeholder
x = tf.compat.v1.placeholder(tf.float32, [None, 1])
y = tf.compat.v1.placeholder(tf.float32, [None, 1])

# neural network middle layer
# input layer 1 ; middle layer 10
Weights_L1 = tf.Variable(tf.random.normal([1, 10]))
biases_L1 = tf.Variable(tf.zeros([1, 10]))
Wx_plus_b_L1 = tf.matmul(x, Weights_L1) + biases_L1
L1 = tf.nn.tanh(Wx_plus_b_L1)

# neural network output layer
Weights_L2 = tf.Variable(tf.random.normal([10, 1]))
biases_L2 = tf.Variable(tf.zeros([1, 1]))
Wx_plus_b_L2 = tf.matmul(L1, Weights_L2) + biases_L2
prediction = tf.nn.tanh(Wx_plus_b_L2)

#second order cost function
loss = tf.reduce_mean(input_tensor=tf.square(y-prediction))
#cg
train_step = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(loss)

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    for _ in range(2000):
        sess.run(train_step,feed_dict={x:x_data,y:y_data})

    prediction_value = sess.run(prediction, feed_dict={x:x_data})

    #plot
    plt.figure()
    plt.scatter(x_data, y_data)
    plt.plot(x_data, prediction_value, 'r-', lw=5)
    plt.show()
