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




class test_OfflinePromotionRelation(unittest.TestCase):
    #线下促销关系模块测试
    log.info(u"~~~线下促销关系模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_OfflinePromotionRelation(self):
        #进入线下促销关系模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入线下促销关系
        testModule(driver,u'促销方案管理',u'线下促销关系')
        
        try:
            driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='ck']")
        except: 
            raise NameError(u"页面未刷新")
            log.error(u"页面无法刷新")

        sleep(1)
    
    def clickButton(self,button):
        u'''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'互容' or button=='mutual':
            #点击互容按钮
            driver.find_element_by_css_selector('#salePmOfflineRelateToolbar > a.easyui-linkbutton.mutualButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#salePmOfflineRelateToolbar > a.easyui-linkbutton.findButton > span > span').click()
            sleep(1)
            
        elif button==u'互斥' or button=='mutex':
            #点击互斥
            driver.find_element_by_css_selector('#salePmOfflineRelateToolbar > a.easyui-linkbutton.mutexButton > span > span').click()
            sleep(1)

        elif button==u"确定" or button=="sure":
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            sleep(1)

        elif button==u"取消" or button=="cancel":
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            sleep(1)
                
    
       
            
        else:
            raise NameError('No Such Button,confirm again please')


    def searchassert(self,th1s,th2s,theme):
        '''本函数用于促销关系查找断言'''
        thh1=[]
        a=''
        for th1 in th1s:
            #print th1.text
            thh1.append(th1.text)
        
        sleep(0.5)
        
        #读取促销主题2
        thh2=[]
        
        for th2 in th2s:
            #print th2.text
            thh2.append(th2.text)
            
        sleep(0.5)
        
        #任意一组，主题1和主题2有一个满足查找条件则查找成功
        n=len(thh1)
        for i in range(n):
            if theme in thh1[i] or theme in thh2[i]:
                a=True
            else:
                a=False
                break
        if a=='':
            raise NameError("Without Data be Searched!!!")
        
        self.assertTrue(a,'Seach Failed!!!'+theme)
        

        
    def test_0search_byPromotionTheme(self):
        u'''按促销主题查找'''
        driver=self.driver

        #进入线上促销关系
        self.to_OfflinePromotionRelation()

        #输入促销主题
        theme=u"促销"
        findCss(driver,"#salePmOfflineRelateToolbar > input:nth-child(1)").send_keys(theme)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        

        #读取促销主题1
        th1s=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='saleTheme']")
        #读取促销主题2
        th2s=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='rsaleTheme']")
        #断言
        self.searchassert(th1s,th2s,theme)
        
    """
        
    def test_1search_byChannel(self):
        u'''按渠道查找'''
        driver=self.driver

        #进入线上促销关系
        self.to_OlinePromotionRelation()


    def test_2search_byApplicableObject(self):
        u'''按适用对象查找'''
        driver=self.driver

        #进入线上促销关系
        self.to_OlinePromotionRelation()
        
        """

    def test_3search_byDocumentCode(self):
        u'''按单据编号查找'''
        driver=self.driver

        #进入线上促销关系
        self.to_OfflinePromotionRelation()

        #输入单据编号
        doc_code="PM201603240002"
        findCss(driver,"#salePmOfflineRelateToolbar > input:nth-child(6)").send_keys(doc_code)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        
        #读取促销主题1
        cd1s=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='salePmCode']")
        
        #读取促销主题2
        cd2s=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='rsalePmCode']")
        
        #断言
        self.searchassert(cd1s,cd2s,doc_code)
        

    def test_4button_Mutual(self):
        u'''互容操作'''
        driver=self.driver

        #进入线上促销关系
        self.to_OfflinePromotionRelation()

        #查找出互斥的促销关系
        rels=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='relationName']")
        n=0
        
        for rel in rels:
            n+=1
            if rel.text==u"互斥":
                findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable tr:nth-child("+str(n)+") > td[field='ck']").click()
                break
            else:
                raise NameError("without the relationship!!")
            
        sleep(0.5)

        #点击互容
        self.clickButton(u"互容")

        #确定
        self.clickButton(u"确定")

        #断言
        self.assertEqual(u"促销关系更改成功",findCss(driver,"body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text)
        


    def test_5button_Mutex(self):
        u'''互斥操作'''
        driver=self.driver

        #进入线上促销关系
        self.to_OfflinePromotionRelation()

        #查找出互容的促销关系
        rels=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable td[field='relationName']")
        n=0
        
        for rel in rels:
            n+=1
            if rel.text==u"互容":
                findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable tr:nth-child("+str(n)+") > td[field='ck']").click()
                break
        sleep(0.5)

        #点击互容
        self.clickButton(u"互斥")

        #确定
        self.clickButton(u"确定")

        #断言
        self.assertEqual(u"促销关系更改成功",findCss(driver,"body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text)
        
        

    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_OfflinePromotionRelation start--')
    
    suite=unittest.TestSuite()
    
    suite.addTest(test_OfflinePromotionRelation('test_0search_byPromotionTheme'))#按促销主题查找
    suite.addTest(test_OfflinePromotionRelation('test_3search_byDocumentCode'))#按单据编号查找
    suite.addTest(test_OfflinePromotionRelation('test_4button_Mutual'))#互容操作
    suite.addTest(test_OfflinePromotionRelation('test_5button_Mutex'))#互斥操作
   
    #执行测试
    
    runner=unittest.TextTestRunner()
    runner.run(suite)

    #unittest.main()

    
    log.info('test_OfflinePromotionRelation end--')
        
