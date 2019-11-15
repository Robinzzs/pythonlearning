import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


#load data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

#parameter summary
def varible_summaries(var):
    with tf.compat.v1.name_scope('summaries'):
        mean = tf.reduce_mean(input_tensor=var)
        tf.compat.v1.summary.scalar('mean', mean)
        with tf.compat.v1.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(input_tensor=tf.square(var-mean)))
        tf.compat.v1.summary.scalar('stddev', stddev)
        tf.compat.v1.summary.scalar('max', tf.reduce_max(input_tensor=var))
        tf.compat.v1.summary.scalar('min', tf.reduce_min(input_tensor=var))
        tf.compat.v1.summary.histogram('histogram', var)


#name-space
with tf.compat.v1.name_scope('input'):
    x = tf.compat.v1.placeholder(tf.float32, [None, 784], name='x-input')
    y = tf.compat.v1.placeholder(tf.float32, [None, 10], name='y-input')

with tf.compat.v1.name_scope('layer'):
    # neural network
    with tf.compat.v1.name_scope('weights'):
        W_L1 = tf.Variable(tf.zeros([784, 10]), name='w')
        varible_summaries(W_L1)
    with tf.compat.v1.name_scope('biases'):
        b_L1 = tf.Variable(tf.zeros([10]), name='b')
        varible_summaries(b_L1)
    with tf.compat.v1.name_scope('wx_plus_b'):
        W_plus_b_L1 = tf.matmul(x, W_L1) + b_L1
    with tf.compat.v1.name_scope('softmax'):
        prediction = tf.nn.softmax(W_plus_b_L1)

with tf.compat.v1.name_scope('loss'):
    # cross entropy
    loss = tf.reduce_mean(input_tensor=tf.nn.softmax_cross_entropy_with_logits(labels=tf.stop_gradient(y), logits=prediction))
    tf.compat.v1.summary.scalar('loss', loss)

with tf.compat.v1.name_scope('train'):
    train_step = tf.compat.v1.train.GradientDescentOptimizer(0.2).minimize(loss)

init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.name_scope('accuracy'):
    with tf.compat.v1.name_scope('correct_prediction'):
        #bool list
        correct_prediction = tf.equal(tf.argmax(input=y,axis=1), tf.argmax(input=prediction,axis=1))
    with tf.compat.v1.name_scope('accuracy'):
        accuracy = tf.reduce_mean(input_tensor=tf.cast(correct_prediction, tf.float32))
        tf.compat.v1.summary.scalar('accuracy', accuracy)

##merge summary
merged = tf.compat.v1.summary.merge_all()


with tf.compat.v1.Session() as sess:
    sess.run(init)
    writer = tf.compat.v1.summary.FileWriter('logs/',sess.graph)
    for epoch in range(51):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            summary,_ = sess.run([merged, train_step],
                                 feed_dict={x:batch_xs,y:batch_ys})

        writer.add_summary(summary, epoch)
        acc = sess.run(accuracy, feed_dict={x:mnist.test.images,
                                            y:mnist.test.labels})
        print("Iter " + str(epoch) + ", Testing Accuracy " + str(acc))
