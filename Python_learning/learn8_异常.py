# 异常处理
# 异常是程序运行时出现的错误,导致程序正常流程中断
# 异常处理是程序在出现异常时,能够正常运行,而不是崩溃
# 处理方式:
# 1. 不做任何处理,让程序崩溃
# 2. 捕获异常:按照希望的方式,处理异常并保持程序继续运行
#   语法:
#   try:
#       可能会异常的代码1
#       可能会异常的代码2
#       ...
#   except 异常类型 as 变量名:
#      # 捕获指定异常类型,[]省略表示捕获所有异常类型
#       处理异常的代码预案
#   finally:
#       无论是否发生异常,都会执行的代码
#   
try:
    print("-"*10)
#    print(error_test)
    print(1/0)
    print("-"*10)
except NameError as e:
    print("名称异常,错误:", e)
except ZeroDivisionError as e:
    print("除零异常,错误:", e)
except Exception as e:
    print("程序异常,错误:", e)
finally:
    print("清理程序资源")
# 异常传递
# 当函数内部发生异常时,如果没有捕获,会将异常传递给调用者,
# 直到被捕获或者传递到最外层导致程序崩溃




# 3. 抛出异常,让调用者处理
#   语法:
#   raise 异常类型(异常信息)
def test():
    print("test函数")
    raise NameError("变量未定义")
try:
    test()
except NameError as e:
    print("名称异常,错误:", e)      
