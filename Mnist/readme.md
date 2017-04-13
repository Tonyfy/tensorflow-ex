## CNN for mnist

可运行程序文件：[mnist_CNN1.py](./mnist_CNN1.py)

程序内容：基于tensorflow构建CNN网络模型，并进行训练和测试。在测试集上获得99.24%的准确率。详细参考[这里](http://wiki.jikexueyuan.com/project/tensorflow-zh/tutorials/mnist_pros.html)

```
step 19600, training accuracy 1
step 19700, training accuracy 1
step 19800, training accuracy 1
step 19900, training accuracy 0.98
test accuracy 0.9924
```

## fully connected for mnist

[mnist_fc.py](./mnist_fc.py)用于构造fc network,对输入进行预测，训练部分，并计算loss。

[fully_connected_feed.py](./fully_connected_feed.py)完成训练（可设置训练过程相关的参数），并在验证集和测试集上进行评估。

训练输出为：

```
Step 1600: loss = 0.53 (0.002 sec)
Step 1700: loss = 0.34 (0.002 sec)
Step 1800: loss = 0.37 (0.002 sec)
Step 1900: loss = 0.45 (0.002 sec)
Training Data Eval:
  Num examples: 55000  Num correct: 49178  Precision @ 1: 0.8941
Validation Data Eval:
  Num examples: 5000  Num correct: 4515  Precision @ 1: 0.9030
Test Data Eval:
  Num examples: 10000  Num correct: 9005  Precision @ 1: 0.9005
```

指定`log`存储的位置，保存训练过程中的checkpoint，使用`tensorboard --logdir=$logdir` 即可在浏览器中（http://localhost:6006/）  观测模型相关的数据。
loss变化如下图：

![loss][loss]

[loss]:imgs/loss.png
图模型结构如下：

![gr][gr]

[gr]:imgs/gragh.png