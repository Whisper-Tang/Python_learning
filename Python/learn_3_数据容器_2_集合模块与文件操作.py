# 扩展数据容器：collections 模块 & pathlib 文件路径操作

######################################
# *** 1. collections 常用数据结构 *** #
######################################
from functools import reduce, partial, lru_cache
from pathlib import Path
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple

# ---------- 1.1 Counter：计数器 ----------
# 统计可迭代对象中元素的出现次数

# 统计文本中的字符频率
text = "hello world, welcome to python"
char_counts = Counter(text)
print(f"字符计数: {char_counts}")
print(f"最常见的 3 个字符: {char_counts.most_common(3)}")

# 统计列表中的元素
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'grape']
word_counts = Counter(words)
print(f"单词计数: {word_counts}")
print(f"'apple' 出现次数: {word_counts['apple']}")
print()

# Counter 支持数学运算
c1 = Counter(['a', 'b', 'c', 'a', 'b'])
c2 = Counter(['b', 'c', 'd', 'd'])
print(f"c1: {c1}, c2: {c2}")
print(f"c1 + c2 (并集计数相加): {c1 + c2}")
print(f"c1 - c2 (差集): {c1 - c2}")
print(f"c1 & c2 (交集取最小值): {c1 & c2}")
print(f"c1 | c2 (并集取最大值): {c1 | c2}")
print()


# ---------- 1.2 defaultdict：带默认值的字典 ----------
# 访问不存在的 key 时，自动用工厂函数生成默认值

# 按首字母分组
names = ['Alice', 'Bob', 'Anna', 'Charlie', 'Brian', 'David', 'Carol']
by_first = defaultdict(list)    # 默认值是空列表
for name in names:
    by_first[name[0]].append(name)
print("按首字母分组:")
for key, value in sorted(by_first.items()):
    print(f"  {key}: {value}")

# 使用 int 做默认值，方便计数
counts = defaultdict(int)
for ch in "abracadabra":
    counts[ch] += 1
print(f"字符计数: {dict(counts)}")
print()


# ---------- 1.3 OrderedDict：有序字典 ----------
# Python 3.7+ 普通 dict 也是有序的，但 OrderedDict 额外提供排序方法
# 主要用于需要按插入顺序迭代的兼容场景

od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(f"OrderedDict: {od}")
od.move_to_end('first')    # 将 'first' 移到最后
print(f"move_to_end('first'): {od}")
od.move_to_end('third', last=False)  # 将 'third' 移到最前
print(f"move_to_end('third', last=False): {od}")
print()


# ---------- 1.4 deque：双端队列 ----------
# 高效地在两端添加/删除元素（O(1) 时间复杂度）

dq = deque([1, 2, 3, 4, 5])
print(f"初始 deque: {dq}")

dq.append(6)      # 右端添加
dq.appendleft(0)  # 左端添加
print(f"append 左右: {dq}")

dq.pop()          # 右端删除
dq.popleft()      # 左端删除
print(f"pop 左右后: {dq}")

# 限制长度的 deque（溢出时自动丢弃旧元素）
limited_dq = deque(maxlen=3)
for i in range(5):
    limited_dq.append(i)
    print(f"  添加 {i}: {limited_dq}")
print(f"最终: {limited_dq}")
print()


# ---------- 1.5 namedtuple：命名元组（复习） ----------
Person = namedtuple('Person', ['name', 'age', 'city'])
p1 = Person('Whisper', 24, '西安')
p2 = Person('Alice', 30, '北京')
print(f"{p1.name} 年龄 {p1.age}，来自 {p1.city}")

# 转为字典和替换字段
print(f"转为字典: {p1._asdict()}")
p1_older = p1._replace(age=25)
print(f"年龄+1: {p1_older}")
print()


######################################
# *** 2. 文件与路径操作（pathlib）*** #
######################################
# pathlib 是 Python 3.4+ 引入的面向对象路径操作库
# 比 os.path 更直观易用


# ---------- 2.1 路径基本操作 ----------
# 获取当前目录
current = Path('.')
print(f"当前目录: {current.resolve()}")   # resolve() 得到绝对路径

# 路径拼接（使用 / 运算符）
data_dir = Path('Jupyter') / 'Data'
print(f"数据目录: {data_dir}")
print(f"数据目录是否存在: {data_dir.exists()}")

# 路径属性
file_path = Path(__file__)
print(f"\n当前文件路径: {file_path}")
print(f"  - 文件名: {file_path.name}")
print(f"  - 后缀: {file_path.suffix}")
print(f"  - 去掉后缀: {file_path.stem}")
print(f"  - 父目录: {file_path.parent}")
print(f"  - 绝对路径: {file_path.resolve()}")
print()


# ---------- 2.2 目录遍历 ----------
# 列出目录内容
python_dir = Path('Python')
if python_dir.exists():
    print(f"{python_dir} 下的文件:")
    for item in sorted(python_dir.iterdir()):
        if item.is_file() and item.suffix == '.py':
            print(f"  📄 {item.name}")
        elif item.is_dir():
            print(f"  📁 {item.name}/")

# glob 模式匹配
print(f"\nPython 下所有 '*模块*' 相关的文件:")
for py_file in Path('Python').glob('*模块*'):
    print(f"  {py_file}")
print()


# ---------- 2.3 文件读写 ----------
# pathlib 方式读写文件
tmp_path = Path('/tmp/python_learn_test.txt')

# 写文件
tmp_path.write_text("第一行内容\n第二行内容\n第三行内容\n", encoding='utf-8')
print(f"写入文件: {tmp_path}")

# 读文件
content = tmp_path.read_text(encoding='utf-8')
print(f"读取内容:\n{content}")

# 分行读取
lines = tmp_path.read_text(encoding='utf-8').splitlines()
print(f"行数: {len(lines)}")

# 清理测试文件
tmp_path.unlink()
print(f"删除测试文件: {not tmp_path.exists()}")
print()


# ---------- 2.4 创建/删除目录 ----------
test_dir = Path('/tmp/python_test_dir')
test_dir.mkdir(parents=True, exist_ok=True)   # 递归创建，存在不报错
print(f"创建目录: {test_dir}")

(test_dir / 'subdir').mkdir(exist_ok=True)
(test_dir / 'test.txt').write_text('test')
print(f"创建子目录和文件")

# 删除非空目录需要手动递归删除
for item in test_dir.rglob('*'):
    if item.is_file():
        item.unlink()
for item in sorted(test_dir.rglob('*'), reverse=True):
    if item.is_dir():
        item.rmdir()
test_dir.rmdir()
print(f"删除目录: {not test_dir.exists()}")
print()


# ---------- 2.5 glob 递归搜索 ----------
# 递归搜索整个仓库的 .py 文件
repo_root = Path('.')
print("仓库中所有 .py 文件:")
for py_file in sorted(repo_root.rglob('*.py'))[:10]:  # 只显示前 10 个
    print(f"  {py_file}")
if len(list(repo_root.rglob('*.py'))) > 10:
    print(f"  ... 还有更多")
print()


# ---------- 2.6 实战：统计仓库代码行数 ----------
def count_code_lines(directory: Path, extensions: tuple = ('.py', '.ipynb')) -> dict:
    """统计指定目录下各类型文件的行数"""
    stats = defaultdict(int)
    total_files = defaultdict(int)

    for file_path in directory.rglob('*'):
        if file_path.is_file() and file_path.suffix in extensions:
            try:
                lines = file_path.read_text(encoding='utf-8').count('\n') + 1
                stats[file_path.suffix] += lines
                total_files[file_path.suffix] += 1
            except Exception:
                pass

    return {ext: {'文件数': total_files[ext], '行数': stats[ext]}
            for ext in extensions}


print("仓库代码统计:")
code_stats = count_code_lines(Path('.'))
for ext, info in code_stats.items():
    print(f"  {ext}: {info['文件数']} 个文件, 共 {info['行数']} 行")


######################################
# *** 3. functools 常用工具 *** #
######################################

# ---------- 3.1 reduce：累积运算 ----------
# 对序列中的元素依次应用函数，最终得到一个值
numbers = [1, 2, 3, 4, 5]
# reduce 等价于: ((((1 + 2) + 3) + 4) + 5)
sum_all = reduce(lambda x, y: x + y, numbers)
product_all = reduce(lambda x, y: x * y, numbers)
print(f"\nreduce 求和: {sum_all}")
print(f"reduce 求积: {product_all}")


# ---------- 3.2 partial：偏函数 ----------
# 预先填充函数的部分参数，生成新函数

def power(base, exponent):
    return base ** exponent


square = partial(power, exponent=2)    # 固定 exponent=2
cube = partial(power, exponent=3)      # 固定 exponent=3
print(f"square(5) = {square(5)}")     # 等价于 power(5, 2)
print(f"cube(5) = {cube(5)}")         # 等价于 power(5, 3)


# ---------- 3.3 lru_cache：LRU 缓存 ----------
# 自动缓存函数返回值，避免重复计算
# 比手动写的 memoize 更强大（支持 maxsize 限制、缓存清除）

@lru_cache(maxsize=128)
def fib_cached(n):
    """带缓存优化的大额斐波那契计算"""
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


# 可以快速计算较大的 n
print(f"\n缓存统计前: fib_cached.cache_info()")
print(f"fib(30) = {fib_cached(30)}")
print(f"缓存统计后: fib_cached.cache_info()")
print(f"fib(35) = {fib_cached(35)}")
print()
