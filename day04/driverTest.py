#coding=utf-8
from selenium import webdriver
from time import sleep


d=webdriver.Chrome()
d.get('https://www.toutiao.com/')
sleep(1)
# d.find_element_by_name('wd').send_keys('selenium')#定位到输入框 并且输入内容
# sleep(1)
# d.find_element_by_class_name('bgs_btn').click()#定位到按钮  并且点击
# sleep(1)
# d.close()#关闭当前网页
# d.find_element_by_link_text(u'录').click()
# d.find_element_by_xpath('//*[@id="u1"]/a[7]')
# d.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
# d.switch_to_alert()#定位到弹出框
# sleep(1)
# d.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys('15901337131')#账户名
# d.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').send_keys('123456')
# d.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()

# d.quit()
# d.maximize_window()#窗口最大化
d.find_element_by_xpath('//*[@id="rightModule"]/div[1]/div/div/div/input').send_keys(u'十九大')
d.find_element_by_xpath('//*[@id="rightModule"]/div[1]/div/div/div/div/button').click()

#切换窗口
all_windows=d.window_handles#d中存储的所有的窗口
current_window=d.current_window_handle#d现在存在的窗口
for window in all_windows:
    if window!=current_window:#即将跳转的窗口
        d.switch_to_window(window)#跳转
sleep(2)



d.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[2]/ul/li[2]').click()
sleep(3)
d.quit()