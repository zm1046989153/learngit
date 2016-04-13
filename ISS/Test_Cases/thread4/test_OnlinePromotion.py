# _*_ coding=utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
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
pro_code='PM201604050012'

#促销主题
pro_theme=u"线上促销主题Auto_test"


class test_OnlinePromotion(unittest.TestCase):
    #线上促销模块
    log.info(u"~~~线上促销模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_OnlinePromotion(self):
        #进入线上促销模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入线上促销
        testModule(driver,u'促销方案管理',u'线上促销')
        
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
            screenshot(driver,u"保存")
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()
            sleep(1)
            
            
    def clickButton(self,button):
        u'''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#salePmOnlineListRToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#salePmOnlineListRToolbar > a.easyui-linkbutton.findButton > span > span').click()
            WebWait(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) > div > div > div > div > div.datagrid-mask")
            sleep(1)

        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#editButton1 > span > span').click()
            sleep(1)

            self.assertEqual(u"编辑",driver.find_element_by_css_selector("#stmConstantForm > div > a.easyui-linkbutton.saveButton > span > span > span").text)
            
        elif button==u'编辑' or button=='view':
            #点击“编辑”按钮
            driver.find_element_by_css_selector('#stmConstantForm > div > a.easyui-linkbutton.saveButton > span > span > span').click()
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            "点击“修改”按钮"
            driver.find_element_by_css_selector('#editButton1 > span > span').click()
            sleep(1)

        elif button==u"保存" or button=="save":
            "点击“保存”按钮"
          
            driver.find_element_by_css_selector("#saveButton > span > span > span").click()
                
            sleep(0.5)                
            #断言
            self.Delete_And_Add_Assert('add')
            
                
    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            try:
                driver.implicitly_wait(5)
                driver.find_element_by_css_selector('#salePmOnlineListRToolbar > a.easyui-linkbutton.deleteButton > span > span').click()
                a=True
                driver.implicitly_wait(30)
                sleep(1)

            except:
                #"详情页删除"
                driver.find_element_by_css_selector("#salePmSuitObjectToolbar > a.easyui-linkbutton.removeDataButton > span > span").click()
                a=False

                driver.implicitly_wait(30)
                sleep(1)
            
            #断言
            self.Delete_And_Add_Assert('delete',a)
            
                
        elif button==u'返回' or button=='return':
            #编辑界面，点击“返回”按钮
            driver.find_element_by_css_selector('#salePmOlineHdToolbar > a.easyui-linkbutton.returnButton > span > span').click()
            sleep(1)

        elif button==u'审批' or button=='check':
            #编辑界面，点击“审批”按钮
            driver.find_element_by_css_selector('#salePmOlineHdToolbar > a.easyui-linkbutton.checkButton > span > span').click()
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
            driver.find_element_by_css_selector('#salePmOlineHdToolbar > a.easyui-linkbutton.checkButton > span > span').click()
            sleep(0.5)
            #确定终止
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            sleep(1)
            #print driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text
            #断言是否终止成功
            self.assertEqual(u"已终止！",driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text)
    

        else:
            raise NameError("No Such Button!comfirm again please!!")

         
    def test_0add_Promotion(self):
        u'''添加促销'''

        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入线上促销
        self.to_OnlinePromotion()

        
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
        findCss(driver,"#salePmOlineHdForm  tr:nth-child(1) > td:nth-child(13) > input").send_keys(theme)
        sleep(0.5)

        #优先级
        findCss(driver,"#salePmOlineHdForm  tr:nth-child(2) > td:nth-child(4) > input").send_keys('5')
       
        sleep(0.5)

        #物流配送方式
        ex=findCss(driver,"#salePmOlineHdForm tr:nth-child(2) > td:nth-child(8) > span > input.combo-text.validatebox-text")
        select(ex)

        #活动对象
        aob=findCss(driver,"#salePmOlineHdForm tr:nth-child(3) > td:nth-child(2) > span > input.combo-text.validatebox-text")
        select(aob)
        
        #渠道
        ch=findCss(driver,"#salePmOlineHdForm  tr:nth-child(3) > td:nth-child(4) > span > input.combo-text.validatebox-text")
        select(ch)

        #促销方式
        prw=findCss(driver,"#salePmOlineHdForm tr:nth-child(3) > td:nth-child(6) > span > input.combo-text.validatebox-text")
        select(prw)

        #促销类型
        prt=findCss(driver,"#salePmOlineHdForm tr:nth-child(3) > td:nth-child(8) > span > input.combo-text.validatebox-text")
        select(prt)
        
        #起始日期
        date_start=findCss(driver,"#salePmOlineHdForm tr:nth-child(4) > td:nth-child(2) > span > input.combo-text.validatebox-text")
        
        date_start.click()
        sleep(0.5)
        date_start.send_keys(Keys.ENTER)
        sleep(0.5)
        
        #结束日期
        date_end=findCss(driver,"#salePmOlineHdForm  tr:nth-child(4) > td:nth-child(4) > span > input.combo-text.validatebox-text")
        date_end.click()
        sleep(0.5)
        date_end.send_keys(Keys.ENTER)
        sleep(0.5)

        #捆绑方式
        bd=findCss(driver,"#salePmOlineHdForm tr:nth-child(5) > td:nth-child(6) > span > input.combo-text.validatebox-text")
        select(bd)

        #促销生效类型
        eft=findCss(driver,"#salePmOlineHdForm tr:nth-child(5) > td:nth-child(8) > span > input.combo-text.validatebox-text.validatebox-invalid")
        select(eft)

        #限定时间
        findCss(driver,"#salePmOlineHdForm tr:nth-child(6) > td:nth-child(6) > input").click()
        sleep(0.5)

        #保存
        self.clickButton(u"保存")

        #返回
        self.clickButton(u"返回")

        #等待界面刷新
        log.info(u"刷新~~~")
        isRefreshed(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable  td[field='ck']")

        #读取新添加促销的促销编号
        global pro_code
        pro_code=findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable  td[field='fdCode']").text
        #print pro_code
        


    def searchbykey(self,keys):
        '''用于按关键字查找促销'''

        driver=self.driver

        #输入关键字
        findCss(driver,"#salePmOnlineListRToolbar > input.easyui-validatebox.validatebox-text").clear()
        sleep(0.5)
        findCss(driver,"#salePmOnlineListRToolbar > input.easyui-validatebox.validatebox-text").send_keys(keys)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")
        sleep(3)

        #断言
        code=findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='fdCode']").text

        ths=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='saleTheme']")
        for th in ths:
            #print th.text
            if th.text in keys or code==keys:
                a=True
                continue
            a=False
            break
        self.assertTrue(a,"Search Failed!!!"+keys)
        sleep(0.5)

    def test_1search_byKeyWord(self):
        u'''按关键字查找促销'''

        log.info(u"开始执行用例...")
        driver=self.driver

        #进入线上促销
        self.to_OnlinePromotion()

        #获取全部数据记录条数
        allre=findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) div.datagrid-pager.pagination > div.pagination-info").text
        #print allre

        #输入编号查找
        code=findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable  td[field='fdCode']").text
        self.searchbykey(code)

        #清空输入框内容，查找
        findCss(driver,"#salePmOnlineListRToolbar > input.easyui-validatebox.validatebox-text").clear()
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        sleep(3)
        #断言是否查找出全部数据
        self.assertEqual(allre,findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) div.datagrid-pager.pagination > div.pagination-info").text)

        #输入促销主题查找
        theme=findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable  td[field='saleTheme']").text
        self.searchbykey(theme)

    
    def test_2search_byActivityTime(self):
        u'''按活动时间查找'''

        log.info(u"开始执行用例...")
        driver=self.driver

        #进入线上促销
        self.to_OnlinePromotion()

        #设置要查找的时间
        start_time='2016-03-01'
        end_time='2016-03-30'
        #将时间传化为时间戳
        tt1=toTime("%Y-%m-%d",start_time)
        tt2=toTime("%Y-%m-%d",end_time)

        sleep(0.5)
        #输入时间查找
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(3) > input.combo-text.validatebox-text").send_keys(start_time)
        sleep(0.5)
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(3) > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        sleep(0.5)
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(5) > input.combo-text.validatebox-text").send_keys(end_time)
        sleep(0.5)
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(5) > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
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

        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入线上促销
        self.to_OnlinePromotion()

        #选择适用对象
        obj=u'九牧王'
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(7) > input.combo-text.validatebox-text").send_keys(obj)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")

        #断言
        objs=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='suiObj']")
        searchAssert(self,objs,obj)

        
    def test_4search_byMakeDate(self):
        u'''按制单日期查找'''

        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入线上促销
        self.to_OnlinePromotion()

         #设置要查找的时间
        start_time='2016-03-10'
        end_time='2016-03-30'
        #将时间传化为时间戳
        tt1=toTime("%Y-%m-%d",start_time)
        tt2=toTime("%Y-%m-%d",end_time)

        sleep(0.5)
        #输入时间查找
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(9) > input.combo-text.validatebox-text").send_keys(start_time)
        sleep(0.5)
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(11) > input.combo-text.validatebox-text").send_keys(end_time)
        sleep(0.5)
        #查找
        self.clickButton(u"查找")
        sleep(3)

        #获取查找结果
        mts=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable  td[field='salePmDate']")
        
        b=''

        for mt in mts:
            #将结果时间转化为时间戳
            mtt=toTime("%Y-%m-%d",mt.text)
            if mtt >tt1 or mtt ==tt1 or mtt < tt2 or mtt == tt2:
                b=True
                continue
            else:
                b=False
                break
        if b=='':
            raise NameError("without data be searched!!!")
        
        self.assertTrue(b,"Search Failed!!!")
        

    def test_5search_byIdentifyDocument(self):
        u'''按单据标识查找'''


        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入线上促销
        self.to_OnlinePromotion()

        #选择促销标识
        di=u"未审批"
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(15) > input").send_keys(di)
        sleep(0.5)
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(15) > input").send_keys(Keys.ENTER)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #断言
        dis=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='chkStatus']")
        searchAssert(self,dis,di)

    def test_6search_byPromotionType(self):
        u'''按促销类型查找'''


        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入线上促销
        self.to_OnlinePromotion()

        #选择促销类型
        types=u"惠赠"
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(17) > input.combo-text.validatebox-text").send_keys(types)
        sleep(0.5)
        findCss(driver,"#salePmOnlineListRToolbar > span:nth-child(17) > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        sleep(0.5)
        
        #查找
        self.clickButton(u"查找")

        #断言
        tps=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='salePmTypeName']")
        searchAssert(self,tps,types)



    def edit_Promotion(self):
        '''进入促销修改'''
        driver=self.driver

        #进入线上促销
        self.to_OnlinePromotion()

        #通过促销编号查找
        code=pro_code
        self.searchbykey(code)

        #选择记录
        findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u"修改")

        #等待界面刷新
        WebWait(driver,"#salePmOnlineHdTabs > div.tabs-panels.tabs-panels-noborder > div:nth-child(1) > div > div > div > div > div.datagrid-mask-msgn")

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOnlineHdTabs  table.datagrid-htable  td[field='dptKey']").text
        isRefreshed(driver,"#salePmOnlineHdTabs  table.datagrid-htable  td[field='dptKey']")
        log.info(u"刷新完成！！！") 

        
        

    def test_7modify_Promotion(self):
        u'''修改促销'''

        log.info(u"开始执行用例...")
        
        driver=self.driver

        #调用函数进入促销修改界面
        self.edit_Promotion()
        

    def test_8modify_AddSuitObject(self):
        u'''添加适用对象'''

        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOnlineHdTabs  table.datagrid-htable  td[field='dptKey']").text
        isRefreshed(driver,"#salePmOnlineHdTabs  table.datagrid-htable  td[field='dptKey']")
        log.info(u"刷新完成！！！") 
        
        #添加适用对象
        findCss(driver,"#salePmSuitObjectToolbar > a.easyui-linkbutton.addButton > span > span").click()
        sleep(0.5)

        #选择第一个店铺
        findCss(driver,"#ModifySuitForm > div.left table.datagrid-btable td[field=\"ck\"]").click()
        sleep(0.5)

        #右移
        findCss(driver,"#ModifySuitForm > div.middle > input.leftToRight").click()
        sleep(0.5)

        #保存
        findCss(driver,"body > div:nth-child(30) > div.panel-body.panel-body-noborder.window-body  a.easyui-linkbutton.saveButton > span > span").click()

        #将提示信息写入log    
        log.info(driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text)

        #断言
        self.assertEqual(u"保存成功！",driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text)
        sleep(0.5)
        driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()
        sleep(1)        

       
    def test_9modify_DeleteSuitObject(self):
        u'''删除适用对象'''


        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()
        
        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOnlineHdTabs  table.datagrid-htable  td[field='dptKey']").text
        isRefreshed(driver,"#salePmOnlineHdTabs  table.datagrid-htable  td[field='dptKey']")
        log.info(u"刷新完成！！！") 

        #选择适用对象
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-panels.tabs-panels-noborder > div:nth-child(1)  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        #删除
        #findCss(driver,"#salePmSuitObjectToolbar > a.easyui-linkbutton.removeDataButton > span > span").click()
        self.clickButton(u"删除")
        sleep(0.5)

    def test_amodify_Add_TimeConstraint(self):
        u'''添加时段约束'''

        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-时段约束
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(2) > a > span.tabs-title").click()
        sleep(0.5)
        
        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOnlineHdTabs  table.datagrid-htable  td[field='startTime']").text
        isRefreshed(driver,"#salePmOnlineHdTabs  table.datagrid-htable  td[field='startTime']")
        log.info(u"刷新完成！！！")

        #添加
        findCss(driver,"#salePmDtTimeToolbar > div > a.easyui-linkbutton.appendDataButton > span > span").click()
        sleep(0.5)
        
        #约束开始时间
        findCss(driver,"#salePmDtTimeToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='startTime'] span.spinner-arrow-down").click()
        sleep(0.5)
        
        #约束结束时间
        findCss(driver,"#salePmDtTimeToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='endTime'] span.spinner-arrow-up").click()
        sleep(0.5)

        #保存
        findCss(driver,"#salePmDtTimeToolbar > div > a.easyui-linkbutton.saveTimeButton > span > span").click()
        sleep(0.5)
        
        #断言
        self.Delete_And_Add_Assert('add')
        


    def test_bmodify_Delete_TimeConstraint(self):
        u'''删除时段约束'''

        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-时段约束
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(2) > a > span.tabs-title").click()
        sleep(0.5)

        
        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOnlineHdTabs  table.datagrid-htable  td[field='startTime']").text
        isRefreshed(driver,"#salePmOnlineHdTabs  table.datagrid-htable  td[field='startTime']")
        log.info(u"刷新完成！！！")

        #选择一条记录
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)
        
        #删除
        findCss(driver,"#salePmDtTimeToolbar > div > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)
        
        #断言
        self.Delete_And_Add_Assert('delete',a=False)
        

    def test_cmodify_AddPromotion_com(self):
        u'''添加促销商品'''

        log.info(u"开始执行用例...")

        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-促销商品
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(3) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmDtPartAccordion  table.datagrid-htable  td[field='groupNum']").text
        isRefreshed(driver,"#salePmDtPartAccordion table.datagrid-htable  td[field='groupNum']")
        log.info(u"刷新完成！！！")

        #添加商品类型
        #添加
        findCss(driver,"#salePmDtPartToolbar > a.easyui-linkbutton.appendDataButton > span > span").click()

        #输入组号
        group_code='1'
        findCss(driver,"#salePmDtPartAccordion > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field=\"groupNum\"]  input").send_keys(group_code)
        sleep(0.5)

        #选择类型
        tp=findCss(driver,"#salePmDtPartAccordion > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field=\"partLevel\"] input.combo-text.validatebox-text")
        tp.click()
        sleep(0.5)
        tp.send_keys(u"商品级")
        sleep(0.5)
        tp.send_keys(Keys.ENTER)
        sleep(0.5)

        #保存
        findCss(driver,"#salePmDtPartToolbar > a.easyui-linkbutton.saveDataButton > span > span").click()
        sleep(1)
        #断言
        self.Delete_And_Add_Assert('add')

        #添加商品
        #选择已添加的商品类型
        findCss(driver,"#salePmDtPartAccordion > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)
        findCss(driver,"#salePmDtPartAccordion").send_keys(Keys.DOWN)
        sleep(0.5)
        
        #添加
        findCss(driver,"#salePmDtPartPartLevelGridToolbar > a.easyui-linkbutton.appendDataButton > span > span").click()
        sleep(0.5)

        #选择商品编码
        findCss(driver,"#salePmDtPartPartLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='masPartHd']  span.combo-arrow").click()
        sleep(0.5)
        findCss(driver,"body > div:nth-child(30) > div > div:nth-child(1)").click()
        sleep(0.5)

        #折扣
        findCss(driver,"#salePmDtPartPartLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='rebate']  input").send_keys('0.8')
        sleep(0.5)

        #数量
        findCss(driver,"#salePmDtPartPartLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='qty']  input").send_keys('5')
        sleep(0.5)

        #保存
        findCss(driver,"#salePmDtPartToolbar > a.easyui-linkbutton.saveDataButton > span > span").click()
        sleep(1)
        #断言
        self.Delete_And_Add_Assert('add')

        
    def test_dmodify_DeletePromotion_com(self):
        u'''删除促销商品'''
        
        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-促销商品
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(3) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmDtPartAccordion  table.datagrid-htable  td[field='groupNum']").text
        isRefreshed(driver,"#salePmDtPartAccordion table.datagrid-htable  td[field='groupNum']")
        log.info(u"刷新完成！！！")
        

        #选择商品类别
        findCss(driver,"#salePmDtPartAccordion > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        findCss(driver,"#salePmDtPartAccordion ").send_keys(Keys.DOWN)

        sleep(0.5)
        
        #选择商品
        findCss(driver,"#salePmDtPartPartLevel div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        #删除商品
        findCss(driver,"#salePmDtPartPartLevelGridToolbar > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)

        #删除商品类别
        findCss(driver,"#salePmDtPartToolbar > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)


    def test_emodify_AddRedemption_com(self):
        u'''添加换购品'''

        driver=self.driver
        log.info(u"开始执行用例...")

        #进入促销修改
        self.edit_Promotion()

        #详情页-换购品
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(4) > a > span.tabs-title").click()
        sleep(0.5)
        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmChangepurchaseAccordion  table.datagrid-htable  td[field='groupNum']").text
        isRefreshed(driver,"#salePmChangepurchaseAccordion  table.datagrid-htable  td[field='groupNum']")
        log.info(u"刷新完成！！！")

        #添加商品类型
        #添加
        findCss(driver,"#salePmChangePurchaseToolbar > a.easyui-linkbutton.appendDataButton > span > span").click()

        #输入组号
        group_code='1'
        findCss(driver,"#salePmChangepurchaseAccordion  > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field=\"groupNum\"]  input").send_keys(group_code)
        sleep(0.5)

        #选择类型
        tp=findCss(driver,"#salePmChangepurchaseAccordion > div > div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field=\"partLevel\"]  input.combo-text.validatebox-text.validatebox-invalid")
        #tp.click()
        sleep(0.5)
        
        tp.send_keys(u"商品级")
        sleep(0.5)
        
        tp.send_keys(Keys.ENTER)
        sleep(0.5)

        #保存
        findCss(driver,"#salePmChangePurchaseToolbar > a.easyui-linkbutton.saveDataButton > span > span").click()
        sleep(1)
        
        #断言
        self.Delete_And_Add_Assert('add')

        #添加商品
        #选择已添加的商品类型
        findCss(driver,"#salePmChangepurchaseAccordion  div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)
        findCss(driver,"#salePmChangepurchaseAccordion").send_keys(Keys.DOWN)
        sleep(0.5)
        
        
        #添加
        findCss(driver,"#salePmChangePurchaseShopChildrenGridToolbar > a.easyui-linkbutton.appendDataButton > span > span").click()
        sleep(0.5)

        #选择商品编码
        findCss(driver,"#salePmDtPartPurchaseShopLevel div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='masPartHd']  span.combo-arrow").click()
        sleep(0.5) 
        findCss(driver,"body > div:nth-child(30) > div > div:nth-child(1)").click()
        sleep(0.5)

        #折扣
        findCss(driver,"#salePmDtPartPurchaseShopLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='rebate']  input").send_keys('0.8')
        sleep(0.5)

        #数量
        findCss(driver,"#salePmDtPartPurchaseShopLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='qty']  input").send_keys('5')
        sleep(0.5)

        #保存
        findCss(driver,"#salePmChangePurchaseToolbar > a.easyui-linkbutton.saveDataButton > span > span").click()
        sleep(1)
        #断言
        self.Delete_And_Add_Assert('add')

        
    def test_fmodify_DeleteRedemption_com(self):
        u'''删除换购品'''


        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-换购品
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(4) > a > span.tabs-title").click()
        sleep(0.5)
        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmChangepurchaseAccordion  table.datagrid-htable  td[field='groupNum']").text
        isRefreshed(driver,"#salePmChangepurchaseAccordion  table.datagrid-htable  td[field='groupNum']")
        log.info(u"刷新完成！！！")

        #选择商品类别
        findCss(driver,"#salePmChangepurchaseAccordion  div.panel.datagrid  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        findCss(driver,"#salePmChangepurchaseAccordion").send_keys(Keys.DOWN)

        sleep(0.5)
        
        #选择商品
        findCss(driver,"#salePmDtPartPurchaseShopLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        #删除商品
        findCss(driver,"#salePmChangePurchaseShopChildrenGridToolbar > a.easyui-linkbutton.removeDataButton> span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)
        sleep(1)

        #删除商品类别
        findCss(driver,"#salePmChangePurchaseToolbar > a.easyui-linkbutton.removeOfflineChangeButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)


    
    def test_gmodify_AddDonation(self):
        u'''添加赠品'''


        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-赠品设置
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(5) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmDtGiftAccordion  table.datagrid-htable  td[field='giftType']").text
        isRefreshed(driver,"#salePmDtGiftAccordion table.datagrid-htable  td[field='giftType']")
        log.info(u"刷新完成！！！")
        

        #添加商品类型
        #添加
        findCss(driver,"#salePmDtGiftToolbar > a.easyui-linkbutton.appendDataButton > span > span").click()
        sleep(0.5)

        #输入赠送类型
        tpe=u'积分'
        tp1=findCss(driver,"#salePmDtGiftAccordion  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field=\"giftType\"]  input.combo-text.validatebox-text.validatebox-invalid")
        tp1.send_keys(tpe)
        sleep(0.5)
        tp1.send_keys(Keys.ENTER)
        sleep(0.5)

        #输入赠送方式
        tp=findCss(driver,"#salePmDtGiftAccordion  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field=\"giftMode\"]  input.combo-text.validatebox-text.validatebox-invalid")
        #tp.click()
        sleep(0.5)
        
        tp.send_keys(u"固定")
        sleep(0.5)
        
        tp.send_keys(Keys.ENTER)
        sleep(0.5)

        #保存
        findCss(driver,"#salePmDtGiftToolbar > a.easyui-linkbutton.savePmDataButton > span > span").click()
        sleep(1)
        
        #断言
        self.Delete_And_Add_Assert('add')

        #添加商品
        #选择已添加的赠品类型
        findCss(driver,"#salePmDtGiftAccordion  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)
        findCss(driver,"#salePmDtGiftAccordion").send_keys(Keys.DOWN)
        sleep(0.5)
        
        
        #添加
        findCss(driver,"#salePmDtGiftIntegralLevelGridToolbar > a.easyui-linkbutton.appendDataButton > span > span").click()
        sleep(0.5)

        #设置赠送积分
        findCss(driver,"#salePmDtGiftIntegralLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table  td[field='qty'] input.datagrid-editable-input.validatebox-text.validatebox-invalid").send_keys("10")
        sleep(0.5) 
       

        #设置总赠送积分
        findCss(driver,"#salePmDtGiftIntegralLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table  td[field='limitQty'] input.datagrid-editable-input.validatebox-text.validatebox-invalid").send_keys('100')
        sleep(0.5)


        #保存
        findCss(driver,"#salePmDtGiftToolbar > a.easyui-linkbutton.savePmDataButton > span > span").click()
        sleep(1)
        #断言
        self.Delete_And_Add_Assert('add')

        
    def test_hmodify_DeleteDonation(self):
        u'''删除赠品'''


        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-赠品设置
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(5) > a > span.tabs-title").click()
        sleep(0.5)
        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmDtGiftAccordion  table.datagrid-htable  td[field='giftType']").text
        isRefreshed(driver,"#salePmDtGiftAccordion table.datagrid-htable  td[field='giftType']")
        log.info(u"刷新完成！！！")
        

        #选择赠品类型
        findCss(driver,"#salePmDtGiftAccordion  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        findCss(driver,"#salePmDtGiftAccordion").send_keys(Keys.DOWN)
        sleep(0.5)
        
        #选择赠品
        findCss(driver,"#salePmDtGiftIntegralLevel  div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)

        #删除赠品
        findCss(driver,"#salePmDtGiftIntegralLevelGridToolbar > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)
        sleep(1)

        #删除赠品类别
        findCss(driver,"#salePmDtGiftToolbar > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)


    def test_imodify_AddTriggerPoint(self):
        u'''添加业务触发点'''

        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-业务触发点
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(6) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOnlineHdTabs   table.datagrid-htable  td[field='seq']").text
        isRefreshed(driver,"#salePmOnlineHdTabs   table.datagrid-htable  td[field='seq']")
        log.info(u"刷新完成！！！")
        
        #添加触发点
        #添加
        findCss(driver,"#salePmDtTrgToolbar > a.easyui-linkbutton.addButton > span > span").click()
        sleep(0.5)

        

        #选择促销类型
        
        tp1=findCss(driver,"#fixedOnlineTrgArea > td:nth-child(11) > span > input.combo-text.validatebox-text")
        tp1.click()
        sleep(0.5)
        
        tp1.send_keys(Keys.DOWN)
        sleep(0.5)
        tp1.send_keys(Keys.ENTER)
        sleep(0.5)

        #选择赠品
        tp=findCss(driver,"#fixedOnlineTrgArea > td:nth-child(13) > span > input.combo-text.validatebox-text.validatebox-invalid")
        tp.click()
        sleep(0.5)
        
        tp.send_keys(Keys.DOWN)
        sleep(0.5)
        
        tp.send_keys(Keys.ENTER)
        sleep(0.5)


        #捆绑数量
        tp.send_keys(Keys.TAB)
        sleep(0.5)
        num=findCss(driver,"#pmTypeGive > td:nth-child(3) > input.easyui-numberbox.validatebox-text.validatebox-invalid")
        num.send_keys('3')
        sleep(0.5) 

        #赠送数量
        num.send_keys(Keys.TAB)
        findCss(driver,"#pmTypeGive td:nth-child(5) input.easyui-numberbox.validatebox-text.validatebox-invalid").send_keys('1')
        sleep(0.5)
        

        #保存
        findCss(driver,"div.panel-body.panel-body-noborder.window-body.panel-noscroll > div > div.panel.layout-panel.layout-panel-center  a.easyui-linkbutton.addTermButton > span > span > span").click()
        sleep(1)
        
        #断言
        self.Delete_And_Add_Assert('add')

        #确定
        findCss(driver,"div.panel-body.panel-body-noborder.window-body.panel-noscroll > div > div.panel.layout-panel.layout-panel-center > div > div > div.panel.layout-panel.layout-panel-south > div > a > span > span > span").click()
        
    def test_jmodify_DeleteTriggerPoint(self):
        u'''删除业务触发点'''

        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-业务触发点
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(6) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOnlineHdTabs   table.datagrid-htable  td[field='seq']").text
        isRefreshed(driver,"#salePmOnlineHdTabs   table.datagrid-htable  td[field='seq']")
        log.info(u"刷新完成！！！") 

        #选择一个触发点
        findCss(driver,"#salePmDtTrgToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table td[field='ck']").click()
        sleep(0.5)


        #删除
        findCss(driver,"#salePmDtTrgToolbar > a.easyui-linkbutton.deleteButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)
        sleep(1)

    def test_kmodify_AddPayment(self):
        u'''添加结算方式'''
        
        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-结算方式
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(7) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOnlineHdTabs   table.datagrid-htable  td[field='stmPayment']").text
        isRefreshed(driver,"#salePmOnlineHdTabs   table.datagrid-htable  td[field='stmPayment']")
        log.info(u"刷新完成！！！") 

        #添加结算方式
        #添加
        findCss(driver,"#salePmDtPaymentToolbar > div > a.easyui-linkbutton.appendDataButton > span > span").click()
        sleep(0.5)
        

        #选择结算方式
        payment=u'支付宝支付'
        pl=findCss(driver,"#salePmDtPaymentToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body  td[field='stmPayment']  input.combo-text.validatebox-text.validatebox-invalid")
        pl.send_keys(payment)
        sleep(0.5)
        pl.send_keys(Keys.ENTER)
        
    
        #保存
        findCss(driver,"#salePmDtPaymentToolbar > div > a.easyui-linkbutton.saveButton > span > span > span").click()
        sleep(1)
        
        #断言
        self.Delete_And_Add_Assert('add')

       
        
    def test_ldelete_DeletePayment(self):
        u'''删除结算方式'''
        log.info(u"开始执行用例...")
        driver=self.driver

        #进入促销修改
        self.edit_Promotion()

        #详情页-结算方式
        findCss(driver,"#salePmOnlineHdTabs > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li:nth-child(7) > a > span.tabs-title").click()
        sleep(0.5)

        log.info(u"等待界面刷新~~~")
        #print findCss(driver,"#salePmOnlineHdTabs   table.datagrid-htable  td[field='stmPayment']").text
        isRefreshed(driver,"#salePmOnlineHdTabs   table.datagrid-htable  td[field='stmPayment']")
        log.info(u"刷新完成！！！") 

        #选择一个结算方式
        findCss(driver,"#salePmDtPaymentToolbar + div.datagrid-view > div.datagrid-view2 > div.datagrid-body  td[field='ck']").click()
        sleep(0.5)

        


        #删除
        findCss(driver,"#salePmDtPaymentToolbar > div > a.easyui-linkbutton.removeDataButton > span > span").click()
        sleep(0.5)

        #断言
        self.Delete_And_Add_Assert('delete',a=False)
        sleep(1)

      
        

    def test_mdelete_Promotion(self):
        u'''删除促销'''

        log.info(u"开始执行用例...")
        driver=self.driver

        #进入线上促销
        self.to_OnlinePromotion()

        #通过促销编号查找
        code=pro_code
        self.searchbykey(code)

        #选择记录
        findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder > div:nth-child(2) table.datagrid-btable  td[field='ck']").click()
        sleep(0.5)

        #删除
        self.clickButton(u"删除")

    
    def tes_nmodify_ApprovalStatus(self):
        u'''修改审批状态'''

        log.info(u"开始执行用例...")

        driver=self.driver

        #进入线上促销
        #self.to_OnlinePromotion()
        
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
    
    
    # 建立测试集
    logging.info('test_OnlinePromotion start--')
    
    suite=unittest.TestSuite()
     
    #suite.addTest(test_OnlinePromotion('test_0add_Promotion')) #添加促销
    
    #suite.addTest(test_OnlinePromotion('test_1search_byKeyWord'))  #按关键字查找
    #suite.addTest(test_OnlinePromotion('test_2search_byActivityTime')) #按活动时间查找
    #suite.addTest(test_OnlinePromotion('test_3search_byApplicableObject')) #按适用对象查找
    #suite.addTest(test_OnlinePromotion('test_4search_byMakeDate')) #按制单日期查找
    #suite.addTest(test_OnlinePromotion('test_5search_byIdentifyDocument')) #按单据标识查找
    #suite.addTest(test_OnlinePromotion('test_6search_byPromotionType')) #按促销类型查找

    
    #suite.addTest(test_OnlinePromotion('test_7modify_Promotion')) #修改促销
    
    #suite.addTest(test_OnlinePromotion('test_8modify_AddSuitObject')) #添加适用对象
    #suite.addTest(test_OnlinePromotion('test_9modify_DeleteSuitObject')) #删除适用对象

    #suite.addTest(test_OnlinePromotion('test_amodify_Add_TimeConstraint')) #添加时段约束
    #suite.addTest(test_OnlinePromotion('test_bmodify_Delete_TimeConstraint')) #删除时段约束
    
    #suite.addTest(test_OnlinePromotion('test_cmodify_AddPromotion_com')) #添加促销商品
    #suite.addTest(test_OnlinePromotion('test_dmodify_DeletePromotion_com')) #删除促销商品

    suite.addTest(test_OnlinePromotion('test_emodify_AddRedemption_com')) #添加换购品
    suite.addTest(test_OnlinePromotion('test_fmodify_DeleteRedemption_com')) #删除换购品

    #suite.addTest(test_OnlinePromotion('test_gmodify_AddDonation')) #添加赠品
    #suite.addTest(test_OnlinePromotion('test_hmodify_DeleteDonation')) #删除赠品

    #suite.addTest(test_OnlinePromotion('test_imodify_AddTriggerPoint')) #添加业务触发点
    #suite.addTest(test_OnlinePromotion('test_jmodify_DeleteTriggerPoint')) #删除业务触发点

    #suite.addTest(test_OnlinePromotion('test_kmodify_AddPayment')) #添加支付方式
    #suite.addTest(test_OnlinePromotion('test_ldelete_DeletePayment')) #删除支付方式

    
    #suite.addTest(test_OnlinePromotion('test_mdelete_Promotion')) #删除促销
    
    #suite.addTest(test_OnlinePromotion('test_nmodify_ApprovalStatus')) #修改审批状态
    
    
   
    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()

    
    logging.info('test_OnlinePromotion end--')
        
