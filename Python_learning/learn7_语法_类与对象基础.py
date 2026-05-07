# 类的定义
import random


class Transport:
    pass

# 类名的命名规范：驼峰命名法
# 类名的每一个单词的首字母都大写


# 创建对象
c1 = Transport()

# 动态添加属性=================>不推荐使用，因为会改变类的定义
c1.brand = "BYD"
c1.model = "E6"
c1.price = 200000
print(c1)
print(c1.__dict__)
# __dict__是Python中自定义类的一个特殊属性
# 用于以字典的形式存储对象的属性和对应的值
# 可以通过__dict__来查看对象的所有属性和对应的值

# 推荐使用方法定义


class Transport:
    # __init__是初始化方法 <==> C++中的构造函数
    # 创建对象时会自动调用，用于初始化对象的属性
    def __init__(self, brand, model, price):  # self类似this,表示对象本身
        self.brand = brand
        self.model = model
        self.price = price


# 创建对象
c1 = Transport("BMW", "X5", 800000)  # self无需手动传递
print(c1)
print(c1.__dict__)


# 实例方法
class Player:
    def __init__(self, name: str, id: str, rank: int, score: int):
        self.name = name
        self.id = id
        self.rank = rank
        self.score = score
    # 玩游戏的方法

    def play(self):
        self.score += random.randint(-13, 25)
        print(f"{self.name}正在排位上分, 最新分数为:{self.score}")
    # 改变ID的方法

    def cangeid(self, new_id: str):
        self.id = new_id
        print(f"{self.name}的id  已变更为 {self.id}")
    # 查看当前排名和分数的方法

    def get_rank(self):
        return self.rank

    def get_score(self):
        return self.score


# 创建对象
p1 = Player("李相赫", "Hide on bush", 1, 2500)
print(p1.__dict__)
p1.play()
p1.play()
p1.play()
p1.play()
p1.play()
p1.play()
p1.play()
p1.play()
p1.play()
p1.play()
p1.play()
p1.play()
p1.cangeid("Faker")
print(p1.__dict__)


# 魔法方法,部分类似c++中的运算符重载
# 魔法方法无需手动调用,会自动调用
# __init__是初始化方法 <==> C++中的构造函数
# __str__是字符串方法 <==> C++中的toString()方法,用于将对象转换为字符串

# __eq__是等于方法 <==> C++中的==运算符重载
# __ne__是不等于方法 <==> C++中的!=运算符重载

# __lt__是小于方法 <==> C++中的<运算符重载
# __gt__是大于方法 <==> C++中的>运算符重载
# __le__是小于等于方法 <==> C++中的<=运算符重载
# __ge__是大于等于方法 <==> C++中的>=运算符重载

# __add__是加法方法 <==> C++中的+运算符重载
# __sub__是减法方法 <==> C++中的-运算符重载
# __mul__是乘法方法 <==> C++中的*运算符重载
# __div__是除法方法 <==> C++中的/运算符重载,已经弃用,建议使用__truediv__代替
# __truediv__是真除法方法 <==> C++中的/运算符重载,返回浮点数结果
# __floordiv__是地板除法方法 <==> C++中的//运算符重载,返回整数结果,向下取整
# __mod__是取余方法 <==> C++中的%运算符重载
# __pow__是指数方法 <==> C++中的**运算符重载

# __and__是与操作符 <==> C++中的&运算符重载
# __or__是或操作符 <==> C++中的|运算符重载
# __not__是非操作符 <==> C++中的!运算符重载

# __isinstance__是 isinstance()方法 <==> C++中的isinstance()函数


class Student:
    def __init__(self, name: str, id: int, age: int):
        self.name = name
        self.id = id
        self.age = age

    def __str__(self):
        return f"姓名:{self.name}, 学号:{self.id}, 年龄:{self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id and self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __le__(self, other):
        return self.age <= other.age

    def __ge__(self, other):
        return self.age >= other.age


s1 = Student("张三", 2021001, 20)
s2 = Student("李四", 2021002, 21)
print(s1)
print(s2)
print(s1 < s2)
print(s1 > s2)
print(s1 <= s2)
print(s1 >= s2)

# 实例属性 和 类属性
# 实例属性: 每个对象都有自己的属性,互不干扰,在__init__方法中定义
# 类属性: 所有对象共享的属性,通过类名来访问,直接在类中定义
# 通过实例查找属性,会先查找实例属性,再查找类属性
# 通过类名查找属性,会直接查找类属性


class Teacher:
    standard_salary: int = 10000  # 类属性,标准薪水
    work_time: int = 8  # 类属性,工作时间,单位:小时

    def __init__(self, name: str, id: int, age: int, salary: int = standard_salary):
        self.name = name  # 实例属性,姓名
        self.id = id  # 实例属性,工号
        self.age = age  # 实例属性,年龄
        self.salary = salary  # 实例属性,薪水

    def __str__(self):
        return f"姓名:{self.name}, 工号:{self.id}, 年龄:{self.age}"


t1 = Teacher("王老师", 2021001, 30, 8000)
print(t1)
print(f"王老师的薪水为:{t1.salary},工作时间{t1.work_time}小时")
t2 = Teacher("李老师", 2021002, 35)
print(t2)
print(f"李老师的薪水为:{t2.salary},工作时间{t2.work_time}小时")
# 由上可见,实例属性优先于类属性

