import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as inputdata
mnist = inputdata.read_data_sets("MNIST_data/", one_hot=True)

#任意的输入
x=tf.placeholder(tf.float32,[None,784])

#模型参数用Variable，可随时改变

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

# softmax,分类器
y = tf.nn.softmax(tf.matmul(x,W)+b)

#real label
y_true = tf.placeholder("float",[None,10])

# 对所有数据点的交叉熵求和
cross_entropy = -tf.reduce_sum(y_true*tf.log(y))

# 梯度下降，学习率0.01,最小化交叉熵cross_entropy
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.global_variables_initializer()

sess =tf.Session()
sess.run(init)

#循环训练1000次
for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    # feed填入训练数据
    sess.run(train_step,feed_dict={x:batch_xs,y_true:batch_ys})
    #print("train processing "+str(i/1000.)+"%")

# 预测正确的结果，布尔型
correct_predition = tf.equal(tf.argmax(y,1),tf.argmax(y_true,1))

#布尔型转化为准确率
accuracy = tf.reduce_mean(tf.cast(correct_predition,"float"))

print(sess.run(accuracy,feed_dict={x:mnist.test.images,y_true:mnist.test.labels}))