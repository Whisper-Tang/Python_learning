# 网页解析
# 从原始的HTML字符串中提取出我们需要的信息
# 例如：标题、段落、图片、链接等

# lxml库解析
# 是一个高性能的HTML/XML解析库（第三方库：pip install lxml）
# 支持XPath和CSS选择器
# 可以方便地从HTML/XML文档中提取信息


# Python中文件的读写操作
# 模式：    r 读取、w 写入、a 追加
#     b 二进制模式、t 文本模式（默认）
#
# 打开---->读取/写入/追加写入---->关闭文件
#
# 打开文件
# 语法：with open(文件路径, 模式，编码方式) as 文件对象:
# with open('test.txt', 'r', encoding='utf-8') as f:
#
# with 是一个上下文管理器，用于自动关闭文件
# 当with语句块执行完毕后，文件会被自动关闭
# 无需手动调用close()方法关闭文件
# 不适用with时：
# f = open('test.txt', 'r', encoding='utf-8')
#
# f.close()
#
# 读写文件
# f.read()/f.write() # 读取/写入文件内容
# f.readlines()/f.readline() # 读取文件所有行/每次读取一行

# 调用系统命令
# import os # 导入os模块，用于调用系统命令
# 语法：os.system(命令)
# 命令是字符串，例如：ls、pwd、cd等,具体命令根据操作系统不同而不同
# 返回值类型：int; 0表示成功，非0表示失败
# 例如：os.system('ls')
#
#   读写json格式文件
# 语法：import json
#           ------>json.loads()/json.load()----->
# json文件               序列化/反序列化                python类/对象
#           <------json.dumps()/json.dump()<-----
# 带s处理的是字符串，不带s处理的是文件
#
# json.dump(python类/对象, 文件对象, ensure_ascii=False, indent=2)
#
# ensure_ascii=False 表示不使用_ascii编码，直接使用中文
# indent=2 表示缩进2个空字符,用于格式化json字符串
#
#
#
from xml.dom.minidom import Document

from lxml import html
with open('/mnt/c/Users/WhisperTang/Desktop/acfun_rank_full.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
    # 解析HTML字符串为Document对象
    Document = html.fromstring(html_content)

    # 解析Document中的元素----Xpath表达式
    
