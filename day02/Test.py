#coding=utf-8
# for i in range(1,10,1):
#     for j in range(1,i+1,1):
#         t=i*j
#         print '%s*%s=%s'%(i,j,t),
#         if j==i:
#             print '%s*%s=%s'%(i,j,t)
#
# def f(month):#参数代表月份
#     if month==1:
#         return 1
#     elif month==2:
#         return 1
#     else:
#         return f(month-1)+f(month-2)
#
#
# print f(10)
# def f(n,num):
#     if n==1:
#         return num*10
#     else:
#         return f(n-1,num)*10
#
# c=0
# for i in range(1,5,1):
#     sum=f(i,3)
#     c+=sum
#
#
# print c
# def f(n,num):#num=2
#     if n==1:
#         return num
#     else:
#         return f(n-1,num)*10+num
#
#
# # print f(5,2)
# sum=0
# for i in range(1,6,1):
#     t=f(i,2)
#     sum+=t
#     print sum
#
#
# print sum
# def f1(n):#分子
#     if n==1:
#         return 2
#     elif n==2:
#         return 3
#     else:
#         return float(f1(n-1))+float(f1(n-2))
#
#
# def f2(n):#分母
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
#     else:
#         return float(f2(n-1)+float(f2(n-2)))
#
# sum=0.00
# for i in range(1,21,1):
#      t= f1(i)/f2(i)
#      sum+=t
#      print sum
#求1+2!+3!+...+20!的和
# def f(n):
#     if n==1:
#         return 1
#     else:
#         return n*f(n-1)
#
#
# print f(20)
# sum=0
# for i in range(1,21,1):
#     t=f(i)
#     sum+=t
#
#
# print sum

# 请计算出100以内的偶数和
# sum=0
# sum2=0
# for i in range(101):
#     if i%2!=0:
#         sum+=i
#     else:
#         sum2+=i
#
#
#
#
# print sum
# print sum2
# score=int(raw_input('请输入小明的成绩'))
# if score>=98:
#     print '奖励mp4'
# elif score>=60:
#     print '不讲不罚'
# else:
#     print '罚写代码'
# 从键盘上输入任意一个整数，输出这个整数是几位数
# num=int(raw_input('请输入一个数字'))1234
# #个位数
# n=num//10
# #十位数
# k=num//10
# #百位数
# m=num//100
# #千位
# j=num//1000
# i=0
# def f(num):
#     n=num//10
#     global i
#     i+=1
#     if n==0:
#         print '%s位数'%i
#     else:
#         f(n)
#
# f(num)
# t=100
# while True:
#
#     t-=5
#     print t
#     if t == 5:
#         break
#     print t
#     if t<0:
#
#         break






















