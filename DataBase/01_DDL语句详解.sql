/*
SQL语句详解
    概述：全称Structured Query Language，是用于操作数据库的编程语言。它由SQL语句组成，用于执行数据库操作和管理数据库。
    分类：DDL语句、DML语句、DCL语句、TCL语句
        DDL语句：数据定义语言，     主要操作: 数据库，数据表，字段；     进行 增删改查（CURD） 操作。
                涉及关键字：CREATE、ALTER、DROP
        DML语句：数据操作语言，     主要操作: 表中的数据;              进行 增删改(CDU) 操作。
                涉及关键字：INSERT、DELETE、UPDATE
        DQL语句：数据查询语言，     主要操作: 表中的数据;              进行 查询 操作。
                涉及关键字：SELECT、FROM、WHERE、ORDER BY
        DCL语句：数据控制语句，     主要操作: 数据库的访问权限；        进行 授权、撤销权限 操作。
                涉及关键字：GRANT、REVOKE
        TCL语句：用于控制数据库的事务，如提交、回滚事务等。
    
    通用语法:
        1. SQL语句,可以写在单行或多行,以分号分隔。
        2. 不区分大小写。一般关键字大写
        3. 注释：
                -- 或 # 单行注释
                /*  多行注释 


*/

# 创建数据库
# 语法: CREATE DATABASE 数据库名;
# 当数据库不存在时,创建数据库。
# 语法：CREATE DATABASE IF NOT EXISTS 数据库名;
#　创建数据库并指定字符集
# 语法：CREATE DATABASE 数据库名 CHARACTER SET 字符集
# CHARACTER SET <==> CHARSET
# 显示所有数据库
# 语法：SHOW DATABASES;
# 使用/切换 数据库
# 语法：USE 数据库名;
# 删除数据库
# 语法：DROP DATABASE 数据库名;

create database if not exists learnDB; # 创建数据库 learnDB
show databases; # 显示所有数据库
use learnDB; # 切换到 learnDB 数据库
drop database if exists learnDB; # 删除数据库 learnDB

create database if not exists learnDB charset utf8;


# 修改数据库字符集
# 语法：ALTER DATABASE 数据库名 CHARACTER SET 字符集
alter database learnDB charset gbk; 

# 查看当前数据库
# 语法：SELECT DATABASE();
select database(); # 查看当前数据库

# ------------------------------------------------------------------
# 表操作
# 01. 创建数据表
# 语法：
# CREATE TABLE 表名 (
#   字段名 数据类型 [约束],
#   字段名 数据类型 [约束],
#   ...
#   字段名 数据类型 [约束]
# );
# example:
create table if not exists staff(
    # 字段1：员工ID, 类型：整数, 主键
    id int primary key,
    # 字段2：姓名, 类型：字符串(20), 非空
    name varchar(20) not null default '',
    # 字段3：年龄, 类型：整数, 非空
    age int not null default 0,
    # 字段4：性别, 类型：枚举, 非空
    sex enum('男','女','未知') not null default '未知'
);
# 数据类型：
#       整数：INT、SMALLINT、MEDIUMINT、TINT
#       字符串：VARCHAR、CHAR、TEXT
#       枚举：ENUM、SET
#       日期时间：DATE、TIME、DATETIME
#       浮点数：FLOAT、DOUBLE
# 约束：
#       非空：NOT NULL
#       主键：PRIMARY KEY
#       唯一索引：UNIQUE
#       索引：INDEX
#       约束：CONSTRAINT

show tables; # 显示所有表
describe staff; # 显示表 staff 的字段信息
# --------------------------------02. 修改数据表---------------------------------------------------------------
#
# --------------------------------重命名数据表---------------------------------------------------------------
# 语法：ALTER TABLE 表名 rename to 新表名;/ rename table 表名 to 新表名;
# example:
alter table staff rename to STAFF; # 重命名表 staff 为 STAFF
rename table STAFF to staff; # 重命名表 STAFF 为 staff
#
# 删除数据表
# 语法：DROP TABLE 表名;
# example:
drop table if exists staff; # 删除表 staff
show tables; # 显示所有表
drop table if exists STAFF; # 删除表 STAFF
#
# ---------------------------------修改数据表字段---------------------------------------------------------------
# 语法：
# 增:   ALTER TABLE 表名 ADD 新字段名 数据类型 [约束];
# 删:   ALTER TABLE 表名 DROP 字段名; 
# 改:   ALTER TABLE 表名 MODIFY 目标字段 新数据类型 [新约束];
# 重:   ALTER TABLE 表名 CHANGE 目标字段 新字段名 新数据类型 [新约束];
# example:
alter table staff add credit varchar(20); # 添加字段 credit, 类型：字符串(20), 非空
alter table staff modify column credit varchar(20) NOT NULL;
# 将字段 credit 重命名为 email
alter table staff change credit email varchar(20) NOT NULL;
alter table staff drop email;

#
#---------------------------------------------数据类型简介---------------------------------------------------------------
#
# 01.整型:
#       INT：       04字节, 有符号, 范围：-2147483648~2147483647
#       SMALLINT：  02字节, 有符号, 范围：-32768~32767
#       MEDIUMINT： 03字节, 有符号, 范围：-16777216~16777215
#       TINT：      01字节, 有符号, 范围：-128~127 
#       UNSIGNED：  04字节, 无符号, 范围：0~65535
# 02.浮点型:
#       FLOAT：     04字节, 有符号, 范围：小数点后7位小数,精确到7位
#       DOUBLE：    08字节, 有符号, 范围：小数点后15位小数,精确到15位
#       DECIMAL：   16字节, 有符号, 范围：高精度小数--------------------------->decimal(10,2) # 10位总精度,2位小数
# 03.字符串型:
#       VARCHAR：  可变长度字符串, 长度：1~65535
#       CHAR：     固定长度字符串, 长度：1~255
#       TEXT：     大文本, 长度：1~65535
#       BLOB：     二进制大, 长度：1~65535
#       ENUM：     枚举类型, 选项：1~65535
#       SET：      集合类型, 选项：1~65535
# 04.日期时间型:
#       DATE：     03字节, 有符号, 范围：1000-01-01~9999-12-31
#       TIME：     03字节, 有符号, 范围：00:00:00~23:59:59
#       DATETIME： 08字节, 有符号, 范围: 1000-01-01 00:00:00~9999-12-31 23:59:59
#
#---------------------------------------------约束概述---------------------------------------------------------------
#
# 01.主键约束       PRIMARY KEY     不能重复, 不能为空, 只能有一个主键
# 02.非空约束       NOT NULL        可以重复
# 03.唯一约束       UNIQUE          可以为NULL
# 04.索引约束       INDEX           
# 05.约束约束       CONSTRAINT      
# 06.外键约束       FOREIGN KEY     用于关联两个表之间的关系
# 07.默认约束       DEFAULT        

