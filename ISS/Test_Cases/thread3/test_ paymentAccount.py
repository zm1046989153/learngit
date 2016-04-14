# _*_ coding=utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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

#组织名称
org_name=u'西安专卖店'



class test_paymentAccount(unittest.TestCase):
    #支付帐号信息模块测试
    log.info(u"~~~支付账号信息模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_paymentAccount(self):
        #支付帐号信息 模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入支付帐号信息模块
        testModule(driver,u'系统管理',u'支付账号信息')
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")

        sleep(1)
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmDptDtPaymentToolbar > a.easyui-linkbutton.newButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmDptDtPaymentToolbar > a.easyui-linkbutton.findPaymentButton > span > span').click()
            sleep(1)

        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#stmShippingTemplateToolbar > a.easyui-linkbutton.viewButton > span > span').click()
            sleep(1)

            self.assertEqual(u"编辑",driver.find_element_by_css_selector("#stmShippingTemplateForm > div > a.easyui-linkbutton.saveButton > span > span > span").text)


        elif button==u'编辑' or button=='edit':
            #点击“编辑”按钮
            driver.find_element_by_css_selector('#stmShippingTemplateForm > div > a.easyui-linkbutton.saveButton > span > span > span').click()
            sleep(1)
            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmDptDtPaymentToolbar > a.easyui-linkbutton.editButton > span > span').click()
            sleep(1)
    

    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmDptDtPaymentToolbar > a.easyui-linkbutton.deleteButton > span > span').click()
            sleep(1)
            
            #点击确认，删除记录并断言
            
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()
            sleep(1)
            dele_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text
            #print dele_text
            log.info(dele_text)
            self.assertEqual(u"删除成功！",dele_text)
            
            #点击取消
            #driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2)").click()
                
        elif button==u'取消' or button=='cancel':
            #编辑界面，点击“取消”按钮
            driver.find_element_by_css_selector('#stmShippingTemplateForm > div > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            #取消
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            
            sleep(1)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("body > div:nth-child(20) > div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.saveButton.l-btn.l-btn-plain > span > span > span").click()
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

    def selectorg(self,org_name):
        '''菜单树中选择指定的组织'''

        driver=self.driver
        n=0
        orgs=findsCss(driver,"#stmDptDtPaymentTree_1_ul > li.level1")
        for org in orgs:
            n+=1
            #print org.text
            if org.text==org_name:
                findCss(driver,"#stmDptDtPaymentTree_1_ul > li:nth-child("+str(n)+") > a > span").click()
                break
        sleep(0.5)


        
    def test_0add_paymentAccount(self):
        u'''添加支付帐号'''
        
        driver=self.driver
        
        #进入支付帐号信息模块
        self.to_paymentAccount()

        #选择组织
        org_name=u"西安专卖店"
        self.selectorg(org_name)
        
            
        #添加
        self.clickButton(u"添加")

        #支付帐号类型
        findCss(driver,"#stmDptDtPaymentForm > table:nth-child(1) tr:nth-child(2) > td.easyui-myText > span > input.combo-text.validatebox-text.validatebox-invalid").click()
        sleep(0.5)
        pay_type=u"微信扫码"
        n=0
        pps=findsCss(driver,"body > div:nth-child(23) > div > div.combobox-item")
        for pp in pps:
            #print pp.text
            n+=1
            if pp.text==pay_type:
                findCss(driver,"body > div:nth-child(23) > div > div:nth-child("+str(n)+")").click()
                break
        sleep(0.5)
        
        #微信应用ID
        wx_appID='weixin_id'
        findCss(driver,"#dptPayment_weixin  tr:nth-child(1) > td.easyui-myText > input").send_keys(wx_appID)
        sleep(0.5)

        #微信商家ID
        wx_storeID="weixin_store_ID"
        findCss(driver,"#dptPayment_weixin  tr:nth-child(2) > td.easyui-myText > input").send_keys(wx_storeID)
        sleep(0.5)

        #微信密钥
        password="12345678"
        findCss(driver,"#dptPayment_weixin tr:nth-child(3) > td.easyui-myText > input").send_keys(password)
        sleep(0.5)

        #保存
        self.clickButton(u"保存")
        

    def test_1search_byAccountType(self):
        u'''按帐号类型查找'''
        
        driver=self.driver
        
        #进入支付帐号信息模块
        self.to_paymentAccount()

        #选择帐号类型
        #设置要查找的帐号类型
        acc_type=u"微信扫码"
        findCss(driver,"#stmDptDtPaymentToolbar > span:nth-child(2) > input.combo-text.validatebox-text").click()
        sleep(0.5)
        tps=findsCss(driver,"body > div:nth-child(16) > div > div.combobox-item") 
        n=0
        for tp in tps:
            n+=1
            #print tp.text
            if tp.text==acc_type:
                findCss(driver,"body > div:nth-child(16) > div > div:nth-child("+str(n)+")").click()
                break
        sleep(0.5)
        #查找
        self.clickButton(u"查找")

        #断言
        pays=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='paymentNname']")
        searchAssert(self,pays,acc_type)
         
                
            

    def test_2search_byOrganizationType(self):
        u'''按组织类型查找'''


        driver=self.driver
        #进入支付帐号信息模块
        self.to_paymentAccount()

        #选择组织类型
        #设置要查找的组织类型
        acc_type=u"终端"
        findCss(driver,"#stmDptDtPaymentToolbar > span:nth-child(4) > input.combo-text.validatebox-text").click()
        sleep(0.5)
        tps=findsCss(driver,"body > div:nth-child(17) > div > div.combobox-item")
        
        n=0
        for tp in tps:
            n+=1
            #print tp.text
            if tp.text==acc_type:
                findCss(driver,"body > div:nth-child(17) > div > div:nth-child("+str(n)+")").click()
                break
        sleep(0.5)
        #查找
        self.clickButton(u"查找")

        #断言
        orgs=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='shopClassName']")
        searchAssert(self,orgs,acc_type)

        

    def test_3search_byOrganizationName(self):
        u'''按组织名称查找'''
        
        driver=self.driver
        
        #进入支付帐号信息模块
        self.to_paymentAccount()

        #选择组织名称
        org_name=u"厦门分公司"
        findCss(driver,"#stmDptDtPaymentToolbar > span:nth-child(6) > span > span").click()
        sleep(0.5)
        oes=findsCss(driver,"body > div:nth-child(18) > div > ul > li:nth-child(1) > ul > li")
        n=0
        for oe in oes:
            #print oe.text
            n+=1
            #print n
            if oe.text==org_name:
                findCss(driver,"body > div:nth-child(18) > div > ul > li:nth-child(1) > ul >li:nth-child("+str(n)+") > div > span").click()
                break
        sleep(0.5)
                
        #查找
        self.clickButton(u"查找")

        #断言
        orgs=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='dptName']")
        searchAssert(self,orgs,org_name)
        



    def test_4modify_paymentAccount(self):
        u'''修改支付帐号'''
        
        driver=self.driver
        
        #进入支付帐号信息模块
        self.to_paymentAccount()
        
        #选择组织
        org_name=u"Atest启尚科技"
        self.selectorg(org_name)

        #选择记录
        findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u"修改")

        #保存
        self.clickButton(u"保存")

    def test_5delete_paymentAccount(self):
        u'''删除支付帐号'''
        
        driver=self.driver
        
        #进入支付帐号信息模块
        self.to_paymentAccount()

        #选择组织
        org_name=u"Atest启尚科技"
        self.selectorg(org_name)

        #选择记录
        findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        #删除
        self.clickButton(u"删除")

  
       
    
    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_paymentAccount start--')
    suite=unittest.TestSuite()
    
    #suite.addTest(test_paymentAccount('test_0add_paymentAccount'))#添加支付帐号
    #suite.addTest(test_paymentAccount('test_1search_byAccountType'))#按帐号类型查找
    #suite.addTest(test_paymentAccount('test_2search_byOrganizationType'))#按组织类型查找
    #suite.addTest(test_paymentAccount('test_3search_byOrganizationName'))#按组织名称查找
    suite.addTest(test_paymentAccount('test_4modify_paymentAccount'))#修改支付帐号
    #suite.addTest(test_paymentAccount('test_5delete_paymentAccount'))#删除支付帐号
    
   
   
   
    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_paymentAccount end--')
        
 
