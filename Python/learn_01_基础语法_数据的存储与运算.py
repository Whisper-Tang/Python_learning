# python中的注释：# 引用起来的内容就是注释，注释是用来解释代码的，注释不会被执行
# python中语句不需要分号结尾，换行就是一条语句的结束
# 仅当需要在同一行写多条语句时，才需要使用分号分隔
print("")
print("hello world!")
print("welcome to python programming language!")

# 变量：变量是用来存储数据的容器，
# 变量名可以由字母、数字和下划线组成，但不能以数字开头，变量名区分大小写·
# 定义变量：变量名 = 值，
# 这与C语言中的变量定义不同，Python中的变量不需要指定类型；
# Python会根据赋值的值自动推断变量的类型
name = "Alice"
age = 30

# Python中的数据类型
# 字面量：直接写出来的值就叫字面量
name = "value"
# 数字类型：整数和浮点数
int_num = 1
float_num = 1.0
# 字符串类型 "" 引用起来的内容就是字符串
str1 = "hello"
str2 = 'world'
# 布尔类型：true/false
bool1 = True
bool2 = False
# 空类型：None
none1 = None

# 数据容器：用来存储数据的容器，常见的数据容器有列表、元组、字典和集合
# 列表类型：[] 引用起来的内容就是列表
list1 = [1, 2, 3]
# 元组类型:() 引用起来的内容就是元组
tuple1 = (1, 2, 3)
# 字典类型: {} 引用起来的内容就是字典
dict1 = {"name": "WhisperTangOvO", "age": 24}
# 集合类型：{} 引用起来的内容就是集合
set1 = {1, 2, 3}

# 一个变量可以存储不同类型的数据，Python是动态类型语言
var = 1
var = "hello"
var = [1, 2, 3]
# 但是一般一个变量存储的数据类型应该保持一致，这样代码更容易理解和维护

# 一次性定义多个变量
a, b, c = 1, 2, 3
# 同时给多个变量赋相同的值
x = y = z = 0

# 标识符：标识符是用来标识变量、函数、类等的名字，标识符必须遵守以下规则：
# 1. 标识符只能由字母、数字和下划线组成，但不能以数字开头
# 2. 标识符区分大小写
# 3. 标识符不能使用Python的关键字
# 命名规范：
# 1. 有意义
# 2. 蛇形命名法：多个单词用下划线分隔且全为小写，例如：variable_name
# 3. 驼峰命名法：每个单词的首字母大写，例如：VariableName
# 4. 常量命名法：所有字母大写，单词之间用下划线分隔，例如：CONSTANT_NAME


# c语言中交换两个变量
a = 5
b = 10
print(f"交换前: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"c语言交换后: a = {a}, b = {b}")
# python中交换两个变量:
# 直接交换，不需要临时变量：a, b = b, a
a, b = b, a
print(f"python交换后: a = {a}, b = {b}")


# 获取数据类型
# type()函数可以获取数据的类型
print(type("嘻嘻"))  # <class 'str'>
print(type(10))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type(True))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>
print("")

# 判断数据类型
# isinstance()函数可以判断数据是否是某个类型
print(isinstance("嘻嘻", str))  # True
print(isinstance(10, int))  # True
print(isinstance(1.0, float))  # True
print(isinstance(True, bool))  # True
print(isinstance(None, type(None)))  # True
print("")

# 字符串定义方式
# 双引号定义字符串
str1 = "双引号定义:hello world"
# 单引号定义字符串
str2 = '单引号定义:hello world'
# 三引号定义字符串，可以定义多行字符串
str3 = """
三引号定义:
    hello
    world
    这是一个多行字符串
    可以换行
    还可以缩进
    # 这是一个注释，因为在三引号内,不会被执行"""
print(str1)
print(str2)
print(str3)
print("")

# 转义字符:\
str4 = """借用转义字符"\\"输出\"\"\"\"\"\"\"\""""
print(str4)
print("")

# 字符串的拼接
str5 = "hello" + " " + "world"
print(f"使用字符串拼接'hello'和'world':\n\t\"hello\" + \" \" + \"world\" =  {str5}")
# *加号仅可以拼接连个字符串,不能拼接字符串和其他类型的数据
# str6 = "hello" + 1  ==> ERROR!!!!!


class Person:
    def __init__(self, name, age, profession, hobby):
        self.name = name
        self.age = age
        self.profession = profession
        self.hobby = hobby

    def introduce(self):
        return f"大家好，我是{self.name}，今年{self.age}岁，职业是{self.profession}，爱好是{self.hobby}。"


person1 = Person("WhisperTangOvO", 24, "程序员", "编程")
print(person1.introduce())
print("")
# 字符串格式化
# 1.字符串占位符
# %s:字符串占位符
# %d:整数占位符
# 前面有多少个占位符，字符串后面%括号内就要有多少个变量，变量的顺序要和占位符的顺序一致
name = "WhisperTangOvO"
age = 24
profession = "程序员"
hobby = "编程"
introduction = "大家好，我是%s，今年%d岁，职业是%s，爱好是%s。" % (name, age, profession, hobby)
print("使用\%作为占位符格式化字符串:")
print(introduction)
print("")

# 2.使用f{}字符串格式化
# 字符串前使用f或F标识符,f后接""引起字符串,
# 字符串中使用{}占位符，{}内可以直接使用变量名或表达式
# f字符串格式化比字符串占位符更简洁和易读，推荐使用f字符串格式化
introduction_f = f"大家好，我是{name}，今年{age}岁，职业是{profession}，爱好是{hobby}。"
print("使用f{}字符串格式化:")
print(introduction_f)
print("")

# python中的输入和输出
# 输入：input()函数可以获取用户输入的数据，

############################################
# input()函数会将用户输入的数据作为字符串返回####
############################################

#  如果需要其他类型的数据，需要进行类型转换.
# name = input("请输入你的名字: ")
# age = int(input("请输入你的年龄: "))
# profession = input("请输入你的职业: ")
# hobby = input("请输入你的爱好: ")
# input后面括号内的内容是提示用户输入的内容，
# 提示会显示在控制台上

# 数据类型强制转换
# 转换方式: 目标类型(原类型值);
# 注意转换时可能会发生错误，例如将一个无法转换为整数的字符串转换为整数会发生错误
str_num = "123"
int_num = int(str_num)  # 将字符串转换为整数
print(f"将字符串'{str_num}'转换为整数: {int_num}")
float_num = float(str_num)  # 将字符串转换为浮点数
print(f"将字符串'{str_num}'转换为浮点数: {float_num}")
bool_num = bool(str_num)  # 将字符串转换为布尔值，非空字符串转换为True，空字符串转换为False
print(f"将字符串'{str_num}'转换为布尔值: {bool_num}")
print("")


# 算数运算符：+ - * / % ** //
# 相比c语言，python中的除法运算符/总是返回一个浮点数，即使两个操作数都是整数
5/2  # 结果是2.5
# 运算符//，表示整数除法，返回商的整数部分
5//2  # 结果是2
# 幂运算符**，表示乘方运算，
2**3  # 结果是2^3=8

# input（）函数获取用户输入的数据，默认是字符串类型，如果需要其他类型的数据，需要进行类型转换
# 例如：age = int(input("请输入你的年龄: ")) #将用户输入的年龄转换为整数类型

# 赋值运算符与c语言逻辑相同，常见的赋值运算符有：= += -= *= /= %= **= //=
# a ?= b  <==> a = a ? b

# 比较运算符：== != > < >= <=

# 逻辑运算符：and or not
# c语言       python      逻辑
# a && b     a and b      与
# a || b     a or b       或
#   !a         not a      非
#
# 运算符:
# in:判断一个元素是否在一个容器中，返回布尔值
# not in:判断一个元素是否不在一个容器中，返回布尔值
# is:判断两个对象是否是同一个对象，返回布尔值
# is not:判断两个对象是否不是同一个对象，返回布尔值
#
