import tensorflow as tf

with tf.compat.v1.Session() as sess:
    rand_a = tf.random.normal([3], 2.0)
    rand_b = tf.random.uniform([3], 1.0, 4.0)
    diff = tf.subtract(rand_a, rand_b)

    print('\nTensor rand_a: ', sess.run(rand_a))
    print('\nTensor rand_b: ', sess.run(rand_b))
    print('\nSubtração entre os 2 tensores é: ', sess.run(diff))