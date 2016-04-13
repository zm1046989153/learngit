
# _*_ coding=utf-8 _*_
from selenium import webdriver
from time import sleep
import sys
from isspublic import*
sys.path.append('D:\\ISS\\Test_Cases\\public')
driver=webdriver.Firefox()
driver.get('http://192.168.1.172:8080/ISS10/index.jsp')
driver.maximize_window()

#填写帐号、密码
driver.find_element_by_css_selector('#loginForm > div:nth-child(1) > input[type="text"]').send_keys('JOE_ADMIN')
driver.find_element_by_css_selector('#loginForm > div:nth-child(2) > input[type="password"]').send_keys('qs8888')

#点击登录按钮
driver.find_element_by_css_selector('#buttonLogin > span > span').click()

#进入销售组织管理
testModule(driver,u'系统管理',u'销售组织管理')
sleep(1)
bt=driver.find_element_by_css_selector('#stmDptToolbar > a.easyui-linkbutton.findButton.004019A01.l-btn.l-btn-plain > span > span')
#stmDptToolbar > a.easyui-linkbutton.addButton.\30 04019A03.l-btn.l-btn-plain
print bt.text
#bt.click()
driver.close()
driver.quit()
