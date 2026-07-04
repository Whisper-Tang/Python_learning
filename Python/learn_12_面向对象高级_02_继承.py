'''
继承:
    ==> 定义:
        一个类可以继承另一个类的属性和方法
    ==> 语法:
        class 子类名(父类名):
            代码块
'''


class Car:
    def __init__(self, brand, model, price, owner: str):
        self.brand = brand
        self.model = model
        self.price = price
        self.__owner = owner

    def drive(self):
        print(f"{self.brand}-{self.model} 正在行驶")

    def stop(self):
        print(f"{self.brand}-{self.model} 已停止")

    def __sale(self):
        print(f"{self.brand}-{self.model} 已售出")

    def get_owner(self):
        return self.__owner
    
    def charge(self):
        print("正在补充动力:")

# 继承重载:
class FuelCar(Car):
    '''
    # 继承重载:
    # 子类可以重写父类的方法,但是方法的参数和返回值必须和父类的方法一致
'''
    def charge(self):
        print(f"{self.brand}-{self.model} 正在加油")
    # 子类重写时,需要调用父类的方法
    # ==> 通过 super() 来调用父类的方法
    #     父类名.方法名() / super().方法名()
    def charge(self):
        super().charge()
        print(f"{self.brand}-{self.model} 正在加油")


class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand}-{self.model} 正在充电")


# 继承(多继承):
'''
    # 多继承:
    # 一个类可以继承多个父类
    # ==> 语法:
    # class 子类名(父类名1, 父类名2, ...):
    #     代码块
    # ==> 注意:
    #     1. 如果多个父类有相同的方法,子类会继承第一个父类的方法
    #     2. 如果子类重写了父类的方法,子类的方法会覆盖父类的方法
'''
class AI_Driver:
    def __init__(self, AI_version: str):
        self.AI_version = AI_version

    def drive(self):
        print(f"AI司机{self.AI_version}正在驾驶")
    
    def stop(self):
        print(f"AI司机{self.AI_version}正在停止")


class AI_Car(ElectricCar, AI_Driver):
    # MRO: 方法解析顺序
    # ==> 子类的方法会先调用,如果子类没有,会调用父类的方法
    # ==> 如果父类有多个,会调用第一个父类的方法
    # ==> 如果第一个父类没有,会调用第二个父类的方法
    pass







if __name__ == "__main__":
    c1 = FuelCar("BMW", "X5", 800000 , "whisper")
    print('------继承测试------')
    c1.drive()
    c1.stop()
    # print(c1.__owner)
    # c1.__sale()
    print(c1.get_owner())
    
    c1._Car__sale() # 使用_FuelCar__sale()会报错,因为FuelCar类没有__sale()方法
    print(c1._Car__owner)

    print('------重写测试------')
    c1.charge()
    c2 = ElectricCar("BYD", "宋Plus", 800000 , "whisper")
    c2.charge()

    print('------多继承测试------')
    c3 = AI_Car("xm", "su7", 800000 , "whisper")
    '''
        class AI_Car(
            brand: Any,
            model: Any,
            price: Any,
            owner: str
            )
        ==> 注意: 
            1. 如果多个父类有相同的方法,子类会继承第一个父类的方法
            2. 如果子类重写了父类的方法,子类的方法会覆盖父类的方法
            3. MRO
    '''
    # 为了c3的初始化包含ai版本,需要自定义重写__init__方法
