# 继承与多态
# 继承是面向对象编程的重要特性，子类可以复用父类的代码
# Python 支持多继承（一个子类可以有多个父类）

######################################
# *** 1. 单继承 *** #
######################################


from abc import ABC, abstractmethod


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} 正在吃东西"

    def sleep(self):
        return f"{self.name} 正在睡觉"

    def info(self):
        return f"我是 {self.name}，今年 {self.age} 岁"


# Dog 继承 Animal
class Dog(Animal):
    # 子类可以添加自己的属性和方法
    def __init__(self, name: str, age: int, breed: str):
        # 调用父类的 __init__ 方法
        super().__init__(name, age)
        self.breed = breed

    # 重写父类方法（多态）
    def eat(self):
        return f"{self.name}（{self.breed}）正在啃骨头"

    # 子类特有方法
    def bark(self):
        return f"{self.name} 汪汪叫！"


class Cat(Animal):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def eat(self):
        return f"{self.name}（{self.color}猫）正在吃小鱼干"

    # 也可以通过 super() 调用父类方法扩展
    def info(self):
        basic_info = super().info()
        return f"{basic_info}，毛色是 {self.color}"


# 测试单继承
dog1 = Dog("旺财", 3, "金毛")
print(dog1.eat())
print(dog1.bark())
print(dog1.info())
print()

cat1 = Cat("咪咪", 2, "黑")
print(cat1.eat())
print(cat1.info())
print()

# isinstance() 检查继承关系
print(f"dog1 是 Animal 的实例: {isinstance(dog1, Animal)}")   # True
print(f"dog1 是 Dog 的实例: {isinstance(dog1, Dog)}")         # True
print(f"dog1 是 Cat 的实例: {isinstance(dog1, Cat)}")         # False
print()


######################################
# *** 2. 多态 *** #
######################################
# 多态：不同子类对同一方法有不同实现，调用时表现各异
# Python 是"鸭子类型"：一个对象只要"走路像鸭子、叫声像鸭子"，就可以当作鸭子使用
# 不强制要求继承关系，只要对象实现了相同方法即可


def feeding_time(animal):
    """多态示例：同一个函数处理不同类型的动物"""
    print(animal.eat())


# 不同子类的 eat() 方法表现不同
feeding_time(dog1)
feeding_time(cat1)
print()


# 鸭子类型示例：只要实现了 speak 方法就能用
class Duck:
    def speak(self):
        return "嘎嘎嘎！"


class Car:
    def speak(self):
        return "滴滴滴！"


def make_sound(something):
    print(something.speak())


make_sound(Duck())   # 嘎嘎嘎！
make_sound(Car())    # 滴滴滴！
print()


######################################
# *** 3. 多继承 *** #
######################################
# Python 支持多继承，使用 MRO（Method Resolution Order）解决冲突
# MRO 顺序：子类 -> 先继承的父类 -> 后继承的父类 -> ...


class Flyable:
    def move(self):
        return "我在天上飞！"


class Swimmable:
    def move(self):
        return "我在水里游！"


# 多继承：Duck 同时继承 Flyable 和 Swimmable
class SuperDuck(Flyable, Swimmable):
    def move(self):
        # 可以选择调用哪个父类的方法
        return f"{Flyable.move(self)} 而且 {Swimmable.move(self)})"


duck2 = SuperDuck()
print(duck2.move())
print()


# 查看 MRO 顺序
print("SuperDuck 的 MRO 顺序:")
for cls in SuperDuck.__mro__:
    print(f"  {cls.__name__}")
# 输出: SuperDuck -> Flyable -> Swimmable -> object
print()


######################################
# *** 4. 私有属性与方法 *** #
######################################
# Python 没有真正的 private，命名约定：
# _name   : 约定为受保护（protected），不建议外部访问
# __name  : 名称改写机制（name mangling），变成 _类名__name


class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner             # 公开属性
        self._bank = "招商银行"         # 约定为 protected（仅提醒）
        self.__balance = balance        # 名称改写为 _BankAccount__balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            return f"存入 {amount} 元，余额: {self.__balance} 元"
        return "存款金额必须大于 0"

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"取出 {amount} 元，余额: {self.__balance} 元"
        return "余额不足或金额无效"

    def get_balance(self):
        return self.__balance


account = BankAccount("Whisper", 1000)
print(account.deposit(500))
print(account.withdraw(200))
# print(account.__balance)        # AttributeError！无法直接访问
print(account._BankAccount__balance)  # 可以通过名称改写访问（不推荐）
print()


######################################
# *** 5. 抽象基类（ABC）*** #
######################################
# 抽象类不能实例化，强制子类实现特定方法


class Shape(ABC):
    @abstractmethod
    def area(self):
        """计算面积（子类必须实现）"""
        pass

    @abstractmethod
    def perimeter(self):
        """计算周长（子类必须实现）"""
        pass

    def describe(self):
        """普通方法，子类可继承"""
        return f"面积: {self.area():.2f}, 周长: {self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# shape = Shape()    # TypeError! 不能实例化抽象类
circle = Circle(5)
rect = Rectangle(4, 6)
print(f"圆: {circle.describe()}")
print(f"矩形: {rect.describe()}")
print()


######################################
# *** 6. @property 装饰器 *** #
######################################
# 将方法调用变成属性访问，优雅实现 getter/setter


class Student:
    def __init__(self, name: str, chinese: float, math: float, english: float):
        self.name = name
        self._chinese = chinese
        self._math = math
        self._english = english

    @property
    def total(self):
        """总分（只读属性）"""
        return self._chinese + self._math + self._english

    @property
    def average(self):
        """平均分（只读属性）"""
        return round(self.total / 3, 1)

    @property
    def grade(self):
        """等级（只读属性，根据平均分动态计算）"""
        avg = self.average
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


s = Student("小明", 92, 88, 95)
print(f"总分: {s.total}")       # 像属性一样访问，其实调用了方法
print(f"平均分: {s.average}")
print(f"等级: {s.grade}")
