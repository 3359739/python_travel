class szc_dog():
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age = value
dog = szc_dog("szc",3)

getattr(dog, 'name')#获取属性要是存在取出值不存在则抛出异常
setattr(dog,'name1','szc1')#设置属性要是存在则修改值不存在则创建属性
hasattr(dog, 'name12')#判断是否存在存在则返回true不存在则返回false
delattr(dog,'name1')#删除属性

