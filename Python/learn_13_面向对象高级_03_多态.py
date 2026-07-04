'''
多态
    多态是指在不同类之间，可以使用相同的方法名，但是实现不同的功能。
'''
class Car:
    def charge(self):
        print('补充动力：')

class ElectricCar(Car):
    def charge(self):
        super().charge()
        print('充电中…………')
        
class GasCar(Car):
    def charge(self):
        super().charge()
        print('加油中…………')


# 充电操作根据传入的参数类型，调用不同的充电方法
def charge_car(car: Car):
    car.charge()

# if __name__ == '__main__':
#     byd = ElectricCar()
#     bmw = GasCar()
    
#     charge_car(byd)
#     charge_car(bmw)

'''
鸭子类
    鸭子类是指在不同类之间，可以使用相同的方法名，但是实现不同的功能。
    这种情况被称为鸭子类
'''
class Duck:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.age}岁的{self.name}正在吃')

class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.age}岁的{self.name}正在吃')

class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.age}岁的{self.name}正在吃')

def eat(duck: Duck):
    duck.eat()

if __name__ == '__main__':
    eat(Duck('鸭子', 1))
    eat(Dog('狗', 1))
    eat(Cat('猫', 1))

'''
    鸭子类型：
        "如果一个对象，结构像鸭子，行为像鸭子，那么——它就是鸭子"
    ==> 我们关注的是对象的 行为 而不是 类型 
'''

