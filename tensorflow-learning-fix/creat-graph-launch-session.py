import tensorflow as tf

m1 = tf.constant([[3,3]])
m2 = tf.constant([[2],[3]])

product = tf.matmul(m1, m2)

# sess = tf.Session()
with tf.compat.v1.Session() as sess:

    result = sess.run(product)

    print(result)

#sess.close()