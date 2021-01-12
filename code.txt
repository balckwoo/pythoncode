# 数值类型
# 整型
# intvar = 0
# # 浮点型
# floatvar = 3.1415926
# # 布尔值类型
# boolvar = True
# intvar2 = []
# intvar3 = None
# intvar4 = False
# # 函数转换
# boolvar2 = (bool(intvar4))
# print(boolvar2)
# 0,None,False,空的量  = 假（False)
# 1,非空的量，非零的数值 = 真（True）
# 序列
# 数据结构
# 有序序列
# 字符串
# strvar = 'admin'
# # 查[] 加的是下标（索引）
# print(strvar[3])
# # find查下标
# print(strvar.find('a',0))
# # 字符串是不可以修改的
# # 可以替换，拿个变量装起来
# print('修改前的字符串是',strvar)
# strvar2=(strvar.replace('adm','youkeng'))
# print('修改后的字符串是',strvar)
# print('生成的心的字符串是',strvar2)
#
# # 把字符串变成列表（分隔字符串）
# strvar3 = '18797763626@.163.com'
# strvar4 = 'a,b,c,d,e'
# a = strvar3.split('@')
# b = a[1].split('.')
# c = b[1]
# d = b[2]
# e = a[0]
# print(e+c+d)
# strvar5 = strvar4.split(',')
# print(strvar5)
# format格式化字符串
# strvar6 = 'admin'
# intvar = 20191223
# floatvar = 1.0
# listvar = ['shangfenrutongheshui']
# print('测试报告{}'.format(listvar))
# print('测试报告{}{}{}{}'.format(strvar6,intvar,floatvar,listvar))

# 列表
# listvar = ['admin',10,3.14,[10,],(10,20)]
# 列表里面有单个数值的数值的是后不需要加，
# listvar2 = [10,20,30]
#
# # 列表增加一个值
# print('原来的列表里面有',listvar2)
# listvar2.append(40)
# print('增加后的列表里面有',listvar2)

# # 使用索引的方式制定添加值
# listvar2.insert(2,999)
# print('使用指定下标增加后的列表里面有',listvar2)
# # 列表删除一个值
# listvar2.pop()
# print('删除后的列表里面有',listvar2)
# # 使用索引的方式指定删除某个值
# listvar2.pop(0)
# print('使用指定下标删除后的列表里面有',listvar2)


# listvar3 = [10,20,30,40,50]
# 查询列表20所在的位置
# 下标（索引）的位置是从0开始的
# 0 = 10, 1=20 ,2=30,3=40,4=50
# print('20所在的位置是',listvar3.index(20))
# listvar3 = [10, 20, 30, 40, 50, 60, 70, 80]
# # 查询到列表里面的值
# print(listvar3[1])
# 1代表起始位置， 4代表最终位置（欺骗+1） ，1代表步长
# print(listvar3[1:4:1])
# print(listvar3[1:4:2])
# print(listvar3[1:4:3])
#
# # 修改
# print('修改前数据是',listvar3)
# listvar3[1]=999
# print('修改后的数据是',listvar3)

# 元组
# 不可增删
# tupvar = ('admin',10,3.14,(10,20,30,40))
# # 元组里面有单个的数值的时候需要加,
# tupvar2 = (1,)
# # 查询
# # 查询它的下标可以用index
# print(tupvar.index('admin'))
# print(tupvar[1])
# 练习题
# data = [[[[10, 20, 30, 40, [('hello', 'hello,python')]]]]]
# # 取出python
# # len() 方法返回对象（字符、列表、元组等）长度或项目个数
# # print(len(data))
# # print(type(data))
# result = data[0][0][0][4][0][1][6:12:1]
# print(result)
# 无序序列
# 字典
# name代表key（键）  value代表 键值对jason
# name一定是唯一的
# 字典展示的顺序是无序的
# dictvar = {"name":"jason"}
# 查询
# print(dictvar['name'])
# # get方法含有默认值 None
# # 不指定默认值
# print(dictvar.get('name2',))
# # 指定默认值
# print(dictvar.get('name2','tiantian'))

# 修改
# print('原本的字典的值是',dictvar)
# dictvar["name"] = "tim"
# print('现在的字典的值是',dictvar)
# # 增加
# print('原本的字典的值是',dictvar)
# dictvar['age'] = 19
# print('现在的字典的值是',dictvar)

# 删除pop
# dictvar.pop('name')
# print('删除后现在的字典的值是',dictvar)

# 取出hello
# dictvar = [(10, 20, 30, {'name': [10, 20, 30, {'admin': 'ajslahellofj'}]})]
# result = dictvar[0][3]['name'][3]['admin'][5:10:1]
# print(result)

# 集合（去重的功能）
# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
# gathervar = {123,2,3,4,5}
# gathervar2 = set()
# print(type(gathervar),type(gathervar2))
# gathervar2 = {10,20,20,20,3}
# print(gathervar2)
# 面试经典题 列表去重
# 列表和字典是不可以使用set去重的
# listvar = [1,2,3,3,3,3,4,5]
# print('原本的列表是',listvar)
# set(listvar)
# print('转换后的是',listvar)
# # 先用变量名l1来接住
# l1 = set(listvar)
# print('转换后的值是',l1)
# # 但是现在是一个集合
# result = list(l1)
# # 再用list转换为一个新的列表
# print('现在的列表是',result)

# 值类型
# 引用类型
# python的值类型：int，str，tuple --- 元素不可变的，要改变只能重新声明或者覆盖
#
# python的引用类型：set，list，dict --- 元素的值时可变的

# for循环
# 生成一个从1到7的列表
