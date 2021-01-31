import tensorflow as tf

with tf.compat.v1.Session() as sess:
    node1 = tf.constant(5, dtype=tf.int32)
    node2 = tf.constant(9, dtype=tf.int32)
    node3 = tf.add(node1, node2)
    
    print("\nA soma do node1 com o node2 é:", sess.run(node3))
    sess.close()