# _*_ coding=utf-8 _*_

from selenium import webdriver
from time import sleep
import sys,unittest,time
import xml.dom.minidom
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

sys.path.append('D:\\ISS\\Test_Cases\\public')
import login
from isspublic import*

#打开xml文件
dom=xml.dom.minidom.parse('D:\\ISS\\Test_Data\\login.xml')
#获取文件元素对象
root=dom.documentElement

com_code='ZM'#用于存放商品编码
com_name=u'zm衬衫（自动化）'#用于存放商品名称

class test_CommodityFile(unittest.TestCase):
    
    #商品档案模块测试
    log.info(u"~~~商品档案模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_CommodityFile(self):
        '''进入商品档案模块'''
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入商品档案
        testModule(driver,u'基础信息',u'商品档案')
        
         #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masPartHdAccordion table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        

    
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#masPartHdToolbar > a.easyui-linkbutton.addButton').click()
            sleep(1)
            
            
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#masPartHdToolbar > a.easyui-linkbutton.findButton').click()
            #print findCss(driver,"#masPartHdAccordion > div:nth-child(1) > div.panel-body.accordion-body > div > div > div.datagrid-mask-msg").text
            WebWait(driver,"#masPartHdAccordion > div:nth-child(1) > div.panel-body.accordion-body > div > div > div.datagrid-mask-msg")
            sleep(1)
            
            
        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#masPartHdToolbar > a.easyui-linkbutton.viewButton').click()
            WebWait(driver,"#masPartHdForm > div.datagrid-mask-msg")
            sleep(1)
            
            #判断是否进入查看界面
            self.assertEqual(u'取消',driver.find_element_by_css_selector("#masPartHdForm > div > a.easyui-linkbutton.cancelButton > span > span").text)
            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#masPartHdToolbar > a.easyui-linkbutton.editButton').click()
            sleep(1)

        elif button==u'修改商品状态' or button=='modifys':
 
            #点击“查看”按钮
            driver.find_element_by_css_selector('#masPartHdToolbar > a.easyui-linkbutton.editMasPartHdStatus').click()
            sleep(1)
            
         

        elif button==u'编辑' or button=='edit':
            #查看界面，点击“编辑”按钮
            driver.find_element_by_css_selector("#masPartHdForm>div>a.easyui-linkbutton.saveButton").click()
            sleep(0.5)
            
            
        elif button==u'取消' or button=='cancel':
            #编辑界面，点击“取消”按钮
            driver.find_element_by_css_selector('#masPartHdForm > div > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮
            driver.find_element_by_css_selector("form#masPartHdForm>div>a.easyui-linkbutton.saveButton").click()
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
        
    def choice_sort(self):
        '''选择商品分类'''
        driver=self.driver

        #选择商品类别
        sleep(1)
        driver.find_element_by_css_selector("#qsmaspartclasswindowZtree_1 > a#qsmaspartclasswindowZtree_1_a").click()
        sleep(0.5)
        
        driver.find_element_by_css_selector("body div.panel-body.panel-body-noborder.window-body.panel-noscroll div.panel.layout-panel.layout-panel-center  div.panel.layout-panel.layout-panel-center table.datagrid-btable td[field='ck']").click()
        
       
        #获取选择的类别名称
        sort_text=driver.find_element_by_css_selector("body div.panel-body.panel-body-noborder.window-body.panel-noscroll div.panel.layout-panel.layout-panel-center  div.panel.layout-panel.layout-panel-center table.datagrid-btable td[field='fdName']").text
        sleep(0.5)
        #保存
        driver.find_element_by_css_selector("body  div.panel-body.panel-body-noborder.window-body.panel-noscroll > div > div.panel.layout-panel.layout-panel-center  div.panel.layout-panel.layout-panel-south > div > a.easyui-linkbutton.saveButton.l-btn.l-btn-plain > span > span").click()
        sleep(0.5)
        #返回商品类别名称
        return sort_text
                
        

    def test_0add_File(self):
        '''商品种类添加'''
        log.info(u"开始执行用例...")

        #进入商品档案模块
        self.to_CommodityFile()

        driver=self.driver
        sleep(1)
        #点击添加按钮
        self.clickButton(u'添加')
        
        #商品编码
        strt=time.strftime('%H%M%S',time.localtime(time.time()))
        global com_code
        com_code='ZM'+strt
        driver.find_element_by_css_selector("#masPartHdForm  tr:nth-child(2) > td:nth-child(11) > input").send_keys(com_code)
        
        #商品名称
        driver.find_element_by_css_selector("#masPartHdForm  tr:nth-child(2) > td:nth-child(13) > input").send_keys(com_name)

        #商品分类
        driver.find_element_by_css_selector("#masPartHdForm  tr:nth-child(2) > td:nth-child(15) > span > input.combo-text.validatebox-text.validatebox-invalid").click()
        self.choice_sort()

        #商品状态
        st=driver.find_element_by_css_selector("#masPartHdForm tr:nth-child(2) > td:nth-child(17) > span > input.combo-text.validatebox-text")
        st.send_keys(u'新增')
        sleep(0.5)
        st.send_keys(Keys.ENTER)

        #上市年度
        driver.find_element_by_css_selector("#masPartHdProdForm  tr:nth-child(1) > td:nth-child(4) > input.easyui-numberbox.validatebox-text.validatebox-invalid").send_keys('2016')

        #商品单位
        su=driver.find_element_by_css_selector("#masPartHdProdForm  tr:nth-child(1) > td:nth-child(6) > span > input.combo-text.validatebox-text")
        su.send_keys(u'件')
        sleep(0.5)
        su.send_keys(Keys.ENTER)

        #商品品牌
        p=driver.find_element_by_css_selector("#masPartHdProdForm  tr:nth-child(1) > td:nth-child(8) > span > input.combo-text.validatebox-text")
        p.send_keys("GREAT MASTER")
        sleep(0.5)
        p.send_keys(Keys.ENTER)
        
        #吊牌价
        driver.find_element_by_css_selector("#masPartHdProdForm tr:nth-child(2) > td:nth-child(6) > input.easyui-numberbox.validatebox-text.validatebox-invalid").send_keys('999')

    
        #保存并断言
        success_text=self.clickButton(u'保存')
        

    def searchbycode(self,code):  
            '''此函数用于按商品编码查找商品,提供要查找的code'''
            
            #输入查找的商品编码
            driver=self.driver
            sb=driver.find_element_by_css_selector("#masPartHdToolbar > input:nth-child(1)")
            sb.clear()
            sleep(0.5)
            sb.send_keys(code)

            #点击查找
            self.clickButton(u'查找')
            #判断页面是否刷新
            log.info(u"等待页面刷新···")
            isRefreshed(driver,"#masPartHdAccordion table.datagrid-btable td[field='ck']")
            log.info(u"刷新完成！！！")

            
    def test_1search_ByCode(self):
        '''按商品编码查找'''
        log.info(u"开始执行用例...")
        
        #进入商品档案模块
        self.to_CommodityFile()
        driver=self.driver
        sleep(1)

        code=driver.find_element_by_css_selector('#masPartHdAccordion table.datagrid-btable td[field="fdCode"]').text
        
        #调用函数查找
        self.searchbycode(code)
        

        #获取查找到的信息
        coes=driver.find_elements_by_css_selector('#masPartHdAccordion table.datagrid-btable td[field="fdCode"]')
        sleep(0.5)

        #调用函数断言
        searchAssert(self,coes,code)

        
        

        
    def test_2search_ByName(self):
        '''按商品名称查找'''
        log.info(u"开始执行用例...")
                    
        #进入商品档案模块
        self.to_CommodityFile()

        driver=self.driver
        sleep(1)
        
        #输入要查找的商品名称
        name=driver.find_element_by_css_selector('#masPartHdAccordion table.datagrid-btable td[field="fdName"]').text
        driver.find_element_by_css_selector("#masPartHdToolbar > input:nth-child(2)").send_keys(name)

        #点击查找
        self.clickButton(u'查找')
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masPartHdAccordion table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        
        #获取查找到的信息
        nas=driver.find_elements_by_css_selector('#masPartHdAccordion table.datagrid-btable td[field="fdName"]')
        sleep(0.5)
        #调用函数断言
        searchAssert(self,nas,name)
        

                    
    def test_3search_BySort(self):
        '''按商品类别查找'''
        log.info(u"开始执行用例...")
                    
        #进入商品档案模块
        self.to_CommodityFile()

        driver=self.driver
        sleep(1)
        
        #选择商品分类
        driver.find_element_by_css_selector("#masPartHdToolbar > span > input.combo-text.validatebox-text").click()
        #调用函数选择分类
        sort_text=self.choice_sort()
        
        #点击查找
        self.clickButton(u'查找')

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masPartHdAccordion table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")

        #获取断言信息
        sorts=driver.find_elements_by_css_selector('#masPartHdAccordion table.datagrid-btable td[field="partClassKey"]')
        sleep(0.5)
        
        #调用函数断言
        searchAssert(self,sorts,sort_text)
        
        

                    
    def test_4view_Com(self):
        '''查看商品档案'''
        log.info(u"开始执行用例...")
                    
        #进入商品档案模块
        self.to_CommodityFile()

        driver=self.driver
        sleep(1)
        
        #输入查找的商品编码
        code=com_code
        driver.find_element_by_css_selector("#masPartHdToolbar > input:nth-child(1)").send_keys(code)

        #点击查找
        self.clickButton('search')

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masPartHdAccordion table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        
        #选择一条记录
        driver.find_element_by_css_selector('#masPartHdAccordion table.datagrid-btable td[field="ck"]').click()
        
        #点击“查看”
        self.clickButton(u'查看')

        

        #点击保存
        self.clickButton(u'取消')
        
        
                    

    def test_5modify_Com(self):
        '''修改商品档案'''
        log.info(u"开始执行用例...")
                    
        #进入商品档案模块
        self.to_CommodityFile()

        driver=self.driver
        sleep(1)
        #查找的code
        code=com_code
        
        #调用函数查找对应编码的商品
        self.searchbycode(code)
        
        #选择一条记录
        driver.find_element_by_css_selector('#masPartHdAccordion table.datagrid-btable td[field="ck"]').click()
        
        #点击“修改”
        self.clickButton(u'修改')

        #等待页面更新
        WebWait(driver,"#masPartHdForm > div.datagrid-mask-msg")

        #修改商品名称
        new_name=u'new_zm衬衫（自动化）'
        nl=driver.find_element_by_css_selector("#masPartHdForm  tr:nth-child(2) > td:nth-child(13) > input")
        nl.clear()
        
        sleep(0.5)
        
        nl.send_keys(new_name)
        
        #点击保存并断言
        self.clickButton(u'保存')

        #再次调用函数查找对应编码的商品
        self.searchbycode(code)
        
        modify_text=driver.find_element_by_css_selector('#masPartHdAccordion table.datagrid-btable td[field="fdName"]').text
        #print modify_text
        self.assertEqual(new_name,modify_text)
        
    def test_6modify_ComStatus(self):
        '''修改商品状态'''
        log.info(u"开始执行用例...")
        
        #进入商品档案模块
        self.to_CommodityFile()

        driver=self.driver
        sleep(1)
        
        #查找的code
        code=com_code
        
        #调用函数查找对应编码的商品
        self.searchbycode(code)
        
        #选择一条记录
        driver.find_element_by_css_selector('#masPartHdAccordion table.datagrid-btable td[field="ck"]').click()
        sleep(0.5)
        
        #点击修改商品状态按钮
        self.clickButton(u'修改商品状态')
        sleep(1)

        #将状态改为已审核
        sb=driver.find_element_by_css_selector('#masPartHdSS tr > td.easyui-myText > span > input.combo-text.validatebox-text')
        sb.clear()
        sleep(0.5)
        sb.send_keys(u'已审核')
        sleep(0.5)
        sb.send_keys(Keys.ENTER)
        
        #点击提交
        driver.find_element_by_css_selector('#masPartHdStatusWindow > div:nth-child(2) > a.easyui-linkbutton.buttonSavemasPartHdStatus.l-btn > span > span').click()
        sleep(1)

        #获取断言信息
        assert_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)").text
        
        self.assertEqual(u'商品状态保存成功！',assert_text)

        
    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit()

                     

if __name__=='__main__':

    log.info("test_CommodityFile start~~~")
                     
    suite=unittest.TestSuite()
    #添加测试
    #suite.addTest(test_CommodityFile('test_0add_File'))#添加商品档案
    #suite.addTest(test_CommodityFile('test_1search_ByCode'))#按商品编码查找
    suite.addTest(test_CommodityFile('test_2search_ByName'))#按商品名称查找
    #suite.addTest(test_CommodityFile('test_3search_BySort'))#按商品分类查找
    #suite.addTest(test_CommodityFile('test_4view_Com'))#查看商品档案
    #suite.addTest(test_CommodityFile('test_5modify_Com'))#修改商品档案
    #suite.addTest(test_CommodityFile('test_6modify_ComStatus'))#修改商品状态
    
    #执行测试
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info("test_CommodityFile end~~~")
        
