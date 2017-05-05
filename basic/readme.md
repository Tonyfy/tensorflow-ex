# 基础操作

* 初始化变量，保存和加载模型

* [可视化训练过程和图模型](../Mnist/readme.md),监测训练情况

* [读取数据](http://wiki.jikexueyuan.com/project/tensorflow-zh/how_tos/reading_data.html)
组织进行训练

        TensorFlow程序读取数据一共有3种方法:
        1,供给数据(Feeding)： 在TensorFlow程序运行的每一步， 让Python代码来供给数据。
        2,从文件读取数据： 在TensorFlow图的起始， 让一个输入管线从文件中读取数据。
        3,预加载数据： 在TensorFlow图中定义常量或变量来保存所有数据(仅适用于数据量比较小的情况)。

* 线程和队列

TensorFlow的Session对象是可以支持多线程的，
因此多个线程可以很方便地使用同一个会话（Session）并且并行地执行操作。
然而，在Python程序实现这样的并行运算却并不容易。所有线程都必须能被同步终止，
异常必须能被正确捕获并报告，回话终止的时候， 队列必须能被正确地关闭。

所幸TensorFlow提供了两个类来帮助多线程的实现：tf.Coordinator和 tf.QueueRunner。
从设计上这两个类必须被一起使用。
Coordinator类可以用来同时停止多个工作线程并且向那个在等待所有工作线程终止的程序报告异常。
QueueRunner类用来协调多个工作线程同时将多个张量推入同一个队列中。

Coordinator类用来帮助多个线程协同工作，多个线程同步终止。 其主要方法有：

     should_stop():如果线程应该停止则返回True。
     request_stop(<exception>): 请求该线程停止。
     join(<list of threads>):等待被指定的线程终止。

QueueRunner类会创建一组线程， 这些线程可以重复的执行Enquene操作，
 他们使用同一个Coordinator来处理线程同步终止。此外，一个QueueRunner会运行一个closer thread，
当Coordinator收到异常报告时，这个closer thread会自动关闭队列。