# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest,time,sys,xml.dom.minidom
from time import sleep
sys.path.append(r'D:\ISS\Test_Cases\public')

import login
from isspublic import*

#打开xml文档
dom=xml.dom.minidom.parse(r'D:\ISS\Test_Data\login.xml')

#得到文档元素对象
root=dom.documentElement


class Test_CustomizedOrders(unittest.TestCase):
    #订制订单
    log.info(u"~~~订制订单模块测试~~~")

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        self.verificationErrors = []

    def to_CommodityOrder(self):
        '''进入订单定制模块'''
        
        #登录进入ISS页面
        driver = self.driver
        driver.get(self.base_url)
        #获得success 标签的username、passwrod 属性值
        logins = root.getElementsByTagName('login')
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        #登录
        login.login(self,username,password)
        sleep(0.5)
        #进入订制订单
        testModule(driver,u'订单管理',u'订制订单')

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#saleOrdHdAccordion table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
       
        sleep(1)
        #需求：订单列表默认显示已付款的订单
        orders=driver.find_elements_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdOrdStatus']")
        
        for order in orders: 
            self.assertEqual(u"已付款",driver.find_element_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdOrdStatus']").text)
        


    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#saleOrdMeasureHdToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
            
            
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#saleOrdHdToolbar > a.easyui-linkbutton.findButton > span > span').click()
            
            sleep(1)
            WebWait(driver,"#saleOrdHdAccordion div.datagrid-mask")
            sleep(0.5)
            
            
            
        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#saleOrdHdToolbar > a.easyui-linkbutton.viewButton > span > span').click()
            sleep(0.5)

            #获取断言信息进行断言
            self.assertEqual(u"订单明细", driver.find_element_by_css_selector("#saleOrdHdForm > div.easyui-tabs.tabs-container > div.tabs-header.tabs-header-plain.tabs-header-noborder  span.tabs-title").text)
            
            
            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#saleOrdMeasureHdToolbar > a.easyui-linkbutton.editButton  > span > span').click()
            sleep(1)

        elif button==u'修改商品状态' or button=='modifys':
 
            #点击“查看”按钮
            driver.find_element_by_css_selector('#masPartHdToolbar > a.easyui-linkbutton.editMasPartHdStatus').click()
            sleep(1)
            

        elif button==u'编辑' or button=='edit':
            #查看界面，点击“编辑”按钮
            driver.find_element_by_css_selector("#saleOrdMeasureHdForm > div > a.easyui-linkbutton.saveButton > span > span").click()
            sleep(0.5)
            
            
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#saleOrdMeasureHdToolbar > a.easyui-linkbutton.deleteButton > span > span').click()
            sleep(0.5)

            #点击确认，删除记录并断言
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            sleep(1)
            dele_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text
            #print dele_text
            log.info(dele_text)
            self.assertEqual(u"删除成功",dele_text)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮
            driver.find_element_by_css_selector("#saleOrdMeasureHdForm > div > a.easyui-linkbutton.saveButton > span > span").click()
            sleep(0.5)
            
             #获取断言信息
            success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
            tip_text=success.text
            
            #确定,关闭提示框
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()
            sleep(1)
            #断言是否保存成功
            self.assertEqual(u"保存成功！",tip_text)
            
        
        else:
            raise NameError('No Such Button,confirm again please')
        
        

    def test_0CommoditySeason_check(self):
        u'''查看订制订单信息'''
        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入订制订单模块
        self.to_CommodityOrder()

    
        
        #选中订单号
        driver.find_element_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #点击查看
        self.clickButton(u"查看")

        sleep(1)
        
        

    def test_1search_by_OrderDate(self):
        u'''按订单日期进行搜索订单'''

        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入订制订单模块
        self.to_CommodityOrder()


        start_time='2016-03-1'
        end_time='2016-03-20'
        #将输入时间转化为时间戳
        tt1=toTime("%Y-%m-%d",start_time)
        tt2=toTime("%Y-%m-%d",end_time)
        
        #定位订单日期前缀并选择订单日期
        driver.find_element_by_css_selector("#saleOrdHdToolbar > span:nth-child(2) > input.combo-text.validatebox-text").clear()
        driver.find_element_by_css_selector("#saleOrdHdToolbar > span:nth-child(2) > input.combo-text.validatebox-text").send_keys(start_time)

        sleep(0.5)        
        
        driver.find_element_by_css_selector("#saleOrdHdToolbar > span:nth-child(4) > input.combo-text.validatebox-text").clear()
        driver.find_element_by_css_selector("#saleOrdHdToolbar > span:nth-child(4) > input.combo-text.validatebox-text").send_keys(end_time)
        
        sleep(0.5)
        
        #定位查找按钮
        self.clickButton(u"查找")

        time.sleep(3)
        
        #获取结果的订单日期
        dates=driver.find_elements_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdOrdDate']")
        
        for date in dates:
            #print date.text
            #将查找结果转化为时间戳
            tt=toTime("%Y-%m-%d",date.text)
            
            #print tt
            
            if tt>tt1 or tt==tt1:
                if tt<tt2 or tt==tt2:
                    a=True
                    continue
                a=False
                break
            else:a=False

            if not a:
                log.info(u"日期查找失败")
                raise NameError ("search Failed")
            
            
        
    def test_2search_by_TheOrderNumber(self):
        u'''按订单号进行搜索'''

        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入订制订单模块
        self.to_CommodityOrder()

        sleep(0.5)
        
        #获取第一条记录的订单号
        code=driver.find_element_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdCode']").text
        sleep(0.5)

        
        driver.find_element_by_css_selector("#saleOrdHdToolbar > input:nth-child(5)").send_keys(code)

        sleep(0.5)

        #点击查找按钮
        self.clickButton(u"查找")
        sleep(3)
        
        #获取断言信息
     
        self.assertEqual(code,driver.find_element_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdCode']").text)

              
    def test_3search_by_TransactionNumber(self):
        u'''按交易号进行搜索'''

        driver=self.driver

        #进入订制订单模块
        self.to_CommodityOrder()

        sleep(0.5)
        
        #获取第一条记录的交易号
        code=driver.find_element_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdTradingCode']").text
        sleep(0.5)

        
        #在交易号输入要搜索的数据
        driver.find_element_by_css_selector("#saleOrdHdToolbar > input:nth-child(6)").send_keys(code)
        sleep(0.5)

        #点击查找按钮
        self.clickButton(u"查找")

        sleep(3) 
        
        #获取断言信息
        
        self.assertEqual(code,driver.find_element_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdTradingCode']").text)


    def test_4search_by_TheOrderStatus(self):
        u'''按订单状态进行搜索'''

        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入订制订单模块
        self.to_CommodityOrder()

        sleep(0.5)
        
        #订单状态输入框不选择状态
        driver.find_element_by_css_selector("#saleOrdHdToolbar > span:nth-child(9) > input.combo-text.validatebox-text").click()
        sleep(0.5)
        driver.find_element_by_css_selector("body > div:nth-child(24) > div > div:nth-child(8)").click()
        sleep(0.5)

        #选择订单状态，未付款
        ol=driver.find_element_by_css_selector("body > div:nth-child(24) > div > div:nth-child(2)")
        orderstatus=ol.text
        ol.click()
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        sleep(3)

        #获取断言信息
        ots=driver.find_elements_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdOrdStatus']")
        for ot in ots:
            self.assertEqual(orderstatus,ot.text)

    def test_5search_by_PaymentStatus(self):
        u'''按支付状态进行搜索'''


        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入订制订单模块
        self.to_CommodityOrder()

        sleep(0.5)
        
        #订单状态输入框不选择状态
        driver.find_element_by_css_selector("#saleOrdHdToolbar > span:nth-child(9) > input.combo-text.validatebox-text").click()
        sleep(0.5)
        driver.find_element_by_css_selector("body > div:nth-child(24) > div > div:nth-child(8)").click()
        sleep(0.5)

        #选择支付状态
        driver.find_element_by_css_selector("#saleOrdHdToolbar > span:nth-child(12) > input").click()
        sleep(0.5)
        psy=driver.find_element_by_css_selector("body > div:nth-child(25) > div > div[value='10020501']")
        
        #获取要选择的支付状态
        paystate=psy.text
        #print paystate
        sleep(0.5)
        #选择
        psy.click()
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        
        sleep(3)
        
        #获取断言信息
        ps=driver.find_elements_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdPayStatusKey']")
        for p in ps:
            self.assertEqual(paystate,p.text)


    def test_6search_by_TheConsignee(self):
        u'''按收货人进行搜索'''


        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入订制订单模块
        self.to_CommodityOrder()

        sleep(0.5)

        
        #获取第一条记录的手机号码

        user=driver.find_element_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdCargoUserName']").text
        sleep(0.5)
        
        driver.find_element_by_css_selector("#saleOrdHdToolbar > input:nth-child(14)").send_keys(user)
        sleep(0.5)

        #点击查找按钮
        self.clickButton(u"查找")
        sleep(3)
        
        #获取断言信息
        urs=driver.find_elements_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdCargoUserName']")
        for ur in urs:
            self.assertEqual(user,ur.text)

    def test_7search_by_ConsigneePhone(self):
        u'''按收货人手机进行搜索'''

        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入订制订单模块
        self.to_CommodityOrder()

        sleep(0.5)

        #获取第一条记录的手机号码

        phone=driver.find_element_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdCargoMobile']").text
        sleep(0.5)
        
        driver.find_element_by_css_selector("#saleOrdHdToolbar > input:nth-child(15)").send_keys(phone)
        sleep(0.5)


        #点击查找按钮
        self.clickButton(u"查找")

        sleep(3)
        
        #获取断言信息
        phs=driver.find_elements_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdCargoMobile']")
        for ph in phs:   
            self.assertEqual(phone,ph.text)


    def test_8search_by_Store(self):
        u'''按店铺为莲花专卖店进行搜索'''

        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入订制订单模块
        self.to_CommodityOrder()

        sleep(0.5)

        #选择店铺查找
        store=u"莲花专卖店"
        driver.find_element_by_css_selector("#saleOrdHdToolbar > span:nth-child(18) > input.combo-text.validatebox-text").send_keys(store)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        sleep(3)

        #断言
        sts=driver.find_elements_by_css_selector("#saleOrdHdAccordion table.datagrid-btable td[field='fdShopDpt']")
        for st in sts:
            self.assertEqual(store,st.text)


               
   
    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    
    #构造测试集
    suite = unittest.TestSuite()
    
    #选择执行的测试用例
    #suite.addTest(Test_CustomizedOrders("test_0CommoditySeason_check")) #查看订制订单
    #suite.addTest(Test_CustomizedOrders("test_1search_by_OrderDate"))#按订单日期查找
    #suite.addTest(Test_CustomizedOrders("test_2search_by_TheOrderNumber"))#按订单号查找
    #suite.addTest(Test_CustomizedOrders("test_3search_by_TransactionNumber"))#按交易号查找
    suite.addTest(Test_CustomizedOrders("test_4search_by_TheOrderStatus"))#按订单状态查找
    #suite.addTest(Test_CustomizedOrders("test_5search_by_PaymentStatus"))#按支付状态查找
    #suite.addTest(Test_CustomizedOrders("test_6search_by_TheConsignee"))#按收货人查找
    #suite.addTest(Test_CustomizedOrders("test_7search_by_ConsigneePhone"))#按收货人手机查找
    #suite.addTest(Test_CustomizedOrders("test_8search_by_Store"))#按店铺查找

 
    #执行测试
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
        


