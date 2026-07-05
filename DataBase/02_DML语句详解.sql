/*
DML语句详解
概述：数据操作语言，用于操作表中的数据，    进行增删改操作。
增删改操作---->更新语句
注意：
进行删改前,!!!!务必备份!!!!
增加数据：INSERT INTO 表名 VALUES (值1, 值2, 值3, ...);
删除数据：DELETE FROM 表名 WHERE 条件;
修改数据：UPDATE 表名 SET 字段名 = 值 WHERE 条件;
*/

# ---------------------------------学习insert语句---------------------------------------------------------------
# 不指定字段,一次插入一行,并指定所有列
# 语法：
# INSERT INTO 表名 VALUES (值1, 值2, ...);
# 指定字段,一次插入一行,并指定部分列
# 语法：
# INSERT INTO 表名 (字段名, 字段名, ...) VALUES (值1, 值2, ...);
# 不指定字段,一次插入多行
# 语法：
# INSERT INTO 表名 VALUES (值1, 值2, ...), (值1, 值2, ...), ...
# 指定字段,一次插入多行
# 语法：
# INSERT INTO 表名 (字段名, 字段名, ...) VALUES (值1, 值2, ...), (值1, 值2, ...), ...

# 综上
# INSERT INTO 表名 (列名,默认所有列) VALUES (行数据1),(行数据2),...;
use learnDB;

show TABLEs;

DESC staff;
# 查看数据表 staff, 字段信息
# 插入一行数据,不指定字段
INSERT INTO staff VALUES (1001, '张三', 20, '男');
# 插入一行数据,指定字段
INSERT INTO staff (id, name) VALUES (1002, '李四');
# 插入多行数据,不指定字段
INSERT INTO staff VALUES (1003, '王五', 25, '男'), (1004, '货员甲', 30, '女');
# 插入多行数据,指定字段
INSERT INTO staff (id, name, sex) VALUES (1005, '炮灰乙','男'), (1006, '土匪丁','女');

# 查看数据表
SELECT * FROM staff;
# 查看所有数据


# ---------------------------------学习UPDATE语句---------------------------------------------------------------
# 修改数据
# 语法：
#       更新所有行
#       UPDATE 表名 SET 字段名1 = 值1, 字段名2 = 值2, ... ;
#       更新指定行
#       UPDATE 表名 SET 字段名1 = 值1, 字段名2 = 值2, ... WHERE 条件;

update staff set sex = '男' where sex = '未知';
update staff set age = 18 where age = 0;


# ---------------------------------学习DELETE语句---------------------------------------------------------------
# 删除数据
# 语法：
#       删除所有行(主键自增序列不清零)
#       DELETE FROM 表名;
#       删除指定行
#       DELETE FROM 表名 WHERE 条件;
#       删除所有行(主键自增序列清零)
#       TRUNCATE TABLE 表名;
delete from staff where age = 20;
delete from staff;