CIFAR-10 is a common benchmark in machine learning for image recognition.

http://www.cs.toronto.edu/~kriz/cifar.html

Code in this directory demonstrates how to use TensorFlow to train and evaluate a convolutional neural network (CNN) on both CPU and GPU. We also demonstrate how to train a CNN over multiple GPUs.

Detailed instructions on how to get started available at:

http://tensorflow.org/tutorials/deep_cnn/

## train phase

执行 ``cifar10_train.py``（初次执行，会下载数据集cifar10）
```
    F:\GFI\tensorflow-ex\cifar>python cifar10_train.py
    >> Downloading cifar-10-binary.tar.gz 100.0%
    Successfully downloaded cifar-10-binary.tar.gz 170052171 bytes.
```

训练时，batch_size = 128，max_iter = 1000000

检查点存入log目录中。

## cifar10

本例含有的图像包含10组数据分类：
```
airplane
automobile
bird
cat
deer
dog
frog
horse
ship
truck
```

## test phase

使用``python cifar10_eval.py`` 评估训练产生的模型，该脚本采用最新的checkpoint，测试集大小为10000.

## 多卡训练

使用脚本``cifar10_multi_gpu_train.py``可进行多卡训练，详见 [这里](http://wiki.jikexueyuan.com/project/tensorflow-zh/tutorials/deep_cnn.html) 。