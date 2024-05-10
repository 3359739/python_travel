class szc_dog():
    def __init__(self, name):
        self.name = name
        print(self)

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


"""
调用类方法时最先调用的是new在由new返回一个对象后才调用init方法
__new__方法是用来创建对象实例的，而__init__方法是用来初始化对象的
__new__方法会返回一个创建好的对象实例（通常是self），而__init__方法是用来初始化这个对象的
因此，在调用__init__方法之前，必须先调用__new__方法。
super().__new__(cls)是调用父类的__new__方法，创建一个对象实例
super().__init__()是调用父类的__init__方法，对创建好的对象实例进行初始化
"""


class szc_dog_version2():
    sss = "dasdas"

    def __init__(self, name):
        self.name = name

    def __len__(self):  # 当我们对者类调用len方法时会进入到这个魔术方法
        return 100

    def __hash__(self):  # 调用hash时调用进入这个魔术方法
        return hash(self)

    def __getitem__(self, item):  # 调用[]时进入这个魔术方法
        return f"值：{self.__dict__[item]}"
        print("szc_dog_version2被调用了")

    def __str__(self):  # 改变打印类的返回值
        return f"这个方法的属性{self.__dict__}"

    def __del__(self):  # 程式结束会调用
        return print("szc_dog_version2被删除了")


    def __call__(self, *args, **kwargs):#这个是直接类名加()可以进入这个方法
        print("call")
        return "szc_dog_version2被调用了"

def __call__(self, *args, **kwargs):#这个是直接类名加()可以进入这个方法
        print("call")
        return "szc_dog_version2被调用了"
dynamic_type=type("szc_dog_version3",(object,),{"name":"123456","__call__":__call__})
# 动态创建一个类szc_dog_version3,继承object,动态添加__call__方法

