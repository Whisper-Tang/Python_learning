/*
*   主键:Primary Key
*       用于唯一标识每一行的字段    
*       - 主键约束不能为空值
*       - 主键约束不能重复值
*       - 单表有且只有一个主键!!
*   
*   创建方式:
*       1. 建表时创建
*          ==>type_1:
*                    create table 表名 (
*                        字段名 数据类型,
*                        字段名 数据类型,
*                        ...
*                        primary key (字段名)
*                    );
*          ==>type_2:
*                    create table 表名 (
*                        字段名 数据类型 primary key,
*                        字段名 数据类型,
*                        ...                  
*                    );
*       2. 建表后创建
*          ==> 添加主键:
*                    alter table 表名 add primary key (字段名);
*          ==> 删除主键:
*                    alter table 表名 drop primary key;
*
*       3. 查看主键:
*          ==> 查看所有主键:
*                    show primary keys;
*          ==> 查看指定表的主键:
*                    show primary keys from 表名;
*/

use learnDB;
select * from staff;

