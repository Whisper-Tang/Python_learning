# 全局变量&局部变量
# 与C语言特性大致相同

from cmd import IDENTCHARS
import re


num1 = '全局变量'


def test1():
    num1 = '局部变量'  # 此处num1为与 全局变量num1 同名的局部变量
    print(num1)
    return num1


test1()
if num1 == '全局变量':
    print("全局变量调用失败")
else:
    print("全局变量调用成功")


def test2():
    global num1     # 想使用全局变量 num1 需要先用global 声明
    num1 = '全局变量调用成功'
    return num1


test2()
if num1 != '全局变量调用成功':
    print("全局变量调用失败")
else:
    print("全局变量调用成功")

###########
#   参数  #
###########
# -----------------------------------
# 1.位置传参
# -----------------------------------
# 定义:


def fun1(p1, p2, p3):
    return 0


# 调用
fun1(1, 2, 3)
# ==>调用参数与定义参数顺序完全一致


# -----------------------------------
# 2.关键字传参
# -----------------------------------
# 定义:
def fun2(a, b, c, d):
    return (a, b, c, d)


# 调用:
print(fun2(b=2, c=3, d=4, a=1))
print(fun2(c=3, d=4, a=1, b=2))
# ==>定义是使用关键字(key)作为形参,调用时使用键值对来传参,不要求顺序
# -----------------------------------
# 位置参数和关键字参数可以混用,
#!!!位置参数必须在关键字参数之前写!!!!
print(fun2(1, 2, d=4, c=3))
# print(fun2(2, 3, d=4, a=1))  #error:a收到多个参数:a=2,a=3
# -----------------------------------


# ------------------------
# 3.默认参数
# ------------------------
# 从第一个有默认参数的参数起,之后的参数必须都有默认值
def fun3(p1, p2, p3, p4=0, p5=0):
    return 0


# ------------------------
# 4.不定长参数(可变参数)
# ------------------------
# ------------------------
# 4.1位置传递的不定长参数(*参数)
# ------------------------
def fun4(*param1):  # 不会封装关键字参数
    return param1
# 参数会被封装为一个元组,存在param1


# 调用:
print(fun4(1, 2, 3))
print(fun4(1, 2, 3, 4, 'str测试'))


# ------------------------
# 4.1关键字传递的不定长参数(**参数)
# ------------------------
# 参数会被封装为一个字典,存在param2
def fun4(**param2):
    return param2


# 调用:
print([s for s in fun4(a=1, b=2, c=3, d=4)])
print([fun4(a=1, b=2, c=3, d=4)[x]
      for x in [s for s in fun4(a=1, b=2, c=3, d=4)]])


# ------------------------
# 5. 特殊参数:函数作为参数
# ------------------------
def my_add(x, y):
    return x+y


def my_calc(x, y, calc):
    return calc(x, y)


print(my_calc(1, 2, my_add))  # 不能传 my_add()

# 类似std::cout


def my_print(x):
    print(x, sep='', end='')
    return my_print


userID = "whisper"
userPSWD = "Apoptoxin"
my_print(userID)('的密码是:')(userPSWD)('\n')

# ------------------------
# 6. 匿名函数
# ------------------------
# lambda 表达式:
# lambda 参数列表 : 函数体          #只能写一行
#
# 定义匿名函数:
# 函数名 = lambda 表达式
#
# example:


def new_add(x, y): return x+y


print(new_add(1, 2))

# 通常作为高阶函数的参数使用
# 表达式结果即为函数返回值

# 计算阶乘


def factorial(x):
    if type(x) != int or x < 0:
        return f"输入值异常:本函数仅支持非负整数求阶乘"
    if x == 0:
        return 1
    f = 1
    for i in range(1, x+1):
        f *= i
    return f


print(factorial(-1))
print(factorial('aaa'))
print(factorial(0))
print(factorial(7))
print(factorial(10))
# print(factorial(100))
# print(factorial(1000))
# print(factorial(1558))  # 最大 Python 3.11+ 的安全限制（4300 位）

"""
    可用三引号作为多行注释
"""