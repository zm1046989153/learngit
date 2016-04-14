# _*_ coding:utf-8 _*_
__author__='Zhenming'

from selenium import webdriver
from time import sleep
import unittest,sys,time
import xml.dom.minidom
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

sys.path.append('D:\\ISS\\Test_Cases\\public')
import login
from isspublic import*

#打开xml文件
dom=xml.dom.minidom.parse('D:\\ISS\\Test_Data\\login.xml')
dom1=xml.dom.minidom.parse('D:\\ISS\\Test_Data\\Measure_WorkOrder.xml')

#获取文档元素对象
root=dom.documentElement
root1=dom1.documentElement
#从xml中获取信息
customers=root1.getElementsByTagName("customer")
customer=customers[0].firstChild.data#获取客户名字      
phones=root1.getElementsByTagName("phone")
phone='13823452345' #获取手机号码
order_num='8' #用于存取工单号
dperson=u"梅林" #用于存放着装人
mman=u"林大华" #用于存放量体师


class test_Measure_WorkOrder(unittest.TestCase):
    #量体工单
    log.info(u"~~~量体工单模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.verificationErrors=[]
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data




    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#saleOrdMeasureHdToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
            
            
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#saleOrdMeasureHdToolbar > a.easyui-linkbutton.findButton > span > span').click()
            WebWait(driver,"#saleOrdMeasureHdAccordion  div.datagrid-mask-msg")
            sleep(1)
            
            
        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            
            #WebWait(driver,)
            driver.find_element_by_css_selector('#saleOrdMeasureHdToolbar > a.easyui-linkbutton.viewButton > span').click()
            sleep(0.5)
            
            #判断是否进入查看界面
            self.assertEqual(u'编辑',driver.find_element_by_css_selector("#saleOrdMeasureHdForm > div > a.easyui-linkbutton.saveButton > span > span").text)
            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#saleOrdMeasureHdToolbar > a.easyui-linkbutton.editButton  > span > span').click()
            
            sleep(1)

        elif button==u'修改量体状态' or button=='modifys':
 
            #点击“量体状态”按钮#
            driver.find_element_by_css_selector('#saleOrdMeasureHdToolbar > a.easyui-linkbutton.editStatusButton > span > span').click()
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
            
            WebWait(driver,"#saleOrdMeasureHdAccordion > div:nth-child(1) > div.panel-body.accordion-body  div.datagrid-mask",20)
            
        
        else:
            raise NameError('No Such Button,confirm again please')


            
        

    def test_0add_WorkOrder(self):
        u"添加量体工单"
        log.info(u'''开始执行测试...''')
        
        
        driver=self.driver
        #进入量体工单模块
        self.to_measureWorkOrder()

        sleep(0.5)

        WebWait(driver,"#saleOrdMeasureHdAccordion  div.datagrid-mask-msg")
        
        #点击添加按钮
        self.clickButton(u"添加")
        sleep(1)

        #选择订单号
        #判断页面是否刷新
        
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm tr:nth-child(1) > td:nth-child(6) > span > input.combo-text.validatebox-text").click()
        sleep(2)
        log.info(u"等待页面刷新···")
        ordern=isRefreshed(driver,"#datagrid-row-r3-2-0")
        log.info(u"刷新完成！！！")
     
        sleep(1)
        ordern.click()
        #选择
        driver.find_element_by_css_selector("body a.easyui-linkbutton.saveButton.l-btn.l-btn-plain > span > span > span").click()

        sleep(1)
        
        #选择预约时间
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm > table td:nth-child(10) > span > input.combo-text.validatebox-text").click()

        sleep(0.5)
        
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm > table td:nth-child(10) > span > input.combo-text.validatebox-text").send_keys(Keys.ENTER)      
     
        #选择过期时间
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm table td:nth-child(12) > span > input.combo-text.validatebox-text").click()

        driver.find_element_by_css_selector("#saleOrdMeasureHdForm table  td:nth-child(12) > span > input.combo-text.validatebox-text").send_keys(Keys.ENTER)   

        sleep(0.5)
        

        #填写客户姓名
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm > table tr:nth-child(2) > td:nth-child(4) > input ").send_keys(customer)

        sleep(0.5)
        
        #填写手机
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm  tr:nth-child(2) > td:nth-child(6) > input.easyui-numberbox.validatebox-text.validatebox-invalid").send_keys(phone)

        sleep(0.5)
        
        #填写国家、省份、城市、区县

        #选择中国
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm tr:nth-child(3) > td:nth-child(2) > span > input").click()

        sleep(0.5)
        driver.find_element_by_css_selector("body > div:nth-child(16) > div > div:nth-child(2)").click()

        sleep(0.5)
        #省份选择北京
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm tr:nth-child(3) > td:nth-child(4) > span > input").click()
        sleep(0.5)
        
        driver.find_element_by_css_selector("body > div:nth-child(17) > div > div:nth-child(1)").click()
        sleep(0.5)

        #城市选择北京市
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm tr:nth-child(3) > td:nth-child(6) > span > input").click()
        sleep(0.5)
        driver.find_element_by_css_selector("body > div:nth-child(18) > div > div").click()

        sleep(0.5)

        
        #区县选择东城区
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm tr:nth-child(3) > td:nth-child(8) > span > input").click()

        sleep(0.5)
        
        driver.find_element_by_css_selector("body > div:nth-child(19) > div > div:nth-child(1)").click()

        sleep(0.5)
        
        #选择量体方式
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm tr:nth-child(5) > td:nth-child(4) > span > input.combo-text.validatebox-text").send_keys(u"到店量体")

        sleep(0.5)
        
       
        #选择量体状态
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm  tr:nth-child(5) > td:nth-child(2) > span > input").send_keys(u"量体")

        sleep(0.5)
        
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm  tr:nth-child(5) > td:nth-child(2) > span > input").send_keys(Keys.ENTER)

        sleep(0.5)
        
        #设置预约门店
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm tr:nth-child(5) > td:nth-child(6) > span > input").click()

        sleep(0.5)
        #选择莲花专卖店
        driver.find_element_by_css_selector("body > div:nth-child(22) > div > div:nth-child(8)").click()

        sleep(0.5)
        
        #选择量体师
        driver.find_element_by_css_selector("#saleOrdMeasureHdForm tr:nth-child(5) > td:nth-child(8) > span > input.combo-text.validatebox-text.validatebox-invalid").click()
        sleep(0.5)
        
        dt=driver.find_element_by_css_selector("body > div:nth-child(23) > div > div:nth-child(1)")
        
        global mman
        mman=dt.text
        
        #print mman
        dt.click()

        #点击保存
       
        self.clickButton(u"保存")
        
     
        #获取工单号
        global order_num
        order_num=driver.find_element_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdBillCode']").text
        #print order_num
        
        
    def test_1look_WorkOrder(self):
        u"查看量体工单"
        log.info(u'''开始执行测试...''')
        
        driver=self.driver
        self.to_measureWorkOrder()#进入量体工单模块
        sleep(0.5)
        
        #选择一个工单
        
        driver.find_element_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='ck']").click()
       

        sleep(0.5)

        #点击查看按钮
        self.clickButton(u"查看")

        sleep(0.5)
        #编辑
        self.clickButton(u"编辑")
        sleep(0.5)

        #保存
        self.clickButton(u"保存")


    def searchbycode(self,code):
        '''按工单号查找'''
        
        driver=self.driver
        
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > input:nth-child(1)").clear()
        sleep(0.5)
        
        #查询栏输入工单号
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > input:nth-child(1)").send_keys(code)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        sleep(3)

        #断言
        cds=driver.find_elements_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdBillCode']")
        searchAssert(self,cds,code)

        
    def test_2search_ByWorkOrder(self):
        u"通过工单号查找"
        log.info(u'''开始执行测试...''')
        
        driver=self.driver
        self.to_measureWorkOrder()#进入量体工单模块

        sleep(0.5)

        #获取列表中第一个记录的工单号，并查找
        code=driver.find_element_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdBillCode']").text
        self.searchbycode(code)
        

    def test_3search_ByAppointmentTime(self):
        u"通过预约时间查找"
        log.info(u'''开始执行测试...''')
        
        driver=self.driver
        self.to_measureWorkOrder()#进入量体工单模块

        sleep(0.5)

        #设置要查找的时间
        t1="2016-01-04"
        t2="2016-02-06"
        #将查找时间转换为时间戳
        tt1=time.mktime(time.strptime(t1,'%Y-%m-%d'))
        tt2=time.mktime(time.strptime(t2,'%Y-%m-%d'))
        #print tt1,tt2
        
        #输入查找时间
        sleep(0.5)
        
        te1=driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > span:nth-child(3) > input")
        sleep(0.5)
        
        te1.send_keys(t1)

        sleep(0.5)

        te1.send_keys(Keys.ENTER)
        
        te2=driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > span:nth-child(5) > input")
        te2.send_keys(t2)
        
        sleep(0.5)
        
        te2.send_keys(Keys.ENTER)

        sleep(0.5)
        
        #点击查找
        self.clickButton(u"查找")
        sleep(3)

        
        #断言查找的结果
        times=driver.find_elements_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdAppointLog']")
        for t in times:
            #print t.text
            #将查找出来的记录预约时间转换为时间戳
            tt=time.mktime(time.strptime(t.text,'%Y-%m-%d  %H:%M:%S'))
            #print tt
            if tt > tt1 or tt==tt1:
                if tt < tt2 or tt==tt2:
                    continue
            else:
                raise NameError("AppointmentTime Search Failed")


    def test_4search_By_AppointmentStore(self):
        
        u'''按预约门店查找'''
        log.info(u'''开始执行测试''')

        driver=self.driver

        #进入量体工单模块
        self.to_measureWorkOrder()

        sleep(0.5)

        #输入预约门店
        store=u'莲花专卖店'
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > span:nth-child(9) > input").send_keys(store)
        sleep(0.5)
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > span:nth-child(9) > input").send_keys(Keys.ENTER)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        
        sleep(3)

        #断言
        sts=driver.find_elements_by_css_selector("#saleOrdMeasureHdAccordion  table.datagrid-btable td[field='fdDptKey']")
        searchAssert(self,sts,store)
        
        
                
    def test_5search_ByMeasureWay(self):
        u"通过量体方式查找"
        log.info(u'''开始执行测试...''')
        
        driver=self.driver
        self.to_measureWorkOrder()#进入量体工单模块

        sleep(0.5)
        way=u"到店量体"
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > span:nth-child(7) > input.combo-text.validatebox-text").send_keys(way)

        sleep(0.5)
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > span:nth-child(7) > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        
        sleep(3)
        
        #断言
        ways=driver.find_elements_by_css_selector("#saleOrdMeasureHdAccordion  table.datagrid-btable td[field='fdMsrWayKey']")
        #for w in ways:
         #   print w.text
        searchAssert(self,ways,way)
        
        
    def test_6search_ByMeasureMaster(self):
        u"通过量体师查找"
        log.info(u'''开始执行测试...''')
        
        driver=self.driver
        self.to_measureWorkOrder()#进入量体工单模块

        sleep(0.5)

        #选择量体师
        master=u"林大华"
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > span:nth-child(11) > input").send_keys(master)
        sleep(0.5)
        
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > span:nth-child(11) > input.combo-text").send_keys(Keys.ENTER)
        sleep(0.5)
        
        #查找
        self.clickButton(u"查找")
        
        sleep(3)
        

        
        #获取断言信息
        masters=driver.find_elements_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdPersonKey']")
        
        searchAssert(self,masters,master)
        
        
    def test_7search_ByMeasureState(self):
        u"通过量体状态查找"
        log.info(u'''开始执行测试...''')
        
        driver=self.driver
        self.to_measureWorkOrder()#进入量体工单模块

        sleep(0.5)

        #选择一个量体状态
        state=u"量体"
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > span:nth-child(14) > input.combo-text.validatebox-text").send_keys(state)
        
        sleep(0.5)
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > span:nth-child(14) > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        
        #查找
        self.clickButton(u"查找")

        sleep(3)
        
        #获取断言信息
        states=driver.find_elements_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdStatusKey']")
        searchAssert(self,states,state)
        
    def test_8search_ByDressPerson(self):
        u"通过着装人查找"
        log.info(u'''开始执行测试...''')
        
        driver=self.driver
        self.to_measureWorkOrder()#进入量体工单模块

        sleep(0.5)
        
        #选择着装人
        pns=driver.find_elements_by_css_selector("#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdCtmKey']")
        for pn in pns:
            #print pn.text
            if pn.text != '':
                person=pn.text
                break
            continue

        #print person
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > input:nth-child(15)").send_keys(person)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        
        sleep(3)
        
        #获取断言信息
        pers=driver.find_elements_by_css_selector("#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdCtmKey']")
        searchAssert(self,pers,person)
        
    

    def test_9search_ByPhone(self):
        u"通过手机号查找"
        log.info(u'''开始执行测试...''')
        
        driver=self.driver
        
        #进入量体工单模块
        self.to_measureWorkOrder()

        sleep(0.5)
        
        #获取第一行记录的手机号码
        phone=driver.find_element_by_css_selector("#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdCargoMobile']").text
        
        sleep(0.5)
        
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > input:nth-child(16)").send_keys(phone)#输入手机号

        sleep(0.5)
        
        #查找
        self.clickButton(u"查找")
        
        sleep(3)
        
        #获取断言信息
        phs=driver.find_elements_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdCargoMobile']")
        for ph in phs:
            self.assertIn(phone,ph.text)
        
        
    def test_amodify_WorkOrder(self):
        u"修改量体工单"
        log.info(u'''开始执行测试...''')
        
        
       
        phone1="18350293137"
        
        driver=self.driver
        #进入量体工单模块
        self.to_measureWorkOrder()

        sleep(0.5)

        
        #点击查找
        code=order_num
        self.searchbycode(code)
        sleep(1)

        #勾选记录
        driver.find_element_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #点击修改按钮
        
        self.clickButton(u"修改")
        
        #修改手机号
        phn=driver.find_element_by_css_selector("#saleOrdMeasureHdForm tr:nth-child(2) > td:nth-child(6) > input.easyui-numberbox.validatebox-text")
        phn.clear()
        sleep(0.5)
        
        phn.send_keys(phone1)
        sleep(0.5)
        
        #点击保存
        self.clickButton(u"保存")
        sleep(1)
        
        
        #判断是否是修改的手机号码
        phs=driver.find_element_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='fdCargoMobile']")
        #print phs.text
        self.assertEqual(phone1,phs.text)
        
    

    def test_bmodify_MeasureState(self):
        u"修改量体状态"
        log.info(u'''开始执行测试...''')
        
        driver=self.driver
        #进入量体工单模块
        self.to_measureWorkOrder()

        sleep(0.5)

        #查找出要修改的量体工单

        self.searchbycode(order_num)
            
        #选择要修改的记录
        driver.find_element_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='ck']").click()

        sleep(0.5)
        
        #点击修改量体状态按钮
        #self.clickButton(u'修改量体状态')
        driver.find_element_by_css_selector("#saleOrdMeasureHdToolbar > a.easyui-linkbutton.editStatusButton > span > span").click()
        sleep(1)
        
        
       
        #修改量体状态
        driver.find_element_by_css_selector("#measureModifyStatusForm tr > td:nth-child(2) > span > input.combo-text.validatebox-text").click()
        
        sleep(0.5)
        
        driver.find_element_by_css_selector("#measureModifyStatusForm tr > td:nth-child(2) > span > input.combo-text.validatebox-text").send_keys(Keys.DOWN)
        driver.find_element_by_css_selector("#measureModifyStatusForm tr > td:nth-child(2) > span > input.combo-text.validatebox-text").send_keys(Keys.ENTER)
        #取消
        #driver.find_element_by_css_selector("body > div:nth-child(33) > div.panel-body.panel-body-noborder.window-body > div:nth-child(2) > a.easyui-linkbutton.cancelButton.l-btn.l-btn-plain > span > span").click()

        sleep(0.5)
        
        #提交
        driver.find_element_by_css_selector("body  div.panel-body.panel-body-noborder.window-body > div:nth-child(2) > a.easyui-linkbutton.saveButton.l-btn.l-btn-plain > span > span").click()

        #获取断言信息
        ms=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
        #print ms.text
        self.assertEqual(u"修改成功",ms.text)
 

        
    def test_cdelete_WorkOrder(self):
        u"删除量体工单"
        log.info(u'''开始执行测试...''')
        
        driver=self.driver
        #进入量体工单模块
        self.to_measureWorkOrder()

        
        #输入工单号，查找
        code=order_num
        self.searchbycode(code)
    
        #选择记录
        driver.find_element_by_css_selector("div#saleOrdMeasureHdAccordion table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #删除
        self.clickButton(u"删除")
        

   


       
    def to_measureWorkOrder(self):
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        
        #进入量体工单模块
        testModule(driver,u'订单管理',u'量体工单')

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#saleOrdMeasureHdAccordion table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
       
        sleep(1)
        


    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        order_number=[]
        self.driver.close()
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

  
if __name__=="__main__":
    #构造测试集
    suite=unittest.TestSuite()
    #suite.addTest(test_Measure_WorkOrder('test_0add_WorkOrder'))#添加量体工单
    
    suite.addTest(test_Measure_WorkOrder('test_1look_WorkOrder'))#查看量体工单
    
    #suite.addTest(test_Measure_WorkOrder('test_2search_ByWorkOrder'))#按工单号查找
    #suite.addTest(test_Measure_WorkOrder('test_3search_ByAppointmentTime'))#按预约时间查找
    #suite.addTest(test_Measure_WorkOrder('test_4search_By_AppointmentStore'))#按预约门店查找
    #suite.addTest(test_Measure_WorkOrder('test_5search_ByMeasureWay'))#按量体方式查找
    #suite.addTest(test_Measure_WorkOrder('test_6search_ByMeasureMaster'))#按量体师查找
    #suite.addTest(test_Measure_WorkOrder('test_7search_ByMeasureState'))#按量体状态查找
    #suite.addTest(test_Measure_WorkOrder('test_8search_ByDressPerson'))#按着装人查找
    #suite.addTest(test_Measure_WorkOrder('test_9search_ByPhone'))#按手机号查找
    
    #suite.addTest(test_Measure_WorkOrder('test_amodify_WorkOrder'))#修改量体工单
    #suite.addTest(test_Measure_WorkOrder('test_bmodify_MeasureState'))#修改量体状态
    #suite.addTest(test_Measure_WorkOrder('test_cdelete_WorkOrder'))#删除量体工单
    
    #suite.addTest(test_Measure_WorkOrder('to_measureWorkOrder'))#进入量体工单模块


    #执行测试
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
