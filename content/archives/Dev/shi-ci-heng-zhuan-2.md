Date:2011-9-21
Title:莫工厂的面试题之一古诗横转(二)
Tags:python
Slug:shi-ci-heng-zhuan-2
要求横转古诗输出，输出的结果请运行一下程序。

之前使用列表解析实现，还可以用map + zip 实现矩阵转换。当然使用NumPy 也可以很方便实现。

代码如下：

    string = u"""静夜思 李白
    床前明月光，
    疑似地上霜。
    举头望明月，
    低头思故乡。
    """

    list_s=[L for L in string.splitlines()[::-1]]
    out=map(list,zip(*list_s))
    print '\n'.join([U'┊'.join(row) for row in out])
