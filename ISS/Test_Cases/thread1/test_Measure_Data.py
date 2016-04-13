# _*_ coding:utf-8 _*_
__author__='Zhenming'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys
import xml.dom.minidom

sys.path.append('D:\\ISS\\Test_Cases\\public')
import login
from isspublic import*

#打开xml文件
dom=xml.dom.minidom.parse('D:\\ISS\\Test_Data\\login.xml')
#dom1=xml.dom.minidom.parse('D:\\ISS\\Test_Data\\Measure_Data.xml')

#获取文档元素对象
root=dom.documentElement
#root1=dom1.documentElement
#获取帐号密码
logins=root.getElementsByTagName("login")
username=logins[0].getAttribute("username")
password=logins[0].getAttribute("password")

swiftnum=''#用于存储流水号

class test_Measure_Data(unittest.TestCase):
    log.info(u"~~~商品档案模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.verificationErrors=[]
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data

        
        
    
    def test_0add_measureData(self):
        u"添加量体据"
        driver=self.driver
        self.to_measureData()#进入量体数据模块
        sleep(2)
        
        #点击添加按钮
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > a.easyui-linkbutton.addButton > span > span").click()
        sleep(2)

        #填写着装人手机
        driver.find_element_by_css_selector("#ctmMeasureHdForm  tr:nth-child(1) > td.easyui-numberbox.validatebox-text > input").send_keys("18350293137")
        sleep(2)
        
        #填写着装人姓名
        dressperson=u"李四"
        driver.find_element_by_css_selector("#ctmMeasureHdForm  tr:nth-child(1) > td.easyui-validatebox.validatebox-text > input").send_keys(dressperson)
        sleep(2)

        #选择性别
        sex=driver.find_element_by_css_selector("#ctmMeasureHdForm tr:nth-child(1) > td:nth-child(12) > span > input.combo-text.validatebox-text")
        sex.click()
        sex.send_keys(Keys.DOWN)
        sex.send_keys(Keys.ENTER)
        sleep(2)
        
        #选择量体时间
        time=driver.find_element_by_css_selector("#ctmMeasureHdForm tr:nth-child(2) > td:nth-child(4) > span > input.combo-text.validatebox-text.validatebox-invalid")
        time.click()
        time.send_keys(Keys.ENTER)

        #保存
        driver.find_element_by_css_selector("#ctmMeasureHdForm > div:nth-child(1) > a:nth-child(1)> span > span > span").click()
        sleep(2)
        
        #获取断言信息
        success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
        #print success.text
        self.assertEqual(u"保存成功！",success.text)
        #确定，回到列表界面
        driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()
        sleep(2)
        
        
        #获取流水号
        global swiftnum
        swiftnum=driver.find_element_by_css_selector("table.datagrid-btable td[field='fdCode']").text
        #print swiftnum

        
    def test_1search_BySwiftNumber(self):
        u"通过流水号查找"
        driver=self.driver
        self.to_measureData()#进入量体数据模块
        sleep(1)
        num=driver.find_element_by_css_selector("table.datagrid-btable td[field='fdCode']").text
        
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > input.easyui-numberbox.validatebox-text").send_keys(num)#输入查找的流水号
        sleep(0.5)

        #点击查找
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > a.easyui-linkbutton.findButton > span > span").click()
        WebWait(driver,"#ctmMeasureHdAccordion div.datagrid-mask")
        sleep(0.5)
        
        
        #对查找结果进行判断
        sns=driver.find_elements_by_css_selector("table.datagrid-btable td[field='fdCode']")
        for sn in sns:
            #print sn.text
            if swiftnum[0] in sn.text:
                continue
            raise NameError("No Such Data")
        

    def test_2search_ByDressPerson(self):
        u"通过着装人姓名查找"
          
        driver=self.driver
        self.to_measureData()#进入量体数据模块
        sleep(0.5)
          
        name=u"李四"#设置着装人姓名
        sleep(0.5)
        
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > input:nth-child(3)").send_keys(name)
        sleep(0.5)
        
        #点击查找
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > a.easyui-linkbutton.findButton > span > span").click()
        WebWait(driver,"#ctmMeasureHdAccordion div.datagrid-mask")
        #对查找结果进行判断
        sleep(2)
        
        ns=driver.find_elements_by_css_selector("table.datagrid-btable td[field='measureStmUser']")
        for n in ns:
            #print n.text
            if name in n.text:
                continue
            raise NameError("No Such Data")

        
    def test_3lookUp_MeasureData(self):
        u"查看量体数据"
        driver=self.driver
        self.to_measureData()#进入量体数据模块
        sleep(2)
        
        #选择一条记录
        driver.find_element_by_css_selector("#ctmMeasureHdAccordion table.datagrid-btable td[field='ck']").click()
        sleep(2)

        #点击查看
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > a.easyui-linkbutton.viewButton > span > span").click()
        sleep(2)
        
        #断言是否进入查看界面
        self.assertEqual(u"编辑",driver.find_element_by_css_selector("#ctmMeasureHdForm  a.easyui-linkbutton.saveButton > span > span > span").text)
        

    def test_4modify_MeasureData(self):
        u"修改量体数据"
        driver=self.driver
        self.to_measureData()#进入量体数据模块
        sleep(2)

     
 
        #输入查找的流水号
        snum=swiftnum
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > input.easyui-numberbox.validatebox-text").send_keys(snum)
        sleep(2)
            
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > a.easyui-linkbutton.findButton > span > span").click()#点击查找
        sleep(2)
            
        #对查找结果进行判断
        self.assertEqual(snum,driver.find_element_by_css_selector("table.datagrid-btable td[field='fdCode']").text)
            
        #选择列表中的第一个记录
        driver.find_element_by_css_selector("table.datagrid-btable td[field='ck']").click()
        sleep(2)

        #点击修改按钮
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > a.easyui-linkbutton.editButton  > span > span").click()
        sleep(2)
        
        #修改试穿商品
        db=driver.find_element_by_css_selector("#ctmMeasureHdForm > table tr:nth-child(1) > td:nth-child(14) > span > input.combo-text.validatebox-text")
        db.click()
        sleep(0.5)
        db.send_keys(Keys.DOWN)
        sleep(0.5)
        db.send_keys(Keys.ENTER)
        sleep(2)
        

        #保存
        driver.find_element_by_css_selector("#ctmMeasureHdForm > div:nth-child(1) > a:nth-child(1)> span > span > span").click()
        sleep(2)
        
        #获取断言信息
        success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
        #print success.text
        self.assertEqual(u"保存成功！",success.text)
        driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

        #print swiftnum[0]
        
    
        
         
        
    def to_measureData(self):
        u"进入量体数据模块"

        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入量体数据模块
        testModule(driver,u'会员管理',u'量体数据')
        isRefreshed(driver,"table.datagrid-btable td[field='ck']")
        
        sleep(1)

        
    def test_5delete_MeasureData(self):
        u"删除量体数据"
        driver=self.driver
        self.to_measureData()#进入量体数据模块
        sleep(2)

        #number="147"#设置要删除的版本流水号
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > input.easyui-numberbox.validatebox-text").send_keys(swiftnum)#输入要查找的流水号
        sleep(1)
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > a.easyui-linkbutton.findButton > span > span").click()#点击查找
        sleep(2)
        
        driver.find_element_by_css_selector("table.datagrid-btable td[field='ck']").click()#选择要删除的记录
        sleep(2)
        
        #点击删除按钮
        driver.find_element_by_css_selector("#ctmMeasureHdToolbar > a.easyui-linkbutton.deleteButton > span > span").click()
        sleep(1)

        #点击确定
        driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
        sleep(1)
        
        #获取断言信息
        dele_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text
        #print dele_text
        self.assertEqual(u"删除成功",dele_text)

     
    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
          
  


if __name__=="__main__":
    #构造测试集
    suite=unittest.TestSuite()
    #suite.addTest(test_Measure_Data('to_measureData'))#进入量体数据模块
    #suite.addTest(test_Measure_Data('test_0add_measureData'))#添加量体数据
    #suite.addTest(test_Measure_Data('test_1search_BySwiftNumber'))#通过流水号查找
    #suite.addTest(test_Measure_Data('test_2search_ByDressPerson'))#通过着装人查找
    
    suite.addTest(test_Measure_Data('test_3lookUp_MeasureData'))#查看量体数据
    #suite.addTest(test_Measure_Data('test_4modify_MeasureData'))#修改量体数据
    #suite.addTest(test_Measure_Data('test_5delete_MeasureData'))#删除量体数据

    #执行测试
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
  
