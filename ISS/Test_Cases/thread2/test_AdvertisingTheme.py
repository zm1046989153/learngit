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

#广告编码
ad_code='ZM_153458'

#状态
ad_state=u"新增"

#广告内容
ad_content=u"广告：广而告之！@#@#￥343"




class test_AdvertisingTheme(unittest.TestCase):
    #广告主题模块测试
    log.info(u"~~~广告主题模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_AdvertisingTheme(self):
        #进入广告主题模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入广告主题
        testModule(driver,u'基础信息',u'广告主题')
        
    
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masAdHdAccordion > div:nth-child(1)  table.datagrid-btable  td[field='ck']")
        
        log.info(u"刷新完成！！！")
       

        sleep(1)
    
    def clickButton(self,button):
        u'''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#masAdHdToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#masAdHdToolbar > a.easyui-linkbutton.findButton > span > span').click()
            sleep(1)

        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#masAdHdToolbar > a.easyui-linkbutton.viewButton > span > span').click()
            sleep(1)

            self.assertEqual(u"编辑",driver.find_element_by_css_selector("#masAdHdForm > div:nth-child(1) > a.easyui-linkbutton.saveButton > span > span > span").text)
            
        elif button==u'编辑' or button=='view':
            #点击“编辑”按钮
            driver.find_element_by_css_selector('#masAdHdForm > div:nth-child(1) > a.easyui-linkbutton.saveButton > span > span > span').click()
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#masAdHdToolbar > a.easyui-linkbutton.editButton > span > span').click()
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

            driver.find_element_by_css_selector("#masAdHdForm > div:nth-child(1) > a.easyui-linkbutton.saveButton > span > span").click()
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

        
    def test_0add_AdvertisingTheme(self):
        u'''添加广告主题'''
        driver=self.driver

        #进入广告主题
        self.to_AdvertisingTheme()

        #添加
        self.clickButton(u'添加')
        
        #广告编码
        global ad_code
        strt=time.strftime("%H%M%S",time.localtime(time.time()))
        ad_code="ZM"+strt
        code=ad_code

        findCss(driver,"#masAdHdForm tr:nth-child(3) > td:nth-child(2) > input").send_keys(code)

        #开始时间、结束时间
        start_time='2016-03-15'
        end_time='2016-03-17'
        findCss(driver,"#masAdHdForm  tr:nth-child(3) > td:nth-child(4) > span > input.combo-text.validatebox-text").send_keys(start_time)
        sleep(0.5)
        findCss(driver,"#masAdHdForm  tr:nth-child(3) > td:nth-child(4) > span > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        sleep(0.5)
        findCss(driver,"#masAdHdForm  tr:nth-child(3) > td:nth-child(6) > span > input.combo-text.validatebox-text").send_keys(end_time)
        sleep(0.5)
        findCss(driver,"#masAdHdForm  tr:nth-child(3) > td:nth-child(6) > span > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        sleep(0.5)

        #状态
        state=u"新增"
        findCss(driver,"#masAdHdForm  tr:nth-child(3) > td:nth-child(8) > span > input.combo-text.validatebox-text").send_keys(state)
        sleep(0.5)
        findCss(driver,"#masAdHdForm  tr:nth-child(3) > td:nth-child(8) > span > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        sleep(0.5)

        #广告内容
        content=ad_content
        findCss(driver,"#masAdHdForm  tr:nth-child(4) > td.easyui-myText > textarea").send_keys(ad_content)
        sleep(0.5)

        #主题
        th=u"主题Theme"
        findCss(driver,"#masAdHdForm tr:nth-child(5) > td:nth-child(2) > input").send_keys(th)

        #保存
        self.clickButton(u"保存")
        
    def timesearchassert(self,start=0,end=0):
        u'''本函数用于对活动时间查找结果进行断言'''
        driver=self.driver
        #读取查找结果的时间
        #活动开始时间
        stps=findsCss(driver,"#masAdHdAccordion > div:nth-child(1)  table.datagrid-btable td[field='timeStart']")
        #活动结束时间
        etps=findsCss(driver,"#masAdHdAccordion > div:nth-child(1)  table.datagrid-btable td[field='timeEnd']")

        start_time=[]
        end_time=[]
        #读取查找出的广告活动开始时间存放在start_time
        for stp in stps:
            st=toTime("%Y-%m-%d %H:%M:%S",stp.text)
            start_time.append(st)
            
        #读取查找出的广告活动结束时间存放在end_time   
        for etp in etps:
            et=toTime("%Y-%m-%d %H:%M:%S",etp.text)
            end_time.append(et)

        #进输入结束时间查找
        if start==0:
            for et in end_time:
                if et <= end:
                    a=True
                else:
                    a=False
                    
        #仅输入开始时间查找
        elif end==0:
            for st in start_time:
                if st >= start:
                    a=True
                else:
                    a=False
                        
        #同时输入开始、结束时间查找       
        else:
            for et in end_time:
                if et <= end:
                    a=True
                else:
                    a=False

            for st in start_time:
                if st >= start:
                    a=True
                else:
                    a=False
         
        return a
                
                

    def test_1search_byTime(self):
        u'''按开始结束时间查找'''
        driver=self.driver

        #进入广告主题
        self.to_AdvertisingTheme()
        start_time='2016-01-15'
        end_time='2016-03-1'
        
        tt1=toTime("%Y-%m-%d",start_time)
        tt2=toTime("%Y-%m-%d",end_time)

        #仅输入开始时间查找
        findCss(driver,"#masAdHdToolbar > span:nth-child(2) > input.combo-text.validatebox-text").send_keys(start_time)
        sleep(0.5)
        
        
        #查找
        self.clickButton(u"查找")

        #断言
        self.assertTrue(self.timesearchassert(tt1,0))
        sleep(5)
        
        #仅输入结束时间查找
        findCss(driver,"#masAdHdToolbar > span:nth-child(2) > input.combo-text.validatebox-text").clear()
        sleep(0.5)
        findCss(driver,"#masAdHdToolbar > span:nth-child(4) > input.combo-text.validatebox-text").clear()
        sleep(0.5)
        findCss(driver,"#masAdHdToolbar > span:nth-child(4) > input.combo-text.validatebox-text").send_keys(end_time)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")

        #断言
        self.assertTrue(self.timesearchassert(0,tt2))
        sleep(5)

        
        #输入开始、结束时间查找
        findCss(driver,"#masAdHdToolbar > span:nth-child(2) > input.combo-text.validatebox-text").clear()
        sleep(0.5)
        findCss(driver,"#masAdHdToolbar > span:nth-child(4) > input.combo-text.validatebox-text").clear()
        sleep(0.5)
        
        findCss(driver,"#masAdHdToolbar > span:nth-child(2) > input.combo-text.validatebox-text").send_keys(start_time)
        sleep(0.5)
        findCss(driver,"#masAdHdToolbar > span:nth-child(4) > input.combo-text.validatebox-text").send_keys(end_time)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")

        #断言
        self.assertTrue(self.timesearchassert(tt1,tt2))



    def test_2search_byState(self):
        u'''按状态查找'''
        driver=self.driver

        #进入广告主题
        self.to_AdvertisingTheme()

        #输入要查找的状态
        state=ad_state
        findCss(driver,"#masAdHdToolbar > span:nth-child(6) > input.combo-text.validatebox-text").send_keys(state)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")

        #断言
        stas=findsCss(driver,"#masAdHdAccordion > div:nth-child(1)  table.datagrid-btable td[field='statusKey']")
        searchAssert(self,stas,state)
        

        
    def test_3view_AdvertisingTheme(self):
        u'''查看广告主题'''
        driver=self.driver

        #进入广告主题
        self.to_AdvertisingTheme()

        #选择一个记录
        findCss(driver,"#masAdHdAccordion > div:nth-child(1)  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #查看
        self.clickButton(u"查看")

        #编辑
        self.clickButton(u"编辑")

        #保存
        self.clickButton(u"保存")

        
        

    def test_4modify_AdvertisingTheme(self):
        u'''修改广告主题'''
        driver=self.driver

        #进入广告主题
        self.to_AdvertisingTheme()
        
        #选择一个记录
        findCss(driver,"#masAdHdAccordion > div:nth-child(1)  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u"修改")

        #修改广告内容
        new_content="NEW_"+ad_content
        findCss(driver,"#masAdHdForm  tr:nth-child(4) > td.easyui-myText > textarea").clear()
        sleep(0.5)
        findCss(driver,"#masAdHdForm  tr:nth-child(4) > td.easyui-myText > textarea").send_keys(new_content)
        sleep(0.5)

        #保存
        self.clickButton(u"保存")

        #断言是否与修改的一致
        self.assertEqual(new_content,findCss(driver,"#masAdHdAccordion > div:nth-child(1)  table.datagrid-btable td[field='context']").text)
         

    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_AdvertisingTheme start--')
    
    suite=unittest.TestSuite()
    
    #suite.addTest(test_AdvertisingTheme('test_0add_AdvertisingTheme'))#添加默认快递
    #suite.addTest(test_AdvertisingTheme('test_1search_byTime'))#按开始结束时间查找
    #suite.addTest(test_AdvertisingTheme('test_2search_byState'))#按状态查找
    #suite.addTest(test_AdvertisingTheme('test_3view_AdvertisingTheme'))#查看广告主题
    suite.addTest(test_AdvertisingTheme('test_4modify_AdvertisingTheme'))#修改广告主题
    
    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()

    
    log.info('test_AdvertisingTheme end--')
        
