use learnDB;
/*
 *  单表查询介绍:
 *          概述: 
 *              按一定条件,从一张SQL表中查找目标数据 
 *          语法格式:
 *              select
 *                  [distinct] 字段1 [AS 别名1], 字段2, ...
 *              from
 *                  表名 [AS 表别名]
 *              where-----------------------------------组前筛选:
 *                  条件1 [and|or 条件2 ...]
 *              group by--------------------------------分组字段:
 *                  字段1, 字段2, ...
 *              having----------------------------------组后筛选:
 *                  条件1 [and|or 条件2 ...]
 *              order by--------------------------------排序字段:
 *                  排序字段1, 排序字段2, ...
 *              limit-----------------------------------限制行数:
 *                  [偏移量,] 行数;
 */
show tables;
# -----------------------------------01.简单查询-------------------------------
/*
 *    #  查询表中的全部数据(所有行所有列的数据)
 *       SELECT * FROM 表名;
 *    
 *    #  查询表中的指定列数据(所有行指定列的数据)
 *       SELECT 列1, 列2, ... FROM 表名;
 *    
 *    #  查询表中的指定列数据并给结果列起别名
 *       SELECT 列1 AS 别名1, 列2 AS 别名2, ... FROM 表名;
 *    
 *    #  查询表中的指定列数据(所有行指定列的数据)
 *       SELECT 表名.列1, 表名.列2, ... FROM 表名;
 *    
 *    #  查询表中的指定列数据并给表起别名
 *       SELECT 表别名.列1, 表别名.列2, ... FROM 表名 AS 表别名;
 */

select name as '姓名', total_score '总分'  # as可以省略
    from Accepted
    order by total_score desc
    limit 10;

# -----------------------------------02.条件查询-------------------------------
#
/* 
 * 条件:
 *       1. 比较运算符
 *          >, >=, <, <=, !=, <>, =
 *       2. 逻辑运算符
 *          and, or, not
 *       3. 模糊查询
 *          like, not like
 *          #   % 通配符(0 ~ n)
 *          #   _ 单字符通配符
 *       4. 范围查询
 *          between 值1 and 值2;        # 连续,闭区间
 *          not between 
 *       5. 成员查询
 *          in (值1, 值2, ...)
 *          not in (值1, 值2, ...)
 *       6. 空值查询
 *          is null, is not null
 */

# -----------------------------------03.排序查询-------------------------------
/*
 *  格式:
 *       select * from 表名 order by 排序字段1 [asc|desc], 排序字段2 [asc|desc], ...;
 *  说明: 
 *       1. [asc|desc]: 排序方向, asc 升序, desc 降序, 默认升序
 *       2. 无论SQL简单还是复杂, order by 均应写在语句 末尾; 严格来说, 应在limit语句之前.
 */
select * from Accepted
    order by total_score desc, roud1_score desc
    limit 10;
# -----------------------------------04.聚合查询-------------------------------
/*  概述:
 *      以列为单位,对表中的数据,进行统计分析.
 *  格式:
 *       select 聚合函数() from 表名;
 *  说明: 
 *       1. 聚合函数:
 *          count():             统计非空值的        数量           ! count不统计空值
 *          sum():               统计非空值的        总和
 *          avg():               统计非空值的        平均值
 *          max():               统计非空值的        最大值 
 *          min():               统计非空值的        最小值
 *          count(distinct):     统计非空值的        去重数量
 */
# select
#     `rank` as '排名',
#     name as '姓名',
#     roud1_score as '初试分',
#     roud2_score as '复试分',
#     total_score as '总分'
# from Accepted
# where
#     roud2_score = 0;
select count(*) as '总人数' from Accepted;      # 106
select count(1) from Accepted;                 # 106
select count(roud2_score) from Accepted where roud2_score != 0;        # 103
# -----------------------细节题--------------------------
# 题目：
#       count(*), count(1) 与 count(字段名) 区别?
# 答案：
#       1.是否计入空值:
#         count(*), count(1): 计入空值
#         count(字段名): 不统计空值
#       2.效率差异:
#         count(key) > count(1) > count(字段名) > count(*)
#         # 说明: key 是主键, 使用索引, 效率最高
#--------------------------------------------------------


select avg(roud1_score) as '初试平均分', avg(roud2_score) as '复试平均分', avg(total_score) as '总分平均分' from Accepted;

select max(roud1_score) as '初试第一', max(roud2_score) as '复试第一' from Accepted;

# -----------------------------------05.分组查询-------------------------------
/*
 *  概述:
 *      以行为单位,对表中的数据,进行统计分析.
 *  格式:
 *       select 
 *          分组字段, 
 *          聚合函数(字段名),
 *          ... ...
 *       from 
 *          表名
 *       where 
 *          条件
 *       group by 
 *          分组字段1, 分组字段2, ...
 *       having 
 *          条件(组内筛选)
 *
 *  注意: 
 *       1. 先分组, 再进行聚合操作.
 *       2. 分组依据: group by 后面的字段的排列组合
 *       3. 分组后: selec后的查询字段必须满足以下情况之一
 *                 i.  字段是分组字段 <==> 查询字段在group by 后面出现
 *                 ii. 字段被聚合函数包裹 <==> 聚合函数(字段名)
 *
 */
alter table Accepted modify `status` enum('拟录取', '未录取') default '未录取' not NULL comment '录取状态' after total_score;
alter table Accepted modify info enum('无', '非全日制', '全日制')  default '无' not null comment '备注';
update Accepted set `status` = '拟录取' where `rank` <= 82;
update Accepted set info = '无' where `status` != '拟录取';
update Accepted set info = '全日制' where `status` = '拟录取';
update Accepted set info = '非全日制' where `rank` in (19,25,43,57,62);

select name, `status`, info from Accepted where `rank` between 58 and 67 order by `rank`


select `status`, info, avg(roud1_score) as '初试平均分' from Accepted group by `status` , info;
#select * from Accepted where (`status` = '拟录取' and info = '无') or (`status` = '未录取' and info != '无');



# -----------------------------------06.去重查询-------------------------------S