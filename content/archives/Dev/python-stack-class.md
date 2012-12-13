Date:2011-09-16
Title:python实现一个Stack类
Tags:python,stack
Slug:python-class-stack

python 实现Stack类。

之前网上也有不同的实现，但是不是感觉版本太老就是感觉写的不好。自己写了一个，请大家指教。


    # -*- coding:utf-8 -*-
    class Stack(object):
        """
            Stack 类
        """
        def __init__(self, other=None):
            """doc test
            >>> s = Stack([1,2,3,4])
            >>> s.pop()
            4
            >>> s.count
            3
            >>> e = Stack([1,2,3,4])
            >>> s != e
            True
            >>> s.push(4)
            >>> s == e
            True
            >>> s += e
            >>> len(s)
            8
            >>> s.clear()
            >>> s.empty
            True
            >>> s.top
            data is empty
            """
            self.data = []
            if other is not None:
                if isinstance(other, Stack):
                    self.data[:] = other.data
                elif isinstance(other, (list, tuple, set)):
                    self.data[:] = list(other)
                else:
                    self.data  = list(other)

        def __repr__(self):
            return "<Stack: %s>" % str(self.data)

        def __len__(self):
            return len(self.data)

        def __eq__(self, other):
            return self.data == self.__cast(other)

        def __getitem__(self, i):
            return self.data[i]

        def __setitem__(self, i, item):
            self.data[i] = item

        def __delitem__(self, i):
            del self.data[i]

        def __add__(self, other):
            if isinstance(other, Stack):
                return self.__class__(self.data + other.data)
            else:
                raise TypeError('unsupported operand type(s) for +: %s' %(getattr(other,"__class__",'')))

        def __iadd__(self, other):
            if isinstance(other, Stack):
                self.data += other.data
                return self
            else:
                raise TypeError('unsupported operand type(s) for +=: %s' %(getattr(other,"__class__",'')))

        def __cast(self, other):
            if isinstance(other, Stack):
                return other.data
            else:
                return other

        @property
        def top(self):
            if self.empty:
                print 'data is empty'
                return None
            return self.data[-1]

        @property
        def count(self):
            return len(self.data)

        @property
        def empty(self):
            return len(self.data) == 0

        def push(self, item):
            self.data.append(item)

        def pop(self):
            if self.empty:
                print 'data is empty'
                return None
            return self.data.pop()

        def clear(self):
            self.data = []
