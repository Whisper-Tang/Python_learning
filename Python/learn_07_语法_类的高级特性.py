# 类的高级特性：继承、多态、属性装饰器、类方法、静态方法、抽象类

from abc import ABC, abstractmethod


# ==============================
# 1. 继承 (Inheritance)
# ==============================
# 语法：class 子类名(父类名):
# 子类继承父类所有属性和方法，可以重写（override）父类方法

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self) -> str:
        return f"{self.name} 发出了声音"

    def __str__(self) -> str:
        return f"{self.name}, {self.age}岁"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        # 调用父类的 __init__
        super().__init__(name, age)
        self.breed = breed

    # 重写父类方法
    def speak(self) -> str:
        return f"{self.name} 说: 汪汪!"

    def fetch(self) -> str:
        return f"{self.name} 正在接飞盘"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} 说: 喵喵~"


dog = Dog("旺财", 3, "金毛")
cat = Cat("咪咪", 2)
print(dog)
print(dog.speak())
print(dog.fetch())
print(cat)
print(cat.speak())
print()


# ==============================
# 2. 多态 (Polymorphism)
# ==============================
# 同一个方法，不同类的对象表现不同

def animal_show(animal: Animal):
    """多态：传入任意 Animal 子类对象，表现出各自的行为"""
    print(f"--> {animal.speak()}")


animals: list[Animal] = [
    Dog("大黄", 5, "中华田园犬"),
    Cat("小花", 1),
    Dog("阿福", 2, "柯基"),
    Cat("小白", 3),
]

for a in animals:
    animal_show(a)
print()


# ==============================
# 3. @property 属性装饰器
# ==============================
# 把方法变成属性一样访问，同时可以添加 getter/setter/deleter

class Student:
    def __init__(self, name: str, score: int):
        self._name = name
        self._score = score  # _score 为私有约定

    @property
    def score(self) -> int:
        """getter：像访问属性一样获取分数"""
        return self._score

    @score.setter
    def score(self, value: int):
        """setter：设置分数时自动校验"""
        if not 0 <= value <= 100:
            raise ValueError(f"分数必须在 0-100 之间，收到: {value}")
        self._score = value

    @property
    def grade(self) -> str:
        """计算属性：根据分数动态计算等级"""
        if self._score >= 90:
            return "A"
        elif self._score >= 80:
            return "B"
        elif self._score >= 70:
            return "C"
        elif self._score >= 60:
            return "D"
        else:
            return "F"


s = Student("张三", 85)
print(f"分数: {s.score}, 等级: {s.grade}")
s.score = 92
print(f"修改后 -> 分数: {s.score}, 等级: {s.grade}")
# s.score = 150  # 会触发 ValueError
print()


# ==============================
# 4. @classmethod 类方法
# ==============================
# 第一个参数是 cls（类本身），可以访问类属性、创建实例

class Person:
    species = "人类"  # 类属性

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> "Person":
        """工厂方法：通过出生年份创建实例"""
        from datetime import datetime
        age = datetime.now().year - birth_year
        return cls(name, age)

    @classmethod
    def get_species(cls) -> str:
        return f"物种: {cls.species}"

    def __str__(self) -> str:
        return f"{self.name}, {self.age}岁"


print(Person.get_species())
p = Person.from_birth_year("李华", 2000)
print(p)
print()


# ==============================
# 5. @staticmethod 静态方法
# ==============================
# 不需要访问实例(self)和类(cls)，只是一个普通函数放在类里

class MathUtils:
    @staticmethod
    def add(x: int, y: int) -> int:
        return x + y

    @staticmethod
    def is_prime(n: int) -> bool:
        """判断是否为质数"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


print(f"3 + 5 = {MathUtils.add(3, 5)}")
print(f"17 是质数吗? {MathUtils.is_prime(17)}")
print(f"18 是质数吗? {MathUtils.is_prime(18)}")
print()


# ==============================
# 6. 抽象类 (Abstract Class)
# ==============================
# 使用 abc 模块定义抽象基类，强制子类实现特定方法

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """计算面积 — 子类必须实现"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """计算周长 — 子类必须实现"""
        pass

    def describe(self) -> str:
        """非抽象方法，子类可直接继承"""
        return f"面积: {self.area():.2f}, 周长: {self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


circle = Circle(5)
rect = Rectangle(4, 6)
print(f"圆 — {circle.describe()}")
print(f"矩形 — {rect.describe()}")

# Shape 不能直接实例化
# s = Shape()  # TypeError: Can't instantiate abstract class
print()


# ==============================
# 综合练习：学生成绩管理系统
# ==============================

class Exam(ABC):
    @abstractmethod
    def cal_total(self) -> float:
        pass


class MidtermExam(Exam):
    """期中考试"""

    def __init__(self, math: float, english: float):
        self.math = math
        self.english = english

    def cal_total(self) -> float:
        return self.math * 0.5 + self.english * 0.5


class FinalExam(Exam):
    """期末考试"""

    def __init__(self, math: float, english: float, science: float):
        self.math = math
        self.english = english
        self.science = science

    def cal_total(self) -> float:
        return self.math * 0.4 + self.english * 0.35 + self.science * 0.25


def print_score(exam: Exam):
    print(f"总成绩: {exam.cal_total():.1f}")


mid = MidtermExam(85, 92)
final = FinalExam(88, 90, 78)

print("期中考试:")
print_score(mid)
print("期末考试:")
print_score(final)
