#! python3
import tensorflow as tf 

#define w1, w2, also define the random seed to get the same result each time.
w1 = tf.Variable(tf.random_normal([2,3],stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1, seed=1))

#set the initial input as a constant here, x is a 1x2 matrix (two dimension array)
x = tf.constant([[0.7, 0.9]])

#two level output
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

with tf.Session() as sess:
    #initialize w1 and w2
    #sess.run(w1.initializer)
    #sess.run(w2.initializer)
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    print('w1: ', sess.run(w1.initial_value))
    print('w2: ', sess.run(w2.initial_value))
    print(sess.run(y))