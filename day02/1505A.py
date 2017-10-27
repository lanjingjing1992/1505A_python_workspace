#coding=utf-8
#计算1至50中是7的倍数的数值之和
#  sum=0
# for i in range(1,51,1):
#     if i%7==0:
#         # print i
#         sum+=i
#
#
# print sum
# list=[]
# while True:
#     num=int(raw_input('请输入数字，输入0结束'))
#
#     if num==0:
#         break
#     list.append(num)
#
# print max(list)
# print min(list)
# list1=[1,2,3]
# list2=[4,5,6]
# list1.extend(list2)
# list1.append(list2)
# print list1
# 输入10位商场中顾客的年龄，并且计算出百分比
# j=0
# k=0
# for i in range(10):
#     age=int(raw_input('请输入年龄'))
#     if age>=30:
#         j+=1
#     else:
#         k+=1
#
#
# print '30以上的人占比例%s'%(j*10)+'%'
# print '30以下的占比例%s'%(k*10)+'%'
# 1~10之间的整数相加，得到的累加值大于20后结束循环，
# sum=0
# for i in range(1,10,1):
#     sum+=i
#     if sum>20:
#         print sum
#         break
#求1~10之间的所有偶数和
# sum=0
# for i in range(1,11,1):
#     if i%2==0:
#         sum+=i
#
#
# print sum

#输出 1 － 100之间能被5整除，但不能被3或8整除的值
# for i in range(1,100,1):
#     if i%5==0 and i%3!=0 and i%8!=0 :
#         print i




#输出　100 -- 999之间, 所有个位为7的数
# for i in range(100,999,1):
#     n=i%10
#     if n==7:
#         print i
#输出  100 -- 999之间, 所有百位 + 十位 == 个位　的数
# for i in range(100,999,1):
#     #个位
#     n=i%10
#     #十位
#     m=i%100//10
#     #百位
#     k=i//100
#
#     if k+m==n:
#         print i

#输出 10 - 99 之间所有“相邻”的值,如: 23, 54, 98
# for i in range(10,99,1):
#     #个位
#     n=i%10
#     #十位
#     m=i//10
#
#     if n-m==1 or m-n==1:
#         print i
# for k in range(1,4,1):
#
#     print '请输入%s班级四位学员的成绩'%k
#     count=0#总成绩
#     for i in range(1,5,1):
#         score=int(raw_input('请输入第%s位学员的成绩'%i) )
#
#         count+=score
#
#     print count/4
list=[]
while True:
    name=raw_input('请输入客户名字')
    list.append(name)
    y_n=raw_input('是否继续输入，输入n结束，其他的话则继续')
    if y_n=='n':
        print '客户姓名列表\n' \
              '***************'
        for i in list:
            print i,
        print '\n***************'
        searchName=raw_input('请输入要查找的姓名')
        if searchName in list:
            print '找到了'
        else:
            print '查无此人'

        break












