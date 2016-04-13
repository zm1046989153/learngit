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

#量体项目编码
item_code='ZM104802'

#量体项目名称
item_name='Measure104802'

#描述信息
item_info=u'这是一个量体项目ZZ（自动化）！！@#%￥'

class test_MeasureItem(unittest.TestCase):
    #量体项目模块测试
    log.info(u"~~~量体项目模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_MeasureItem(self):
        #进入量体项目
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入量体项目
        testModule(driver,u'基础信息',u'量体项目')
         #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masMeasureHdAccordion > div > div.panel-body.accordion-body  table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(1)
      
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#masMeasureHdToolbar  a.easyui-linkbutton.addPropButton > span > span').click()
   
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#masMeasureHdToolbar   a.easyui-linkbutton.findButton > span > span').click()  
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#masMeasureHdToolbar  a.easyui-linkbutton.editButton > span > span').click()
            sleep(1)
    
            
        elif button==u'导入' or button=='import':
            #点击“导入”按钮
            driver.find_element_by_css_selector('#masMeasureHdToolbar  a.easyui-linkbutton.importPersonButton').click()
            sleep(1)
            
    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#masMeasureHdToolbar  a.easyui-linkbutton.deleteButton > span > span').click()
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
            driver.find_element_by_css_selector('body > div:nth-child(13) > div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.cancelButton.l-btn > span > span').click()
            sleep(0.5)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("body div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.saveButton.l-btn > span > span").click()
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

        
    def test_0add_Item(self):
        u'''添加角色'''
        driver=self.driver
        #进入量体项目
        self.to_MeasureItem()

        #添加
        self.clickButton(u'添加')

        #量体项编码
        global item_code
        strt=time.strftime('%H%M%S',time.localtime(time.time()))
        item_code='ZM'+strt
        code=item_code
        driver.find_element_by_css_selector("#ModifyMeasureHdForm  tr:nth-child(1) > td.easyui-myText > input").send_keys(code)
        sleep(0.5)
        
        #量体项名称
        global item_name
        item_name='Measure'+strt
        name=item_name
        driver.find_element_by_css_selector("#ModifyMeasureHdForm tr:nth-child(2) > td.easyui-myText > input").send_keys(name)
        sleep(0.5)
        
        #描述信息
        info=item_info
        driver.find_element_by_css_selector("#ModifyMeasureHdForm  tr:nth-child(3) > td.easyui-myText > textarea").send_keys(info)
        sleep(0.5)

        #排序
        driver.find_element_by_css_selector("#ModifyMeasureHdForm tr:nth-child(4) > td.easyui-myText > input.easyui-numberbox.validatebox-text").send_keys('1')
        sleep(0.5)
        

        #保存
        self.clickButton(u'保存')

        
        
    def searchbycode(self,code):
        '''按编号查找'''
        driver=self.driver
        #输入编号查找
        driver.find_element_by_css_selector("#masMeasureHdToolbar > input:nth-child(1)").clear()
        sleep(0.5)
        driver.find_element_by_css_selector("#masMeasureHdToolbar > input:nth-child(1)").send_keys(code)
        sleep(0.5)
        #查找
        self.clickButton(u'查找')

        #断言
        cds=driver.find_elements_by_css_selector("#masMeasureHdAccordion > div > div.panel-body.accordion-body  table.datagrid-btable td[field='fdCode']")
        searchAssert(self,cds,code)

        
        
         
    def test_1search_ByItemCode(self):
        u'''按量体项编号查找'''
        driver=self.driver
        #进入量体项目
        self.to_MeasureItem()
        
        #查找
        code=driver.find_element_by_css_selector("#masMeasureHdAccordion > div > div.panel-body.accordion-body  table.datagrid-btable td[field='fdCode']").text
        self.searchbycode(code)

       
    def test_2search_ByItemName(self):
        u'''按量体项名称查找'''
        driver=self.driver
        #进入量体项目
        self.to_MeasureItem()

        #输入要查找的名称
        name=driver.find_element_by_css_selector("#masMeasureHdAccordion > div > div.panel-body.accordion-body  table.datagrid-btable td[field='fdName']").text
        driver.find_element_by_css_selector("#masMeasureHdToolbar > input:nth-child(2)").send_keys(name)
        sleep(0.5)

        #查找
        self.clickButton(u'查找')

        #断言
        nas=driver.find_elements_by_css_selector("#masMeasureHdAccordion > div > div.panel-body.accordion-body  table.datagrid-btable td[field='fdName']")
        searchAssert(self,nas,name)
        
        
        

    def test_3search_ByItemInfo(self):
        u'''按描述信息查找'''
        driver=self.driver
        #进入量体项目
        self.to_MeasureItem()

        #输入要查找的描述信息
        info=item_info
        driver.find_element_by_css_selector("#masMeasureHdToolbar > input:nth-child(3)").send_keys(info)

        #查找
        self.clickButton(u'查找')

        #断言
        infs=driver.find_elements_by_css_selector("#masMeasureHdAccordion > div > div.panel-body.accordion-body  table.datagrid-btable td[field='fdMemo']")
        searchAssert(self,infs,info)

        

    def test_4modify_Item(self):
        u'''修改量体项目'''
        driver=self.driver
        #进入量体项目
        self.to_MeasureItem()

        #查找要修改的量体项目
        code=item_code
        self.searchbycode(code)

        #选择记录
        driver.find_element_by_css_selector("#masMeasureHdAccordion > div > div.panel-body.accordion-body  table.datagrid-btable td[field='ck']").click()

        #修改
        self.clickButton(u"修改")

        #修改项目名称
        name='new_'+item_name
        driver.find_element_by_css_selector("#ModifyMeasureHdForm tr:nth-child(2) > td.easyui-myText > input").clear()
        sleep(0.5)
        driver.find_element_by_css_selector("#ModifyMeasureHdForm tr:nth-child(2) > td.easyui-myText > input").send_keys(name)
        sleep(0.5)
        
        #保存
        self.clickButton(u'保存')
        
        #再次查找
        self.searchbycode(code)
        
        #断言名称与修改是否一致
        self.assertEqual(name,driver.find_element_by_css_selector("#masMeasureHdAccordion > div > div.panel-body.accordion-body  table.datagrid-btable td[field='fdName']").text)

    def test_5delete_Item(self):
        u'''删除量体项目'''
        driver=self.driver
        #进入量体项目
        self.to_MeasureItem()
        
        #查找要删除的量体项目
        code=item_code
        self.searchbycode(code)

        #选择记录
        driver.find_element_by_css_selector("#masMeasureHdAccordion > div > div.panel-body.accordion-body  table.datagrid-btable td[field='ck']").click()

        #删除
        self.clickButton(u'删除')
        

    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    #建立测试集
    log.info('test_EmployeeInfo start--')
    suite=unittest.TestSuite()
    
    #suite.addTest(test_MeasureItem('test_0add_Item'))#添加量体项目
    #suite.addTest(test_MeasureItem('test_1search_ByItemCode'))#按项目编码查找
    #suite.addTest(test_MeasureItem('test_2search_ByItemName'))#按项目名称查找
    #suite.addTest(test_MeasureItem('test_3search_ByItemInfo'))#按描述信息查找
    suite.addTest(test_MeasureItem('test_4modify_Item'))#修改量体项目
    #suite.addTest(test_MeasureItem('test_5delete_Item'))#删除量体项目
    
   
    
    
    #执行测试
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_EmployeeInfo end--')
        
