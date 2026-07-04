# Python 学习笔记总览

> 本仓库为 Python 系统性学习笔记，涵盖基础语法、函数、面向对象、异常处理、爬虫开发及数据分析等模块。

---

## 目录

1. [仓库结构](#仓库结构)
2. [基础语法](#基础语法)
   - [变量与数据类型](#1-变量与数据类型)
   - [运算符](#2-运算符)
   - [字符串操作](#3-字符串操作)
   - [输入与输出](#4-输入与输出)
3. [流程控制语句](#流程控制语句)
   - [if 条件判断](#1-if-条件判断)
   - [match-case 模式匹配](#2-match-case-模式匹配)
   - [while 循环](#3-while-循环)
   - [for 循环](#4-for-循环)
4. [数据容器](#数据容器)
   - [列表 List](#1-列表-list)
   - [字符串 String](#2-字符串-string)
   - [元组 Tuple](#3-元组-tuple)
   - [集合 Set](#4-集合-set)
   - [字典 Dictionary](#5-字典-dictionary)
   - [命名元组 NamedTuple / 数据类 DataClass](#6-命名元组与数据类)
   - [扩展模块：collections 与 pathlib](#7-扩展模块collections-与-pathlib-new)
5. [函数](#函数)
   - [函数定义与调用](#1-函数定义与调用)
   - [变量作用域](#2-变量作用域)
   - [参数传递方式](#3-参数传递方式)
   - [匿名函数 Lambda](#4-匿名函数-lambda)
6. [类型注解](#类型注解)
7. [模块与包](#模块与包)
8. [类与对象](#类与对象)
   - [类的定义与实例化](#1-类的定义与实例化)
   - [实例方法](#2-实例方法)
   - [魔法方法（运算符重载）](#3-魔法方法运算符重载)
   - [实例属性与类属性](#4-实例属性与类属性)
9. [继承与多态（NEW）](#继承与多态new)
   - [单继承](#1-单继承)
   - [多态与鸭子类型](#2-多态与鸭子类型)
   - [多继承与 MRO](#3-多继承与-mro)
   - [私有属性](#4-私有属性)
   - [抽象基类 ABC](#5-抽象基类-abc)
   - [@property 装饰器](#6-property-装饰器)
10. [高级特性（NEW）](#高级特性new)
    - [装饰器 Decorator](#1-装饰器-decorator)
    - [生成器 Generator](#2-生成器-generator)
    - [上下文管理器](#3-上下文管理器)
    - [静态方法与类方法](#4-静态方法与类方法)
11. [异常处理](#异常处理)
12. [爬虫开发](#爬虫开发)
    - [HTTP 请求与 JSON 解析](#1-http-请求与-json-解析)
    - [XPath 网页解析](#2-xpath-网页解析)
    - [正则表达式](#3-正则表达式)
13. [数据分析](#数据分析)
    - [环境配置](#1-环境配置)
    - [Pandas 入门](#2-pandas-入门)
    - [Pandas 进阶（NEW）](#3-pandas-进阶new)
    - [Matplotlib 可视化](#4-matplotlib-可视化)
14. [附录：源文件索引](#附录源文件索引)

---

## 仓库结构

```
Python_Learing_Hub/
├── Python/                           # Python 基础语法学习（共 18 个学习文件，含 4 个新增）
│   ├── learn_1_基础语法_数据的存储与运算.py
│   ├── learn_2_基础语法_流程控制语句.py
│   ├── learn_3_基础语法_数据容器.py
│   ├── learn_3_数据容器_2_集合模块与文件操作.py  # [NEW] collections / pathlib
│   ├── learn_4_函数基础_1_定义与调用.py
│   ├── learn_4_函数基础_2_变量与传参.py
│   ├── learn_5_语法_类型注解.py
│   ├── learn_6_语法_模块.py
│   ├── learn_7_语法_类与对象基础.py
│   ├── learn_7_语法_类的高级特性.py            # 继承/多态/@property/@classmethod/@staticmethod/ABC
│   ├── learn_7_语法_继承与多态.py              # [NEW] 继承/多态/ABC/@property 详解
│   ├── learn_7_语法_高级特性.py                # [NEW] 装饰器/生成器/上下文管理器
│   ├── learn_8_异常.py
│   ├── learn_9_爬虫_1.py              # 爬虫：HTTP请求与JSON数据处理
│   ├── learn_9_爬虫_2_网页解析.py      # 爬虫：lxml 与 XPath 入门
│   ├── learn_9_爬虫_3_xpath简单语法.py  # 爬虫：XPath 实战（OP.GG 排行）
│   ├── learn_9_爬虫_4_数据清洗_正则表达式.py # 爬虫：正则表达式
│   ├── learn_10_数据分析.py            # 数据分析概念与环境配置
│   ├── DiyModuleTest.py               # 自定义模块示例
│   └── Package/
│       └── myPackageTest.py           # 包管理示例
├── Jupyter/                           # Jupyter Notebook（数据分析实战）
│   ├── Pandas入门.ipynb               # Pandas DataFrame 操作
│   ├── Pandas进阶.ipynb               # [NEW] 合并/分组/透视/清洗
│   ├── matplotlib.ipynb               # Matplotlib 数据可视化
│   ├── venv_test.ipynb                # 虚拟环境测试
│   └── Data/                          # 数据集
│       ├── opgg_tier.csv / opgg_tier_adjust*.csv
│       └── score.csv / score_format.csv
└── git/                               # Git 测试文件
```

---

## 基础语法

### 1. 变量与数据类型

- **变量定义**：`变量名 = 值`（无需声明类型，Python 自动推断）
- **命名规范**：蛇形命名法（`my_variable`），类名用驼峰命名法
- **多变量赋值**：`a, b, c = 1, 2, 3` 或 `x = y = z = 0`
- **变量交换**：`a, b = b, a`（Python 特色，无需临时变量）

#### 基本数据类型

| 类型          | 示例               | 备注             |
| ------------- | ------------------ | ---------------- |
| 整数 int      | `x = 10`           | 无大小限制       |
| 浮点 float    | `y = 3.14`         |                  |
| 字符串 str    | `s = "hello"`      | 单/双/三引号均可 |
| 布尔 bool     | `b = True / False` | 首字母大写       |
| 空值 NoneType | `n = None`         | 表示空值         |

- **类型检查**：`type(obj)` 获取类型，`isinstance(obj, type)` 判断类型

### 2. 运算符

| 类别 | 运算符                               | 说明                              |
| ---- | ------------------------------------ | --------------------------------- | --- | ----- |
| 算术 | `+ - * / // % **`                    | `/` 总是返回浮点数，`//` 向下取整 |
| 赋值 | `= += -= *= /= //= %= **=`           | `a += b` → `a = a + b`            |
| 比较 | `== != > < >= <=`                    | 返回布尔值                        |
| 逻辑 | `and`（与）, `or`（或）, `not`（非） | 非C风格的 `&&` `                  |     | ` `!` |
| 成员 | `in`, `not in`                       | 判断元素是否在容器中              |
| 身份 | `is`, `is not`                       | 判断是否为同一对象                |

### 3. 字符串操作

- **拼接**：`"hello" + " " + "world"`（`+` 仅拼接字符串）
- **格式化**：
  - 旧式占位符：`"我是%s，%d岁" % (name, age)`
  - **推荐 f-string**：`f"我是{name}，{age}岁"`
- **方法**：`upper()` / `lower()` / `strip()` / `split()` / `find()` / `count()` / `replace()` / `startswith()` / `endswith()`
- **切片**：`s[start:end:step]`，如 `s[::-1]` 反转字符串
- **不可变性**：字符串一旦定义，不可修改

### 4. 输入与输出

- **输出**：`print(value, end='\n')`
- **输入**：`input("提示信息")` → **返回字符串**，需转换类型：`int(input("年龄："))`
- **类型转换**：`int()`, `float()`, `bool()`, `str()` — 格式：`目标类型(原值)`

---

## 流程控制语句

### 1. if 条件判断

```python
if 条件:
    代码块
elif 条件:
    代码块
else:
    代码块
```

- 必须带冒号 `:`，代码块必须缩进（通常 4 空格）
- Python 用缩进表示代码块范围，严禁混用 tab 和空格

### 2. match-case 模式匹配

```python
match 变量:
    case 值1:
        代码块
    case _ if 条件:
        代码块
    case _:   # 默认
        代码块
```

- Python 3.10 引入，等价于 C 语言的 `switch-case`
- 不需要 `break`，执行完自动退出

### 3. while 循环

```python
while 条件:
    代码块
    if 条件:
        break     # 提前退出
else:              # 正常结束（非break退出）时执行
    代码块
```

### 4. for 循环

```python
for 变量 in 可迭代对象:
    代码块
else:              # 正常遍历完成时执行
    代码块
```

- `range(start, stop, step)`：生成整数序列，左闭右开区间
- 可遍历列表、元组、字符串、字典等

---

## 数据容器

### 1. 列表 List

```python
my_list = [元素1, 元素2, ...]   # 有序、可变、可重复
```

| 操作       | 语法/方法                                 |
| ---------- | ----------------------------------------- |
| 索引访问   | `my_list[i]`（支持负索引）                |
| 删除元素   | `del my_list[i]`                          |
| 追加       | `my_list.append(item)`                    |
| 插入       | `my_list.insert(index, item)`             |
| 删除并返回 | `my_list.pop(index)`                      |
| 删除指定值 | `my_list.remove(value)`                   |
| 排序       | `my_list.sort()` / `sorted(my_list)`      |
| 逆置       | `my_list.reverse()`                       |
| 切片       | `my_list[start:end:step]`                 |
| 列表推导式 | `[表达式 for 变量 in 可迭代对象 if 条件]` |
| 解包       | `a, b, *rest = my_list`                   |

### 2. 字符串 String

- 字符序列，**不可变**，支持索引与切片
- 本质是**字符列表**，大部分列表操作适用于字符串

### 3. 元组 Tuple

```python
my_tuple = (元素1, 元素2, ...)   # 有序、不可变
```

- 单元素元组需加逗号：`(元素,)`
- 支持切片、解包、`count()`、`index()`
- 常用于存储不可修改的数据或函数多返回值
- **解包**：`a, b, c = my_tuple`, 扩展解包：`a, *b, c = my_tuple`

### 4. 集合 Set

```python
my_set = {元素1, 元素2, ...}   # 无序、可变、元素唯一
empty_set = set()              # 空集合（不能用 {}，那是空字典）
```

| 操作     | 方法                  | 运算符 |
| -------- | --------------------- | ------ |
| 交集     | `s1.intersection(s2)` | `&`    |
| 并集     | `s1.union(s2)`        | `\|`   |
| 差集     | `s1.difference(s2)`   | `-`    |
| 添加     | `s.add(item)`         |        |
| 删除     | `s.remove(item)`      |        |
| 随机删除 | `s.pop()`             |        |

### 5. 字典 Dictionary

```python
my_dict = {键1: 值1, 键2: 值2, ...}   # 无序（3.7+有序）、可变
```

- **键**：必须是不可变类型（str, int, tuple 等）
- **值**：任意类型
- 常用方法：`keys()`, `values()`, `items()`, `get(key)`, `pop(key)`, `update(dict)`, `del dict[key]`

### 6. 命名元组与数据类

- **NamedTuple** (`collections.namedtuple`)：可通过名称访问的不可变元组
- **DataClass** (`dataclasses.dataclass`)：自动生成 `__init__`、`__repr__` 等方法的可变数据类

### 7. 扩展模块：collections 与 pathlib（NEW）

**collections 模块：**

| 类            | 用途                                          |
| ------------- | --------------------------------------------- |
| `Counter`     | 元素计数器，`.most_common(n)` 获取最常见项    |
| `defaultdict` | 带默认值的字典，`defaultdict(list/int)`       |
| `OrderedDict` | 有序字典，`.move_to_end()` 调整顺序           |
| `deque`       | 双端队列，`appendleft/popleft`，可设置 maxlen |
| `namedtuple`  | 命名元组，`._asdict()`, `._replace()`         |

**pathlib 路径操作：**

| 操作        | 语法                                      |
| ----------- | ----------------------------------------- |
| 路径拼接    | `Path('A') / 'B'`                         |
| 绝对路径    | `path.resolve()`                          |
| 文件名/后缀 | `path.name`, `path.suffix`, `path.stem`   |
| 遍历目录    | `path.iterdir()`                          |
| 模式匹配    | `path.glob('*.py')`, `path.rglob('*.py')` |
| 读写文本    | `path.read_text()`, `path.write_text()`   |
| 创建/删除   | `path.mkdir()`, `path.unlink()`           |

**functools 常用工具：**

| 函数        | 用途                                     |
| ----------- | ---------------------------------------- |
| `reduce`    | 累积运算：`reduce(lambda x,y: x+y, seq)` |
| `partial`   | 偏函数：预先填充部分参数                 |
| `lru_cache` | LRU缓存装饰器，`.cache_info()` 查看缓存  |

> 源文件：[learn*3*数据容器*2*集合模块与文件操作.py](Python/learn_3_数据容器_2_集合模块与文件操作.py)

---

## 函数

### 1. 函数定义与调用

```python
def 函数名(参数列表):
    """文档字符串（Sphinx / Google 格式）"""
    函数体
    return 返回值   # 可返回多个值，自动组包为元组
```

- 先定义后调用（无函数声明概念）
- 多返回值 → 元组，支持解包接收

### 2. 变量作用域

- **局部变量**：在函数内定义，仅函数内可见
- **全局变量**：在函数外定义，函数内需用 `global` 关键字声明后才能修改

### 3. 参数传递方式

| 方式                 | 语法             | 说明                             |
| -------------------- | ---------------- | -------------------------------- |
| 位置传参             | `func(1, 2, 3)`  | 按定义顺序传参                   |
| 关键字传参           | `func(a=1, c=3)` | 键值对形式，可不按顺序           |
| 默认参数             | `func(a=0)`      | 有默认值的参数之后都必须有默认值 |
| \*args（不定长）     | `func(*args)`    | 封装为**元组**                   |
| \*\*kwargs（不定长） | `func(**kwargs)` | 封装为**字典**                   |
| 函数作为参数         | `func(calc)`     | 高阶函数                         |

### 4. 匿名函数 Lambda

```python
lambda 参数: 表达式       # 只能一行，表达式结果即为返回值
```

---

## 类型注解

```python
变量名: 类型 = 值                    # score: int = 256
容器名: 容器类型[元素类型] = 值       # names: list[str] = ['a', 'b']

def 函数名(参数: 类型) -> 返回类型:    # def add(x: int, y: int) -> int:
    函数体
```

- 类型注解只是**提示**，不影响程序运行，但有助于代码可读性和 IDE 智能提示

---

## 模块与包

### 模块

- 一个 `.py` 文件就是一个模块
- 导入方式：

| 导入语法                          | 调用方式        |
| --------------------------------- | --------------- |
| `import 模块名`                   | `模块名.函数()` |
| `import 模块名 as 别名`           | `别名.函数()`   |
| `from 模块名 import 函数`         | `函数()`        |
| `from 模块名 import 函数 as 别名` | `别名()`        |
| `from 模块名 import *`            | `函数()`        |

- `__name__ == '__main__'`：判断是否为直接运行
- `__all__`：控制 `from 模块 import *` 导出的内容

### 包 (Package)

```
Package/
├── __init__.py    # 包描述文件（__all__列表控制导入范围）
└── 模块.py
```

- `from 包名.模块名 import 函数`

---

## 类与对象

### 1. 类的定义与实例化

```python
class 类名:
    def __init__(self, 参数...):   # 构造函数（等价于C++构造函数）
        self.属性 = 值

对象 = 类名(参数)    # self 自动传入，无需手动传递
```

- **命名规范**：驼峰命名法 (PascalCase)
- `__dict__`：以字典形式存储对象属性

### 2. 实例方法

```python
class MyClass:
    def 方法名(self, 参数):     # self 相当于 this 指针
        函数体
```

### 3. 魔法方法（运算符重载）

| 魔法方法       | 对应运算符/功能           |
| -------------- | ------------------------- |
| `__init__`     | 构造函数                  |
| `__str__`      | `str(obj)` / `print(obj)` |
| `__eq__`       | `==`                      |
| `__ne__`       | `!=`                      |
| `__lt__`       | `<`                       |
| `__gt__`       | `>`                       |
| `__le__`       | `<=`                      |
| `__ge__`       | `>=`                      |
| `__add__`      | `+`                       |
| `__sub__`      | `-`                       |
| `__mul__`      | `*`                       |
| `__truediv__`  | `/`（真除法）             |
| `__floordiv__` | `//`（地板除）            |
| `__mod__`      | `%`                       |
| `__pow__`      | `**`                      |
| `__and__`      | `&`                       |
| `__or__`       | `\|`                      |

### 4. 实例属性与类属性

- **实例属性**：`self.x = val`（每个对象独立拥有）
- **类属性**：直接在类体中定义，所有实例共享
- 查找优先级：实例属性 → 类属性

---

## 继承与多态（NEW）

### 1. 单继承

```python
class Animal:
    def __init__(self, name, age):
        self.name = name; self.age = age
    def eat(self):
        return f"{self.name} 正在吃东西"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # 调用父类构造
        self.breed = breed
    def eat(self):                    # 重写父类方法
        return f"{self.name} 正在啃骨头"
```

- `super()` 调用父类方法
- 子类可添加自己特有的属性和方法
- `isinstance(obj, Class)` 检查继承关系

### 2. 多态与鸭子类型

- **多态**：不同子类对同一方法有不同实现，调用时表现各异
- **鸭子类型**：Python 特色——「走路像鸭子、叫声像鸭子，就是鸭子」，不强制要求继承关系

### 3. 多继承与 MRO

```python
class SuperDuck(Flyable, Swimmable):   # 多继承
    pass
```

- MRO（Method Resolution Order）：`类名.__mro__`，决定了方法查找顺序
- 遇到冲突时，优先使用先继承的父类方法

### 4. 私有属性

| 写法  | 说明                                  |
| ----- | ------------------------------------- |
| `_x`  | 约定为 protected（提醒不要外部访问）  |
| `__x` | 名称改写为 `_类名__x`，一定程度防访问 |

### 5. 抽象基类 ABC

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass       # 子类必须实现

class Circle(Shape):           # 必须实现 area()
    def area(self):
        return 3.14159 * self.radius ** 2
```

- 抽象类不能实例化，强制子类实现指定方法

### 6. @property 装饰器

```python
class Student:
    @property
    def total(self):            # 像属性一样访问方法
        return self.chinese + self.math + self.english

s = Student()
print(s.total)                  # 无需括号
```

- 将方法调用变成属性访问，优雅实现只读 getter
- 配合 `@xxx.setter` 可实现 setter

> 源文件：[learn*7*语法\_类的高级特性.py](Python/learn_7_语法_类的高级特性.py) | [learn*7*语法\_继承与多态.py](Python/learn_7_语法_继承与多态.py)

---

## 高级特性（NEW）

### 1. 装饰器 Decorator

装饰器本质是一个返回函数的函数，用于在不修改原函数代码的前提下添加功能。

```python
@timer(unit="毫秒")            # 带参数的装饰器
def slow_func():
    pass

# 等价于: slow_func = timer(unit="毫秒")(slow_func)
```

| 应用场景 | 说明                      |
| -------- | ------------------------- |
| 日志记录 | 记录函数调用日志          |
| 性能计时 | 统计函数执行耗时          |
| 权限校验 | 检查用户是否有权限调用    |
| 缓存     | `@lru_cache` 避免重复计算 |

- `@memoize`（手动缓存）、`@CountCalls`（类装饰器）
- 多装饰器叠加：从下往上执行

### 2. 生成器 Generator

使用 `yield` 关键字的函数，惰性计算，节省内存。

```python
def count_up_to(n):
    i = 0
    while i < n:
        yield i               # 每次 yield 返回一个值，函数暂停
        i += 1
```

- **生成器表达式**：`(x**2 for x in range(5))`（小括号，非列表推导式）
- `send(value)` 向生成器内部发送值
- `itertools` 模块：`count()`, `cycle()`, `chain()`, `combinations()`, `permutations()`

### 3. 上下文管理器

确保资源被正确释放（文件、数据库连接等）。

```python
# 方式一：自定义类
class FileLogger:
    def __enter__(self): ...       # 进入 with 时执行
    def __exit__(self, *args): ... # 退出 with 时执行

# 方式二：contextlib 简化
from contextlib import contextmanager
@contextmanager
def timer(name):
    start = time.time()
    yield                          # yield 之前是进入，之后是退出
    print(f"{time.time() - start}")
```

| 实现方式                 | 适用场景             |
| ------------------------ | -------------------- |
| `__enter__` / `__exit__` | 复杂逻辑，需保持状态 |
| `@contextmanager`        | 简单场景，代码更简洁 |

### 4. 静态方法与类方法

```python
class MyClass:
    @staticmethod
    def static_func(): ...     # 无需 self/cls，纯工具函数

    @classmethod
    def class_func(cls): ...   # 第一个参数是 cls（类本身）
```

| 类型         | 用途                            |
| ------------ | ------------------------------- |
| staticmethod | 不访问类或实例，放类里仅为归属  |
| classmethod  | 需要访问类的工厂方法/替代构造器 |

> 源文件：[learn*7*语法\_高级特性.py](Python/learn_7_语法_高级特性.py)

---

## 异常处理

```python
try:
    可能异常的代码
except 异常类型1 as e:
    处理方案1
except 异常类型2 as e:
    处理方案2
except Exception as e:   # 兜底捕获
    通用处理
finally:
    清理代码（无论如何都执行）
```

- **异常传递**：函数内未捕获的异常会向上抛给调用者
- **主动抛出**：`raise 异常类型("异常信息")`
- 常见异常：`NameError`, `ZeroDivisionError`, `TypeError`, `ValueError`, `FileNotFoundError`

---

## 爬虫开发

### 1. HTTP 请求与 JSON 解析

- `requests.get(url, headers={...})`：发送 GET 请求
- `User-Agent`：模拟浏览器身份，必备请求头
- `Referer`：来源页面，部分网站防爬检测
- `json.loads(str)` / `json.dumps(obj, ensure_ascii=False, indent=2)`：JSON 序列化/反序列化
- `json.load(fp)` / `json.dump(obj, fp)`：操作文件的 JSON 方法（不带 s）

**实战案例**：爬取 ACFUN 排行日榜 JSON 数据，自动生成精美 HTML 排行页面

### 2. XPath 网页解析

- 使用 `lxml` 库（`pip install lxml`）
- 核心流程：获取 HTML → `lxml.html.fromstring(html)` → XPath 提取

**XPath 常用语法：**

| 表达式          | 说明           |
| --------------- | -------------- |
| `/`             | 从根节点选取   |
| `//`            | 从任意位置选取 |
| `@`             | 选取属性       |
| `.`             | 当前节点       |
| `..`            | 父节点         |
| `[n]`           | 第 n 个元素    |
| `[@attr="val"]` | 属性值筛选     |
| `text()`        | 获取文本内容   |

**文件读写**：`with open(file, mode, encoding) as f:` 使用上下文管理器，自动关闭文件

**实战案例**：爬取 OP.GG 英雄联盟天梯排行榜，数据存入 CSV 文件

### 3. 正则表达式

| 表达式   | 说明                       |
| -------- | -------------------------- |
| `.`      | 任意单字符（除换行）       |
| `\d`     | 数字（大写取反）           |
| `\s`     | 空白字符（大写取反）       |
| `\w`     | 字母数字下划线（大写取反） |
| `[abc]`  | 字符集，匹配其中任意一个   |
| `[^abc]` | 排除字符集                 |
| `[a-z]`  | 范围匹配                   |
| `*`      | 0 次或多次                 |
| `+`      | 1 次或多次                 |
| `?`      | 0 次或 1 次                |
| `{n}`    | 恰好 n 次                  |
| `{n,m}`  | n~m 次                     |
| `^`      | 字符串开头                 |
| `$`      | 字符串结尾                 |

**re 模块函数**：`re.match()` / `re.search()` / `re.findall()` / `re.sub()`

- 匹配原则：**贪婪匹配** + **已匹配字符不重复匹配**

---

## 数据分析

### 1. 环境配置

| 组件             | 说明                                 |
| ---------------- | ------------------------------------ |
| Jupyter Notebook | 基于 Web 的交互式编程笔记本          |
| Pandas           | 数据处理与分析（Series / DataFrame） |
| NumPy            | 数值计算基础                         |
| Matplotlib       | 数据可视化                           |
| Seaborn          | 高级统计可视化                       |
| Scikit-learn     | 机器学习                             |

安装与配置：

```bash
pip install jupyter pandas numpy matplotlib
pip install ipykernel
python -m ipykernel install --user --name 环境名 --display-name "显示名"
```

### 2. Pandas 入门

- **Series**：一维带标签数组（表格一列）
- **DataFrame**：二维带标签数组（整张表格）

常用操作：

| 操作           | 语法                                 |
| -------------- | ------------------------------------ |
| 创建 DataFrame | `pd.DataFrame([{列: 值, ...}, ...])` |
| 读取 CSV       | `pd.read_csv('file.csv')`            |
| 查看数据       | `df.head()`, `df.tail()`             |
| 描述统计       | `df.describe()`                      |
| 查询/筛选      | `df[df['列'] > 值]`                  |
| 分组聚合       | `df.groupby('列').mean()`            |
| 排序           | `df.sort_values('列')`               |

### 3. Pandas 进阶（NEW）

| 功能       | 关键方法                                               |
| ---------- | ------------------------------------------------------ |
| 条件筛选   | `df[(条件1) & (条件2)]`, `df.query('表达式')`          |
| 标签/位置  | `df.loc[行标签, 列标签]`, `df.iloc[行位置, 列位置]`    |
| 数据合并   | `pd.merge(df1, df2, on='key', how='inner/left/right')` |
| 纵向拼接   | `pd.concat([df1, df2], ignore_index=True)`             |
| 分组聚合   | `df.groupby('列').agg(新列名=('原列', '聚合函数'))`    |
| 数据透视   | `pd.pivot_table(df, values, index, columns, aggfunc)`  |
| 缺失值处理 | `df.isnull()`, `df.dropna()`, `df.fillna(值)`          |
| 重复值处理 | `df.duplicated()`, `df.drop_duplicates()`              |
| 自定义转换 | `df['列'].apply(lambda x: ...)`, `df['列'].map(dict)`  |
| Top N      | `df.nlargest(n, '列')`, `df.nsmallest(n, '列')`        |

> 笔记本：[Pandas进阶.ipynb](Jupyter/Pandas进阶.ipynb)

### 4. Matplotlib 可视化

常用图表元素：

| 功能       | 方法调用                                           |
| ---------- | -------------------------------------------------- |
| 画布       | `plt.figure(figsize=(宽, 高), dpi=分辨率)`         |
| 标题       | `plt.title('标题')`                                |
| 坐标轴标签 | `plt.xlabel('X轴'), plt.ylabel('Y轴')`             |
| 图例       | `plt.legend(['标签1', '标签2'])`                   |
| 网格       | `plt.grid(True)`                                   |
| 坐标轴范围 | `plt.xlim(小, 大), plt.ylim(小, 大)`               |
| 刻度       | `plt.xticks(list), plt.yticks(list)`               |
| 折线图     | `plt.plot(x, y)`                                   |
| 柱状图     | `plt.bar(类别, 数值)`                              |
| 饼图       | `plt.pie(数值, labels=标签, autopct='%1.1f%%')`    |
| 子图       | `fig, axes = plt.subplots(行, 列, figsize=(w, h))` |

- 中文显示配置：`plt.rcParams['font.sans-serif'] = ['中文字体名']`

---

## 附录：源文件索引

| 文件                                                    | 主要内容                                 |
| ------------------------------------------------------- | ---------------------------------------- |
| `Python/learn_1_基础语法_数据的存储与运算.py`           | 变量、数据类型、字符串、输入输出、运算符 |
| `Python/learn_2_基础语法_流程控制语句.py`               | if/else、match-case、while、for          |
| `Python/learn_3_基础语法_数据容器.py`                   | 列表、字符串、元组、集合、字典           |
| `Python/learn_3_数据容器_2_集合模块与文件操作.py` [NEW] | collections、pathlib、functools          |
| `Python/learn_4_函数基础_1_定义与调用.py`               | 函数定义、文档、多返回值                 |
| `Python/learn_4_函数基础_2_变量与传参.py`               | 全局/局部变量、参数传递、lambda          |
| `Python/learn_5_语法_类型注解.py`                       | 变量、容器、函数类型注解                 |
| `Python/learn_6_语法_模块.py`                           | import、模块、包、`__all__`              |
| `Python/learn_7_语法_类与对象基础.py`                   | 类定义、实例方法、魔法方法、属性         |
| `Python/learn_7_语法_类的高级特性.py`                   | 继承/多态/@property/@classmethod/ABC     |
| `Python/learn_7_语法_继承与多态.py` [NEW]               | 继承/多态/ABC/@property/私有属性详解     |
| `Python/learn_7_语法_高级特性.py` [NEW]                 | 装饰器/生成器/上下文管理器/itertools     |
| `Python/learn_8_异常.py`                                | try/except/finally、raise                |
| `Python/learn_9_爬虫_1.py`                              | HTTP请求、JSON处理、HTML生成             |
| `Python/learn_9_爬虫_2_网页解析.py`                     | lxml、文件读写、JSON序列化               |
| `Python/learn_9_爬虫_3_xpath简单语法.py`                | XPath实战（OP.GG排行→CSV）               |
| `Python/learn_9_爬虫_4_数据清洗_正则表达式.py`          | 正则表达式语法、re模块                   |
| `Python/learn_10_数据分析.py`                           | 数据分析概念、环境配置                   |
| `Python/DiyModuleTest.py`                               | 自定义模块（圆的面积）                   |
| `Jupyter/Pandas入门.ipynb`                              | DataFrame 创建与操作                     |
| `Jupyter/Pandas进阶.ipynb` [NEW]                        | 数据合并/分组/透视/清洗/apply            |
| `Jupyter/matplotlib.ipynb`                              | 折线图、柱状图、饼图、子图               |
| `Jupyter/venv_test.ipynb`                               | 虚拟环境测试、Pandas 练习                |

---

> 生成日期：2026年6月10日  
> 本笔记通过对仓库中所有学习代码文件的梳理与归纳生成，旨在提供一个系统化的 Python 学习速查手册。
