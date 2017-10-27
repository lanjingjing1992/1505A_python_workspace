#coding=utf-8
class Menu:
    def __init__(self):#相当于构造函数 创建对象的时候自动调用构造函数 self指代本类对象的一个指针

        self.map={1:['鱼香肉丝',16],2:['宫保鸡丁',20],3:['醋溜土豆丝',10]}#属性


class Customer:
        def __init__(self):#构造方法  初始化方法
            self.m = Menu()  # 创建对象
            self.str='您的点餐信息如下\n' \
                      '******************************\n' \
                      '编号   菜品名称   价钱   数量   小计\n'
            self.sum=0
        def login(self):

            name = raw_input('请输入管理员姓名')
            if name=='admin':
                passwd=raw_input('请输入管理员密码')
                if passwd=='123':
                    print 'welcome'#管理员权限

                    # print self.m.map[1][0]#第一个是键 第二个是下标
                    # print self.m.map[2][0]

                    self.addmenu()
                else:
                    print '密码错误'
                    self.login()
            else:
                print '输入姓名错误'
                self.login()
        def addmenu(self):
            name = raw_input('请输入新的菜名')
            price = int(raw_input('请输入新的价格'))
            # 当前共有多少个菜
            n = len(self.m.map)
            self.m.map.update({n+1: [name, price]})  # 用来新添键值对
            y_n = raw_input('是否继续添加 输入y则继续，输入其他则停止')
            if y_n == 'y':
                self.addmenu()
            else:

                self.Calc()
        def Calc(self):#结账

            print '菜单展示\n' \
                  '*****************************\n' \
                  '编号        菜名        单价'
            # name=self.m.map[1][0]
            # price=self.m.map[1][1]
            for i in range(1,len(self.m.map)+1,1):
                print '%s          %s         %s'%(i,self.m.map[i][0],self.m.map[i][1])

            # print '1         %s            %s'%(self.m.map[1][0],self.m.map[1][1])
            # print '2         %s            %s'%(self.m.map[2][0], self.m.map[2][1])
            # print '3         %s            %s'%(self.m.map[3][0], self.m.map[3][1])
            id=int(raw_input('请根据才到输入您所需的菜品编号'))
            num=int(raw_input('请输入所需菜品的数量'))
            y_n=raw_input('是否继续点餐，输入n结束，输入其他则继续')
            count=self.m.map[id][1]*num
            self.sum+=count
            self.str+='%s     %s     %s     %s     %s\n'%(id,self.m.map[id][0],self.m.map[id][1],num,count)
            if y_n=='n':
                #显示账单

                self.str+= '--------------------------------\n' \
                      '总计：%s元\n' \
                      '**********************************'%self.sum
                print self.str
                file=open('test.txt','w+')#打开文件
                file.write(self.str)#写入文件
                # file.seek(0,0)#游标放到开头的位置
                # data=file.read()#读取
                # print data
                file.close()#关闭文件

            else:
                self.Calc()


number=raw_input('如果您是管理员请输入1，顾客的话输入其他')
c = Customer()
if number=='1':

    c.login()
else:
    c.Calc()






