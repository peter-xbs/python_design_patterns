# _*_ coding:utf-8 _*_

### 1. 抽象基类的使用

from abc import abstractmethod, ABCMeta


class Test(metaclass=ABCMeta):
    """
    本身不可被实例化，可用作其他class的祖先，内被定义的abstractmethod方法，必须被子类重写，否则子类在实例化中也会报错
    """
    @abstractmethod
    def walk(self):
        print('walk')

    @abstractmethod
    def swim(self):
        print('swim')

    def fly(self):
        print('fly')


class Test2(Test):
    def walk(self):
        print('walk2')

    def swim(self):
        print('swim2')

# t1 = Test()  # 不可实例化
t2 = Test2()
t3 = Test2()
t2.walk()  # 必须重写
t3.swim()  # 必须重写
t3.fly()  # 非abstractmethod，无需重写
print(t2 == t3)  # 非单例模式，不相等
