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

#商品编码
com_code='GC3540011'

#尺寸
SKU_size='60'


class test_SKUSet(unittest.TestCase):
    #SKU设置模块测试
    log.info(u"~~~SKU设置模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_SKUset(self):
        #进入SKU设置模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入SKU设置
        testModule(driver,u'基础信息',u'SKU设置')
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masPartDtSkuAccordion > div:nth-child(1) > div.panel-body.accordion-body table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")
       
        sleep(1)
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#masPartDtSkuToolbar  a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#masPartDtSkuToolbar  a.easyui-linkbutton.findButton > span > span').click()
            
            WebWait(driver,"#masPartDtSkuAccordion > div:nth-child(1) > div.panel-body.accordion-body > div > div > div.datagrid-mask-msg")
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#masPartDtSkuToolbar  a.easyui-linkbutton.editButton > span > span').click()
            sleep(1)
    
            
        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#masPartDtSkuToolbar  a.easyui-linkbutton.viewButton > span > span').click()
            WebWait(driver,"#masPartDtSkuForm > div.datagrid-mask-msg")
            sleep(1)
            edl=driver.find_element_by_css_selector("#masPartDtSkuForm > div > a.easyui-linkbutton.saveButton > span > span > span")
            #print edl.text
            self.assertEqual(u'编辑',edl.text)
            
            
        elif button==u'编辑' or button=='edit':
            #点击“编辑”按钮
            driver.find_element_by_css_selector("#masPartDtSkuForm > div > a.easyui-linkbutton.saveButton > span > span > span").click()
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
            driver.find_element_by_css_selector('#masPartDtSkuForm > div > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            #取消
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            
            sleep(1)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("#masPartDtSkuForm > div > a.easyui-linkbutton.saveButton > span > span > span").click()
            WebWait(driver,"#masPartDtSkuForm > div.datagrid-mask-msg")
            sleep(1)
            
            
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

        """
    def test_0add_SKU(self):
        u'''添加SKU'''
        driver=self.driver
        #进入SKU设置
        self.to_SKUset()

        #点击添加
        self.clickButton(u'添加')

        #商品编码
        driver.find_element_by_css_selector("#masPartDtSkuForm  td:nth-child(5) > span > input.combo-text.validatebox-text.validatebox-invalid").click()
        sleep(0.5)
        
        #选择商品编码，并获取该编码
        driver.find_element_by_css_selector("body > div:nth-child(16) > div > div.combobox-item").click()
        global com_code
        com_code=driver.find_element_by_css_selector("body > div:nth-child(16) > div > div.combobox-item").text

        #选择颜色
        driver.find_element_by_css_selector("#masPartDtSkuForm  tr:nth-child(1) > td:nth-child(7) > span > input.combo-text.validatebox-text").click()
        sleep(0.5)
        driver.find_element_by_css_selector("body > div:nth-child(17) > div > div[value='1001941']").click()
        
     
        

        #选择尺寸
        driver.find_element_by_css_selector("#masPartDtSkuForm  tr:nth-child(1) > td:nth-child(9) > span > input.combo-text.validatebox-text").click()
        sleep(0.5)
        driver.find_element_by_css_selector("body > div:nth-child(18) > div > div.combobox-item").click()
        sleep(0.5)
        #global SKU_size
        SKU_size=driver.find_element_by_css_selector("body > div:nth-child(18) > div > div.combobox-item").text
        
        #取消
        self.clickButton(u'取消')

        #保存
        self.clickButton(u'保存')
        
        """
         
    def test_1search_ByComCode(self):
        u'''按商品编码查找'''
        driver=self.driver
        #进入SKU设置
        self.to_SKUset()


        #输入要查找的编码
        driver.find_element_by_css_selector("#masPartDtSkuToolbar > span:nth-child(2) > input.combo-text.validatebox-text").click()
        sleep(1)
        des=driver.find_elements_by_css_selector("#masPartDtSkuAccordion table.datagrid-btable td[field='masParthdKey']")
        for de in des:
            if de.text!='':
                code=de.text
                #print code
                break
            continue
        #print code
        cds=driver.find_elements_by_css_selector("body > div:nth-child(20) > div > div.combobox-item")
        n=0
        for cd in cds:
            n+=1
            #print cd.text
            if cd.text==code:
                driver.find_element_by_css_selector("body > div:nth-child(20) > div > div:nth-child("+str(n)+")").click()
                break
            continue
        sleep(0.5)
                
        #查找
        self.clickButton(u'查找')

        #断言
        cds=driver.find_elements_by_css_selector("#masPartDtSkuAccordion > div:nth-child(1) > div.panel-body.accordion-body table.datagrid-btable td[field='masParthdKey']")
        
        searchAssert(self,cds,code)

        
    def test_2search_BySize(self):
        u'''按尺寸查找'''
        driver=self.driver
        #进入SKU设置
        self.to_SKUset()
        
        #输入要查找的尺寸
        
        #读取列表中的一个尺寸
        ses=driver.find_elements_by_css_selector("#masPartDtSkuAccordion table.datagrid-btable td[field='sizeKey']")
        for se in ses:
            if se.text!='':
                size=se.text
                #print size
                break
            continue
                
        #print size
        #点击尺寸输入框
        driver.find_element_by_css_selector("#masPartDtSkuToolbar > span:nth-child(4) > input.combo-text.validatebox-text").click()
        sleep(1)
        #选择读取的尺寸，查找
        szs=driver.find_elements_by_css_selector("body > div:nth-child(21) > div  div.combobox-item")
        n=0
        for sz in szs:
            n+=1
            #print sz.text
            if sz.text==size:
                driver.find_element_by_css_selector("body > div:nth-child(21) > div > div:nth-child("+str(n)+")").click()
                break
            continue
        sleep(0.5)
                
        #查找
        self.clickButton(u'查找')

        #断言
        szs=driver.find_elements_by_css_selector("#masPartDtSkuAccordion > div:nth-child(1) > div.panel-body.accordion-body table.datagrid-btable td[field='sizeKey']")
        #for sz in szs:
           # print sz.text
        searchAssert(self,szs,size)

        
    def test_3look_SKUSet(self):
        u'''查看SKU'''
        driver=self.driver
        #进入SKU设置
        self.to_SKUset()

        #选择要查看的记录
        driver.find_element_by_css_selector("#masPartDtSkuAccordion  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #点击查看
        self.clickButton(u'查看')

        #点击编辑
        self.clickButton(u'编辑')
    
        #点击保存
        self.clickButton(u'保存')
        
        
   
    """
    def test_4modify_SKUSet(self):
        u'''修改SKU'''
        driver=self.driver
        #进入SKU设置
        self.to_SKUset()
        #选择要修改的记录
        driver.find_element_by_css_selector("#masPartDtSkuAccordion > div:nth-child(1) > div.panel-body.accordion-body table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #点击修改
        self.clickButton(u'修改')

        #点击取消
        self.clickButton(u'取消')
        driver.find_element_by_css_selector("#masPartDtSkuForm > table > tbody > tr:nth-child(1) > td:nth-child(7) > span > input.combo-text.validatebox-text").clear()

        #点击保存
        self.clickButton(u'保存')
        """
    
    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_EmployeeInfo start--')
    suite=unittest.TestSuite()
    
    #suite.addTest(test_SKUSet('test_0add_SKU'))#添加SKU
    #suite.addTest(test_SKUSet('test_1search_ByComCode'))#按商品编码查找
    suite.addTest(test_SKUSet('test_2search_BySize'))#按尺寸查找
    suite.addTest(test_SKUSet('test_3look_SKUSet'))#查看SKU
    #suite.addTest(test_SKUSet('test_4modify_SKUSet'))#修改SKU

    #执行测试
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_EmployeeInfo end--')
        
