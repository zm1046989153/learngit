# _*_ coding=utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

#角色编码
role_code='ZM_role'

#角色名称
role_name='ZM_ATRole'

#描述信息
role_info=u'这是一个角色ZZ（自动化）！！@#%￥'

class test_RoleInfo(unittest.TestCase):
    #商品类别模块测试
    log.info(u"~~~商品类别模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_RoleInfo(self):
        #进入角色信息模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入角色信息
        testModule(driver,u'系统管理',u'角色信息')
                   
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#content table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
       
        sleep(1)
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmRoleToolbar a.easyui-linkbutton.addButton').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmRoleToolbar  a.easyui-linkbutton.findButton').click()
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmRoleToolbar  a.easyui-linkbutton.editButton').click()
            sleep(1)
    
            
        elif button==u'导入' or button=='import':
            #点击“导入”按钮
            driver.find_element_by_css_selector('#stmRoleToolbar  a.easyui-linkbutton.importPersonButton').click()
            sleep(1)
            
    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmRoleToolbar  a.easyui-linkbutton.deleteButton').click()
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
            driver.find_element_by_css_selector('#stmMenuItemLayout > div.panel.layout-panel.layout-panel-south.layout-split-south > div > div:nth-child(2) > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("#stmMenuItemLayout > div.panel.layout-panel.layout-panel-south.layout-split-south > div > div:nth-child(2) > a.easyui-linkbutton.saveButton > span").click()
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

        
    def test_0add_Role(self):
        u'''添加角色'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入角色信息
        self.to_RoleInfo()

        #添加
        self.clickButton(u'添加')

        #勾选菜单权限
        driver.find_element_by_css_selector("#stmMenuItemTreeRole_2_check").click()
        sleep(0.5)

        #角色编号
        global role_code
        strt=time.strftime('%H%M%S',time.localtime(time.time()))
        role_code='ZM_role'+strt
        code=role_code
        driver.find_element_by_css_selector("#ModifystmMenuItemForm tr:nth-child(1) > td:nth-child(4) > input").send_keys(code)
        sleep(0.5)
        
        #角色名称
        name=role_name
        driver.find_element_by_css_selector("#ModifystmMenuItemForm tr:nth-child(1) > td:nth-child(6) > input").send_keys(name)
        sleep(0.5)
        
        #描述信息
        info=role_info
        driver.find_element_by_css_selector("#ModifystmMenuItemForm tr:nth-child(2) > td:nth-child(4) > textarea").send_keys(info)
        sleep(0.5)

        #保存
        self.clickButton(u'保存')
        
        
        
        
    def searchbycode(self,code):
        '''按编号查找'''
        driver=self.driver
        driver.find_element_by_css_selector("#stmRoleToolbar > input:nth-child(1)").clear()
        sleep(0.5)
        #输入编号
        driver.find_element_by_css_selector("#stmRoleToolbar > input:nth-child(1)").send_keys(code)
        sleep(0.5)

        #点击查找
        self.clickButton(u'查找')

                   

        #断言
        cds=driver.find_elements_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='fdCode']")
        searchAssert(self,cds,code)
        
        
         
    def test_1search_ByRoleCode(self):
        u'''按角色编号查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入角色信息
        self.to_RoleInfo()

        #获取全部记录数
        a1=driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) div.datagrid-pager.pagination > div.pagination-info").text
        #print a1
        #调用函数查找角色
        code=driver.find_element_by_css_selector("#content table.datagrid-btable td[field='fdCode']").text
        self.searchbycode(code)

        #清空输入内容，查找
        cip=driver.find_element_by_css_selector("#stmRoleToolbar > input:nth-child(1)")
        cip.clear()
        sleep(0.5)

        #查找
        self.clickButton(u'查找')
                   
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#content > div.tabs-panels.tabs-panels-noborder table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        
        
        #断言是否查找出全部记录
        a2=driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder  div.datagrid-pager.pagination > div.pagination-info").text
        self.assertEqual(a1,a2)
        
        
    def test_2search_ByRoleName(self):
        u'''按角色名称查找'''
        log.info(u"开始执行用例...")

        
        driver=self.driver
        #进入角色信息
        self.to_RoleInfo()
        
        #输入要查找的角色名称
        name=driver.find_element_by_css_selector("#content table.datagrid-btable td[field='fdName']").text
        sleep(0.5)
        driver.find_element_by_css_selector("#stmRoleToolbar > input:nth-child(2)").send_keys(name)
        sleep(0.5)

        #查找
        self.clickButton(u'查找')
    
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#content table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        
        #断言
        nas=driver.find_elements_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='fdName']")
        searchAssert(self,nas,name)
        
        

    def test_3search_ByRoleState(self):
        u'''按角色状态查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入角色信息
        self.to_RoleInfo()

        #选择要查找的角色状态
        st=driver.find_element_by_css_selector("#stmRoleToolbar > span > input.combo-text.validatebox-text")

        states=[u'启用',u'禁用']
        for state in states:
            #print state
            st.clear()
            sleep(0.5)
            st.send_keys(state)
            sleep(0.5)
            
            #查找
            self.clickButton(u'查找')
        
            #断言
            stas=driver.find_elements_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='fdIsValid']")
            searchAssert(self,stas,state)

        
        
    def test_4search_byRoleInfo(self):
        u'''按描述信息查找'''
        log.info(u"开始执行用例...")

        
        driver=self.driver
        #进入角色信息
        self.to_RoleInfo()

        #输入要查找的描述信息
        info=role_info
        driver.find_element_by_css_selector("#stmRoleToolbar > input:nth-child(5)").send_keys(info)

        #查找
        self.clickButton(u'查找')

                   
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#content table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")

        #断言
        inps=driver.find_elements_by_css_selector("#content  table.datagrid-btable td[field='fdMemo']")
        searchAssert(self,inps,info)

    def test_5modify_Role(self):
        u'''修改角色'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入角色信息
        self.to_RoleInfo()

        #查找
        code=role_code
        self.searchbycode(code)
                   
        #选择记录
        driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='ck']").click()

        #修改
        self.clickButton(u'修改')

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmMenuItem > div > div > div > div.datagrid-view2 > div.datagrid-header > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > div > input[type='checkbox']")
        log.info(u"刷新完成！！！")
    
        sleep(0.5)

        #修改描述信息
        driver.find_element_by_css_selector("#ModifystmMenuItemForm > table > tbody > tr:nth-child(2) > td:nth-child(4) > textarea").clear()
        sleep(0.5)
        
        new_info=u"NEW_描述信息！@￥#￥%"
        driver.find_element_by_css_selector("#ModifystmMenuItemForm > table > tbody > tr:nth-child(2) > td:nth-child(4) > textarea").send_keys(new_info)
        sleep(0.5)

        #保存
        self.clickButton(u'保存')

        #刷新界面
        ActionChains(driver)
        

        #再次查找
        self.searchbycode(code)
        
        #断言‘描述信息’是否与修改的一致
        self.assertEqual(new_info,driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='fdMemo']").text)
        

    def test_6delete_Role(self):
        u'''删除角色'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入角色信息
        self.to_RoleInfo()

        #查找
        code=role_code
        self.searchbycode(code)
                   
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#content table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        

        #选择记录
        driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='ck']").click()
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
    
    suite.addTest(test_RoleInfo('test_0add_Role'))#添加员工
    #suite.addTest(test_RoleInfo('test_1search_ByRoleCode'))#按角色编号查找
    #suite.addTest(test_RoleInfo('test_2search_ByRoleName'))#按角色名称查找
    #suite.addTest(test_RoleInfo('test_3search_ByRoleState'))#按角色状态查找
    #suite.addTest(test_RoleInfo('test_4search_byRoleInfo'))#按描述信息查找
    suite.addTest(test_RoleInfo('test_5modify_Role'))#修改角色信息
    #suite.addTest(test_RoleInfo('test_6delete_Role'))#删除角色信息

    
    
    #执行测试
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_EmployeeInfo end--')
        
