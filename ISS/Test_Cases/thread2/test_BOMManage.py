# _*_ coding=utf-8 _*_

from selenium import webdriver
from selenium import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
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
com_code='CSP2150003'

#商品类别
com_type=u'运动鞋'



class test_BOMManager(unittest.TestCase):
    #BOM管理模块测试
    log.info(u"~~~BOM管理模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_BOMManager(self):
        #BOM管理模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入BOM管理
        testModule(driver,u'基础信息',u'BOM管理')
        
 
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masBomHdAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(1)

    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#masBomHdToolbar  a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#masBomHdToolbar  a.easyui-linkbutton.findButton > span > span').click()
            WebWait(driver,"#masBomHdAccordion > div:nth-child(1) > div.panel-body.accordion-body > div > div > div.datagrid-mask-msgn")
            
            sleep(1)

        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#masBomHdToolbar  a.easyui-linkbutton.viewButton > span > span').click()
            sleep(1)

            self.assertEqual(u"编辑",driver.find_element_by_css_selector("#masBomHdForm  a.easyui-linkbutton.saveButton > span > span > span").text)


        elif button==u'编辑' or button=='edit':
            #点击“编辑”按钮
            driver.find_element_by_css_selector('#masBomHdForm  a.easyui-linkbutton.saveButton > span > span > span').click()
            sleep(1)
            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#masBomHdToolbar   a.easyui-linkbutton.editButton > span > span').click()
            WebWait(driver,"#masBomHdForm  div.datagrid-mask-msgn")
            sleep(1)
    

    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#masBomHdToolbar   a.easyui-linkbutton.deleteButton > span > span').click()
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
            driver.find_element_by_css_selector('#masBomHdForm > div:nth-child(1) > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            #取消
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            
            sleep(1)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("#masBomHdForm > div:nth-child(1) > a.easyui-linkbutton.saveButton > span > span > span").click()
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


    def select_comtype(self):
        '''选择商品类别'''

        driver=self.driver

        #选择类别
        findCss(driver,"#qsmaspartclasswindowZtree_2_ul li:nth-child(1) > a#qsmaspartclasswindowZtree_3_a > span").click()
        sleep(0.5)
        global com_type
        com_type=findCss(driver,"body > div:nth-child(20) > div.panel-body.panel-body-noborder.window-body.panel-noscroll  table.datagrid-btable td[field='fdName']").text
        sleep(0.5)
        
        findCss(driver,"body > div:nth-child(20) > div.panel-body.panel-body-noborder.window-body.panel-noscroll  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        #选择
        findCss(driver,"body > div:nth-child(20) a.easyui-linkbutton.saveButton.l-btn.l-btn-plain > span > span > span").click()
        sleep(0.5)
        return com_type

        
    def test_0add_BOM(self):
        u'''添加BOM'''
        
        driver=self.driver
        
        #进入BOM管理
        self.to_BOMManager()

        #添加
        self.clickButton(u"添加")

        #选择商品类别
        findCss(driver,"#masBomHdForm  tr:nth-child(1) > td:nth-child(7) > span > input.combo-text.validatebox-text.validatebox-invalid").click()
        sleep(1)
        self.select_comtype()

        #选择商品编码
        global com_code
        findCss(driver,"#masBomHdForm tr:nth-child(1) > td:nth-child(9) > span > input.combo-text.validatebox-text.validatebox-invalid").click()
        sleep(0.5)
        cd=findCss(driver,"body > div:nth-child(16) > div.combo-panel.panel-body.panel-body-noheader > div")
        com_code=cd.text
        #print com_code
        sleep(0.5)
        cd.click()
        sleep(0.5)
        
        
        #保存
        self.clickButton(u"保存")
        


    def test_1search_byCommodityCategory(self):
        u'''按商品类别查找'''
        
        driver=self.driver
        
        #进入BOM管理
        self.to_BOMManager()

        #选择商品类别
        findCss(driver,"#masBomHdToolbar > span:nth-child(2) > input.combo-text.validatebox-text").click()
        sleep(1)
        com_type=self.select_comtype()
        #print com_type

        #查找
        self.clickButton(u"查找")

        #断言
        tps=findsCss(driver,"#masBomHdAccordion > div:nth-child(1)  table.datagrid-btable  td[field='partClassKey']")
        searchAssert(self,tps,com_type)
        

    def test_2search_byCommodityCode(self):
        u'''按商品编码查找'''
        
        driver=self.driver
        
        #进入BOM管理
        self.to_BOMManager()

        #选择商品编码
        findCss(driver,"#masBomHdToolbar > span:nth-child(4) > input.combo-text.validatebox-text").click()
        sleep(0.5)
        code=com_code

        cds=findsCss(driver,"body > div:nth-child(17) > div > div.combobox-item")
        n=0
        for cd in cds:
            #print cd.text
            n+=1
            if cd.text == code:
                findCss(driver,"body > div:nth-child(17) > div > div:nth-child("+str(n)+")").click()
                break
        sleep(0.5)
        #查找
        self.clickButton(u"查找")
        
        while 1:
            try:
                driver.implicitly_wait(0)
                WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#masBomHdAccordion div.datagrid-mask-msg")))
                #print findCss(driver,"#masBomHdAccordion  div.datagrid-mask-msg").text
                
                continue
                
            except:
                break
            
            finally:
                driver.implicitly_wait(30)
              
            
        #断言
        cdps=findsCss(driver,"#masBomHdAccordion  table.datagrid-btable  td[field='masPartDtSkuKey']")
        searchAssert(self,cdps,code)

    def test_3view_BOM(self):
        u'''查看BOM'''
        
        driver=self.driver
        
        #进入BOM管理
        self.to_BOMManager()

        #选择一个BOM
        findCss(driver,"#masBomHdAccordion  table.datagrid-btable  td[field='ck']").click()
        sleep(0.5)
        #查看
        self.clickButton(u"查看")
        sleep(5)

        #编辑
        self.clickButton(u"编辑")
        sleep(5)

        #保存
        self.clickButton(u"保存")
        
        


    def test_4modify_BOM(self):
        u'''修改BOM'''
        
        driver=self.driver
        
        #进入BOM管理
        self.to_BOMManager()

        #选择一个BOM
        findCss(driver,"#masBomHdAccordion > div:nth-child(1)  table.datagrid-btable  td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u"修改")
   
        #修改商品编号
        findCss(driver,"#masBomHdForm tr:nth-child(1) > td:nth-child(9) > span > input.combo-text.validatebox-text.validatebox-invalid").click()
        sleep(0.5)
        findCss(driver,"body > div:nth-child(16) > div.combo-panel.panel-body.panel-body-noheader > div:nth-child(2)").click()
        

        #保存
        self.clickButton(u"保存")
        

    def test_5delete_BOM(self):
        u'''删除BOM'''
        
        driver=self.driver
        
        #进入BOM管理
        self.to_BOMManager()

        #选择一个BOM
        findCss(driver,"#masBomHdAccordion table.datagrid-btable  td[field='ck']").click()
        sleep(0.5)

        #删除
        self.clickButton(u"删除")
        
    
    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_BOMManager start--')
    suite=unittest.TestSuite()
    
    #suite.addTest(test_BOMManager('test_0add_BOM'))#添加BOM
    #suite.addTest(test_BOMManager('test_1search_byCommodityCategory'))#按商品类别查找
    #suite.addTest(test_BOMManager('test_2search_byCommodityCode'))#按商品编码查找
    #suite.addTest(test_BOMManager('test_3view_BOM'))#查看BOM
    #suite.addTest(test_BOMManager('test_4modify_BOM'))#修改BOM
    suite.addTest(test_BOMManager('test_5delete_BOM')) #删除BOM
   
    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_BOMManager end--')
        
