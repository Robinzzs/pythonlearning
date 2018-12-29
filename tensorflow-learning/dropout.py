import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#load data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)

# neural network middle layer
# input 784; middle layer 40
W_L1 = tf.Variable(tf.truncated_normal([784, 1000], stddev=0.1))
b_L1 = tf.Variable(tf.zeros([1000])+0.1)
W_plus_b_L1 = tf.matmul(x, W_L1) + b_L1
L1 = tf.nn.tanh(W_plus_b_L1)
L1_drop = tf.nn.dropout(L1, keep_prob)

# neural network middle layer 2
# middle layer 20
W_L2 = tf.Variable(tf.truncated_normal([1000, 1000], stddev=0.1))
b_L2 = tf.Variable(tf.zeros([1000])+0.1)
W_plus_b_L2 = tf.matmul(L1, W_L2) + b_L2
L2 = tf.nn.tanh(W_plus_b_L2)
L2_drop = tf.nn.dropout(L2, keep_prob)

# neural network middle layer 2
# middle layer 20
W_L3 = tf.Variable(tf.truncated_normal([1000, 1000], stddev=0.1))
b_L3 = tf.Variable(tf.zeros([1000])+0.1)
W_plus_b_L3 = tf.matmul(L2, W_L3) + b_L3
L3 = tf.nn.tanh(W_plus_b_L3)
L3_drop = tf.nn.dropout(L3, keep_prob)

# # neural network output layer
W_L4 = tf.Variable(tf.truncated_normal([1000, 10], stddev=0.1))
b_L4 = tf.Variable(tf.zeros([10])+0.1)
W_plus_b_L4 = tf.matmul(L3, W_L4) + b_L4
prediction = tf.nn.softmax(W_plus_b_L4)


# cross entropy
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=prediction))

train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

init = tf.global_variables_initializer()

#bool list
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(prediction,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(31):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict=
                     {x:batch_xs,y:batch_ys, keep_prob:0.7})

        test_acc = sess.run(accuracy, feed_dict=
                            {x:mnist.test.images,
                             y:mnist.test.labels,keep_prob:1.0})
        train_acc = sess.run(accuracy, feed_dict=
                            {x:mnist.train.images,
                             y:mnist.train.labels,keep_prob:1.0})
        print("Iter " + str(epoch) +
              ", Testing Accuracy " + str(test_acc) +
              "Training Accuracy" + str(train_acc))
