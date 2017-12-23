# !Python3
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
a = tf.constant([1 ,2], name='a')
b = tf.constant([2 ,3], name='b')
result = a+b
print(result)
testWeight = tf.Variable(tf.random_normal([2,3], stddev=2))


with tf.Session() as sess:    
    print(sess.run(hello).decode())
    print(sess.run(a))
    print(sess.run(result))
    sess.run(testWeight.initializer)
    print(sess.run(testWeight.initial_value))
    
