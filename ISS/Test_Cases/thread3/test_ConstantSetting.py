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

#常数编码
con_code='ZM_153458'

#常数值
con_value="Value"

#常数说明
con_info=u'ZM常数说明！@￥！@#！54'



class test_ConstantSetting(unittest.TestCase):
    #常数配置模块测试
    log.info(u"~~~常数配置模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_ConstantSetting(self):
        #进入常数配置模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入常数配置
        testModule(driver,u'系统管理',u'常数配置')
        
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmConstantAccordion > div:nth-child(1)  table.datagrid-btable  td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(1)
    
    def clickButton(self,button):
        u'''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmConstantToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmConstantToolbar > a.easyui-linkbutton.findButton > span > span').click()
            sleep(1)

        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#stmConstantToolbar > a.easyui-linkbutton.viewButton > span > span').click()
            sleep(1)

            self.assertEqual(u"编辑",driver.find_element_by_css_selector("#stmConstantForm > div > a.easyui-linkbutton.saveButton > span > span > span").text)
            
        elif button==u'编辑' or button=='view':
            #点击“编辑”按钮
            driver.find_element_by_css_selector('#stmConstantForm > div > a.easyui-linkbutton.saveButton > span > span > span').click()
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmConstantToolbar > a.easyui-linkbutton.editButton > span > span').click()
            sleep(1)
                
    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmConstantToolbar > a.easyui-linkbutton.deleteButton > span').click()
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

            driver.find_element_by_css_selector("#stmConstantForm > div > a.easyui-linkbutton.saveButton > span > span > span").click()
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

        
    def test_0add_Constant(self):
        u'''添加常数'''
        driver=self.driver

        #进入常数配置
        self.to_ConstantSetting()

        #添加
        self.clickButton(u'添加')

        #常数编号
        global con_code
        strt=time.strftime('%H%M%S',time.localtime(time.time()))
        con_code="ZM_"+strt
        code=con_code
        findCss(driver,"#stmConstantForm tr:nth-child(1) > td:nth-child(5) > input").send_keys(code)
        sleep(0.5)

        #常数的值
        global con_value
        con_value="Value_"+strt
        value=con_value
        findCss(driver,"#stmConstantForm  tr:nth-child(1) > td:nth-child(7) > input").send_keys(value)
        sleep(0.5)

        #常数说明
        info=con_info
        findCss(driver,"#stmConstantForm  tr:nth-child(1) > td:nth-child(9) > input").send_keys(info)
        sleep(0.5)

        #保存
        self.clickButton(u"保存")
        

    def searchbycode(self,code):
        '''按编码查找'''
        driver=self.driver

        #输入要查找的编码
        findCss(driver,"#stmConstantToolbar > input:nth-child(1)").clear()
        sleep(0.5)
        findCss(driver,"#stmConstantToolbar > input:nth-child(1)").send_keys(code)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #等待页面刷新
        WebWait(driver,"#stmConstantAccordion > div:nth-child(1) > div.panel-body.accordion-body div.datagrid-mask-msgn")

        #断言
        cds=findsCss(driver,"#stmConstantAccordion > div:nth-child(1) table.datagrid-btable td[field='fdCode']")
        searchAssert(self,cds,code)
        


    def test_1search_byConstantCode(self):
         u'''按常数编号查找'''
 
         driver=self.driver

         #进入常数配置
         self.to_ConstantSetting()

         #输入编号并查找
         code=findCss(driver,"#stmConstantAccordion > div:nth-child(1) table.datagrid-btable td[field='fdCode']").text
         self.searchbycode(code)

    def test_2search_byConstantInfo(self):
         u'''按常数说明查找'''

         driver=self.driver

         #进入常数配置
         self.to_ConstantSetting()

         #输入常数说明查找
         info=findCss(driver,"#stmConstantAccordion > div:nth-child(1) table.datagrid-btable td[field='fdDesc']").text
         findCss(driver,"#stmConstantToolbar > input:nth-child(2)").send_keys(info)
         sleep(0.5)
         
         #查找
         self.clickButton(u'查找')

         #断言
         ifns=findsCss(driver,"#stmConstantAccordion > div:nth-child(1) table.datagrid-btable td[field='fdDesc']")
         searchAssert(self,ifns,info)


    def test_3view_Constant(self):
         u'''查看常数'''

         driver=self.driver

         #进入常数配置
         self.to_ConstantSetting()

         sleep(0.5)

         #选择一条记录
         findCss(driver,"#stmConstantAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
         sleep(0.5)

         #查看
         self.clickButton(u"查看")

         #编辑
         self.clickButton(u"编辑")
         
         #保存
         self.clickButton(u"保存")
         

         
         

    def test_4modify_Constant(self):
         u'''修改常数'''

         driver=self.driver

         #进入常数配置
         self.to_ConstantSetting()

         #查找
         code=con_code
         self.searchbycode(code)

         #选择一条记录
         findCss(driver,"#stmConstantAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
         sleep(0.5)

         #修改
         self.clickButton(u"修改")

         #修改常数值
         new_value="NEW_"+con_value

         findCss(driver,"#stmConstantForm  tr:nth-child(1) > td:nth-child(7) > input").clear()
         sleep(0.5)
         findCss(driver,"#stmConstantForm  tr:nth-child(1) > td:nth-child(7) > input").send_keys(new_value)
         sleep(0.5)

         #保存
         self.clickButton(u"保存")

         #再次查找
         self.searchbycode(code)

         #断言
         eds=findsCss(driver,"#stmConstantAccordion > div:nth-child(1) table.datagrid-btable td[field='fdConstantValue']")
         searchAssert(self,eds,new_value)
         

         

         

   

    def test_5delete_Constant(self):
        u'''删除常数'''

        driver=self.driver

        #进入常数配置
        self.to_ConstantSetting()

        #查找
        code=con_code
        self.searchbycode(code)

        #选择一条记录
        findCss(driver,"#stmConstantAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #删除
        self.clickButton(u"删除")



    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_ConstantSetting start--')
    
    suite=unittest.TestSuite()
    
    #suite.addTest(test_ConstantSetting('test_0add_Constant'))#添加常数
    
    #suite.addTest(test_ConstantSetting('test_1search_byConstantCode'))#按常数编码查找
    #suite.addTest(test_ConstantSetting('test_2search_byConstantInfo'))#按常数说明查找
    
    #suite.addTest(test_ConstantSetting('test_3view_Constant'))#查看常数
    
    suite.addTest(test_ConstantSetting('test_4modify_Constant'))#修改常数
    
    #suite.addTest(test_ConstantSetting('test_5delete_Constant'))#删除常数
    
   
    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_ConstantSetting end--')
        
