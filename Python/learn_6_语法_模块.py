# 类似于c的分文件编写,或者说c语言的库函数
# Python模块(module): 一个.py文件就是一个模块，模块是Python程序的基本组织单位。
# 在模块中可以定义变量、函数、类，以及可执行的代码。
# 自定义模块<==>自定义库函数

# 导入模块
# import 模块名 <==> #include <函数库>

# 导入形式                          调用方式
# import 模块名                     模块名.函数
# import random                    print(random.randint(1, 100))

# import 模块名 as 别名              别名.函数
# form 模块名 import 函数            函数           #只导入某个函数功能
# form 模块名 import 函数 as 别名     别名
# form 模块名 import *               函数           #导入所有函数,但是不用写模块文件
# __all__:模块级别的特殊变量,用于在模块中指定*所引入的模块功能
# __all__ = "函数功能,..."

from Package.myPackageTest import *  # 调用包
import DiyModuleTest
radius: float = 2
print(f"半径为{radius}的圆面积为(π=3.14): {DiyModuleTest.circle_Area(radius)}")


# 包(Package)
# 本质时一个文件夹,该文件夹包含若干个python模块文件(.py文件) 以及 一个__init__.py文件
# Package -┮----- __init__.py
#          ┕----- 模块文件若干
# 包名.模块名.函数功能名
# __init__.py 中为包的描述信息
# __version__ = "1.0.0"  #版本信息
# __author__ = "whisper"  #作者信息
# __all__ = ["模块名"]
# #用于在使用 " form 包名 import * " 进行模块导入时,
# *指定的是那些模块

# from ______  import *
# _____处本质上是一个引入功能的文件路径,默认为相对路径
# 若模块或包在其他路径下,应使用绝对路径
