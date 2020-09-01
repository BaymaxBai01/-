import pymysql

# 打开
  #第一件事
conn = pymysql.connect(host="rm-2ze0u172x2a69w5h6qo.mysql.rds.aliyuncs.com",
                       port=3306,
                       user="aura",
                       password="zgbLZTgs"
                       # 如果需要在某一数据库中查询的时候，需要添加下面的指定数据库的命令
                       ,database="aura"
                       )

# print(conn) #如果没报错，就说明链接成功
  #第二件事
# cursor = conn.cursor() # 不用管，拿一个游标（光标）
cursor = conn.cursor(pymysql.cursors.DictCursor) #在获取游标的时候传一个参数，返回格式为字典

# 操作

"""测试"""
# sql = """
# SELECT 'Hello,world.';
# """

"""1. 查看有多少数据库"""
# sql = """
# SHOW DATABASES;
# """

"""2. 选择其中一个数据库来使用"""
# sql = """
# use aura;
# """

"""3. 查看数据库内有多少表"""
# sql = """
# SHOW TABLES;
# """

"""4. 查看一下表结构（关系型数据库）"""
# sql = """
# DESC student;
# """

"""5. 查询"""
# sql = """
# select * from student
# limit 10;
# """

# sql = """
# select count(*) from student;
# """

"""6.数据需求1"""
# sql = """
# select
# class as '班级',
# max(age) as '最大年龄',
# min(age) as '最小年龄',
# avg(age) as '平均年龄',
# std(age) as '标准差年龄'
# from student
# where math is not null  --先执行where过滤条件
#   and english is not null
#   and chinese is not null
#   and math between 0 and 100  --between and 包含0和100
#   and english between 0 and 100
#   and chinese between 0 and 100
# group by class  --然后进行分组
# -- 备注：由于sql语句在python中不可以使用注释，所以这条code仅限阅读，不做执行，执行请见下面code
# ;
# """

sql = """
select
class as '班级',
max(english) as '英语最高分',
min(math) as '数学最低分',
avg(chinese) as '语文平均分',
sum(english+math+chinese) as '总分'
from student
where math is not null
  and english is not null
  and chinese is not null
  and math between 0 and 100
  and english between 0 and 100
  and chinese between 0 and 100
group by class
;
"""

nums = cursor.execute(sql)
data = cursor.fetchall()
for item in data:
    print(item)
    # print(item.get("Database")) #获取json格式数据的值

# 关闭

cursor.close()
conn.close()