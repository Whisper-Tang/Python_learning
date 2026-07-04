# 类型注解用于表示变量,参数,函数返回值的类型

# 变量名:变量类型 = 值
from operator import truediv


score: int = 256
high: float = 177.5
name: str = 'whisper'
passStatus: bool = False
pic: None = None

# 容器名:容器类型[元素类型] = 容器
names: list[str] = ['whisper', 'nigger']

# def 函数名(形参: 变量类型, 形参: 容器类型[元素类型]) -> 返回值类型:
def test(p1:int,p2:dict[int:str]) -> bool :
    return True
