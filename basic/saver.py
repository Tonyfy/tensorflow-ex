import tensorflow as tf

w = tf.Variable(tf.random_normal([784,100],mean=0,stddev=0.1,dtype=tf.float32),name="weight")
b = tf.Variable(tf.random_normal([100],mean=0,stddev=0.1,dtype=tf.float32),name="bias")

init = tf.global_variables_initializer()
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    savepath = saver.save(sess,save_path="./modelpath/model.ckpt")
    print("model has been saved!\n")
