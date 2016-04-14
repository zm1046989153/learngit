# _*_ coding=utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

#员工编码
empl_code='ZM102113'

#员工名称
empl_name='ZM_ATest'

#联系电话

phone='15980912011'


#登录帐号
strt=time.strftime('%H%M%S',time.localtime(time.time()))
account='ZMC163331'

#岗位名称
position=u"导购员"



class test_EmployeeInfo(unittest.TestCase):
    #人员信息模块测试
    log.info(u"~~~人员信息模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_EmployeeInformation(self):
        #进入人员信息模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入人员信息
        testModule(driver,u'系统管理',u'人员信息')
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='ck']")
     
        log.info(u"刷新完成！！！")
        sleep(1)
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmPersonHdToolbar  a.easyui-linkbutton.addPersonButton').click()
           
            sleep(1)
            
            
            
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmPersonHdToolbar  a.easyui-linkbutton.findPersonButton').click()
            WebWait(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) > div > div > div.panel.layout-panel.layout-panel-center div.datagrid-mask-msg")
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmPersonHdToolbar  a.easyui-linkbutton.editButton').click()
            sleep(1)
            

        elif button==u'登录密码重置' or button=='import':
            #点击“登录密码重置”按钮
            driver.find_element_by_css_selector('#stmPersonHdToolbar  a.easyui-linkbutton.resetPwd').click()
            sleep(1)

            
        elif button==u'角色分配' or button=='import':
            #点击“角色分配”按钮
            driver.find_element_by_css_selector('#stmPersonHdToolbar  a.easyui-linkbutton.prvlgAvg').click()
            sleep(1)
            
        elif button==u'门店分配' or button=='import':
            #点击“门店分配”按钮
            driver.find_element_by_css_selector('#stmPersonHdToolbar  a.easyui-linkbutton.dataPrvlg').click()
            sleep(1)

        elif button==u'复制' or button=='import':
            #点击“复制”按钮
            driver.find_element_by_css_selector('#stmPersonHdToolbar  a.easyui-linkbutton.copy').click()
            sleep(1)
            
        elif button==u'导入' or button=='import':
            #点击“导入”按钮
            driver.find_element_by_css_selector('#stmPersonHdToolbar  a.easyui-linkbutton.importPersonButton').click()
            sleep(1)
            
    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmPersonHdToolbar  a.easyui-linkbutton.deleteButton').click()
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
            driver.find_element_by_css_selector('body div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.cancelButton> span > span').click()
            sleep(0.5)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮
            driver.find_element_by_css_selector('#stmPersonHdTForm > div > a.easyui-linkbutton.saveButton.l-btn.l-btn-plain > span > span').click()
            
            sleep(1)
            
            #获取断言信息
            
            success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
            tip_text=success.text
            #print tip_text
            log.info(tip_text)
            #截图断言信息
            screenshot(driver,u'人员信息保存')
            
            #确定,关闭提示框
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

            #断言是否保存成功
            self.assertEqual(u"保存成功！",tip_text)

           
            
        
        else:
            raise NameError('No Such Button,confirm again please')
        
    def login_NewEmployee(self,username,password='123456',a=True):
        
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.get(self.base_url)
        
        #新用户登录
        driver.find_element_by_css_selector("#loginForm > div:nth-child(1) > input[name='stmUserPwd.fdName']").send_keys(username)
        sleep(0.5)
        driver.find_element_by_css_selector("#loginForm > div:nth-child(2) > input[name='stmUserPwd.fdPassword']").send_keys(password)
        sleep(0.5)
        #print driver.find_element_by_css_selector("#showMsg").text
        
        driver.find_element_by_xpath(".//*[@id='buttonLogin']").click()
        sleep(0.5)
        

        #首次登录
       
        
        msg=driver.find_element_by_css_selector("#showMsg").text
        sleep(0.5)

        #首次登陆,更改密码
        if msg==u"首次登录，请修改密码！" or msg==u'请输入新密码':            
            #填写新密码
            new_passwd='qs8888'
            driver.find_element_by_css_selector("#new > input[name='fdNewPassword']").send_keys(new_passwd)
            sleep(0.5)
            #确认密码
            driver.find_element_by_css_selector("#retype > input[name='fdRePassword']").send_keys(new_passwd)
            sleep(0.5)
            #点击修改
            driver.find_element_by_css_selector("#buttonLogin > span > span").click()
            sleep(1)
            password=new_passwd

        else:
            pass


        #断言是否进入系统
        sleep(1)
        #print driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div > div > div > h5").text
        self.assertEqual(u'欢迎使用',driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div > div > div > h5").text)
        
        driver.close()
        sleep(0.5)
        driver.quit()

        
    def test_01add_Employee(self):
        u'''添加人员'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()
        
        #点击添加按钮，进入添加界面
        self.clickButton(u'添加')
        #driver.find_element_by_xpath("//*[@id='stmPersonHdToolbar']/div[2]/a[2]/span/span[text()=u'添加']")        

        #员工编号
        #strt=time.strftime('%H%M%S',time.localtime(time.time()))
        global empl_code
        empl_code='ZM'+strt
        driver.find_element_by_css_selector("#stmPersonHdTForm  tr:nth-child(1) > td:nth-child(9) > input").send_keys(empl_code)
        sleep(0.5)

        #员工名称
        driver.find_element_by_css_selector("#stmPersonHdTForm tr:nth-child(1) > td:nth-child(11) > input").send_keys(empl_name)

        #手机号码
        global phone
        pr=random.randint(10000,99999)
        phone='183502'+str(pr)
        driver.find_element_by_css_selector("#stmPersonHdTForm  tr:nth-child(1) > td.easyui-numberbox.validatebox-text > input").send_keys(phone)

        #登录帐号
        global account
        account='ZMC'+strt
        driver.find_element_by_css_selector("#stmPersonHdTForm  tr:nth-child(1) > td:nth-child(16) > input").send_keys(account)
        

        #所在区域
        driver.find_element_by_css_selector("#stmPersonHdTForm tr:nth-child(2) > td:nth-child(4) > span > input.combo-text.validatebox-text").click()
        sleep(1)
       
        
       
        #左侧菜单树点击选择地区范围
        #print findCss(driver,"body  div.panel-body.panel-body-noborder.window-body.panel-noscroll  div.panel.layout-panel.layout-panel-west > div.panel-header.panel-header-noborder > div.panel-title").text
        try:
            
            driver.find_element_by_css_selector("body div.panel-body.panel-body-noborder.window-body.panel-noscroll  div.content_wrap > div.zTreeDemoBackground.left > ul.ztree.destinationTree > li > a>span:nth-child(2)").click()

        except:
            #界面未刷新，点击取消按钮，再次进入区域选择界面
            #取消
            findCss(driver,"body  div.panel-body.panel-body-noborder.window-body.panel-noscroll > div > div.panel.layout-panel.layout-panel-center div.panel.layout-panel.layout-panel-south > div > a.easyui-linkbutton.cancelButton > span > span").click()
            sleep(0.5)
            #确定
            findCss(driver,"body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            #所在区域
            driver.find_element_by_css_selector("#stmPersonHdTForm tr:nth-child(2) > td:nth-child(4) > span > input.combo-text.validatebox-text").click()
            sleep(1)
            #选择区域范围
            driver.find_element_by_css_selector("body div.panel-body.panel-body-noborder.window-body.panel-noscroll  div.content_wrap > div.zTreeDemoBackground.left > ul.ztree.destinationTree > li > a>span:nth-child(2)").click()

        sleep(0.5)

        #点击选择地区
        driver.find_element_by_css_selector("body  div.panel-body.panel-body-noborder.window-body.panel-noscroll  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #保存
        driver.find_element_by_css_selector("body div.panel-body.panel-body-noborder.window-body.panel-noscroll a.easyui-linkbutton.saveButton.l-btn.l-btn-plain").click()
       
        sleep(0.5)

        #性别
        sexbt=driver.find_element_by_css_selector("#stmPersonHdTForm tr:nth-child(2) > td:nth-child(6) > span > input.combo-text.validatebox-text")
        sexbt.click()
        sleep(0.3)
        sexbt.send_keys(Keys.DOWN)
        sleep(0.3)
        sexbt.send_keys(Keys.ENTER)
        sleep(0.5)
        
        #在岗状态
        stbt=driver.find_element_by_css_selector("#stmPersonHdTForm tr:nth-child(2) > td.easyui-myText > span > input.combo-text.validatebox-text.validatebox-invalid")
        stbt.click()
        sleep(0.3)
        stbt.send_keys(Keys.DOWN)#在岗
        sleep(0.3)
        stbt.send_keys(Keys.ENTER)
        sleep(0.5)
        

        #岗位名称
        driver.find_element_by_css_selector("#stmPersonHdTForm tr:nth-child(3) > td:nth-child(2) > span > input.combo-text.validatebox-text.validatebox-invalid").click()
        
        psts=driver.find_elements_by_css_selector("body > div:nth-child(18) > div div.combobox-item")
        n=0
       
        for pst in psts:
            #print pst.text
            n+=1
            if pst.text==position:
                driver.find_element_by_css_selector("body > div:nth-child(18) > div > div:nth-child("+str(n)+")").click()
                break
            
        #角色分配
        driver.find_element_by_css_selector("#stmPersonRoleLeft table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        #左移
        driver.find_element_by_css_selector("#rightStmPersonRoleButton").click()
        sleep(0.5)

        #门店分配
        
        #进入门店分配界面
        driver.find_element_by_link_text(u"门店分配").click()
        sleep(0.5)

        #选择一个门店
        driver.find_element_by_css_selector("#stmPersonDataPrvlgLeft div.datagrid-body > table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #左移
        driver.find_element_by_css_selector("#stmPersonDataPrvlgRightButton").click()
        sleep(0.5)

        #保存
        self.clickButton(u'保存')

        #新用户登录
        self.login_NewEmployee(account)
     
        
    def test_02add_EmployeeCopy(self):
        u'''员工复制添加'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()
        
        sleep(1)
        
        #选择员工
        driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #复制
        self.clickButton(u'复制')
        
        #员工编号
        
        strt=time.strftime('%H%M%S',time.localtime(time.time()))
        cempl_code='ZM'+strt
        driver.find_element_by_css_selector("#copyPersonForm tr:nth-child(4) > td.easyui-myText > input").send_keys(cempl_code)
        sleep(0.5)
        
        #员工名称
        name=empl_name
        driver.find_element_by_css_selector("#copyPersonForm  tr:nth-child(5) > td.easyui-myText > input").send_keys(name)
        sleep(0.5)
        
        #联系手机
        phone='1835038'+strt
        driver.find_element_by_css_selector("#copyPersonForm  tr:nth-child(6) > td.easyui-numberbox.validatebox-text > input").send_keys(phone)
        sleep(0.5)
        
        #登录帐号
        account='ZMC'+strt
        driver.find_element_by_css_selector("#copyPersonForm  tr:nth-child(7) > td:nth-child(2) > input").send_keys(account)
        sleep(0.5)

        #确定
        driver.find_element_by_css_selector("html.panel-fit body.easyui-layout div.panel div.panel-body div a.easyui-linkbutton span.l-btn-left span.l-btn-text span").click()

        sleep(0.5)
            
        #获取断言信息
        success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
        tip_text=success.text
            
        #确定,关闭提示框
        driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

        #断言是否复制成功
        self.assertEqual(u"复制成功",tip_text)
        
        #新用户登录
        try:
            self.login_NewEmployee(account)

        except:
            log.error("New employee login fail")

        #删除复制添加的员工
        
        #查找员工
        code=cempl_code
        self.searchbycode(code)
        
        #选择员工
        driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #删除
        self.clickButton(u'删除')
        

        
    def searchbycode(self,code):
        '''按编号查找'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        driver.find_element_by_css_selector("#fdCode").clear()
        sleep(0.5)
        driver.find_element_by_css_selector("#fdCode").send_keys(code)

        #点击查找
        self.clickButton(u'查找')
        sleep(3)

        #断言
        cds=driver.find_elements_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='fdCode']")
        sleep(0.5)
        searchAssert(self,cds,code)
        
         
    def test_1search_ByEmployeeCode(self):
        u'''按员工编号查找'''
        log.info(u"开始执行测试...")
        
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()
        #查找
        code=driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='fdCode']").text
        self.searchbycode(code)
    
        
    def test_2search_ByEmployeeName(self):
        u'''按员工名称查找'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()

        #输入员工名称
        name=driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='fdName']").text
        driver.find_element_by_css_selector("#fdName").send_keys(name)
        
        #查找
        self.clickButton(u'查找')
        sleep(3)

        #断言
        nas=driver.find_elements_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='fdName']")
        searchAssert(self,nas,name)
        
        
        
    def test_3search_ByPhones(self):
        u'''按联系手机查找'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()

        #输入手机号码
        phone=driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='mobile']").text
        driver.find_element_by_css_selector("#mobile").send_keys(phone)
        
        #查找
        self.clickButton(u'查找')

        #断言
        phs=driver.find_elements_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='mobile']")
        searchAssert(self,phs,phone)
        
        
    def test_4search_ByEmployeePosition(self):
        u'''按员工的岗位名称查找'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()

        
        #选择岗位名称
        driver.find_element_by_css_selector("#stmPersonHdToolbar > div:nth-child(1) > span > input.combo-text.validatebox-text").click()
        sleep(0.5)
        psts=driver.find_elements_by_css_selector("body > div.panel.combo-p  div.combobox-item")
        n=0
        
        for pst in psts:
            #print pst.text
            n+=1
            if pst.text==position:
                driver.find_element_by_css_selector("body > div.panel.combo-p div:nth-child("+str(n)+")").click()
                break
        sleep(1)
        
        #查找
        self.clickButton(u'查找')
        sleep(3)

        #断言
        pns=driver.find_elements_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='jobName']")
        searchAssert(self,pns,position)
        

    def test_5modify_EmployeeInfo(self):
        u'''修改员工信息'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()

        #查找修改的员工
        code=empl_code
        self.searchbycode(code)

        #选择员工
        driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #点击修改
        self.clickButton(u'修改')

        #修改员工名称
        new_name='New_ZMauto'
        nal=driver.find_element_by_css_selector("#stmPersonHdTForm tr:nth-child(1) > td:nth-child(11) > input")
        nal.clear()
        sleep(0.5)
        nal.send_keys(new_name)
        sleep(0.5)

        #保存
        self.clickButton(u'保存')

        #再次查找
        self.searchbycode(code)
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='ck']")
     
        log.info(u"刷新完成！！！")
        sleep(1)

        #判断员工名称与修改是否一致
        self.assertEqual(new_name,driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='fdName']").text)
        

    def test_6modify_LoginPasswdReset(self):
        u'''登录密码重置'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()

        #查找员工
        code=empl_code
        self.searchbycode(code)
        
        
        #选择员工
        driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        #获取该员工的登录帐号
        account=driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='loginName']").text
        

        #点击登录密码重置
        self.clickButton(u'登录密码重置')
        
        #点击确认
        driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
        sleep(0.5)
        
        #断言提示语
        rt=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text
        self.assertEqual(u'密码重置成功',rt)
        
        #确定
        driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()

        #员工登录验证
        self.login_NewEmployee(account)
        
        
    def test_7modify_RoleAssignment(self):
        u'''角色分配'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()

        #未选择员工，判断按钮是否置灰
        da=driver.find_element_by_css_selector("#stmPersonHdToolbar > div:nth-child(2) > a.easyui-linkbutton.prvlgAvg").get_attribute('class')
        self.assertIn("l-btn-disabled",da)
        sleep(0.5)
        #选择多个员工，按钮置灰
        
        driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-htable td[field='ck']> div > input[type='checkbox']").click()
        sleep(0.5)
        da=driver.find_element_by_css_selector("#stmPersonHdToolbar > div:nth-child(2) > a.easyui-linkbutton.prvlgAvg").get_attribute('class')
        self.assertIn("l-btn-disabled",da)
        
        #查找员工
        code=empl_code
        self.searchbycode(code)
        
        #选择员工
        driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  div.datagrid-body table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #选择一个员工，按钮可用
        da=driver.find_element_by_css_selector("#stmPersonHdToolbar > div:nth-child(2) > a.easyui-linkbutton.prvlgAvg").get_attribute('class')
        self.assertNotIn("l-btn-disabled",da)

        #角色分配
        self.clickButton(u'角色分配')

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#first > div > div > div > div.datagrid-view2 > div.datagrid-body td[field='ck']")
     
        log.info(u"刷新完成！！！")
        sleep(1)
        
        
        #全选右移
        driver.find_element_by_css_selector("#stmPersonRoleLeftWindow  table.datagrid-htable > tbody > tr > td:nth-child(1) > div > input[type='checkbox']").click()
        sleep(0.5)
        driver.find_element_by_css_selector("#rightStmPersonRoleWindowButton").click()
        sleep(1)

        #全选左移
        driver.find_element_by_css_selector("#first table.datagrid-htable > tbody > tr > td:nth-child(1) > div > input[type='checkbox']").click()
        sleep(0.5)
        
        driver.find_element_by_css_selector("#leftStmPersonRoleWindowButton").click()
        sleep(1)
        
        #重置
        driver.find_element_by_css_selector("#reSettingStmPersonRoleWindowButton").click()
        sleep(1)

        #选择一个左移
        driver.find_element_by_css_selector("#first > div > div > div > div.datagrid-view2 > div.datagrid-body td[field='ck']").click()
        
        sleep(0.5)
        
        driver.find_element_by_css_selector("#leftStmPersonRoleWindowButton").click()
        sleep(1)
        
        #选择一个右移
        driver.find_element_by_css_selector("#stmPersonRoleLeftWindow > div > div > div > div.datagrid-view2 > div.datagrid-body td[field='ck']").click()
        
        sleep(0.5)
        driver.find_element_by_css_selector("#rightStmPersonRoleWindowButton").click()
        sleep(1)

        #获取选择的角色名称
        role=driver.find_element_by_css_selector("#first > div > div > div > div.datagrid-view2 > div.datagrid-body td[field='fdName']").text
        #print role
        #保存
        driver.find_element_by_css_selector('body  div.panel-body.panel-body-noborder.window-body > div:nth-child(2) > a.easyui-linkbutton.saveButton.l-btn > span > span').click()
        sleep(0.5)
            
        #获取断言信息
            
        success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
        tip_text=success.text
        log.info(tip_text)
        
        #确定,关闭提示框
        driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

        #等待页面刷新完成
        WebWait(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) > div > div > div.panel.layout-panel.layout-panel-center div.datagrid-mask-msg")
            
        #再次查找
        self.searchbycode(code)

        #断言角色是否与修改后的一致
        self.assertEqual(role,driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='usrRole']").text)
        
        
    def test_8modify_Storedistribution(self):
        u'''门店分配'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()

         #查找员工
        code=empl_code
        self.searchbycode(code)
        
        #选择员工
        driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #点击门店分配
        self.clickButton(u'门店分配')
        sleep(1)
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"body  div.panel-body.panel-body-noborder.window-body > div:nth-child(1) > div.left  div.datagrid-body td[field='ck']")
     
        log.info(u"刷新完成！！！")
        sleep(1)
        
        
        #全选右移
        driver.find_element_by_css_selector("html.panel-fit body.easyui-layout div.panel div.panel-body div div.left div.panel div.datagrid-wrap div.datagrid-view div.datagrid-view2 div.datagrid-header div.datagrid-header-inner table.datagrid-htable tbody tr.datagrid-header-row td div.datagrid-header-check input").click()
        sleep(0.5)
        
        driver.find_element_by_css_selector("#dataPrvlgRightButton").click()
        sleep(1)

        #全选左移
        driver.find_element_by_css_selector("html.panel-fit body.easyui-layout div.panel div.panel-body div div.right div.panel div.datagrid-wrap div.datagrid-view div.datagrid-view2 div.datagrid-header div.datagrid-header-inner table.datagrid-htable tbody tr.datagrid-header-row td div.datagrid-header-check input").click()
        sleep(0.5)
        
        driver.find_element_by_css_selector("#dataPrvlgLeftButton").click()
        sleep(1)
        
        #重置
        driver.find_element_by_css_selector("#dataPrvlgResettingButton").click()
        sleep(1)
        
        
        #选择一个左移
        driver.find_element_by_css_selector("body  div.panel-body.panel-body-noborder.window-body > div:nth-child(1) > div.right  div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)
        
        driver.find_element_by_css_selector("#dataPrvlgLeftButton").click()
        sleep(1)
        
        #选择一个右移
        driver.find_element_by_css_selector("body  div.panel-body.panel-body-noborder.window-body > div:nth-child(1) > div.left  div.datagrid-body td[field='ck']").click()
        
        sleep(0.5)
        driver.find_element_by_css_selector("#dataPrvlgRightButton").click()
        sleep(1)

        #获取选择的门店名称
        store=driver.find_element_by_css_selector("body  div.panel-body.panel-body-noborder.window-body > div:nth-child(1) > div.right  div.datagrid-body > table td[field='shopName']").text
        #print store

        #保存
        driver.find_element_by_css_selector('body  div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.saveButton.l-btn > span > span').click()
    
        sleep(0.5)
            
        #获取断言信息
            
        success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
        tip_text=success.text
        
        log.info(tip_text)
        #确定,关闭提示框
        driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

        #等待页面刷新完成
        WebWait(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) > div > div > div.panel.layout-panel.layout-panel-center div.datagrid-mask-msg")
        
        #再次查找
        self.searchbycode(code)

        #断言门店是否与修改后的一致
        #print driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='usrShop']").text
        self.assertEqual(store,driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='usrShop']").text)
           
            
    def test_9adelete_Employee(self):
        u'''删除员工'''
        log.info(u"开始执行测试...")
        
        driver=self.driver
        #进入人员信息
        self.to_EmployeeInformation()
        
        #查找员工
        code=empl_code
        self.searchbycode(code)
        
        #选择员工
        driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2)  table.datagrid-btable td[field='ck']").click()
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
    

    #suite.addTest(test_EmployeeInfo('test_01add_Employee'))#添加员工
    #suite.addTest(test_EmployeeInfo('test_02add_EmployeeCopy'))#员工复制添加
    
    #suite.addTest(test_EmployeeInfo('test_1search_ByEmployeeCode'))#按员工编号查找
    #suite.addTest(test_EmployeeInfo('test_2search_ByEmployeeName'))#按员工名称查找
    #suite.addTest(test_EmployeeInfo('test_3search_ByPhones'))#按联系手机查找
    #suite.addTest(test_EmployeeInfo('test_4search_ByEmployeePosition'))#按岗位名称查找
    
    #suite.addTest(test_EmployeeInfo('test_5modify_EmployeeInfo'))#修改员工信息
    suite.addTest(test_EmployeeInfo('test_6modify_LoginPasswdReset'))#登录密码重置
    #suite.addTest(test_EmployeeInfo('test_7modify_RoleAssignment'))#角色分配
    
    #suite.addTest(test_EmployeeInfo('test_8modify_Storedistribution'))#门店分配
    
    
    #suite.addTest(test_EmployeeInfo('test_9adelete_Employee'))#员工删除
   
    
    
    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)

    #unittest.main()
    log.info('test_EmployeeInfo end--')
        
