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

#设备编码
device_code='ZM094001'

#设备名称
device_name=u'ZM导购屏'



class test_Device(unittest.TestCase):
    #设备信息模块测试
    log.info(u"~~~设备信息模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_Device(self):
        #进入设备信息模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入设备信息
        testModule(driver,u'系统管理',u'设备信息')
        
        
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
            driver.find_element_by_css_selector('#mchDeviceHdTToolbar > a.easyui-linkbutton.addDeviceButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#mchDeviceHdTToolbar > a.easyui-linkbutton.findDeviceButton > span > span').click()
            sleep(1)
            WebWait(driver,"#content > div.tabs-panels.tabs-panels-noborder div.datagrid-mask-msg")
            
            #print driver.find_element_by_css_selector("#content > div.tabs-panels.tabs-panels-noborder div.datagrid-mask-msg").text

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#mchDeviceHdTToolbar > a.easyui-linkbutton.editDeviceButton > span > span').click()
            sleep(1)
                
    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#mchDeviceHdTToolbar > a.easyui-linkbutton.deleteButton > span > span').click()
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
            driver.find_element_by_css_selector('body  div.panel-body.panel-body-noborder.window-body  a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            #取消
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            
            sleep(1)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮
            driver.find_element_by_css_selector("body  div.panel-body.panel-body-noborder.window-body  a.easyui-linkbutton.saveButton > span > span").click()
            sleep(0.5)
            
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

        
    def test_0add_Device(self):
        u'''添加设备'''
        log.info(u"开始执行用例...") 
        driver=self.driver

        #进入设备信息
        self.to_Device()

        #添加
        self.clickButton(u'添加')

        #设备类型
        dt=findCss(driver,"#ModifyDeviceForm tr:nth-child(3) > td.easyui-myText > span > input.combo-text.validatebox-text.validatebox-invalid")
        dt.click()
        sleep(0.5)
        dt.send_keys(Keys.DOWN)
        sleep(0.5)
        dt.send_keys(Keys.ENTER)
        sleep(0.5)

        #MAC编码
        strt=time.strftime("%H%M%S",time.localtime(time.time()))
        mac_code="MAC"+strt
        findCss(driver,"#ModifyDeviceForm  tr:nth-child(4) > td.easyui-myText > input").send_keys(mac_code)
        sleep(0.5)

        #设备编码
        global device_code
        device_code='ZM'+strt

        findCss(driver,"#ModifyDeviceForm  tr:nth-child(5) > td.easyui-myText > input").send_keys(device_code)
        sleep(0.5)

        #设备名称
        findCss(driver,"#ModifyDeviceForm  tr:nth-child(6) > td.easyui-myText > input").send_keys(device_name)
        sleep(0.5)

        #UUID编码
        uuid_code='UUID'+strt
        findCss(driver,"#ModifyDeviceForm  tr:nth-child(7) > td.easyui-myText > input").send_keys(uuid_code)
        sleep(0.5)

        #保存
        self.clickButton(u"保存")

        
    def test_1search_byDeviceName(self):
        u'''按设备名称查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver

        #进入设备信息
        self.to_Device()

        #选择设备名称
        findCss(driver,"#mchDeviceHdTToolbar > span:nth-child(2) > input.combo-text.validatebox-text").click()
        
        dns=findsCss(driver,"body > div:nth-child(16) > div > div.combobox-item")
        n=0
        for dn in dns:
            n+=1
           
            #print dn.text
            if dn.text==device_name:
                findCss(driver,"body > div.panel.combo-p > div > div:nth-child("+str(n)+")").click()
                break
        
        sleep(0.5)
        #查找
        self.clickButton(u"查找")

        #断言
        nas=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='fdName']")
        searchAssert(self,nas,device_name)


    def selectdata(self,localtions,data):
        '''用于下拉选框中选择数据'''

        driver=self.driver

        scds=findsCss(driver,localtions+"> div.combobox-item")
        n=0
        for scd in scds:
            n+=1
            #print n
            #print scd.text
            if scd.text==data:
                findCss(driver,localtions+"> div:nth-child("+str(n)+")").click()
                
                break
        sleep(0.5)


    def searchbycode(self,code):
        '''按编号查找'''
        
        driver=self.driver

        findCss(driver,"#mchDeviceHdTToolbar > span:nth-child(4) > input.combo-text.validatebox-text").click()
        sleep(0.5)
        scds=findsCss(driver,"body > div:nth-child(17) > div >div.combobox-item")
        n=0
        for scd in scds:
            n+=1
            #print n
            #print scd.text
            if scd.text==code:
                findCss(driver,"body > div:nth-child(17) > div > div:nth-child("+str(n)+")").click()
                
                break
        sleep(0.5)


        #查找
        self.clickButton(u'查找')

        
        #断言
        cds=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='fdCode']")
        searchAssert(self,cds,code)
        
             

    def test_2search_byDeviceCode(self):
        u'''按设备编码查找'''

        log.info(u"开始执行用例...") 
        driver=self.driver

        #进入设备信息
        self.to_Device()

        #选择设备编码查找
        code=device_code
        self.searchbycode(code)


        
    def test_3search_byOrganization(self):
        u'''按所属部门查找'''
        driver=self.driver

        #进入设备信息
        self.to_Device()

        #选择所属部门
        findCss(driver,"#mchDeviceHdTToolbar > span:nth-child(6) > input.combo-text.validatebox-text").click()
        sleep(0.5)

        #设置要选择的部门
        org=u"总部"
        local="body > div:nth-child(18) > div"

        #选择部门
        self.selectdata(local,org)

        #查找
        self.clickButton(u"查找")

        #断言
        sts=findsCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='fdDptName']")
        searchAssert(self,sts,org)
        

    def test_4search_byDeviceType(self):
        u'''按设备类型查找'''
        log.info(u"开始执行用例...") 
        driver=self.driver

        #进入设备信息
        self.to_Device()

        

        detypes=["IPAD",u"导购屏",u"POS机"]
        local="body > div:nth-child(19) > div"
       
        for dt in detypes:
            #选择设备类型
            findCss(driver,"#mchDeviceHdTToolbar > span:nth-child(8) > input.combo-text.validatebox-text").click()
            sleep(0.5)
            #选择部门
            self.selectdata(local,dt)
            #查找
            self.clickButton(u"查找")
            sleep(1)
            
            

    def test_5search_byOrgType(self):
        u'''按组织类型查找'''
        log.info(u"开始执行用例...") 
        driver=self.driver

        #进入设备信息
        self.to_Device()

        #选择组织类型
        findCss(driver,"#mchDeviceHdTToolbar > span:nth-child(11) > input.combo-text.validatebox-text").click()
        sleep(0.5)

        orgtype=u"终端"
   
        local="body > div:nth-child(20) > div"
        #选择组织类型
        self.selectdata(local,orgtype)

        #查找
        self.clickButton(u"查找")
        
        

    def test_6modify_Device(self):
        u'''修改设备'''
        log.info(u"开始执行用例...") 
        driver=self.driver
        #进入设备信息
        self.to_Device()

        #查找设备
        code=device_code

        #查找
        self.searchbycode(code)

        #选择记录
        findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u"修改")

        #修改设备名称
        new_name="NEW_"+device_name

        findCss(driver,"#ModifyDeviceForm > table > tbody > tr:nth-child(6) > td.easyui-myText > input").clear()
        sleep(0.5)
        findCss(driver,"#ModifyDeviceForm > table > tbody > tr:nth-child(6) > td.easyui-myText > input").send_keys(new_name)
        sleep(0.5)

        #保存
        self.clickButton(u"保存")

        #等待界面刷新完成
        WebWait(driver,"#content > div.tabs-panels.tabs-panels-noborder div.panel.layout-panel.layout-panel-center  div.datagrid-mask")

        #再次查找
        self.searchbycode(code)

        #断言是否与修改的一致
        self.assertEqual(new_name,findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder  table.datagrid-btable td[field='fdName']").text)
          
       

    def test_7delete_Device(self):
        u'''删除设备'''
        log.info(u"开始执行用例...") 
        driver=self.driver

        #进入设备信息
        self.to_Device()

        #查找设备
        code=device_code

        #查找
        self.searchbycode(code)

        #选择记录
        findCss(driver,"#content > div.tabs-panels.tabs-panels-noborder table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #删除
        self.clickButton(u"删除")

 


    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_Device start--')
    suite=unittest.TestSuite()
    
    #suite.addTest(test_Device('test_0add_Device'))#添加设备
    #suite.addTest(test_Device('test_1search_byDeviceName'))#按设备名称查找
    #suite.addTest(test_Device('test_2search_byDeviceCode'))#按设备编码查找
    suite.addTest(test_Device('test_3search_byOrganization'))#按所属部门查找
    #suite.addTest(test_Device('test_4search_byDeviceType'))#按设备类型查找
    #suite.addTest(test_Device('test_5search_byOrgType'))#按组织类型查找

    #suite.addTest(test_Device('test_6modify_Device'))#修改
    #suite.addTest(test_Device('test_7delete_Device'))#删除
    


    
   

    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_Device end--')
        
