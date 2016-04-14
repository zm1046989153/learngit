# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest,time,sys,xml.dom.minidom
from selenium.webdriver.common.keys import Keys
from time import sleep
sys.path.append(r'D:\ISS\Test_Cases\public')

import login

from isspublic import*

#打开xml文档
dom=xml.dom.minidom.parse(r'D:\ISS\Test_Data\login.xml')

#得到文档元素对象
root=dom.documentElement

phone="15666666666"

class Test_MemberInformation(unittest.TestCase):
    #会员信息
    log.info(u"~~~会员信息模块测试~~~")
    
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        url=root.getElementsByTagName('url')  
        self.base_url=url[0].firstChild.data
        logins=root.getElementsByTagName('login')
        #获得null 标签的username、passwrod 属性值
        self.username=logins[0].getAttribute("username")
        self.password=logins[0].getAttribute("password")
        prompt_info=logins[0].firstChild.data
        self.accept_next_alert = True
        self.verificationErrors =[]




    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#ctmVipHdToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
            
            
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#ctmVipHdToolbar > a.easyui-linkbutton.findButton > span > span').click()
            sleep(1)
            WebWait(driver,"#ctmVipHdAccordion  div.datagrid-mask-msgn")
            
            
            
        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#ctmVipHdToolbar > a.easyui-linkbutton.viewButton > span > span').click()
            sleep(1)
            
            #判断是否进入查看界面
            self.assertEqual(u'编辑',driver.find_element_by_css_selector("#ctmVipHdForm > div > a.easyui-linkbutton.saveButton > span > span > span").text)
            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#ctmVipHdToolbar > a.easyui-linkbutton.editButton > span > span').click()
            sleep(1)


        elif button==u'删除' or button=='delete':
            #查看界面，点击“删除”按钮
            driver.find_element_by_css_selector("#ctmVipHdToolbar > a.easyui-linkbutton.deleteButton > span > span").click()
            sleep(0.5)

            #点击确认，删除记录并断言
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            sleep(1)
            dele_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text
            #print dele_text
            log.info(dele_text)
            self.assertEqual(u"删除成功",dele_text)
            
            

        elif button==u'编辑' or button=='edit':
            #查看界面，点击“编辑”按钮
            driver.find_element_by_css_selector("#ctmVipHdForm a.easyui-linkbutton.saveButton> span > span > span").click()
            
            sleep(0.5)

        
            
            
        elif button==u'取消' or button=='cancel':
            #编辑界面，点击“取消”按钮
            driver.find_element_by_css_selector('#masPartHdForm > div > a.easyui-linkbutton.cancelButton').click()
            sleep(0.5)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮
            driver.find_element_by_css_selector("#ctmVipHdForm > div > a.easyui-linkbutton.saveButton > span >span").click()
            sleep(0.5)
            
            #获取断言信息
            try:
                success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
            except:
                raise NameError("Data Save Failed!!!")
            
            tip_text=success.text
            log.info(tip_text)
            
            #确定,关闭提示框
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

            #断言是否保存成功
            self.assertEqual(u"保存成功！",tip_text)
            
        
        else:
            raise NameError('No Such Button,confirm again please')
        


    #会员信息的添加功能
    def test_0MemberInformation_add(self):
        u'''添加会员名称为zzt006的会员信息'''

        #进入会员管理
        driver=self.driver
        self.to_member()
        sleep(1)

        #点击添加按钮
        driver.find_element_by_css_selector("#ctmVipHdToolbar > a.easyui-linkbutton.addButton > span > span").click()
        sleep(1)
        #输入会员信息
        #会员名称
        driver.find_element_by_css_selector("td.easyui-myText > input[name=\"model.fdName\"]").clear()
        driver.find_element_by_css_selector("td.easyui-myText > input[name=\"model.fdName\"]").send_keys("zzt006")
        sleep(0.5)

        #性别
        seb=driver.find_element_by_xpath("//*[@id=\"ctmVipHdForm\"]/table/tbody/tr[1]/td[4]/span/input[1]")
        sleep(0.5)
        seb.click()
        sleep(0.5)
        seb.send_keys(Keys.DOWN)
        sleep(0.5)
        seb.send_keys(Keys.ENTER)
        sleep(0.5)
        #年龄
        driver.find_element_by_xpath(".//*[@id='ctmVipHdForm']/table/tbody/tr[1]/td[6]/input").send_keys('24')
        sleep(0.5)

        #生日
        br=driver.find_element_by_xpath("//*[@id='ctmVipHdForm']/table/tbody/tr[1]/td[8]/span/input[1]")
        sleep(0.5)
        br.click()
        sleep(0.5)
        br.send_keys(Keys.ENTER)
        sleep(0.5)
    
        
        #手机号
        global phone
        strt=time.strftime("%H%M%S",time.localtime(time.time()))
        phone='18350'+strt
        driver.find_element_by_css_selector("td.easyui-numberbox.validatebox-text > input[name=\"model.fdMobile\"]").clear()
        sleep(0.5)
        driver.find_element_by_css_selector("td.easyui-numberbox.validatebox-text > input[name=\"model.fdMobile\"]").send_keys(phone)
        sleep(0.5)

        #会员级别
        me=driver.find_element_by_xpath("(//input[@type='text'])[12]")
        me.click()
        sleep(0.5)
        me.send_keys(Keys.DOWN)
        sleep(0.5)
        me.send_keys(Keys.ENTER)
        sleep(0.5)
        
        #会员日期
        md=driver.find_element_by_xpath("(//input[@type='text'])[14]")
        sleep(0.5)
        md.click()
        sleep(0.5)
        md.send_keys(Keys.ENTER)
        sleep(0.5)

        #国家
        driver.find_element_by_css_selector("#ctmVipHdForm > table > tbody > tr:nth-child(4) > td:nth-child(2) > span > input").click()
        sleep(0.5)
        driver.find_element_by_css_selector("body > div:nth-child(18) > div > div:nth-child(2)").click()
        sleep(0.5)
        
        #省份
        p=driver.find_element_by_css_selector("#ctmVipHdForm > table > tbody > tr:nth-child(4) > td:nth-child(4) > span > input")
        sleep(0.5)
        p.click()
        sleep(0.5)
        p.send_keys(Keys.DOWN)
        sleep(0.5)
        p.send_keys(Keys.ENTER)
        sleep(0.5)
        
        #城市
        p=driver.find_element_by_css_selector("#ctmVipHdForm > table > tbody > tr:nth-child(4) > td:nth-child(6) > span > input")
        sleep(0.5)
        p.click()
        sleep(0.5)
        p.send_keys(Keys.DOWN)
        sleep(0.5)
        p.send_keys(Keys.ENTER)
        sleep(0.5)

        #区县
        p=driver.find_element_by_css_selector("#ctmVipHdForm > table > tbody > tr:nth-child(4) > td:nth-child(8) > span > input")
        sleep(0.5)
        p.click()
        sleep(0.5)
        p.send_keys(Keys.DOWN)
        sleep(0.5)
        p.send_keys(Keys.ENTER)
        sleep(0.5)
        
        
        #保存
        self.clickButton(u"保存")
      

    #会员信息的查找功能
    def test_1Search_by_MumberName(self):
        u'''按会员名称查找'''

        #进入会员管理
        driver=self.driver
        self.to_member()

        #输入要查找的名称
        name=findCss(driver,"#ctmVipHdAccordion table.datagrid-btable td[field='fdName']").text
        findCss(driver,"#ctmVipHdToolbar > input:nth-child(1)").clear()
        sleep(0.5)
        findCss(driver,"#ctmVipHdToolbar > input:nth-child(1)").send_keys(name)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        sleep(2)
        
        #获取断言信息进行断言
        nas=findsCss(driver,"#ctmVipHdAccordion table.datagrid-btable td[field='fdName']")

        searchAssert(self,nas,name)

    def test_2Search_by_PhoneNumber(self):
        u'''按手机号码查找'''

        #进入会员管理
        driver=self.driver
        self.to_member()

        #查找
        phone=findCss(driver,"#ctmVipHdAccordion table.datagrid-btable td[field='fdMobile']").text
        findCss(driver,"#ctmVipHdToolbar > input:nth-child(2)").clear()
        sleep(0.5)
        findCss(driver,"#ctmVipHdToolbar > input:nth-child(2)").send_keys(phone)
        sleep(0.5)
        #点击查找
        self.clickButton(u"查找")
        sleep(1)

        #获取断言信息进行断言
        phs=findsCss(driver,"#ctmVipHdAccordion table.datagrid-btable td[field='fdMobile']")

        searchAssert(self,phs,phone)
    

    #会员信息的查看功能
    def test_3MemberInformation_check(self):
        u'''查看会员'''
        #进入会员管理
        driver=self.driver
        self.to_member()

        #选择记录
        findCss(driver,"#ctmVipHdAccordion table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #查看
        self.clickButton(u"查看")
     
        #编辑
        self.clickButton(u"编辑")

        #保存
        self.clickButton(u"保存")
          


    #会员信息的修改功能
    def test_4MemberInformation_revise(self):
        u'''修改会员记录'''
         #进入会员管理
        driver=self.driver
        self.to_member()

        #通过手机号查找
        findCss(driver,"#ctmVipHdToolbar > input:nth-child(2)").send_keys(phone)
        sleep(0.5)
        self.clickButton(u"查找")
        #选择一条记录
        findCss(driver,"#ctmVipHdAccordion table.datagrid-btable td[field='ck']").click()

        #修改
        self.clickButton(u"修改")


        #保存
        self.clickButton(u"保存")

    #会员信息的删除功能
    def test_5MemberInformation_delete(self):
        u'''删除会员名称为zzt006的记录'''
         #进入会员管理
        driver=self.driver
        self.to_member()

        #通过手机号查找
        findCss(driver,"#ctmVipHdToolbar > input:nth-child(2)").send_keys(phone)
        sleep(0.5)
        self.clickButton(u"查找")
        
        #选择一条记录
        findCss(driver,"#ctmVipHdAccordion table.datagrid-btable td[field='ck']").click()

        #删除
        self.clickButton(u"删除")
          


    #进入会员管理模块
    def to_member(self):
        driver=self.driver
        driver.get(self.base_url)
        login.login(self,self.username,self.password)
        self.assertEqual('GREAT MASTER',driver.title)
        #点击会员管理
        driver.find_element_by_css_selector("#menuAccordion > div:nth-child(2) > div.panel-header.accordion-header > div.panel-title").click()
        sleep(0.5)
        #点击会员信息
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/ul/li/div").click()
        sleep(1)

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#ctmVipHdAccordion table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！") 
     

    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        #self.driver.close()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
        

if __name__ == "__main__":
    
    #构造测试集
    suite = unittest.TestSuite()

    
    #suite.addTest(Test_MemberInformation("test_0MemberInformation_add"))
    #suite.addTest(Test_MemberInformation("test_1Search_by_MumberName"))
    suite.addTest(Test_MemberInformation("test_2Search_by_PhoneNumber"))
    #suite.addTest(Test_MemberInformation("test_3MemberInformation_check"))
    #suite.addTest(Test_MemberInformation("test_4MemberInformation_revise"))
    #suite.addTest(Test_MemberInformation("test_5MemberInformation_delete"))
                            
 
    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)
    #unittest.main()   


