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

#促销编号
pro_code='PM201604110005'

#促销主题
pro_theme=u"促销"


class test_OfflinePromotion(unittest.TestCase):
 
    log.info(u"~~~线下促销模块测试~~~")
    
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_OfflinePromotion(self):
        #进入线下促销
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入线下促销
        testModule(driver,u'促销方案管理',u'线下促销')
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='ck']")
        log.info(u"刷新完成！！！")
        sleep(1)

        
    def Delete_And_Add_Assert(self,opera,a=True):
        '''本函数用于添加和删除成功时的断言'''
        driver=self.driver
        
        if opera=='delete':
             #点击确认，删除记录并断言
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            sleep(1)
            if a:
                dele_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text
            else:
                dele_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text
            #print dele_text
            log.info(dele_text)
            self.assertEqual(u"删除成功",dele_text)
            #确定
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()


        elif opera=='add':
            #将提示信息写入log    
            log.info(driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text)
            #断言是否保存成功
            self.assertEqual(u"保存成功！",driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text)
            sleep(0.5)
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()
            sleep(1)
            

    def clickButton(self,button):
        u'''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#salePmOfflineListRToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#salePmOfflineListRToolbar > a.easyui-linkbutton.findButton > span > span').click()
            WebWait(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) > div > div > div > div > div.datagrid-mask")
            sleep(1)

        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#editButton > span > span').click()
            sleep(1)

            self.assertEqual(u"返回",driver.find_element_by_css_selector("#salePmOfflineHdToolbar > a.easyui-linkbutton.returnButton > span > span").text)
            
        elif button==u'返回' or button=='return':
            #点击“返回”按钮
            driver.find_element_by_css_selector('#salePmOfflineHdToolbar > a.easyui-linkbutton.returnButton > span > span').click()
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#editButton > span > span').click()
            sleep(1)
                
    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#salePmOfflineListRToolbar > a.easyui-linkbutton.deleteButton > span > span').click()
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
            driver.find_element_by_css_selector('#stmShippingForm > div:nth-child(1) > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            #取消
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            
            sleep(1)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("#saveButton > span > span > span").click()
            sleep(0.5)
            
             #获取断言信息
            
            success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
            tip_text=success.text
            log.info(tip_text)
            
            #确定,关闭提示框
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

            #断言是否保存成功
            self.assertEqual(u"保存成功！",tip_text)

        elif button==u'审批' or button=='check':
            #编辑界面，点击“审批”按钮
            driver.find_element_by_css_selector('#salePmOfflineHdToolbar > a.easyui-linkbutton.checkButton > span > span').click()
            sleep(0.5)
            #确定审批
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            sleep(0.5)
            #断言是否审批成功
            self.assertEqual(u"审批成功！",driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text)
            sleep(1)
            #确定
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()
            
        elif button==u'终止' or button=='stop':
            #编辑界面，点击“终止”按钮
            driver.find_element_by_css_selector('#salePmOfflineHdToolbar > a.easyui-linkbutton.checkButton > span > span').click()
            sleep(0.5)
            #确定终止
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            sleep(1)
            #print driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text
            #断言是否终止成功
            self.assertEqual(u"已终止！",driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text)

            
        else:
            raise NameError('No Such Button,confirm again please')

        
    def test_0add_Promotion(self):
        u'''添加促销'''

        driver=self.driver
        #进入线下促销
        self.to_OfflinePromotion()

        
        def select(localtion):
            '''用于下拉选择第一个选项'''
            localtion.click()
            sleep(0.5)
            localtion.send_keys(Keys.DOWN)
            sleep(0.5)
            localtion.send_keys(Keys.ENTER)
            sleep(0.5)


        
        
        #添加
        self.clickButton(u"添加")

        #促销主题
        theme=pro_theme
        findCss(driver,"#salePmOfflineHdForm  tr:nth-child(1) > td:nth-child(13) > input").send_keys(theme)
        sleep(0.5)

        #优先级
        findCss(driver,"#salePmOfflineHdForm  tr:nth-child(2) > td:nth-child(4) > input").send_keys('5')
       
        sleep(0.5)


        #活动对象
        aob=findCss(driver,"#salePmOfflineHdForm  tr:nth-child(2) > td:nth-child(6) > span > input.combo-text.validatebox-text.validatebox-invalid")
        select(aob)
        
        #渠道
        ch=findCss(driver,"#salePmOfflineHdForm  tr:nth-child(2) > td:nth-child(8) > span > input.combo-text.validatebox-text.validatebox-invalid")
        select(ch)

        #促销方式
        prw=findCss(driver,"#salePmOfflineHdForm tr:nth-child(3) > td:nth-child(2) > span > input.combo-text.validatebox-text.validatebox-invalid")
        select(prw)

        #促销类型
        prt=findCss(driver,"#salePmOfflineHdForm  tr:nth-child(3) > td:nth-child(4) > span > input.combo-text.validatebox-text.validatebox-invalid")
        select(prt)
        
        #起始日期
        date_start=findCss(driver,"#salePmOfflineHdForm tr:nth-child(4) > td:nth-child(2) > span > input.combo-text.validatebox-text.validatebox-invalid")
        
        date_start.click()
        sleep(0.5)
        date_start.send_keys(Keys.ENTER)
        sleep(0.5)
        
        #结束日期
        date_end=findCss(driver,"#salePmOfflineHdForm  tr:nth-child(4) > td:nth-child(4) > span > input.combo-text.validatebox-text.validatebox-invalid")
        date_end.click()
        sleep(0.5)
        date_end.send_keys(Keys.ENTER)
        sleep(0.5)

        #捆绑方式
        bd=findCss(driver,"#salePmOfflineHdForm  tr:nth-child(3) > td:nth-child(6) > span > input.combo-text.validatebox-text.validatebox-invalid")
        select(bd)


        #限定时间
        findCss(driver,"#salePmOfflineHdForm > table > tbody > tr:nth-child(5) > td:nth-child(2) > input").click()
        sleep(0.5)

        #保存
        self.clickButton(u"保存")

        #返回
        #self.clickButton(u"返回")
        driver.refresh()

        #进入线下促销
        testModule(driver,u'促销方案管理',u'线下促销')
        

        #等待界面刷新
        log.info(u"刷新~~~")
        isRefreshed(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='ck']")

        #读取新添加促销的促销编号
        global pro_code
        pro_code=findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='fdCode']").text
        #print pro_code
        


    def searchbykey(self,keys):
        '''用于按关键字查找促销'''

        driver=self.driver

        #输入关键字
        findCss(driver,"#salePmOfflineListRToolbar > input.easyui-validatebox.validatebox-text").clear()
        sleep(0.5)
        findCss(driver,"#salePmOfflineListRToolbar > input.easyui-validatebox.validatebox-text").send_keys(keys)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")
        sleep(3)

        #断言
        #获取编号
        code=findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='fdCode']").text
        #获取主题
        ths=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='saleTheme']")
        for th in ths:
            #print th.text
            if keys in th.text or code==keys:
                a=True
                continue
            else:
                a=False
                break
        self.assertTrue(a,"search Failed!!!"+keys)
        sleep(0.5)

    def test_1search_byKeyWord(self):
        u'''按关键字查找促销'''

        
        driver=self.driver

        #进入线下促销
        self.to_OfflinePromotion()
        sleep(0.5)

        #获取全部数据记录条数
        allre=findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) div.datagrid-pager.pagination > div.pagination-info").text
        #print allre
        

        #输入编号查找
        code=findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='fdCode']").text
        self.searchbykey(code)

        #清空输入框内容，查找
        findCss(driver,"#salePmOfflineListRToolbar > input.easyui-validatebox.validatebox-text").clear()
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        sleep(3)

        #断言是否查找出全部记录
        self.assertEqual(allre,findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) div.datagrid-pager.pagination > div.pagination-info").text)

        #输入促销主题查找
        theme=findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='saleTheme']").text
        self.searchbykey(theme)

    
    def test_2search_byActivityTime(self):
        u'''按活动时间查找'''

        
        driver=self.driver

        #进入线下促销
        self.to_OfflinePromotion()

        #设置要查找的时间
        start_time='2016-03-01'
        end_time='2016-03-30'
        #将时间传化为时间戳
        tt1=toTime("%Y-%m-%d",start_time)
        tt2=toTime("%Y-%m-%d",end_time)

        sleep(0.5)
        #输入时间查找
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(3) > input.combo-text.validatebox-text").send_keys(start_time)
        sleep(0.5)
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(3) > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        sleep(0.5)
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(5) > input.combo-text.validatebox-text").send_keys(end_time)
        sleep(0.5)
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(5) > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")
        sleep(3)

        #获取查找结果
        #活动开始时间
        sts=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable  td[field='startDate']")
        #活动结束时间
        ets=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable  td[field='endDate']")

        #判断查找结果是否正确
        for st in sts:
            stt=toTime("%Y-%m-%d",st.text)
            #print st.text
            #print stt
            if stt > tt1 or stt==tt1:
                a=True
                continue
            else:
                a=False
                break
        for et in ets:
            ett=toTime("%Y-%m-%d",et.text)
            if ett < tt2 or ett == tt2:
                a=True
                continue
            else:
                a=False
                break
        #断言 
        self.assertTrue(a,"Search Failed!!!")
            
        
        
        

    def test_3search_byApplicableObject(self):
        u'''按适用对象查找'''

        
        driver=self.driver

        #进入线上促销
        self.to_OfflinePromotion()

        #选择适用对象
        obj=u'九牧王'
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(7) > input.combo-text.validatebox-text").send_keys(obj)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")

        #断言
        objs=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='suitObj']")
        searchAssert(self,objs,obj)

        
    def test_4search_byMakeDate(self):
        u'''按制单日期查找'''

        
        
        driver=self.driver

        #进入线下促销
        self.to_OfflinePromotion()

        #设置要查找的时间
        start_time='2016-03-20'
        end_time='2016-03-30'
        #将时间传化为时间戳
        tt1=toTime("%Y-%m-%d",start_time)
        tt2=toTime("%Y-%m-%d",end_time)

        sleep(0.5)
        #输入时间查找
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(9) > input.combo-text.validatebox-text").send_keys(start_time)
        sleep(0.5)
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(11) > input.combo-text.validatebox-text").send_keys(end_time)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")
        sleep(3)

        #获取查找结果
        mts=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='salePmDate']")

        for mt in mts:
            #将结果时间转化为时间戳
            mtt=toTime("%Y-%m-%d",mt.text)
            if mtt >tt1 or mtt ==tt1 or mtt < tt2 or mtt == tt2:
                b=True
                continue
            else:
                b=False
                break
        self.assertTrue(b,"Search Failed!!!")
        

    def test_5search_byIdentifyDocument(self):
        u'''按单据标识查找'''

        
        driver=self.driver

        #进入线下促销
        self.to_OfflinePromotion()

        #选择促销标识
        di=u"未审批"
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(15) > input").send_keys(di)
        sleep(0.5)
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(15) > input").send_keys(Keys.ENTER)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #断言
        dis=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='chkStatus']")
        searchAssert(self,dis,di)

    def test_6search_byPromotionType(self):
        u'''按促销类型查找'''

        
        driver=self.driver

        #进入线下促销
        self.to_OfflinePromotion()

        #选择促销类型
        types=u"捆绑"
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(17) > input.combo-text.validatebox-text").send_keys(types)
        sleep(0.5)
        findCss(driver,"#salePmOfflineListRToolbar > span:nth-child(17) > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        sleep(0.5)
        
        #查找
        self.clickButton(u"查找")

        #断言
        tps=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='salePmTypeName']")
        searchAssert(self,tps,types)


    def edit_Promotion(self):
        '''进入促销修改页面'''

        driver=self.driver

        #进入线下促销
        self.to_OfflinePromotion()

        #通过促销编号查找
        code=pro_code
        self.searchbykey(code)

        #选择记录
        findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u"修改")

        #页面等待
        print findCss(driver,"#salePmOfflineHdTabs > div.tabs-panels.tabs-panels-noborder > div:nth-child(1) > div > div > div > div > div.datagrid-mask-msgn").text
        WebWait(driver,"#salePmOfflineHdTabs > div.tabs-panels.tabs-panels-noborder > div:nth-child(1) > div > div > div > div > div.datagrid-mask-msgn")

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineHdTabs   table.datagrid-htable  td[field='seq']").text
        isRefreshed(driver,"#salePmOfflineHdTabs   table.datagrid-htable  td[field='seq']")
        log.info(u"刷新完成！！！") 
        
        


    def test_7modify_Promotion(self):
        u'''修改促销'''
        
        driver=self.driver

        #调用函数进入促销修改界面
        self.edit_Promotion()

    def test_8modify_AddRedemption_com(self):
        u'''添加换购品'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-换购品
        findCss(driver,"#salePmOfflineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(5) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineDtChangepurchaseAccordion   table.datagrid-htable  td[field='groupNum']").text
        isRefreshed(driver,"#salePmOfflineDtChangepurchaseAccordion   table.datagrid-htable  td[field='groupNum']")
        log.info(u"刷新完成！！！") 

        #添加商品类型
        #添加
        findCss(driver,"#salePmOfflineDtChangePurchaseToolbar > a.easyui-linkbutton.appendDataButton > span > span").click()

        #输入组号
        group_code='1'
        findCss(driver,"#salePmOfflineDtChangepurchaseAccordion  > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field=\"groupNum\"]  input").send_keys(group_code)
        sleep(0.5)

        #选择类型 
        tp=findCss(driver,"#salePmOfflineDtChangepurchaseAccordion > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field=\"partLevel\"]  input.combo-text.validatebox-text.validatebox-invalid")
        #tp.click()
        sleep(0.5)
        
        tp.send_keys(u"商品级")
        sleep(0.5)
        
        tp.send_keys(Keys.ENTER)
        sleep(0.5)

        #保存
        findCss(driver,"#salePmOfflineDtChangePurchaseToolbar > a.easyui-linkbutton.saveDataButton > span > span").click()
        sleep(1)
        
        #断言
        self.Delete_And_Add_Assert('add')

        #添加商品
        #选择已添加的商品类型
        findCss(driver,"#salePmOfflineDtChangepurchaseAccordion div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)
        findCss(driver,"#salePmOfflineDtChangepurchaseAccordion").send_keys(Keys.DOWN)
        sleep(0.5)
        
        
        #添加
        findCss(driver,"#salePmOfflineDtChangePurchaseShopChildrenGridToolbar > a.easyui-linkbutton.appendDataButton > span > span").click()
        sleep(0.5)

        #选择商品编码
        findCss(driver,"#salePmOfflineDtPartPurchaseShopLevel div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='masPartHd']  span.combo-arrow").click()
        sleep(0.5) 
        findCss(driver,"body > div:nth-child(25) > div > div:nth-child(1)").click()
        sleep(0.5)

        #折扣
        findCss(driver,"#salePmOfflineDtPartPurchaseShopLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='rebate']  input").send_keys('0.8')
        sleep(0.5)

        #数量
        findCss(driver,"#salePmOfflineDtPartPurchaseShopLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='qty']  input").send_keys('5')
        sleep(0.5)

        #保存
        findCss(driver,"#salePmOfflineDtChangePurchaseToolbar > a.easyui-linkbutton.saveDataButton > span > span").click()
        sleep(1)
        #断言
        self.Delete_And_Add_Assert('add')

        


    def test_9modify_AddTriggerPoint(self):
        u'''添加业务触发点'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()
        sleep(3)


        #添加触发点
        #添加
        findCss(driver,"#salePmOfflineDtTrgToolbar > a.easyui-linkbutton.addButton > span > span").click()
        sleep(0.5)


        #选择促销类型
        
        tp1=findCss(driver,"#fixedOfflineTrgArea td span.combo input.combo-text.validatebox-text.validatebox-invalid")
        tp1.click()
        sleep(0.5)
        tp1.send_keys(Keys.DOWN)
        sleep(0.5)
        tp1.send_keys(Keys.ENTER)
        sleep(1)

        #设置捆绑商品数量
        tp1.send_keys(Keys.TAB)
        sleep(0.5)
        tp2=findCss(driver,"#trgPmTypeBindProf td.easyui-myText input.easyui-numberbox.validatebox-text.validatebox-invalid")
        tp2.send_keys('3')
        sleep(0.5)

        #设置让利金额
        tp2.send_keys(Keys.TAB)
        sleep(0.5)
        tp3=findCss(driver,"#trgPmTypeBindProf td.easyui-myText input.easyui-numberbox.validatebox-text.validatebox-invalid")
        tp3.send_keys('100')
        sleep(0.5) 

        #换购品数量
        tp3.send_keys(Keys.TAB)
        findCss(driver,"#trgPmTypeBindProf td.easyui-myText input.easyui-numberbox.validatebox-text.validatebox-invalid").send_keys('2')
        sleep(0.5)
     
        #换购品组号
        tp3=findCss(driver,"#trgPmTypeBindProfSubjoin > td.easyui-myText > span > input.combo-text.validatebox-text.validatebox-invalid")
        tp3.click()
        sleep(0.5)
        
        tp3.send_keys(Keys.DOWN)
        sleep(0.5)
        tp3.send_keys(Keys.ENTER)
        sleep(0.5)

        #保存
        findCss(driver,"div.panel-body.panel-body-noborder.window-body.panel-noscroll > div > div.panel.layout-panel.layout-panel-center  a.easyui-linkbutton.addTermButton > span > span > span").click()
        sleep(1)
        
        #断言
        self.Delete_And_Add_Assert('add')

        #确定
        findCss(driver,"div.panel-body.panel-body-noborder.window-body.panel-noscroll > div > div.panel.layout-panel.layout-panel-center > div > div > div.panel.layout-panel.layout-panel-south > div > a > span > span > span").click()
        
    def test_amodify_DeleteTriggerPoint(self):
        u'''删除业务触发点'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #选择一个触发点
        findCss(driver,"#salePmOfflineDtTrgToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table  td[field='ck']>div>input").click()
        sleep(0.5)


        #删除
        findCss(driver,"#salePmOfflineDtTrgToolbar > a.easyui-linkbutton.deleteButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)
        sleep(1)


    def test_bmodify_DeleteRedemption_com(self):
        u'''删除换购品'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-换购品
        findCss(driver,"#salePmOfflineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(5) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineDtChangepurchaseAccordion   table.datagrid-htable  td[field='groupNum']").text
        isRefreshed(driver,"#salePmOfflineDtChangepurchaseAccordion   table.datagrid-htable  td[field='groupNum']")
        log.info(u"刷新完成！！！")
        

        #选择商品类别
        findCss(driver,"#salePmOfflineDtChangepurchaseAccordion div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        findCss(driver,"#salePmOfflineDtChangepurchaseAccordion").send_keys(Keys.DOWN)

        sleep(0.5)
        
        #选择商品
        findCss(driver,"#salePmOfflineDtPartPurchaseShopLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        #删除商品
        findCss(driver,"#salePmOfflineDtChangePurchaseShopChildrenGridToolbar > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)
        sleep(1)

        #删除商品类别
        findCss(driver,"#salePmOfflineDtChangePurchaseToolbar > a.easyui-linkbutton.removeDataChangeButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)



    def test_cmodify_AddSuitObject(self):
        u'''添加适用对象'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-适用对象设置
        findCss(driver,"#salePmOfflineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(2) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineHdTabs    table.datagrid-htable  td[field='dptKey']").text
        isRefreshed(driver,"#salePmOfflineHdTabs    table.datagrid-htable  td[field='dptKey']")
        log.info(u"刷新完成！！！") 

        
        #添加适用对象
        findCss(driver,"#salePmOfflineSuitObjectToolbar > a.easyui-linkbutton.addButton > span > span").click()
        sleep(0.5)

        #选择第一个店铺
        findCss(driver,"#salePmOfflineDtSuitObjectAddForm > div.left table.datagrid-btable td[field=\"ck\"]").click()
        sleep(0.5)

        #右移
        findCss(driver,"#salePmOfflineDtSuitObjectAddForm > div.middle > input.leftToRight").click()
        sleep(0.5)

        #保存
        findCss(driver,"#ordsalePmOfflineSuitObjectToolbarAddToolbar > a.easyui-linkbutton.saveButton > span > span").click()

        #断言
        self.Delete_And_Add_Assert('add')        

       
    def test_dmodify_DeleteSuitObject(self):
        u'''删除适用对象'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-适用对象设置
        findCss(driver,"#salePmOfflineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(2) > a > span.tabs-title").click()
        sleep(0.5)
        
        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineHdTabs    table.datagrid-htable  td[field='dptKey']").text
        isRefreshed(driver,"#salePmOfflineHdTabs    table.datagrid-htable  td[field='dptKey']")
        log.info(u"刷新完成！！！") 


        #选择适用对象
        findCss(driver,"#salePmOfflineSuitObjectToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        #删除
        findCss(driver,"#salePmOfflineSuitObjectToolbar > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)


    def test_emodify_Add_TimeConstraint(self):
        u'''添加时段约束'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-时段约束
        findCss(driver,"#salePmOfflineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(3) > a > span.tabs-title").click()
        sleep(0.5)
        
        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineHdTabs    table.datagrid-htable  td[field='startTime']").text
        isRefreshed(driver,"#salePmOfflineHdTabs    table.datagrid-htable  td[field='startTime']")
        log.info(u"刷新完成！！！") 

        #添加
        findCss(driver,"#salePmOfflineDtTimeToolbar > div > a.easyui-linkbutton.appendDataButton > span > span").click()
        sleep(0.5)
        
        #约束开始时间
        findCss(driver,"#salePmOfflineDtTimeToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='startTime'] span.spinner-arrow-down").click()
        sleep(0.5)
        
        #约束结束时间
        findCss(driver,"#salePmOfflineDtTimeToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='endTime'] span.spinner-arrow-up").click()
        sleep(0.5)

        #保存
        findCss(driver,"#salePmOfflineDtTimeToolbar > div > a.easyui-linkbutton.saveTimeButton > span > span").click()
        sleep(0.5)
        
        #断言
        self.Delete_And_Add_Assert('add')
        


    def test_fmodify_Delete_TimeConstraint(self):
        u'''删除时段约束'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-时段约束
        findCss(driver,"#salePmOfflineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(3) > a > span.tabs-title").click()
        sleep(0.5)
        
        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineHdTabs    table.datagrid-htable  td[field='startTime']").text
        isRefreshed(driver,"#salePmOfflineHdTabs    table.datagrid-htable  td[field='startTime']")
        log.info(u"刷新完成！！！") 

        #选择一条记录
        findCss(driver,"#salePmOfflineDtTimeToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)
        
        #删除
        findCss(driver,"#salePmOfflineDtTimeToolbar > div > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)
        
        #断言
        self.Delete_And_Add_Assert('delete',a=False)



    def test_gmodify_AddPromotion_com(self):
        u'''添加促销商品'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-促销商品
        findCss(driver,"#salePmOfflineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(4) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineDtPartAccordion    table.datagrid-htable  td[field='groupNum']").text
        isRefreshed(driver,"#salePmOfflineDtPartAccordion    table.datagrid-htable  td[field='groupNum']")
        log.info(u"刷新完成！！！")
        
        #添加商品类型
        #添加
        findCss(driver,"#salePmOfflineDtPartToolbar > a.easyui-linkbutton.appendDataButton > span > span").click()

        #输入组号
        group_code='1'
        findCss(driver,"#salePmOfflineDtPartAccordion > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field=\"groupNum\"]  input").send_keys(group_code)
        sleep(0.5)

        #选择类型
        tp=findCss(driver,"#salePmOfflineDtPartAccordion > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field=\"partLevel\"] input.combo-text.validatebox-text")
        tp.click()
        sleep(0.5)
        tp.send_keys(u"商品级")
        sleep(0.5)
        tp.send_keys(Keys.ENTER)
        sleep(0.5)

        #保存
        findCss(driver,"#salePmOfflineDtPartToolbar > a.easyui-linkbutton.saveDataButton > span > span").click()
        sleep(1)
        #断言
        self.Delete_And_Add_Assert('add')

        #添加商品
        #选择已添加的商品类型
        findCss(driver,"#salePmOfflineDtPartAccordion > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)
        findCss(driver,"#salePmOfflineDtPartAccordion").send_keys(Keys.DOWN)
        sleep(0.5)
        
        #添加
        findCss(driver,"#salePmOfflineDtPartPartLevelGridToolbar > a.easyui-linkbutton.appendDataButton > span > span").click()
        sleep(0.5)

        #选择商品编码
        findCss(driver,"#salePmOfflineDtPartPartLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='masPartHd']  span.combo-arrow").click()
        sleep(0.5)
        findCss(driver,"body > div:nth-child(25) > div > div:nth-child(1)").click()
        sleep(0.5)

        #折扣
        findCss(driver,"#salePmOfflineDtPartPartLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='rebate']  input").send_keys('0.8')
        sleep(0.5)

        #数量
        findCss(driver,"#salePmOfflineDtPartPartLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='qty']  input").send_keys('5')
        sleep(0.5)

        #保存
        findCss(driver,"#salePmOfflineDtPartToolbar > a.easyui-linkbutton.saveDataButton > span > span").click()
        sleep(1)
        #断言
        self.Delete_And_Add_Assert('add')

        
    def test_hmodify_DeletePromotion_com(self):
        u'''删除促销商品'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-促销商品
        findCss(driver,"#salePmOfflineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(4) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineDtPartAccordion    table.datagrid-htable  td[field='groupNum']").text
        isRefreshed(driver,"#salePmOfflineDtPartAccordion    table.datagrid-htable  td[field='groupNum']")
        log.info(u"刷新完成！！！")
        

        #选择商品类别
        findCss(driver,"#salePmOfflineDtPartAccordion > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        findCss(driver,"#salePmOfflineDtPartAccordion").send_keys(Keys.DOWN)

        sleep(0.5)
        
        #选择商品
        findCss(driver,"#salePmOfflineDtPartPartLevel div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        #删除商品
        findCss(driver,"#salePmOfflineDtPartPartLevelGridToolbar > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)

        #删除商品类别
        findCss(driver,"#salePmOfflineDtPartToolbar > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)


    def test_imodify_AddPayment(self):
        u'''添加结算方式'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-结算方式
        findCss(driver,"#salePmOfflineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(6) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineHdTabs   table.datagrid-htable  td[field='stmPayment']").text
        isRefreshed(driver,"#salePmOfflineHdTabs  table.datagrid-htable  td[field='stmPayment']")
        log.info(u"刷新完成！！！")

        #添加结算方式
        #添加
        findCss(driver,"#salePmOfflineDtPaymentToolbar > div > a.easyui-linkbutton.appendDataButton > span > span").click()
        sleep(0.5)
        

        #选择结算方式
        payment=u'支付宝支付'
        pl=findCss(driver,"#salePmOfflineDtPaymentToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body  td[field='stmPayment']  input.combo-text.validatebox-text.validatebox-invalid")
        pl.send_keys(payment)
        sleep(0.5)
        pl.send_keys(Keys.ENTER)
        
    
        #保存
        findCss(driver,"#salePmOfflineDtPaymentToolbar > div > a.easyui-linkbutton.saveButton > span > span > span").click()
        sleep(1)
        
        #断言
        self.Delete_And_Add_Assert('add')

       
        
    def test_jdelete_DeletePayment(self):
        u'''删除结算方式'''

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-结算方式
        findCss(driver,"#salePmOfflineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(6) > a > span.tabs-title").click()
        sleep(0.5)
        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOfflineHdTabs   table.datagrid-htable  td[field='stmPayment']").text
        isRefreshed(driver,"#salePmOfflineHdTabs  table.datagrid-htable  td[field='stmPayment']")
        log.info(u"刷新完成！！！")

        #选择一个结算方式
        findCss(driver,"#salePmOfflineDtPaymentToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body  td[field='ck']").click()
        sleep(0.5)


        #删除
        findCss(driver,"#salePmOfflineDtPaymentToolbar > div > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)
        sleep(1)




    def test_kdelete_Promotion(self):
        u'''删除促销'''
        
        driver=self.driver

        #进入线下促销
        self.to_OfflinePromotion()

        #通过促销编号查找
        code=pro_code
        self.searchbykey(code)

        #选择记录
        findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='ck']").click()
        sleep(0.5)

        #删除
        self.clickButton(u"删除")
           

    def test_lmodify_ApprovalStatus(self):
        u'''修改审批状态'''

        log.info(u"开始执行用例...")

        driver=self.driver

        #添加促销
        self.test_0add_Promotion()
        
        #选择添加的记录
        findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='ck']").click()
        sleep(0.5)
        
        #修改
        self.clickButton(u"修改")
        sleep(0.5)

        #审批
        self.clickButton(u"审批")

        #终止
        self.clickButton(u"终止")

        
    
        

   
        
    def tearDown(self):
        log.info("该条用例执行执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':

    
    #建立测试集
    logging.info('test_OnlinePromotion start--')
    
    suite=unittest.TestSuite()
    
    suite.addTest(test_OfflinePromotion('test_0add_Promotion'))#添加促销方案
    
    suite.addTest(test_OfflinePromotion('test_1search_byKeyWord'))#按关键字查找
    suite.addTest(test_OfflinePromotion('test_2search_byActivityTime'))#按活动时间查找
    suite.addTest(test_OfflinePromotion('test_3search_byApplicableObject'))#按适用对象查找
    suite.addTest(test_OfflinePromotion('test_4search_byMakeDate'))#按制单日期查找
    suite.addTest(test_OfflinePromotion('test_5search_byIdentifyDocument'))#按单据标识查找
    suite.addTest(test_OfflinePromotion('test_6search_byPromotionType'))#按促销类型查找
    suite.addTest(test_OfflinePromotion('test_7modify_Promotion'))#修改促销
    
    suite.addTest(test_OfflinePromotion('test_8modify_AddRedemption_com'))#添加换购品
    
    suite.addTest(test_OfflinePromotion('test_9modify_AddTriggerPoint'))#添加业务触发点
    suite.addTest(test_OfflinePromotion('test_amodify_DeleteTriggerPoint'))#删除业务触发点

    suite.addTest(test_OfflinePromotion('test_bmodify_DeleteRedemption_com'))#删除换购品

    suite.addTest(test_OfflinePromotion('test_cmodify_AddSuitObject'))#添加适用对象
    suite.addTest(test_OfflinePromotion('test_dmodify_DeleteSuitObject'))#删除适用对象

    suite.addTest(test_OfflinePromotion('test_emodify_Add_TimeConstraint'))#添加时段约束
    suite.addTest(test_OfflinePromotion('test_fmodify_Delete_TimeConstraint'))#删除时段约束

    suite.addTest(test_OfflinePromotion('test_gmodify_AddPromotion_com'))#添加促销商品
    suite.addTest(test_OfflinePromotion('test_hmodify_DeletePromotion_com'))#删除促销商品

    suite.addTest(test_OfflinePromotion('test_imodify_AddPayment'))#添加结算方式
    suite.addTest(test_OfflinePromotion('test_jdelete_DeletePayment'))#删除结算方式

    #suite.addTest(test_OfflinePromotion('test_kdelete_Promotion'))#删除促销
    
    #suite.addTest(test_OfflinePromotion('test_lmodify_ApprovalStatus'))#修改审批状态
   
    #执行测试
    
    runner=unittest.TextTestRunner()
    runner.run(suite)

    #unittest.main()

    
    log.info('test_DefaultExpress end--')
        
