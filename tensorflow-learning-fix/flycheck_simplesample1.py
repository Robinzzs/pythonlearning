import tensorflow as tf
import numpy as np

#sample
x_data = np.random.rand(100)
y_data = x_data*0.1 +0.2

#make linear model
b = tf.Variable(1.1)
k = tf.Variable(0.5)
y = k * x_data + b

#second order cost function
loss = tf.reduce_mean(input_tensor=tf.square(y_data-y))
#cg
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.2)

#minimize cost function
train = optimizer.minimize(loss)

init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        if step%20 ==0:
            print(step,sess.run([k,b]))
