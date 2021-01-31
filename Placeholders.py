import tensorflow as tf

with tf.compat.v1.Session() as sess:
    a = tf.compat.v1.placeholder(tf.int32, shape=(3, 1))
    b = tf.compat.v1.placeholder(tf.int32, shape=(1, 3))
    c = tf.matmul(a, b)

    print(sess.run(c, feed_dict={a: [[3], [2], [1]], b: [[1, 2, 3]]}))