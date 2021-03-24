# 通过class关键字定义了一个类
class Person:
    # 类变量
    name = "zouqun"
    age = 0
    gender = 'man'
    weigeht = 0

    def __init__(self,name,age,gender,weight):
        # self.变量名的方式，叫实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        print("__init__")

    def set_param(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age

    def set_age(self, gender):
        self.gender = gender

    def set_age(self, weigeht):
        self.weigeht = weigeht

    @classmethod
    def eat(self):
        print(f"{self.name} is eating")

    def play(self):
        print(f"{self.name} is playing")

    def jump(self):
        print(f"{self.name} is jumping")

# 类的实例化
# 类变量需要用类来访问，实例变量需要用实例来访问
# zs = Person("zhangs",20,"男",90)
# zs.eat()
# zs.play()
# zs.jump()
# print(f"张三的姓名是{zs.name},年龄是{zs.age}，性别是{zs.gender},体重是{zs.weight}公斤")
#
# print(Person.name)
# Person.name = 'tom'
# print(Person.name)

# 类方法和实例方法
Person.eat()