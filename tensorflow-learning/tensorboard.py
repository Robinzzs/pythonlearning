import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


#load data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

#parameter summary
def varible_summaries(var):
    with tf.name_scope('summaries'):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', mean)
        with tf.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var-mean)))
        tf.summary.scalar('stddev', stddev)
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.scalar('min', tf.reduce_min(var))
        tf.summary.histogram('histogram', var)


#name-space
with tf.name_scope('input'):
    x = tf.placeholder(tf.float32, [None, 784], name='x-input')
    y = tf.placeholder(tf.float32, [None, 10], name='y-input')

with tf.name_scope('layer'):
    # neural network
    with tf.name_scope('weights'):
        W_L1 = tf.Variable(tf.zeros([784, 10]), name='w')
        varible_summaries(W_L1)
    with tf.name_scope('biases'):
        b_L1 = tf.Variable(tf.zeros([10]), name='b')
        varible_summaries(b_L1)
    with tf.name_scope('wx_plus_b'):
        W_plus_b_L1 = tf.matmul(x, W_L1) + b_L1
    with tf.name_scope('softmax'):
        prediction = tf.nn.softmax(W_plus_b_L1)

with tf.name_scope('loss'):
    # cross entropy
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=prediction))
    tf.summary.scalar('loss', loss)

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

init = tf.global_variables_initializer()

with tf.name_scope('accuracy'):
    with tf.name_scope('correct_prediction'):
        #bool list
        correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(prediction,1))
    with tf.name_scope('accuracy'):
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        tf.summary.scalar('accuracy', accuracy)

##merge summary
merged = tf.summary.merge_all()


with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter('logs/',sess.graph)
    for epoch in range(51):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            summary,_ = sess.run([merged, train_step],
                                 feed_dict={x:batch_xs,y:batch_ys})

        writer.add_summary(summary, epoch)
        acc = sess.run(accuracy, feed_dict={x:mnist.test.images,
                                            y:mnist.test.labels})
        print("Iter " + str(epoch) + ", Testing Accuracy " + str(acc))
