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


#快递公司编号
ex_code='ZM185036'

#快递公司名称
ex_name=u"启尚物流"




class test_DefaultExpress(unittest.TestCase):
    #默认快递模块测试
    log.info(u"~~~默认快递模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_DefaultExpress(self):
        #进入默认快递模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入默认快递
        testModule(driver,u'系统管理',u'默认快递')
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmShippingAccordion > div:nth-child(1) table.datagrid-btable  td[field='ck']")
        
        log.info(u"刷新完成！！！")
    
    def clickButton(self,button):
        u'''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmShippingToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmShippingToolbar > a.easyui-linkbutton.findButton > span > span').click()
            
            sleep(1)

        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#stmShippingToolbar > a.easyui-linkbutton.viewButton > span > span').click()
            sleep(1)

            self.assertEqual(u"编辑",driver.find_element_by_css_selector("#stmShippingForm > div:nth-child(1) > a.easyui-linkbutton.saveButton > span > span > span").text)
            
        elif button==u'编辑' or button=='view':
            #点击“编辑”按钮
            driver.find_element_by_css_selector('#stmShippingForm > div:nth-child(1) > a.easyui-linkbutton.saveButton > span > span > span').click()
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmShippingToolbar > a.easyui-linkbutton.editButton > span > span').click()
            sleep(1)
                
    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmShippingToolbar > a.easyui-linkbutton.deleteButton > span > span').click()
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
            driver.find_element_by_css_selector('#stmShippingForm > div:nth-child(1) > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            #取消
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            
            sleep(1)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("#stmShippingForm > div:nth-child(1) > a.easyui-linkbutton.saveButton > span > span > span").click()
            sleep(0.5)
            
             #获取断言信息
            
            success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
            tip_text=success.text
            log.info(tip_text)
            
            #确定,关闭提示框
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

            #断言是否保存成功
            self.assertEqual(u"保存成功！",tip_text)
            
        else:
            raise NameError('No Such Button,confirm again please')

        
    def test_0add_DefaultExpress(self):
        u'''添加默认快递'''
        driver=self.driver

        #进入默认快递
        self.to_DefaultExpress()

        #添加
        self.clickButton(u'添加')

        #快递公司编号
        global ex_code
        strt=time.strftime("%H%M%S",time.localtime(time.time()))
        ex_code='ZM'+strt
        code=ex_code
        findCss(driver,"#stmShippingForm  tr:nth-child(1) > td:nth-child(6) > input").send_keys(code)
        sleep(0.5)

        #快递公司名称
        global ex_name
        ex_name=u"启尚物流"+strt
        
        name=ex_name
        
        findCss(driver,"#stmShippingForm  tr:nth-child(1) > td:nth-child(8) > input").send_keys(name)
        sleep(0.5)

        #保存
        self.clickButton(u"保存")
        
        
        
    def searchbycode(self,code):
        u'''按编码查找'''
        driver=self.driver
        
        findCss(driver,"#stmShippingToolbar > input:nth-child(1)").clear()
        sleep(0.5)

        #输入编码
        findCss(driver,"#stmShippingToolbar > input:nth-child(1)").send_keys(code)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #断言
        cds=findsCss(driver,"#stmShippingAccordion > div:nth-child(1) table.datagrid-btable td[field='fdCode']")
        searchAssert(self,cds,code)
        
    
    def test_1search_byExpressCompanyCode(self):
        u'''按快递公司编码查找'''
        driver=self.driver


        #进入默认快递
        self.to_DefaultExpress()

        #输入编码查找
        code=ex_code
        self.searchbycode(code)
        
        
    def test_2search_byExpressCompanyName(self):
        u'''按快递公司名称查找'''
        driver=self.driver

        #进入默认快递
        self.to_DefaultExpress()

        #输入快递公司名称
        name=ex_name
        findCss(driver,"#stmShippingToolbar > input:nth-child(2)").send_keys(name)
        sleep(0.5)

        #查找
        self.clickButton(u'查找')

        #断言
        nas=findsCss(driver,"#stmShippingAccordion > div:nth-child(1) table.datagrid-btable td[field='fdName']")
        searchAssert(self,nas,name)
        

    def test_3view_DefaultExpress(self):
        u'''查看默认快递'''
        driver=self.driver

        #进入默认快递
        self.to_DefaultExpress()
        

        #选择快递
        findCss(driver,"#stmShippingAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #查看
        self.clickButton(u"查看")
        self.assertEqual('true',findCss(driver,"#stmShippingForm  tr:nth-child(1) > td:nth-child(6) > input").get_attribute("readonly"))

        #编辑
        self.clickButton(u"编辑")
        

        #保存
        self.clickButton(u"保存")
        

    def test_4modify_DefaultExpress(self):
        u'''修改默认快递'''
        driver=self.driver

        #进入默认快递
        self.to_DefaultExpress()
        
        #输入编码查找
        code=ex_code
        self.searchbycode(code)
        

        #选择快递
        findCss(driver,"#stmShippingAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        #修改
        self.clickButton(u"修改")

        #修改公司名称
        new_name="NEW_"+ex_name
        findCss(driver,"#stmShippingForm  tr:nth-child(1) > td:nth-child(8) > input").clear()
        sleep(0.5)
        findCss(driver,"#stmShippingForm  tr:nth-child(1) > td:nth-child(8) > input").send_keys(new_name)
        sleep(0.5)

        #保存
        self.clickButton(u"保存")

        #再次查找
        self.searchbycode(code)
        

        #断言
        self.assertEqual(new_name,findCss(driver,"#stmShippingAccordion > div:nth-child(1) table.datagrid-btable td[field='fdName']").text)
        

        

    def test_5delete_DefaultExpress(self):
        u'''删除默认快递'''
        driver=self.driver

        #进入默认快递
        self.to_DefaultExpress()

        #输入编码查找
        code=ex_code
        self.searchbycode(code)
        

        #选择快递
        findCss(driver,"#stmShippingAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #删除
        self.clickButton(u"删除")
         

    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_DefaultExpress start--')
    
    suite=unittest.TestSuite()
    
    #suite.addTest(test_DefaultExpress('test_0add_DefaultExpress'))#添加默认快递
    #suite.addTest(test_DefaultExpress('test_1search_byExpressCompanyCode'))#按默认快递公司编号查找
    #suite.addTest(test_DefaultExpress('test_2search_byExpressCompanyName'))#按默认快递公司名称查找
    #suite.addTest(test_DefaultExpress('test_3view_DefaultExpress'))#查看默认快递
    suite.addTest(test_DefaultExpress('test_4modify_DefaultExpress'))#修改默认快递
    #suite.addTest(test_DefaultExpress('test_5delete_DefaultExpress'))#删除默认快递
    
  
   
    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()

    
    log.info('test_DefaultExpress end--')
        
