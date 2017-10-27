#coding=utf-8
import requests
import urllib

# 函数: 承运公司名到文本
def GetComName(comCode):
    if comCode=='shentong':
        return '申通快递'
    elif comCode=='zhontong':
        return '中通快递'
    elif comCode=='ems':
        return 'EMS'
    elif comCode=='huitongkuaidi':
        return '汇通快运'
    elif comCode=='baishiwuliu':
        return '单号输入错误'
    else:
        return comCode


p = {}
p['text'] = input("请输入快递运单编号: ")  #比如: 227728570825
autoComNum = requests.get("http://www.kuaidi100.com/autonumber/autoComNum", params=p)
com = autoComNum.json()


if com['auto'] == []:
    print("这是一个错误的运单编号!")

else:
    print("\n---------------- 承运公司 ------------------\n")
    i=0
    for this in com['auto']:
        i = i + 1
        print( str(i) + ". " + GetComName(this['comCode']) + "\n")


    num = input("承运公司序号: ")
    print("\n---------------- 正在查询, 请稍等... ------------------\n")
    data = {}
    data['type'] = com['auto'][int(num)-1]['comCode']
    data['postid'] =  p['text']
    query = requests.get("http://www.kuaidi100.com/query", params=data)
    res = query.json()
    print("\n---------------- 跟踪信息 ------------------\n")
    for this in res['data']:
        print(this['time'] + "\t" + this['context'] + "\n")
