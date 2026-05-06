
# 圆的面积
def circle_Area(radius: float) -> float:
    return round(3.14*radius*radius, 2)


# __name__ : 直接运行文件时,值为'__main__';作为模块被引入时值为"模块名"
if __name__ == '__main__':
    print('自定义模块测试成功')
elif __name__ == 'DiyModuleTest':
    print('自定义模块引入成功')
else:
    print(__name__)
