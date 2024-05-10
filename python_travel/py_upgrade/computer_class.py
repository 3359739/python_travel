class dog_xzc:
    age=456
    def __init__(self, age=19,name='alxe'):
        self.age = age
        self.__name=name#在变量前面加上__变成私有变量
    @classmethod#添加了后的方法只能访问类变量不能访问实例变量
    def hot(self):
        print(self.age)
    def get(self):#slef指向的是调用对象
        print(self)
        print(self.age)
    @classmethod
    def get_2(cls):#加上classmethod后self或cls是指向本身也就是dog_xzc而不去调用对象
        print(cls)
    @staticmethod
    def static():#staticmethod相当于定义了一个局部域函数为该类专门服务，
        print("123456")
# dog_xzc(15).get()
# dog_xzc().hot()
# a=dog_xzc()
# print(a._dog_xzc__name)#强制访问私有变量
# a.get()
# a.get_2()
# print(a.static())

class cat_xzc:
    # 注意函数名不能和变量名一样
    def __init__(self):
        self._name=None
    @property  #设置为专门获取的,这个方法是专门为想要私有变量的变量赋值和获取
    def name(self):
        print("获取")
        return self._name
    @name.setter #专门设置的函数name+setter
    def name(self,nameS):
        self._name=nameS
name=cat_xzc()
name.name=456789
print(name.name)