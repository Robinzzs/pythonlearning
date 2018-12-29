import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#load data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

#init weight
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

#init biase
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],
                          padding='SAME')

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# change format
x_image = tf.reshape(x,[-1,28,28,1])

# init fist layer
W_conv1 = weight_variable([5,5,1,32])
#5*5 sample window, 32 kernal from 1 plane
b_conv1 = bias_variable([32])

h_conv1 = tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# init second layer
W_conv2 = weight_variable([5,5,32,64])
#5*5 sample window, 64 kernal from 32 plane
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# 28*28 convolute1 -> 28*28, pooling1 -> 14*14
# convolute2 -> 14*14, pooling2 ->7*7
# get 64 plane with 7*7 size

# init first full connect layer
W_fc1 = weight_variable([7*7*64, 1024])
#full connect layer have 1024 neural net
b_fc1 = bias_variable([1024])

# pooling2 layer output change to 1D
h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])

h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1)) + b_fc1

# dropout
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)

#init second full connect layer
W_fc2 = weight_variable([1024,10])
b_fc2 =bias_variable([10])

# compute output
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2) + b_fc2)

# cross entropy
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=prediction))

train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

#bool list
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(prediction,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={x:batch_xs,y:batch_ys,
                                            keep_prob:0.7})

        acc = sess.run(accuracy, feed_dict={x:mnist.test.images,
                                            y:mnist.test.labels,
                                            keep_prob:1.0})
        print("Iter " + str(epoch) + ", Testing Accuracy=" + str(acc))
