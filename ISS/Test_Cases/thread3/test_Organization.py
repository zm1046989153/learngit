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

#组织编码
org_code='ZM160159'

#组织名称
org_name=u'Atest启尚科技'



class test_Organization(unittest.TestCase):
    log.info(u"~~~销售组织管理模块测试~~~")
    #销售组织管理模块测试
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_Organization(self):
        #销售组织管理模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入销售组织管理
        testModule(driver,u'系统管理',u'销售组织管理')
        
      
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmDptAccordion table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(1)
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmDptToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmDptToolbar > a.easyui-linkbutton.findButton > span > span').click()
            WebWait(driver,"#stmDptAccordion > div > div > div.datagrid-mask")
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmDptToolbar > a.easyui-linkbutton.editButton > span > span').click()
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

            driver.find_element_by_css_selector("body div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.saveButton.l-btn > span > span").click()
            sleep(0.5)
            
             #获取断言信息
            
            success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)")
            tip_text=success.text
            
            #print tip_text
            log.info(tip_text)
            
            #确定,关闭提示框
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

            #断言是否保存成功
            self.assertEqual(u"保存成功！",tip_text)
            
        else:
            raise NameError('No Such Button,confirm again please')

        
    def test_0add_Organization(self):
        u'''添加销售组织'''
        
        driver=self.driver
        
        #进入销售组织管理模块
        self.to_Organization()

        #添加
        self.clickButton(u'添加')

        #组织编号
        global org_code
        strt=time.strftime("%H%M%S",time.localtime(time.time()))
        org_code='ZM'+strt
        code=org_code
        findCss(driver,"#ModifyDptForm  tr:nth-child(2) > td:nth-child(2) > input").send_keys(code)
        sleep(0.5)
        
        #组织名称
        name=org_name
        findCss(driver,"#ModifyDptForm  tr:nth-child(2) > td:nth-child(4) > input").send_keys(name)
        sleep(0.5)
        
        #组织类型
        findCss(driver,"#ModifyDptForm  tr:nth-child(3) > td:nth-child(2) > span > input.combo-text.validatebox-text").send_keys(u"终端")
        sleep(0.5)
        findCss(driver,"#ModifyDptForm  tr:nth-child(3) > td:nth-child(2) > span > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        sleep(0.5)
        
        #经营性质
        findCss(driver,"#ModifyDptForm  tr:nth-child(3) > td:nth-child(4) > span > input.combo-text.validatebox-text.validatebox-invalid").send_keys(u"直营")
        sleep(0.5)
        #findCss(driver,"#ModifyDptForm  tr:nth-child(3) > td:nth-child(4) > span > input.combo-text.validatebox-text.validatebox-invalid").send_keys(Keys.ENTER)
        #sleep(0.5)
        
        #所属地区
        
        findCss(driver,"#ModifyDptForm  tr:nth-child(4) > td:nth-child(2) > span > input").click()
        sleep(1)
        try:
            
            findCss(driver,"ul.ztree.destinationTree li:nth-child(1) > ul.level0 > li:nth-child(1) > a > span:nth-child(2)").click()
            sleep(0.5)
            
        except:
            #所属地区选择界面无法刷新时，退出界面重新进入
            #点击取消
            findCss(driver,"body div.panel-body.panel-body-noborder.window-body.panel-noscroll  div.panel.layout-panel.layout-panel-center div.panel.layout-panel.layout-panel-south > div > a.easyui-linkbutton.cancelButton > span > span").click()
            sleep(0.5)
            #确定
            findCss(driver,"body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
      
            #再次进入地区选择界面
            findCss(driver,"#ModifyDptForm  tr:nth-child(4) > td:nth-child(2) > span > input").click()
            sleep(1)
            
            #判断页面是否刷新
            log.info(u"等待页面刷新···")
            isRefreshed(driver,"ul.ztree.destinationTree li:nth-child(1) > ul.level0 > li:nth-child(1) > a > span:nth-child(2)")
        
            log.info(u"刷新完成！！！")

            findCss(driver,"ul.ztree.destinationTree li:nth-child(1) > ul.level0 > li:nth-child(1) > a > span:nth-child(2)").click()
            sleep(0.5)
            
        findCss(driver,"body div.panel-body.panel-body-noborder.window-body.panel-noscroll > div > div.panel.layout-panel.layout-panel-center table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
         

        #选择
        findCss(driver,"body  div.panel-body.panel-body-noborder.window-body.panel-noscroll > div > div.panel.layout-panel.layout-panel-center  a.easyui-linkbutton.saveButton> span > span > span").click()
    
        
        #地址
        ad=u"厦门软件园"
        findCss(driver,"#ModifyDptForm  tr:nth-child(4) > td:nth-child(4) > input").send_keys(ad)
        sleep(0.5)
        
        #负责人
        findCss(driver,"#ModifyDptForm  tr:nth-child(6) > td:nth-child(2) > input").send_keys(u"张三")
        sleep(0.5)
        
        #手机号码
        phone='18350394564'
        findCss(driver,"#ModifyDptForm  tr:nth-child(6) > td:nth-child(4) > input").send_keys(phone)
        sleep(0.5)
        
        #默认快递
        xp=findCss(driver,"#ModifyDptForm tr:nth-child(7) > td:nth-child(2) > span > input.combo-text.validatebox-text.validatebox-invalid")
        xp.click()
        sleep(0.5)
        xp.send_keys(Keys.DOWN)
        sleep(0.5)
        xp.send_keys(Keys.ENTER)
        sleep(0.5)
        
        #保存
        self.clickButton(u"保存")


    def searchbycode(self,code):
        '''按编号查找'''
        driver=self.driver

        findCss(driver,"#stmDptToolbar > input:nth-child(1)").clear()
        sleep(0.5)

        #输入要查找的编号
        findCss(driver,"#stmDptToolbar > input:nth-child(1)").send_keys(code)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        sleep(3)

        #断言
        cds=findsCss(driver,"#stmDptAccordion table.datagrid-btable td[field='fdCode']")
        searchAssert(self,cds,code)

        
    def test_1search_byOrgCode(self):
        u'''按组织编号查找'''
        
        driver=self.driver
        
        #进入销售组织管理模块
        self.to_Organization()

        #输入编号查找
        code=findCss(driver,"#stmDptAccordion table.datagrid-btable td[field='fdCode']").text
        self.searchbycode(code)
        

    def test_2search_byOrgName(self):
        u'''按组织名称查找'''
        
        driver=self.driver
        
        #进入销售组织管理模块
        self.to_Organization()

        #输入要查找的名称
        name=findCss(driver,"#stmDptAccordion table.datagrid-btable td[field='fdName']").text
        findCss(driver,"#stmDptToolbar > input:nth-child(2)").send_keys(name)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #断言
        nas=findsCss(driver,"#stmDptAccordion table.datagrid-btable td[field='fdName']")

        searchAssert(self,nas,name)
        

    def test_3modify_Organization(self):
        u'''修改销售组织'''
        
        driver=self.driver
        
        #进入销售组织管理模块
        self.to_Organization()
        
        #查找要修改的记录
        code=org_code
        self.searchbycode(code)

        #选择记录
        findCss(driver,"#stmDptAccordion table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u"修改")

        #修改组织名称
        name='NEW_'+org_name
        findCss(driver,"#ModifyDptForm > table > tbody > tr:nth-child(2) > td:nth-child(4) > input").clear()
        sleep(0.5)
        findCss(driver,"#ModifyDptForm > table > tbody > tr:nth-child(2) > td:nth-child(4) > input").send_keys(name)
        sleep(0.5)

        #保存
        self.clickButton(u"保存")

        #再次查找
        self.searchbycode(code)

        #断言是否与修改一致
        nas=findsCss(driver,"#stmDptAccordion table.datagrid-btable td[field='fdName']")
        searchAssert(self,nas,name)
        

    def test_4delete_Organization(self):
        u'''删除销售组织'''
        
        driver=self.driver
        
        #进入销售组织管理模块
        self.to_Organization()

         #查找要删除的记录
        code=org_code
        self.searchbycode(code)

        #选择记录
        findCss(driver,"#stmDptAccordion table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #删除
        self.clickButton(u"删除")
     

    
    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_Organization start--')
    suite=unittest.TestSuite()
    
    suite.addTest(test_Organization('test_0add_Organization'))#添加销售组织
    #suite.addTest(test_Organization('test_1search_byOrgCode'))#按销售组织编号查找
    #suite.addTest(test_Organization('test_2search_byOrgName'))#按销售组织名称查找
    #suite.addTest(test_Organization('test_3modify_Organization'))#修改销售组织
    #suite.addTest(test_Organization('test_4delete_Organization'))#删除销售组织


    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_Organization end--')
        
