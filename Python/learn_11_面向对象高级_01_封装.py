'''
封装
    将数据的属性和操作函数封装到一个类中，形成一个独立的实体
    隐藏内部实现细节，仅对外暴露必要的接口（功能调用函数）
    ==> 优点:
        1. 提高代码的可维护性和可扩展性
        2. 防止外部直接修改内部数据，保护数据安全
        3. 提高代码的可读性和可理解性
        4. 便代码的复用和维护
    ==> 公共属性\方法: 对外暴露的方法
    ==> 私有属性\方法: 内部的实现细节
'''

# 私有定义:
# 私有属性定义: 以'__'开头的属性,只能在类的内部访问
# 私有方法定义: 以'__'开头的方法,只能在类的内部访问
# ==> Python中没有私有属性\方法,只是通过  约定的命名规范  来实现


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
        print(f"{self.brand}-{self.model} 已售出" )
    def get_owner(self):
        return self.__owner


if __name__ == "__main__":
    c1 = Car("BMW", "X5", 800000 , "whisper")
    c1.drive()
    c1.stop()
    # print(c1.__owner)
    # c1.__sale()
    print(c1.get_owner())


# 强制访问类内私有属性\方法
# ==> 通过类名__属性名 来访问
# ==> 但是不建议这样做,因为这样会破坏封装的原理
# ==> 只有在特殊情况下,才建议这样做
    c1._Car__sale()
    print(c1._Car__owner)