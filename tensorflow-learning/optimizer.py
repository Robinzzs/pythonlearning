import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#load data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)
lr = tf.Variable(0.001, dtype = tf.float32)

# neural network
W_L1 = tf.Variable(tf.truncated_normal([784, 500], stddev=0.1))
b_L1 = tf.Variable(tf.zeros([500])+0.1)
W_plus_b_L1 = tf.matmul(x, W_L1) + b_L1
L1 = tf.nn.tanh(W_plus_b_L1)
L1_drop = tf.nn.dropout(L1, keep_prob)

W_L2 = tf.Variable(tf.truncated_normal([500, 300], stddev=0.1))
b_L2 = tf.Variable(tf.zeros([300])+0.1)
W_plus_b_L2 = tf.matmul(L1_drop, W_L2) + b_L2
L2 = tf.nn.tanh(W_plus_b_L2)
L2_drop = tf.nn.dropout(L2, keep_prob)

W_L3 = tf.Variable(tf.truncated_normal([300, 10], stddev=0.1))
b_L3 = tf.Variable(tf.zeros([10])+0.1)
W_plus_b_L3 = tf.matmul(L2_drop, W_L3) + b_L3
prediction = tf.nn.softmax(W_plus_b_L3)

# cross entropy
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=prediction))

# train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)
train_step = tf.train.AdamOptimizer(lr).minimize(loss)


init = tf.global_variables_initializer()

#bool list
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(prediction,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(51):
        sess.run(tf.assign(lr, 0.001*(0.95 ** epoch)))
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict=
                     {x:batch_xs,y:batch_ys,keep_prob:1.0})

        learning_rate=sess.run(lr)
        acc = sess.run(accuracy, feed_dict=
                       {x:mnist.test.images,y:mnist.test.labels,
                        keep_prob:1.0})
        print("Iter " + str(epoch) +
              ", Testing Accuracy=" + str(acc) +
              ", Learning Rate=" + str(learning_rate))
