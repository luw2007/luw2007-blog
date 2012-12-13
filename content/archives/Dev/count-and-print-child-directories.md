Date:2011-09-08
Title:计算当前目录下的子目录数量并打印子目录名称
Tags:count dirs, tree, python
Slug:count-and-print-child-directories

##问题:
组里有人问，有什么好方法来统计当前目录下所有子目录的数量。

##解决方案:
我大致综合大家提出的方法，做了一个对照。实现方法有4个 。其中test_diskwalk.py 是利用python 的os.walk 做的。

1. time find /usr/ -type d  |wc -l
2. time python test_diskwalk.py /usr/
3. time tree -ad /usr/ |tail -1
4. ls -aR /usr/|grep ":$" |wc -l

大致结果是ls 和tree快， find 接近是ls 的1.5倍。 os.walk 更慢。测试不太精准，权当娱乐。


##对照测试具体步骤：
利用python os.walk 实现的,disk_walk 模块是利用os.walk 实现，见附录

    ~$>cat test_diskwalk.py
    import disk_walk
    import argparse

    parser = argparse.ArgumentParser(description='list contents of directories.')
    parser.add_argument('path', metavar='path',
                       help='input a directory')
    args = parser.parse_args()
    dirs=disk_walk.diskwalk(args.path).enumerate_dirs()

    #print ' '.join(dirs)
    print '%d directories' % len(dirs)


使用time 进行的测试，需要考虑linux系统的目录缓存。 每次测试前清空缓存
测试结果如下：

    [root@fedora lw]#  time ls -aR /usr/|grep ":$" |wc -l
    19064
    real 0m22.114s
    user 0m0.873s
    sys 0m2.151s

    [root@fedora lw]# time tree -ad /usr/|tail -1
    19167 directories
    real 0m23.967s
    user 0m0.533s
    sys 0m4.013s

    [root@fedora lw]#  time python test_diskwalk.py /usr/  > /dev/null
    19167 directories
    real 0m36.643s
    user 0m3.384s
    sys 0m4.173s

    [root@fedora lw]#  time find /usr/ -type d > /dev/null
    real 0m32.541s
    user 0m0.431s
    sys 0m2.263s


可以看到 ls 最快，但是结果不知道什么原因少了很多。 tree 和 test_diskwalk.py 的结果一样，但是速度相差还是比较大的。

python的程序定制行比较强。如果不是大量io，也无所谓的。

###附录：disk_walk.py

    import os

    class diskwalk(object):
        """API for getting directory walking collections"""
        def __init__(self, path):
                self.path = path

        def enumerate_paths(self):
            """Returns the path to all the files in a directory as a list"""
            path_collection = []
            for dirpath, dirnames, filenames, in os.walk(self.path):
                for file in filenames:
                    fullpath = os.path.join(dirpath, file)
                    path_collection.append(fullpath)
            return path_collection

        def enumerate_files(self):
            """Returns all the files in a directory as a list"""
            file_collection = []
            for dirpath, dirnames, filenames, in os.walk(self.path):
                for file in filenames:
                    file_collection.append(file)
            return file_collection

        def enumerate_dirs(self):
            """Returns all the directories in a directory as a list"""
            dir_collection = []
            for dirpath, dirnames, filenames, in os.walk(self.path):
                for dir  in dirnames:
                    dir_collection.append(dir)
            return dir_collection


