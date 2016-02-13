import numpy as np
from numpy import genfromtxt

import tensorflow.python.platform
import tensorflow as tf

import Loading_Data

sess = tf.InteractiveSession()

x = tf.placeholder("float", shape = [Loading_Data.data])

x1 = tf.placeholder("float", shape = [None, 9])
w1 = tf.Variable(tf.zeros([9, 4]))

x2 = tf.placeholder("float", shape = [None, 4])
w2 = tf.Variable(tf.zeros([4, 3]))

b1 = tf.Variable(tf.zeros([4]))
b2 = tf.Variable(tf.zeros([3]))

def weight_variable(shape):
	initial = tf.truncated_normal(shape, stddev = 0.1)
	return tf.Variable(initial)
	
def bias_variable(shape):
	initial = tf.constant(0.1, shape = shape)
	return tf.Variable(initial)
	
def conv2d(x, w):
	return tf.nn.conv2d(x, w, strides = [3, 3, 1, 1], padding = 'SAME')
	
def max_pool_3x3(x):
	return tf.nn.max_pool(x, ksize = [1, 3, 3, 1], strides = [1, 1, 1, 1], padding = 'SAME')
	



#EVALUATING DATA#
cross_entropy = -tf.reduce_sum(W * tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4)

for i in range(40):
	
	if i%100 == 0:
		
		train_accuracy = accuracy.eval(feed_dict={x:batch[0], y_: batch[1], keep_prob: 1.0})
		print "step %d, training accuracy %g"%(i, train_accuracy)
		train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
