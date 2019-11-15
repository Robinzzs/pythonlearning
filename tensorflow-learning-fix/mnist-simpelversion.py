import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#load data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

x = tf.compat.v1.placeholder(tf.float32, [None, 784])
y = tf.compat.v1.placeholder(tf.float32, [None, 10])

# neural network middle layer
# input 784; middle layer 40
W_L1 = tf.Variable(tf.zeros([784, 10]))
b_L1 = tf.Variable(tf.zeros([10]))
W_plus_b_L1 = tf.matmul(x, W_L1) + b_L1
prediction = tf.nn.softmax(W_plus_b_L1)

# # neural network middle layer 2
# # middle layer 20
# W_L2 = tf.Variable(tf.random.normal([100, 60]))
# b_L2 = tf.Variable(tf.random.normal([60]))
# W_plus_b_L2 = tf.matmul(L1, W_L2) + b_L2
# L2 = tf.nn.tanh(W_plus_b_L2)


# # neural network output layer
# W_L3 = tf.Variable(tf.random.normal([60, 10]))
# b_L3 = tf.Variable(tf.random.normal([10]))
# W_plus_b_L3 = tf.matmul(L2, W_L3) + b_L3
# prediction = tf.nn.softmax(W_plus_b_L3)

# second order cost function
# loss = tf.reduce_mean(tf.square(y - prediction))

# cross entropy
loss = tf.reduce_mean(input_tensor=tf.nn.softmax_cross_entropy_with_logits(labels=tf.stop_gradient(y), logits=prediction))

train_step = tf.compat.v1.train.GradientDescentOptimizer(0.2).minimize(loss)

init = tf.compat.v1.global_variables_initializer()

#bool list
correct_prediction = tf.equal(tf.argmax(input=y,axis=1), tf.argmax(input=prediction,axis=1))

accuracy = tf.reduce_mean(input_tensor=tf.cast(correct_prediction, tf.float32))

with tf.compat.v1.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={x:batch_xs,y:batch_ys})

        acc = sess.run(accuracy, feed_dict={x:mnist.test.images,
                                            y:mnist.test.labels})
        print("Iter " + str(epoch) + ", Testing Accuracy " + str(acc))
