import tensorflow as tf

with tf.compat.v1.Session() as sess:
    node1 = tf.constant(21, dtype=tf.int32)
    node2 = tf.constant(7, dtype=tf.int32)
    div = tf.divide(node1, node2)

    print('\nDivisão entre os 2 tensores é: ', sess.run(div))