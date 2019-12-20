# _*_ coding:utf-8 _*_

# @Author: Xinbao Sun
# @Purpose: for singleton mode, totally six methods

# 1. 装饰器实现单例模式

def singleton(cls):
    def wrapper(*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = cls(*args,**kwargs)
        return cls._instance
    return wrapper

@singleton
class SingleTonTest:
    def __init__(self):
        pass
    def swim(self):
        print('swim')

s1 = SingleTonTest()
s2 = SingleTonTest()
s1.swim()
print(s1 == s2)


# 2. metaclass and __call__实现单例模式
class MyType(type):
    def __call__(self, *args, **kwargs):
        """
        self指的是SingleTonTest类
        """
        if not hasattr(self,'_instance'):
            self._instance = super(MyType,self).__call__(*args,**kwargs)
        return self._instance

class SingleTonTest(metaclass=MyType):
    @classmethod
    def swim(cls):
        print('swim2')

#SingleTonTest是元类MyType的对象，对象加括号执行元类中的__call__方法
s1 = SingleTonTest()
s2 = SingleTonTest()

s2.swim()
print(s1 == s2)

# 3. 基于__new__实现单例模式
class SingleTonTest(object):
    def __new__(cls, *args, **kwargs):
        """
        cls：<class '__main__.SingleTonTest'>
        """
        if not hasattr(cls,'_instance'):
            cls._instance = super(SingleTonTest, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, inp='okay'):
        self.inp = inp

    def fly(self):
        print('fly:'+self.inp)
    @classmethod
    def swim(cls):
        print('swim3')

s1 = SingleTonTest()
s2 = SingleTonTest()
s1.fly()
s2.swim()
print(s1 == s2)
