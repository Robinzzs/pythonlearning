import tensorflow as tf

W = tf.Variable([.1], dtype=tf.float32)
b = tf.Variable([-.1], dtype=tf.float32)

x = tf.placeholder(tf.float32)

linear_model = W * x + b

y = tf.placeholder(tf.float32)

loss = tf.reduce_sum(tf.square(linear_model - y))

sess = tf.Session()

# initialization
init = tf.global_variables_initializer()
sess.run(init)

optimizer = tf.train.GradientDescentOptimizer(0.001)
train = optimizer.minimize(loss)

x_train = [1, 2, 3, 6, 8]
y_train = [4.8, 8.5, 10.4, 21.0, 25.3]

for i in range(10000):
    sess.run(train, {x: x_train, y: y_train})
    #print(i, sess.run(W), sess.run(b))

print('W: %s b:%s loss: %s'
      %(sess.run(W), sess.run(b), sess.run(loss, {x: x_train, y: y_train})))


####Plot
import matplotlib.pyplot as plt
plt.style.use('ggplot')

z_train = sess.run(W) * x_train +sess.run(b)
# fig, ax = plt.subplots()
# ax.scatter(x_train, y_train)

# fig.set_size_inches(8,6)
# ax.set_xlabel('X',fontsize=18)
# ax.set_ylabel('Y',fontsize=18)
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.show()
plt.scatter(x_train, y_train)
plt.plot(x_train, z_train)

plt.xlabel('X')
plt.ylabel('Y')
plt.show()
