import tensorflow as tf

x = tf.Variable([1,2])
a = tf.Variable([3,3])

sub = tf.subtract(x, a)
add = tf.add(x, sub)

init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))
