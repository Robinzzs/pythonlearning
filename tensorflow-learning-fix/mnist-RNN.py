import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#load data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

#
n_inputs = 28  # 28 samples
max_time = 28  # 28 lines
lstm_size = 100  # hidden cell
n_classes = 10   # 10 classes
batch_size = 50  # 1 batch 50 samples
n_batch = mnist.train.num_examples // batch_size


x = tf.compat.v1.placeholder(tf.float32, [None, 784])
y = tf.compat.v1.placeholder(tf.float32, [None, 10])

weights = tf.Variable(tf.random.truncated_normal([lstm_size, n_classes],
                                          stddev=0.1))
biases = tf.Variable(tf.constant(0.1, shape=[n_classes]))

def RNN(X, weights, biases):
    # inputs = [batch_size, max_time, n_inputs ]
    inputs = tf.reshape(X, [-1,max_time, n_inputs])
    # define basical LSTM CELL
    lstm_cell = tf.compat.v1.nn.rnn_cell.BasicLSTMCell(lstm_size)
    # final_state[0] cell state
    # final_state[1] hidden state
    output, final_state = tf.compat.v1.nn.dynamic_rnn(lstm_cell, inputs,
                                            dtype=tf.float32)
    results = tf.nn.softmax(tf.matmul(final_state[1], weights)+
                            biases)
    return results

# calculate RNN results
prediction = RNN(x, weights, biases)

# loss function
cross_entropy = tf.reduce_mean(input_tensor=tf.nn.softmax_cross_entropy_with_logits(labels=tf.stop_gradient(y), logits=prediction))

train_step = tf.compat.v1.train.AdamOptimizer(1e-4).minimize(cross_entropy)

#bool list
correct_prediction = tf.equal(tf.argmax(input=y,axis=1), tf.argmax(input=prediction,axis=1))

accuracy = tf.reduce_mean(input_tensor=tf.cast(correct_prediction, tf.float32))

init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    sess.run(init)
    for epoch in range(6):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={x:batch_xs,y:batch_ys})

        acc = sess.run(accuracy, feed_dict={x:mnist.test.images,
                                            y:mnist.test.labels})
        print("Iter " + str(epoch) + ", Testing Accuracy=" + str(acc))
