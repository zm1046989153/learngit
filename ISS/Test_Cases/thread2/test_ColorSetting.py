# _*_ coding=utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
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

#颜色编码
color_code='ZM180346'

#颜色名称
color_name=u'ZM_color（自动化）'

#描述信息
color_info=u'蓝色（blue）是一种颜色！！？'

class test_ColorSetting(unittest.TestCase):
    #颜色配置模块测试
    log.info(u"~~~颜色配置模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_ColorSetting(self):
        #进入颜色配置模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入颜色配置
        testModule(driver,u'基础信息',u'颜色配置')
    
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmColorAccordion  table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")
       
        sleep(1)
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmColorToolbar > a.easyui-linkbutton.addButton').click()
           
            sleep(1)
            
            
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmColorToolbar > a.easyui-linkbutton.findButton').click()
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmColorToolbar > a.easyui-linkbutton.editButton').click()
            sleep(1)
            

        elif button==u'导入' or button=='import':
            #查看界面，点击“导入”按钮
            driver.find_element_by_css_selector('#stmColorToolbar > a.easyui-linkbutton.importButton ').click()
            sleep(0.5)
            

        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmColorToolbar > a.easyui-linkbutton.deleteButton').click()
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
            driver.find_element_by_css_selector('body div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.cancelButton> span > span').click()
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


    def searchAssert(self,paths,assert_text):
        '''本函数用于对查找结果断言'''
        driver=self.driver
        n=len(paths)
        
        if n==0:
            #未查找到数据，抛出异常
            raise NameError("Without Data be Searched")
        
        #判断查找到的数据是否正确 
        for path in paths:
            self.assertIn(assert_text,path.text)
            
            '''
             
            if assert_text in path.text:
                continue
            
            else:
                raise NameError("Search Failed!!")
                '''
        
        
    def test_0add_Color(self):
        '''添加颜色'''

        driver=self.driver
        #进入颜色配置
        self.to_ColorSetting()
        
        #点击添加按钮，进入添加界面
        self.clickButton(u'添加')
        
        #填写颜色编码
        strt=time.strftime('%H%M%S',time.localtime(time.time()))
        global color_code
        color_code='ZM'+strt
        driver.find_element_by_css_selector("#stmColorForm  tr:nth-child(1) > td.easyui-myText > input").send_keys(color_code)
        sleep(0.5)
        
        #填写颜色名称
        global color_name
        color_name=u'ZM_color（自动化）'+strt
        driver.find_element_by_css_selector("#stmColorForm  tr:nth-child(2) > td.easyui-myText > input").send_keys(color_name)
        sleep(0.5)

        #填写描述信息
        driver.find_element_by_css_selector("#stmColorForm  tr:nth-child(4) > td.easyui-myText > textarea").send_keys(color_info)
        sleep(0.5)

        #保存
        self.clickButton(u'保存')

    def searchbycode(self,code):
        '''通过颜色编码查找'''
        
        driver=self.driver
        #输入颜色编码
        driver.find_element_by_css_selector('#stmColorToolbar > span:nth-child(4) > input.combo-text.validatebox-text').click()
        sleep(0.5)
        #print code
        driver.find_element_by_css_selector("body > div:nth-child(16) > div > div[value="+code+"]").click()
       
        sleep(0.5)

        #点击查找
        self.clickButton(u'查找')
        
        #断言查找结果
        cds=driver.find_elements_by_css_selector("#stmColorAccordion  table.datagrid-btable td[field='fdCode']")
        self.searchAssert(cds,code)
        

    def test_1search_ByColorCode(self):
        '''按颜色编码查找颜色'''
        
        driver=self.driver
        #进入颜色配置
        self.to_ColorSetting()

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmColorAccordion  table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")
       
        sleep(0.5)

        #获取记录条数信息，用于全部查找断言
        alls_text=driver.find_element_by_css_selector("#stmColorAccordion  div.panel-body.accordion-body > div > div > div.datagrid-pager.pagination >  div.pagination-info").text
        #print alls_text

        #查找方式一：通过颜点击选择色编码查找
        code=driver.find_element_by_css_selector("#stmColorAccordion  table.datagrid-btable td[field='fdCode']").text
        #调用函数通过颜色编码查找颜色
        self.searchbycode(code)


        '''
        #清空输入框内容
        driver.find_element_by_css_selector("#stmColorToolbar > span:nth-child(4) > input").clear()
        sleep(1)

        #查找
        self.clickButton(u"查找")

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmColorAccordion  table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")
       
        sleep(1)

        #断言是否查找出全部记录
        self.assertEqual(alls_text,driver.find_element_by_css_selector("#stmColorAccordion  div.panel-body.accordion-body > div > div > div.datagrid-pager.pagination >  div.pagination-info").text)
        '''


        
       
        
        #刷新页面
        co=driver.find_element_by_css_selector("#content > div.tabs-header.tabs-header-plain.tabs-header-noborder > div.tabs-wrap > ul > li.tabs-selected > a.tabs-inner > span.tabs-title.tabs-closable")
        ActionChains(driver).move_to_element(co).perform()
        sleep(0.5)
        ActionChains(driver).context_click(co).perform()
        sleep(0.5)
        driver.find_element_by_css_selector("#indexmm > div:nth-child(1) > div").click()
        sleep(1)

        
        
        #查找方式二：输入颜色编码，查找
        sc=driver.find_element_by_css_selector('#stmColorToolbar > span:nth-child(4) > input.combo-text.validatebox-text')
        sc.clear()
        sleep(0.5)
        #输入要查找的颜色编码
        sc.send_keys(code)
        sleep(0.5)
        #回车选择
        sc.send_keys(Keys.ENTER)

        #点击查找
        self.clickButton(u'查找')
        sleep(1)

        cds=driver.find_elements_by_css_selector("#stmColorAccordion  table.datagrid-btable td[field='fdCode']")
        #调用断言函数
        self.searchAssert(cds,code)
        '''
        #选择全部

        driver.find_element_by_css_selector("#stmColorToolbar > span:nth-child(4) > input.combo-text.validatebox-text").click()
        sleep(0.5)
        code=u'全部'
        driver.find_element_by_css_selector("body > div:nth-child(16) > div > div[value="+code+"]").click()
    
        sleep(0.5)


        #查找
        self.clickButton(u"查找")

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmColorAccordion  table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")
       
        sleep(1)

        #断言是否查找出全部记录
        self.assertEqual(alls_text,driver.find_element_by_css_selector("#stmColorAccordion  div.panel-body.accordion-body > div > div > div.datagrid-pager.pagination >  div.pagination-info").text)
        '''

    def test_2search_ByColorName(self):
        '''按颜色名称查找颜色'''
        
        driver=self.driver
        #进入颜色配置
        self.to_ColorSetting()
        
        #点击选择颜色名称
        driver.find_element_by_css_selector("#stmColorToolbar > span:nth-child(6) > input").click()
        sleep(0.5)
        name=driver.find_element_by_css_selector("#stmColorAccordion  table.datagrid-btable td[field='fdName']").text
        sleep(0.5)
        driver.find_element_by_css_selector("body > div:nth-child(17) > div>div[value="+name+"]").click()
        
        #点击查找
        self.clickButton(u'查找')

        #获取断言信息，调用断言函数进行断言
        nms=driver.find_elements_by_css_selector("#stmColorAccordion  table.datagrid-btable td[field='fdName']")

        #调用断言函数
        self.searchAssert(nms,name)

        

    def test_3search_ByColorInfo(self):
        '''按描述信息查找颜色'''
        
        driver=self.driver
        #进入颜色配置
        self.to_ColorSetting()
        
        #输入描述信息
        info=color_info
        driver.find_element_by_css_selector("#stmColorToolbar > input.easyui-validatebox.validatebox-text").send_keys(info)
        sleep(1)

        #点击查找
        self.clickButton(u'查找')

        #对查找结果断言
        infs=driver.find_elements_by_css_selector("#stmColorAccordion  table.datagrid-btable td[field='fdRmk']")
        self.searchAssert(infs,info)
        

    def test_4modify_Color(self):
        '''修改颜色配置'''

        driver=self.driver
        #进入颜色配置
        self.to_ColorSetting()

        #查找出要修改的颜色
        code=color_code
        self.searchbycode(code)

        #选择要修改的颜色
        driver.find_element_by_css_selector("#stmColorAccordion  table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #点击修改按钮
        self.clickButton(u'修改')

        #修改颜色名称
        name='new'+color_name

        nb=driver.find_element_by_css_selector("#stmColorForm  tr:nth-child(2) > td.easyui-myText > input")
        nb.clear()
        sleep(0.5)
        nb.send_keys(name)
        sleep(0.5)
        
        #点击保存
        self.clickButton(u'保存')
        sleep(1)
        
        #再次查找修改的颜色
        #self.searchbycode(code)
        self.clickButton(u'查找')
        
        #断言是否和修改的名称一致
        nms=driver.find_elements_by_css_selector("#stmColorAccordion  table.datagrid-btable td[field='fdName']")
        
        #调用断言函数
        self.searchAssert(nms,name)
        

    def test_5delete_Color(self):
        u'''删除颜色'''

        driver=self.driver
        #进入颜色配置
        self.to_ColorSetting()

        #通过颜色编码查找要删除的颜色
        code=color_code
        self.searchbycode(code)

        #选择要删除的记录
        driver.find_element_by_css_selector("#stmColorAccordion  table.datagrid-btable td[field='ck']").click()

        #删除
        self.clickButton(u'删除')
        

    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit()



if __name__=='__main__':
    
    #建立测试集
    suite=unittest.TestSuite()
    
    #suite.addTest(test_ColorSetting('test_0add_Color'))#添加颜色
    suite.addTest(test_ColorSetting('test_1search_ByColorCode'))#按颜色编码查找
    #suite.addTest(test_ColorSetting('test_2search_ByColorName'))#按颜色名称查找
    #suite.addTest(test_ColorSetting('test_3search_ByColorInfo'))#按描述信息查找
    #suite.addTest(test_ColorSetting('test_4modify_Color'))#修改颜色
    #suite.addTest(test_ColorSetting('test_5delete_Color'))#删除颜色
    
    #执行测试
    runner=unittest.TextTestRunner()
    #runner.run(suite)
    unittest.main()
        
        
