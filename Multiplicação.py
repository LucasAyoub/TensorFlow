import tensorflow as tf

with tf.compat.v1.Session() as sess:
    tensor_a = tf.constant([[4., 2.]])
    tensor_b = tf.constant([[3.], [7.]])
    prod = tf.multiply(tensor_a, tensor_b)

    print('\ntensor_a: \n', sess.run(tensor_a))
    print('\ntensor_b: \n', sess.run(tensor_b))
    print('\nProduto Element-wise Entre os Tensores: \n', sess.run(prod))