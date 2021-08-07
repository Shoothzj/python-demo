import tensorflow as tf

print(tf.__version__)

a = tf.constant([1.0,2.0], name="a")
b = tf.constant([2.0,3.0], name="b")

result = tf.add(a, b)
print(result)

