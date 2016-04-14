# _*_ coding=utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys,unittest,time
import xml.dom.minidom

sys.path.append('D:\\ISS\\Test_Cases\\public')
import login
from isspublic import*

#打开xml文件
dom=xml.dom.minidom.parse('D:\\ISS\\Test_Data\\login.xml')
#获取文件元素对象
root=dom.documentElement

#尺码编码
size_code='ZM101716'

#尺码名称
size_name=u'ZM_Size(自动化)103411'

#描述信息
size_info=u'尺码XXL！！？'

class test_SizeSetting(unittest.TestCase):
    #尺码配置模块测试
    log.info(u"~~~尺码配置模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_SizeSetting(self):
        #进入尺码配置
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入颜色配置
        testModule(driver,u'基础信息',u'尺码配置')

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmSizeAccordion table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(1)
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmSizeToolbar > a.easyui-linkbutton.addButton').click()
           
            sleep(1)
            
            
            
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmSizeToolbar > a.easyui-linkbutton.findButton').click()
            #print findCss(driver,"#stmSizeAccordion > div:nth-child(1) > div.panel-body.accordion-body > div > div > div.datagrid-mask-msg").text
            #等待页面刷新
            WebWait(driver,"#stmSizeAccordion > div:nth-child(1) > div.panel-body.accordion-body > div > div > div.datagrid-mask")
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmSizeToolbar > a.easyui-linkbutton.editButton').click()
            sleep(1)
            

        elif button==u'导入' or button=='import':
            #查看界面，点击“导入”按钮
            driver.find_element_by_css_selector('#stmSizeToolbar > a.easyui-linkbutton.importButton ').click()
            sleep(0.5)
            

        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmSizeToolbar > a.easyui-linkbutton.deleteButton').click()
            sleep(1)
            
            #点击确认，删除记录并断言
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            sleep(1)
            dele_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text
            #print dele_text
            self.assertEqual(u"删除成功",dele_text)
            
            #点击取消
            #driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2)").click()
                
        elif button==u'取消' or button=='cancel':
            #编辑界面，点击“取消”按钮
            driver.find_element_by_css_selector('body div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.cancelButton> span > span').click()
            sleep(0.5)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮
            driver.find_element_by_css_selector("body div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.saveButton > span > span").click()
            
            sleep(0.5)
            
             #获取断言信息
            success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
            tip_text=success.text
            
            #确定,关闭提示框
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

            #断言是否保存成功
            self.assertEqual(u"保存成功！",tip_text)
            
        
        else:
            raise NameError('No Such Button,confirm again please')

        
        
    def test_0add_Size(self):
        u'''添加尺码'''
        driver=self.driver
        #进入尺码配置
        self.to_SizeSetting()
        
        #点击添加按钮，进入添加界面
        self.clickButton(u'添加')

        
        strt=time.strftime('%H%M%S',time.localtime(time.time()))
        #尺码编码
        global size_code
        size_code='ZM'+strt
        driver.find_element_by_css_selector("#stmSizeForm  tr:nth-child(1) > td.easyui-myText > input").send_keys(size_code)
        sleep(0.5)

        #尺码名称
        global size_name
        size_name=u'ZM_Size(自动化)'+strt
        driver.find_element_by_css_selector("#stmSizeForm tr:nth-child(2) > td.easyui-myText > input").send_keys(size_name)
        sleep(0.5)

        #保存
        self.clickButton(u'保存')

    def searchbycode(self,code):
        '''按编码查找'''

        driver=self.driver
        #点击选择要查找的尺码
        driver.find_element_by_css_selector("#stmSizeToolbar > span:nth-child(3) > input").click()
       
        sleep(0.5)
        #print code
        driver.find_element_by_css_selector("body > div:nth-child(16) > div > div[value="+code+"]").click()
        sleep(0.5)

        #点击查找
        self.clickButton(u'查找')

        #查找结果断言
        szs=driver.find_elements_by_css_selector("#stmSizeAccordion table.datagrid-btable td[field='fdCode']")
        
        #调用函数断言
        searchAssert(self,szs,code)
        
        
         
    def test_1search_BySizeCode(self):
        u'''按尺码编码查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码配置
        self.to_SizeSetting()
        
        #要查找的编码
        code=driver.find_element_by_css_selector("#stmSizeAccordion table.datagrid-btable td[field='fdCode']").text
        #print code
        #调用函数查找
        self.searchbycode(code)

        
    def test_2search_BySizeName(self):
        u'''按尺码名称查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码配置
        self.to_SizeSetting()

        #设置要查找的尺码名称
        name=driver.find_element_by_css_selector("#stmSizeAccordion table.datagrid-btable td[field='fdName']").text

        #选择尺码名称
        driver.find_element_by_css_selector("#stmSizeToolbar > span:nth-child(6) > input").click()
        sleep(0.5)
        driver.find_element_by_css_selector("body > div:nth-child(17) > div > div[value="+'\''+name+'\''+"]").click()
        sleep(0.5)
        
        #查找
        self.clickButton(u'查找')

        #断言
        nas=driver.find_elements_by_css_selector("#stmSizeAccordion table.datagrid-btable td[field='fdName']")
        searchAssert(self,nas,name)
        

    def test_3modify_Size(self):
        u'''修改尺码'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码配置
        self.to_SizeSetting()

        #查找要修改的尺码
        code=size_code
        self.searchbycode(code)

        #勾选查找出的尺码
        driver.find_element_by_css_selector("#stmSizeAccordion table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u'修改')

        #修改尺码名称
        name='n_'+size_name

        sl=driver.find_element_by_css_selector("#stmSizeForm tr:nth-child(2) > td.easyui-myText > input")
        sl.clear()
        sleep(0.5)
        sl.send_keys(name)
        sleep(0.5)

        #保存
        self.clickButton(u'保存')
        sleep(0.5)
        
        #等待页面刷新
        WebWait(driver,"#stmSizeAccordion > div:nth-child(1) > div.panel-body.accordion-body > div > div > div.datagrid-mask")
        
        #再次查找
        self.clickButton(u"查找")
        sleep(0.5)
        
        #断言是否和修改的一致
        self.assertEqual(name,driver.find_element_by_css_selector("#stmSizeAccordion table.datagrid-btable td[field='fdName']").text)
        


    def test_4delete_Size(self):
        u'''删除尺码'''

        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码配置
        self.to_SizeSetting()
        
        #查找要修改的尺码
        code=size_code
        self.searchbycode(code)

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmSizeAccordion table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        sleep(0.5)

        #勾选查找出的尺码
        driver.find_element_by_css_selector("#stmSizeAccordion table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #删除
        self.clickButton(u'删除')
        


    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit()




if __name__=='__main__':
    
    #建立测试集
    suite=unittest.TestSuite()
    
    suite.addTest(test_SizeSetting('test_0add_Size'))#添加颜色
    #suite.addTest(test_SizeSetting('test_1search_BySizeCode'))#按尺码编码查找
    #suite.addTest(test_SizeSetting('test_2search_BySizeName'))#按尺码名称查找
    suite.addTest(test_SizeSetting('test_3modify_Size'))#修改尺码
    suite.addTest(test_SizeSetting('test_4delete_Size'))#删除尺码
    
    
    #执行测试
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
        
        
