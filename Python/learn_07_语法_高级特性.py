# Python 高级特性：装饰器、生成器、上下文管理器

######################################
# *** 1. 装饰器（Decorator）*** #
######################################
# 装饰器本质上是一个函数，接收一个函数作为参数，返回一个新函数
# 用于在不修改原函数代码的前提下，给函数添加额外功能
# 应用场景：日志记录、性能计时、权限校验、缓存等


# ---------- 1.1 装饰器原理 ----------
from contextlib import contextmanager
import itertools
import time


def my_decorator(func):
    """最简单的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__} 之前...")
        result = func(*args, **kwargs)
        print(f"调用 {func.__name__} 之后，结果: {result}")
        return result
    return wrapper


@my_decorator
def add(a, b):
    return a + b


# 等价于: add = my_decorator(add)
print(add(3, 5))
print()


# ---------- 1.2 带参数的装饰器 ----------


def timer(unit: str = "秒"):
    """计时装饰器：可以指定时间单位"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            label = "毫秒" if unit == "毫秒" else "秒"
            value = elapsed * 1000 if unit == "毫秒" else elapsed
            print(f"[计时] {func.__name__} 执行耗时: {value:.4f} {label}")
            return result
        return wrapper
    return decorator


@timer(unit="毫秒")
def slow_sum(n):
    """计算 1 到 n 的和"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(f"1 到 100000 的和: {slow_sum(100000)}")
print()


# ---------- 1.3 常用装饰器示例 ----------
# 缓存装饰器：避免重复计算（手动实现）
def memoize(func):
    """简单缓存装饰器"""
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


@memoize
def fibonacci(n):
    """递归计算斐波那契数（没有缓存会很慢）"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"fibonacci(30) = {fibonacci(30)}")
print()


# ---------- 1.4 类装饰器 ----------
# 装饰器也可以是一个类，利用 __call__ 方法


class CountCalls:
    """统计函数被调用次数的装饰器"""

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)


@CountCalls
def greet(name):
    return f"你好, {name}!"


print(greet("Whisper"))
print(greet("World"))
print()


# ---------- 1.5 多个装饰器叠加 ----------
# 装饰器从下往上执行（离函数近的先执行）


def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper


@bold
@italic
def text():
    return "Hello"


# 等价于: text = bold(italic(text))
# italic 先包裹 → bold 再包裹
print(text())  # <b><i>Hello</i></b>
print()


######################################
# *** 2. 生成器（Generator）*** #
######################################
# 生成器是一种特殊的迭代器，使用 yield 关键字
# 特点：惰性计算（用到时才生成值），节省内存


# ---------- 2.1 yield 基础 ----------
def count_up_to(n):
    """简单生成器：逐个产生 0 到 n-1"""
    i = 0
    while i < n:
        yield i
        i += 1


gen = count_up_to(5)
print(f"生成器对象: {gen}")
print(f"next: {next(gen)}")   # 0
print(f"next: {next(gen)}")   # 1

# for 循环自动迭代生成器
print("for 循环迭代:")
for num in count_up_to(3):
    print(num, end=' ')
print("\n")


# ---------- 2.2 生成器表达式 ----------
# 类似列表推导式，但用小括号，返回生成器而非列表
squares_gen = (x**2 for x in range(5))
print(f"生成器表达式: {squares_gen}")
print(f"转为列表: {list(squares_gen)}")
print()


# ---------- 2.3 yield 双向通信 ----------
# send() 方法可以向生成器内部发送值


def accumulator():
    """累加器：接收外部发送的值并累计"""
    total = 0
    while True:
        value = yield total       # yield 左侧 = 等号左边 接收 send 的值
        if value is None:
            break
        total += value


acc = accumulator()
print(f"初始值: {next(acc)}")          # 必须先启动生成器
print(f"send(10): {acc.send(10)}")    # 发送 10，累积后 total = 10
print(f"send(20): {acc.send(20)}")    # 发送 20，累积后 total = 30
acc.close()
print()


# ---------- 2.4 实战：逐行读取大文件 ----------
# 对于大文件，生成器可以避免一次性加载全部内容到内存
def read_large_file(file_path):
    """逐行读取文件（生成器版本）"""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()


# 示例：读取本文件自身
print("读取本文件前 5 行:")
for i, line in enumerate(read_large_file(__file__)):
    if i >= 5:
        break
    print(f"  第{i+1}行: {line[:60]}...")
print()


# ---------- 2.5 itertools 常用工具 ----------

# count: 无限计数器
counter = itertools.count(start=1, step=2)
print(f"count 前3个: {[next(counter) for _ in range(3)]}")

# cycle: 无限循环
colors = itertools.cycle(['红', '绿', '蓝'])
print(f"cycle 前5个: {[next(colors) for _ in range(5)]}")

# chain: 串联多个可迭代对象
chained = itertools.chain([1, 2], ['a', 'b'], (True, False))
print(f"chain: {list(chained)}")

# combinations: 组合
print(f"combinations('ABC', 2): {list(itertools.combinations('ABC', 2))}")

# permutations: 排列
print(f"permutations('AB', 2): {list(itertools.permutations('AB', 2))}")
print()


######################################
# *** 3. 上下文管理器 *** #
######################################
# with 语句背后的机制：__enter__ 和 __exit__
# 确保资源（文件、数据库连接、锁等）被正确释放


# ---------- 3.1 自定义类实现上下文管理器 ----------
class FileLogger:
    """简单的文件日志器（上下文管理器）"""

    def __init__(self, filename: str):
        self.filename = filename
        self.file = None

    def __enter__(self):
        print(f"[上下文管理器] 打开文件: {self.filename}")
        self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"[上下文管理器] 发生异常: {exc_type.__name__}: {exc_value}")
        else:
            print(f"[上下文管理器] 文件正常关闭")
        # 返回 True 会吞掉异常，返回 False（或不返回）异常继续传播
        return False


print("=== 正常执行 ===")
with FileLogger('/tmp/test_log.txt') as f:
    f.write("测试日志内容\n")

print("\n=== 异常执行 ===")
try:
    with FileLogger('/tmp/test_log2.txt') as f:
        f.write("这行会写入\n")
        raise ValueError("模拟异常")
except ValueError as e:
    print(f"异常被捕获: {e}")
print()


# ---------- 3.2 使用 contextlib 简化 ----------


@contextmanager
def timer_context(name: str):
    """计时上下文管理器（使用 contextmanager 装饰器）"""
    print(f"[{name}] 开始...")
    start = time.time()
    yield                          # yield 前面 = 进入上下文时执行
    end = time.time()              # yield 后面 = 退出上下文时执行
    print(f"[{name}] 结束，耗时: {end - start:.4f} 秒")


with timer_context("文件处理"):
    # 模拟耗时操作
    total = sum(range(1000000))

# 等价于:
# with timer_context("文件处理"):
#     total = sum(range(1000000))
print()


# ---------- 3.3 实战：数据库连接模拟 ----------
class DatabaseConnection:
    """模拟数据库连接（上下文管理器实战）"""

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        print(f"[数据库] 连接 {self.db_name}...")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"[数据库] 断开 {self.db_name} 连接")
        self.connected = False
        return False

    def query(self, sql: str):
        if not self.connected:
            raise RuntimeError("未连接数据库！")
        return f"执行查询: {sql} → 返回模拟数据"


with DatabaseConnection("Python_Learning") as db:
    print(db.query("SELECT * FROM students"))
    print(db.query("SELECT COUNT(*) FROM students"))


######################################
# *** 4. 静态方法与类方法 *** #
######################################
class DateUtil:
    """日期工具类"""

    @staticmethod
    def is_workday(weekday: int) -> bool:
        """静态方法：判断是否为工作日（不需要访问类或实例）"""
        return 1 <= weekday <= 5

    @classmethod
    def from_string(cls, date_str: str):
        """类方法：从字符串创建实例（第一个参数是 cls）"""
        parts = date_str.split('-')
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))


# 静态方法可通过实例或类名调用
print(f"周一是否工作日: {DateUtil.is_workday(1)}")   # True
print(f"周六是否工作日: {DateUtil.is_workday(6)}")   # False
