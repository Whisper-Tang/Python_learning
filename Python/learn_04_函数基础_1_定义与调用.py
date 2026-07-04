######################################
# *** ***Python中函数的定义方式*** *** #
######################################
# def 函数名(参数列表):
#   函数体
#   ...
#   return 返回值

# 定义加法函数
def my_sum(num1=0, num2=0):
    return num1 + num2


# 调用加法函数
a = my_sum(20, 10)
# print(a)

# 定义圆的面积和周长函数


def circle_Area_Len(rid=0):
    # 返回值可以有多个，多个返回值被组包为一个元组
    return round(3.14*(rid**2), 2), round(6.28*rid, 2)


# 调用获取面积和周长
circle_Area, circle_Len = circle_Area_Len(24.5)  # 解包获取返回值
# print(circle_Area,circle_Len)
# C语言中可以先声明函数,然后调用,之后再写实现函数
# Python函数没有声明,且必须先定义实现,才能调用!!!!!!!!!!!!!!!

######################################
# *** ***Python中函数的说明文档*** *** #
######################################

# def 函数名(参数列表):
#   """                           # 函数的说明文档开始和结尾用三引号包裹
#   :param param1:                #
#   :type param1:                 #
#   :param param2:                #
#   :type param2:                 #
#   ...                           # 说明文档内容
#   ...                           #
#   :return:                      #
#   :rtype:                       #
#   """                           # 说明文档结尾
#
#   函数体
#   ...
#   return 返回值

# example：

# Python推荐格式：
def Python_circle_Area_Len(rid=0):
    """
    计算圆的面积和周长。

    根据给定的半径计算圆的面积和周长，并保留两位小数。

    :param rid: 圆的半径 (radius id)，必须为非负数。
    :type rid: int or float
    :return: 一个包含两个元素的元组。
    :rtype: tuple(float, float)
    :raises ValueError: 如果半径为负数时抛出。

    示例:
        >>> area, length = circle_Area_Len(5)
        >>> print(area)
        78.5
    """
    return round(3.14*(rid**2), 2), round(6.28*rid, 2)

# Google格式
def google_circle_Area_Len(rid=0):
    """
    计算圆的面积和周长。

    根据给定的半径计算圆的面积和周长，结果保留两位小数。

    参数:
        rid (float): 圆的半径。

    返回:
        tuple: 包含两个浮点数的元组：
            - 第一个元素是面积 (Area)。
            - 第二个元素是周长 (Length)。

    示例:
        >>> area, length = circle_Area_Len(5)
        >>> print(area)
        78.5
    """
    return round(3.14 * (rid**2), 2), round(6.28 * rid, 2)
# 函数的说明文档采用Sphinx 文档格式

# 函数嵌套调用时，函数调用栈与C语言的逻辑相同
