#coding=utf-8
import urllib2
import urllib
import BeautifulSoup


values={'postid':'227728570825'}
user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
headers = { 'User-Agent' : user_agent }
data=urllib.urlencode(values)
url='http://www.kuaidi100.com/'
req = urllib2.Request(url,data,headers)
response=urllib2.urlopen(req)
html=response.read()
print html