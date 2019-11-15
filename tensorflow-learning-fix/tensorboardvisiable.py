import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib.tensorboard.plugins import projector

# load data
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# loop num
max_steps = 1001
# fig num
image_num = 3000
# PATH
DIR = '/home/zzs/pythonlearning/tensorflow-learning/'

# define session
sess = tf.compat.v1.Session()

# load fig
embedding = tf.Variable(tf.stack(mnist.test.images[:image_num]), trainable=False, name='embedding')

#parameter
def variable_summaries(var):
    with tf.compat.v1.name_scope('summaries'):
        mean = tf.reduce_mean(input_tensor=var)
        tf.compat.v1.summary.scalar('mean',mean)
        with tf.compat.v1.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(input_tensor=tf.square(var-mean)))
        tf.compat.v1.summary.scalar('stddev',stddev)
        tf.compat.v1.summary.scalar('max',tf.reduce_max(input_tensor=var))
        tf.compat.v1.summary.scalar('min',tf.reduce_min(input_tensor=var))
        tf.compat.v1.summary.histogram('histogram',var)

# name space
with tf.compat.v1.name_scope('Input'):
    x = tf.compat.v1.placeholder(tf.float32,[None,784],name='x-input')
    y = tf.compat.v1.placeholder(tf.float32,[None,10],name='y-input')

# show fig
with tf.compat.v1.name_scope('input_reshape'):
    image_shaped_input = tf.reshape(x,[-1,28,28,1])
    tf.compat.v1.summary.image('input', image_shaped_input,10)

with tf.compat.v1.name_scope('layer'):
    with tf.compat.v1.name_scope('weights'):
        W = tf.Variable(tf.zeros([784,10]),name='W')
        variable_summaries(W)
    with tf.compat.v1.name_scope('biases'):
        b = tf.Variable(tf.zeros([10]),name='b')
        variable_summaries(b)
    with tf.compat.v1.name_scope('wx_plus_b'):
        wx_plus_b = tf.matmul(x,W) + b
    with tf.compat.v1.name_scope('softmax'):
        prediction = tf.nn.softmax(wx_plus_b)

with tf.compat.v1.name_scope('loss'):
    loss = tf.reduce_mean(input_tensor=tf.nn.softmax_cross_entropy_with_logits(labels=tf.stop_gradient(y),logits=prediction))
    tf.compat.v1.summary.scalar('loss',loss)

with tf.compat.v1.name_scope('train'):
    train_step = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(loss)

sess.run(tf.compat.v1.global_variables_initializer())

with tf.compat.v1.name_scope('accuracy'):
    with tf.compat.v1.name_scope('correct_prediction'):
        correct_prediction = tf.equal(tf.argmax(input=y,axis=1),tf.argmax(input=prediction,axis=1))
    with tf.compat.v1.name_scope('accuracy'):
        accuracy = tf.reduce_mean(input_tensor=tf.cast(correct_prediction,tf.float32))
        tf.compat.v1.summary.scalar('accuracy',accuracy)

# produce metadata file ##fix Remove function
if tf.io.gfile.exists(DIR + 'projector/projector/metadata.tsv'):
    tf.io.gfile.remove(DIR + 'projector/projector/metadata.tsv')
with open(DIR + 'projector/projector/metadata.tsv','w') as f:
    labels = sess.run(tf.argmax(input=mnist.test.labels[:],axis=1))
    for i in range(image_num):
        f.write(str(labels[i]) + '\n')

# merge summary
merged = tf.compat.v1.summary.merge_all()

# define writer
projector_writer = tf.compat.v1.summary.FileWriter(DIR + 'projector/projector',sess.graph)
# saver
saver = tf.compat.v1.train.Saver()
# define config
config = projector.ProjectorConfig()
embed = config.embeddings.add()
embed.tensor_name = embedding.name
embed.metadata_path = DIR + 'projector/projector/metadata.tsv'
embed.sprite.image_path = DIR + 'projector/data/mnist_10k_sprite.png'
# patch fig
embed.sprite.single_image_dim.extend([28,28])
projector.visualize_embeddings(projector_writer, config)

for i in range(max_steps):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    run_options = tf.compat.v1.RunOptions(trace_level=tf.compat.v1.RunOptions.FULL_TRACE)
    run_metadata = tf.compat.v1.RunMetadata()
    summary,_  = sess.run([merged, train_step], feed_dict={x:batch_xs,y:batch_ys}, options=run_options, run_metadata=run_metadata)
    projector_writer.add_run_metadata(run_metadata,'step%03d' % i)
    projector_writer.add_summary(summary, i)

    if i%100 == 0:
        acc = sess.run(accuracy, feed_dict={x:mnist.test.images,
                                            y:mnist.test.labels})
        print("Iter " + str(i) + ", Testing Accuracy= " + str(acc) )

saver.save(sess, DIR + 'projector/projector/a_model.ckpt', global_step=max_steps)
projector_writer.close()
sess.close()
