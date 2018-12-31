import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#load data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# neural network middle layer
# input 784; middle layer 40
W_L1 = tf.Variable(tf.zeros([784, 10]))
b_L1 = tf.Variable(tf.zeros([10]))
W_plus_b_L1 = tf.matmul(x, W_L1) + b_L1
prediction = tf.nn.softmax(W_plus_b_L1)


# cross entropy
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=prediction))

train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

init = tf.global_variables_initializer()

#bool list
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(prediction,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(accuracy, feed_dict={x:mnist.test.images,
                                        y:mnist.test.labels}))
    saver.restore(sess, 'net/my_net.ckpt')
    print(sess.run(accuracy, feed_dict={x:mnist.test.images,
                                        y:mnist.test.labels}))
