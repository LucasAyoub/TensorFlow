import tensorflow as tf

with tf.compat.v1.Session() as sess:
    hello = tf.constant('Hello, TensorFlow!')
    print(hello)
    print(sess)
    print(sess.run(hello))
