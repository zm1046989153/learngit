# _*_ coding=utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys,unittest,time
import xml.dom.minidom
import random

sys.path.append('D:\\ISS\\Test_Cases\\public')
import login
from isspublic import*

#打开xml文件
dom=xml.dom.minidom.parse('D:\\ISS\\Test_Data\\login.xml')
#获取文件元素对象
root=dom.documentElement

#用户编码
user_code='ZM_141452'

#用户名称
user_name=u'AtZMing'



class test_UserInformation(unittest.TestCase):
    #用户信息模块测试
    log.info(u"~~~用户信息模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_UserInformation(self):
        #用户信息模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入用户信息
        testModule(driver,u'系统管理',u'用户信息')
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmUserAccordion table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        sleep(1)

    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmUserToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmUserToolbar > a.easyui-linkbutton.findButton > span > span').click()
            sleep(1)

        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#stmUserToolbar > a.easyui-linkbutton.viewButton > span > span').click()
            sleep(1)

            self.assertEqual(u"编辑",driver.find_element_by_css_selector("#stmUserForm > div:nth-child(1) > a.easyui-linkbutton.saveButton > span > span > span").text)


        elif button==u'编辑' or button=='edit':
            #点击“编辑”按钮
            driver.find_element_by_css_selector('#stmUserForm > div:nth-child(1) > a.easyui-linkbutton.saveButton > span > span > span').click()
            sleep(1)
            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmUserToolbar > a.easyui-linkbutton.editButton > span > span').click()
            sleep(1)
    

    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmDptToolbar > a.easyui-linkbutton.deleteButton > span').click()
            sleep(1)
            
            #点击确认，删除记录并断言
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            sleep(1)
            dele_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text
            #print dele_text
            log.info(dele_text)
            self.assertEqual(u"删除成功",dele_text)
            
            #点击取消
            #driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2)").click()
                
        elif button==u'取消' or button=='cancel':
            #编辑界面，点击“取消”按钮
            driver.find_element_by_css_selector('body > div:nth-child(17) > div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            #取消
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            
            sleep(1)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("#stmUserForm  a.easyui-linkbutton.saveButton > span > span > span").click()
            sleep(0.5)
            
            #获取断言信息
            
            success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
            tip_text=success.text
            
            #print tip_text
            log.info(tip_text)
            
            #确定,关闭提示框
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

            #断言是否保存成功
            self.assertEqual(u"保存成功！",tip_text)
            
        else:
            raise NameError('No Such Button,confirm again please')

        
    def test_0add_User(self):
        u'''添加用户'''

        log.info(u"开始执行用例...")
        
        driver=self.driver
        
        #进入用户信息模块
        self.to_UserInformation()

        #添加
        self.clickButton(u'添加')

        #用户名称
        name=user_name
        findCss(driver,"#stmUserForm tr:nth-child(1) > td:nth-child(7) > input").send_keys(name)
        sleep(0.5)

        #用户编码
        global user_code
        strt=time.strftime("%H%M%S",time.localtime(time.time()))
        user_code="ZM_"+strt
        code=user_code

        findCss(driver,"#stmUserForm  tr:nth-child(1) > td:nth-child(9) > input").send_keys(code)
        sleep(0.5)

        #注册日期
        findCss(driver,"#stmUserForm  tr:nth-child(2) > td:nth-child(2) > span > input.combo-text.validatebox-text").click()
        sleep(0.5)
        findCss(driver,"#stmUserForm  tr:nth-child(2) > td:nth-child(2) > span > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        sleep(0.5)

        #失效日期
        date='2026-03-14'
        findCss(driver,"#stmUserForm  tr:nth-child(2) > td:nth-child(4) > span > input.combo-text.validatebox-text").send_keys(date)
        sleep(0.5)
        
        #保存
        self.clickButton(u"保存")
        
        

    def searchbycode(self,code):
        u'''按编号查找'''
        driver=self.driver

        #输入要查找的编码
        findCss(driver,"#fdCode").clear()
        sleep(0.5)
        findCss(driver,"#fdCode").send_keys(code)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")

        #断言
        cds=findsCss(driver,"#stmUserAccordion > div:nth-child(1) table.datagrid-btable td[field='fdCode']")
        searchAssert(self,cds,code) 
 
        
    def test_1search_byUserCode(self):
        u'''按用户编码查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        
        #进入用户信息模块
        self.to_UserInformation()

        #输入用户编码,查找
        code=user_code
        self.searchbycode(code)
        

    def test_2search_byUserName(self):
        u'''按用户名称查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        
        #进入用户信息模块
        self.to_UserInformation()

        #输入用户名称
        name=user_name
        findCss(driver,"#fdName").send_keys(name)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #断言
        nas=findsCss(driver,"#stmUserAccordion > div:nth-child(1) table.datagrid-btable td[field='fdName']")
        searchAssert(self,nas,name)
        

    def test_3iew_User(self):
        u'''查看用户'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        
        #进入用户信息模块
        self.to_UserInformation()

        #查找
        code=user_code
        self.searchbycode(code)

        #选择
        findCss(driver,"#stmUserAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #查看
        self.clickButton(u"查看")

        #编辑
        self.clickButton(u"编辑")
        
        #保存
        self.clickButton(u'保存')
        
        

    def test_4modify_User(self):
        u'''修改用户'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        
        #进入用户信息模块
        self.to_UserInformation()

        #查找
        code=user_code
        self.searchbycode(code)

        #选择
        findCss(driver,"#stmUserAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u"修改")

        user_info=u"zm用户说明！@#￥@￥"

        findCss(driver,"#stmUserForm  tr:nth-child(1) > td:nth-child(11) > input").clear()
        sleep(0.5)
        findCss(driver,"#stmUserForm  tr:nth-child(1) > td:nth-child(11) > input").send_keys(user_info)

        #保存
        self.clickButton(u"保存")

        #再次查找
        self.searchbycode(code)

        #断言是否被正常修改
        assertEqual(user_info,findCss(driver,"#stmUserAccordion > div:nth-child(1) table.datagrid-btable td[field='fdDesc']"))
        


       
    
    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_UserInformation start--')
    suite=unittest.TestSuite()
    
    suite.addTest(test_UserInformation('test_0add_User'))#添加用户
    #suite.addTest(test_UserInformation('test_1search_byUserCode'))#按用户编码查找
    #suite.addTest(test_UserInformation('test_2search_byUserName'))#按用户名称查找
    #suite.addTest(test_UserInformation('test_3iew_User'))#查看用户
    suite.addTest(test_UserInformation('test_4modify_User'))#修改用户
    
    
       
   
    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_UserInformation end--')
        
