#coding=utf-8
# a='hello'
# a=1
# a=1.11
# a=1+3j
# a=(1,2,3,'hello')#元组 tuple
# a=[1,2,3,'hh']#列表 list
# a={'a':1,'b':3}#字典  map
# print type(a)

# a=7.888
# print type(a)
# b=2.0
# print type(b)
# c=a//b
# print type(c)
# print c
# while True:
#     a=raw_input('请输入')
#     if a=='a':
#         print 'this is a'
#     elif a=='b':
#         print 'this is b'
#         break
#     else:
#         print 'else'

#冒泡排序的结构  双重for循环

# list=[]
# for i in range(5):#i的取值从0到5  包括0 但是不包括5 包括前面 不包括后面
#     n=int(raw_input('请输入数字'))
#     list.append(n)
#
#
# def BubbleSort(list):
#     for i in range(len(list)):#list的长度
#         for j in range(len(list)-i-1):
#             if list[j]>list[j+1]:
#                 temp=list[j]
#                 list[j]=list[j+1]
#                 list[j+1]=temp
#
#
#     print list
#
#
#
# BubbleSort(list)


for i in range(1,8,2):
    t=i*'*'
    print t.center(7)



for i in range(7,0,-2):
    t=i*'*'
    print t.center(7)