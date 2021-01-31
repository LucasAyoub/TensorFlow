import tensorflow as tf

with tf.compat.v1.Session() as sess:
    node = tf.Variable(tf.zeros([2, 2]))

    init = tf.compat.v1.global_variables_initializer()
    sess.run(init)

    print("\nTensor Original:\n", sess.run(node))

    node = node.assign(node + tf.ones([2, 2]))

    print("\nTensor depois da adição:\n", sess.run(node))
