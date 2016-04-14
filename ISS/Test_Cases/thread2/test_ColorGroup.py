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

#颜色组编码
cgroup_code='MM'

#颜色组名称
cgroup_name='ZZ'


class test_ColorGroup(unittest.TestCase):
    #颜色组模块测试
    log.info(u"~~~颜色组模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_ColorGroup(self):
        #进入颜色组配置模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入颜色组配置
        testModule(driver,u'基础信息',u'颜色组配置')
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmColorGroupHd table td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(1)
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmColorGroupHdToolbar > div:nth-child(4) > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmColorGroupHdToolbar > div:nth-child(4) > a.easyui-linkbutton.findButton > span > span').click()
            WebWait(driver,"#stmColorGroupHd > div > div > div > div.datagrid-mask")
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmColorGroupHdToolbar > div:nth-child(4) > a.easyui-linkbutton.editButton > span > span').click()
            sleep(1)
    
            
        elif button==u'导入' or button=='import':
            #点击“导入”按钮
            driver.find_element_by_css_selector('#stmColorGroupHdToolbar > div:nth-child(4) > a.easyui-linkbutton.importButton > span > span').click()
            sleep(1)
            
            
            
        elif button==u'编辑' or button=='edit':
            #点击“编辑”按钮
            driver.find_element_by_css_selector("#masPartDtSkuForm > div > a.easyui-linkbutton.saveButton > span > span > span").click()
            sleep(1)
            
    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmColorGroupHdToolbar  a.easyui-linkbutton.deleteButton > span > span').click()
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
            driver.find_element_by_css_selector('#masPartDtSkuForm > div > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            #取消
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            
            sleep(1)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("body div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.saveButton> span").click()
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

        
    def test_0add_ColorGroup(self):
        u'''添加颜色组'''

        log.info(u"开始执行测试...")
        driver=self.driver
        #进入颜色组配置
        self.to_ColorGroup()

        #点击添加
        self.clickButton(u'添加')

        try:
            driver.find_element_by_css_selector("#ModifyColorGroupForm > div.right div.datagrid-header > div > table > tbody > tr > td:nth-child(1) > div > input[type='checkbox']").click()
        except:
            log.error(u"页面未刷新")
            raise NameError(u"页面未刷新")
        sleep(0.5)

        #颜色组编码
        global cgroup_code
        strt=time.strftime("%H%M%S",time.localtime(time.time()))
        cgroup_code='ZM'+strt
        code=cgroup_code
        driver.find_element_by_css_selector("#groupCode").send_keys(code)

        #颜色组名称
        global cgroup_name
        cgroup_name=u'ZM组'+strt
        name=cgroup_name
        driver.find_element_by_css_selector("#ModifyColorGroupForm  tr > td:nth-child(12) > input").send_keys(name)

        #选择颜色
        driver.find_element_by_css_selector("#ModifyColorGroupForm > div.left div.datagrid-body > table td[field='ck']").click()

        #右移
        driver.find_element_by_css_selector("#rightButton").click()

        #保存
        self.clickButton(u'保存')

        
    def searchbycode(self,code):
        '''按编号查找'''

        driver=self.driver
        
        #输入要查找的编号
        driver.find_element_by_css_selector("#stmColorGroupHdToolbar > div:nth-child(3) > span:nth-child(2) > input").clear()
        sleep(0.5)
        driver.find_element_by_css_selector("#stmColorGroupHdToolbar > div:nth-child(3) > span:nth-child(2) > input").send_keys(code)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #断言
        cds=driver.find_elements_by_css_selector("#stmColorGroupHd  table.datagrid-btable td[field='fdCode']")
        searchAssert(self,cds,code)
        
         
    def test_1search_ByCGroupCode(self):
        u'''按颜色组编码查找'''
        driver=self.driver
        
        #进入颜色组配置
        self.to_ColorGroup()
        
        #输入要查找的编号
        code=driver.find_element_by_css_selector("#stmColorGroupHd  table.datagrid-btable td[field='fdCode']").text
        
        #调用函数查找
        self.searchbycode(code)
        
        


    def test_2search_ByCGroupName(self):
        u'''按颜色组名称查找'''

        log.info(u"开始执行测试...")
        
        driver=self.driver
        
        #进入颜色组配置
        self.to_ColorGroup()

        #输入要查找的颜色组名称
        name=driver.find_element_by_css_selector("#stmColorGroupHd  table.datagrid-btable td[field='fdName']").text
        driver.find_element_by_css_selector("#stmColorGroupHdToolbar > div:nth-child(3) > span:nth-child(4) > input").send_keys(name)
        sleep(0.5)

        #点击查找
        self.clickButton(u'查找')

        #断言
        nas=driver.find_elements_by_css_selector("#stmColorGroupHd  table.datagrid-btable td[field='fdName']")
        searchAssert(self,nas,name)
        
    


    def test_3modify_ColorGroup(self):
        u'''修改颜色组'''

        log.info(u"开始执行测试...")
        driver=self.driver
        #进入颜色组配置
        self.to_ColorGroup()

        #查找要修改的颜色组
        code=cgroup_code
        self.searchbycode(code)
        
        #选择要修改的记录
        driver.find_element_by_css_selector("#stmColorGroupHd  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u'修改')

        #左移选择的颜色
        try:
            driver.find_element_by_css_selector("#ModifyColorGroupForm > div.left div.datagrid-body > table td[field='ck']").click()
        except:
            log.error(u"页面未刷新")
            raise NameError(u"页面未刷新")
        sleep(0.5)

        driver.find_element_by_css_selector("#ModifyColorGroupForm > div.right div.datagrid-header > div > table > tbody > tr > td:nth-child(1) > div > input[type='checkbox']").click()
        sleep(0.5)
        
        #左移
        driver.find_element_by_css_selector("#leftButton").click()

        #保存
        self.clickButton(u'保存')
        
        

    def test_4import_ColorGroup(self):
        u'''导入颜色组'''

        log.info(u"开始执行测试...")
        driver=self.driver
        #进入颜色组配置
        self.to_ColorGroup()

        #导入
        self.clickButton(u"导入")
        
        
        
    def test_5delete_ColorGroup(self):
        u'''删除颜色组'''
        driver=self.driver
        #进入颜色组配置
        self.to_ColorGroup()

        #查找要删除的颜色组
        code=cgroup_code
        self.searchbycode(code)
        sleep(1)
        
        #选择要删除的记录
        driver.find_element_by_css_selector("#stmColorGroupHd  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

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
    
    #suite.addTest(test_ColorGroup('test_0add_ColorGroup'))#添加颜色组
    #suite.addTest(test_ColorGroup('test_1search_ByCGroupCode'))#按颜色组编号查找
    #suite.addTest(test_ColorGroup('test_2search_ByCGroupName'))#按颜色组名称查找
    suite.addTest(test_ColorGroup('test_3modify_ColorGroup'))#修改颜色组
    #suite.addTest(test_ColorGroup('test_4import_ColorGroup'))#导入颜色组
    #suite.addTest(test_ColorGroup('test_5delete_ColorGroup'))#删除颜色组
   
    #执行测试
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_EmployeeInfo end--')
        
