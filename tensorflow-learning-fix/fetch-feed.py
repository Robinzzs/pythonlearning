import tensorflow as tf

#Fetch
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)

add = tf.add(input2, input3)
mul = tf.multiply(input1, add)

with tf.compat.v1.Session() as sess:
    result = sess.run([mul, add])
    print(result)


#Feed
in1 = tf.compat.v1.placeholder(tf.float32)
in2 = tf.compat.v1.placeholder(tf.float32)
put = tf.multiply(in1, in2)

with tf.compat.v1.Session() as sess:
    print(sess.run(put, feed_dict={in1:[7.0],in2:[2.0]}))
