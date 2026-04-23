##全局变量&局部变量
# 与C语言特性大致相同

num1 = '全局变量'

def test1():
    num1 = '局部变量' # 此处num1为与 全局变量num1 同名的局部变量
    print(num1)
    return num1
test1()
     
def test2():
    global num1     # 想使用全局变量 num1 需要先用global 声明
    num1 = "全局变量调用成功"
    return num1

print(num1)
