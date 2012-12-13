Date:2011-9-16
Title:莫工厂的面试题之一古诗横转
Tags:python
Slug:shi-ci-heng-zhuan

要求横转古诗输出，输出的结果请运行一下程序。

    string = u"""静夜思 李白
    床前明月光，
    疑似地上霜。
    举头望明月，
    低头思故乡。
    """


    list_s=[L for L in string.splitlines()[::-1]]
    row_num = max(map(len,list_s))
    out=[[row[L] for row in list_s] for L in xrange(row_num)]
    print '\n'.join([U'┊'.join(row) for row in out])
