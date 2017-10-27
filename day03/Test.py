#coding=utf-8
# 请实现如下添加修改学生姓名的功能：
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
        for i in range(len(list)):
            if searchName == list[i]:
                print '找到了'
                newName=raw_input('请输入要替换的新名字')
                list[i]=newName
                print list
                break

            else:
                print '查无此人'
        break


