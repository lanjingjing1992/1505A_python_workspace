#coding=utf-8
import re
def f(language):
    # pattern = re.compile(r'<!DOCTYPE html>(.*?)<html>',re.I | re.M)
    pattern=re.compile(r'/<!DOCTYPE html>.<\/html>/' )
    items = re.findall(pattern, language)
    for item in items:
        # pattern = re.compile(r'<span>(.*?)</span>')
        # i = re.findall(pattern, item)
        print item
        # res_span=r'<span>(.*?)<span>'
        # s=re.findall(res_span,item,re.S|re.M)
        # if len(s)!=0:
        #     print s


#方法测试
language = '''<!DOCTYPE html>hello<html>'''
# f(language)