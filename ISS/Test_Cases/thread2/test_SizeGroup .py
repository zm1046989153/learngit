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

#尺码组编码
sgroup_code='SIZE102457'

#尺码组名称
sgroup_name='ZM_SIZE103014'

#品牌
brand=u'启尚'

#品类
category=u'成衣'

#版型
version=u'修身'

#描述信息
sgroup_info=u'这是一个尺码组！@￥@%#123112'

class test_SizeGroup(unittest.TestCase):
    #尺码组配置模块测试
    log.info(u"~~~尺码组配置模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_SizeGroup(self):
        #进入尺码组配置模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入尺码组配置
        testModule(driver,u'基础信息',u'尺码组配置')
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmSizeGroupAction  table.datagrid-btable td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(1)
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmSizeGroupToolbar > a.easyui-linkbutton.addPropButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmSizeGroupToolbar > a.easyui-linkbutton.findButton > span > span').click()
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmSizeGroupToolbar > a.easyui-linkbutton.editButton > span > span').click()
            sleep(1)
    
            
        elif button==u'导入' or button=='import':
            #点击“导入”按钮
            driver.find_element_by_css_selector('#stmSizeGroupToolbar > a.easyui-linkbutton.importButton > span > span').click()
            sleep(1)
            
            
        elif button==u'编辑' or button=='edit':
            #点击“编辑”按钮
            driver.find_element_by_css_selector("#masPartDtSkuForm > div > a.easyui-linkbutton.saveButton > span > span > span").click()
            sleep(1)
            
    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmSizeGroupToolbar > a.easyui-linkbutton.deleteButton > span > span').click()
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
            driver.find_element_by_css_selector('body  div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            #取消
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            
            sleep(1)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("body  div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.easyui-linkbutton.saveButton > span > span").click()
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

        
    def test_0add_SizeGroup(self):
        u'''添加尺码组'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码组
        self.to_SizeGroup()

        #点击添加
        self.clickButton(u'添加')

        #尺码组编码
        global sgroup_code
        strt=time.strftime("%H%M%S",time.localtime(time.time()))
        sgroup_code='SIZE'+strt
        code=sgroup_code
        driver.find_element_by_css_selector("#ModifySizeForm  tr:nth-child(1) > td:nth-child(8) > input").send_keys(code)
        sleep(0.5)

        #尺码组名称
        global sgroup_name
        sgroup_name='ZM_SIZE'+strt
        name=sgroup_name
        driver.find_element_by_css_selector("#ModifySizeForm  tr:nth-child(1) > td:nth-child(10) > input").send_keys(name)
        sleep(0.5)

        #品牌
        driver.find_element_by_css_selector("#ModifySizeForm  tr:nth-child(2) > td.easyui-myText > span > input.combo-text.validatebox-text.validatebox-invalid").send_keys(brand)
        sleep(0.5)

        #品类
        driver.find_element_by_css_selector("#partClassKey").click()
        sleep(0.5 )
        cys=driver.find_elements_by_css_selector("#treeDemo > li")
        n=0
        for cy in cys:
            #print cy.text
            n+=1
            if cy.text==category:
                cys=driver.find_element_by_css_selector("#treeDemo > li:nth-child("+str(n)+") > a > span").click()
                break
                
        #版型
        driver.find_element_by_css_selector("#ModifySizeForm tr:nth-child(3) > td:nth-child(2) > span > input.combo-text.validatebox-text").send_keys(version)
        sleep(0.5)

        #描述信息
        driver.find_element_by_css_selector("#ModifySizeForm tr:nth-child(3) > td:nth-child(4) > input").send_keys(sgroup_info)
        sleep(0.5)

        #选择尺码
        driver.find_element_by_css_selector("#ModifySizeForm > div.left  div.datagrid-body > table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #右移
        driver.find_element_by_css_selector("#ModifySizeForm > div.middle > input.leftToRight").click()
        sleep(0.5)

        #保存
        self.clickButton(u'保存')


    def isRefreshed(self):
        '''判断页面是否刷新'''
        #用于判断页面是否刷新
        driver=self.driver
        while 1:
            try:
                driver.implicitly_wait(5)
                log.info(driver.find_element_by_css_selector("#stmSizeGroupAction  div.datagrid-mask-msg").text)
                print driver.find_element_by_css_selector("#stmSizeGroupAction  div.datagrid-mask-msg").text
                sleep(0.5)
                continue
            except:
                driver.implicitly_wait(20)
                break
        sleep(0.5)

        
    def test_1search_byCategory(self):
        u'''按品类查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码组
        self.to_SizeGroup()

        #选择品类
        driver.find_element_by_css_selector("#stmSizefdpartClass").send_keys(category)
        
        sleep(0.5)
        
        #查找
        self.clickButton(u'查找')

        #判断页面是否刷新
        self.isRefreshed()

        #断言
        cts=findsCss(driver,"#stmSizeGroupAction table.datagrid-btable td[field='partClassKey']")
        searchAssert(self,cts,category)

      
    def test_2search_byBrand(self):
        u'''按品牌查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码组
        self.to_SizeGroup()

        #输入要查找的品牌
        findCss(driver,"#stmSizeGroupToolbar > span:nth-child(7) > input").send_keys(brand)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")



        #判断页面是否刷新
        self.isRefreshed()

        #断言
        bds=findsCss(driver,"#stmSizeGroupAction table.datagrid-btable td[field='brandKey']")
        searchAssert(self,bds,brand)

    def test_3search_byVersion(self):
        u'''按版型查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码组
        self.to_SizeGroup()


        #输入要查找的版型
        findCss(driver,"#stmSizeGroupToolbar > span:nth-child(11) > input").send_keys(version)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #判断页面是否刷新
        self.isRefreshed()

        #断言
        vns=findsCss(driver,"#stmSizeGroupAction table.datagrid-btable td[field='stereoTypeKey']")
        searchAssert(self,vns,version)


    def searchbycode(self,code):
        '''按编号查找'''
        driver=self.driver

        #输入要查找的编号
        findCss(driver,"#stmSizeGroupToolbar > span:nth-child(14) > input").send_keys(code)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #判断页面是否刷新
        self.isRefreshed()

        #断言
        cds=findsCss(driver,"#stmSizeGroupAction table.datagrid-btable td[field='fdCode']")
        searchAssert(self,cds,code)


    def test_4search_bySGroupCode(self):
        u'''按尺码组编码查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码组
        self.to_SizeGroup()

        #查找
        code=sgroup_code
        self.searchbycode(code)

    def test_5search_bySGroupName(self):
        u'''按尺码组名称查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码组
        self.to_SizeGroup()

         #输入要查找的尺码组名称
        name=sgroup_name
        findCss(driver,"#stmSizeGroupToolbar > span:nth-child(16) > input").send_keys(name)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #判断页面是否刷新
        self.isRefreshed()

        #断言
        nas=findsCss(driver,"#stmSizeGroupAction table.datagrid-btable td[field='fdName']")
        searchAssert(self,nas,name)

        
        
    def test_6search_bySGroupInfo(self):
        u'''按描述信息查找'''
        log.info(u"开始执行用例...")
         
        driver=self.driver
        #进入尺码组
        self.to_SizeGroup()

        #输入要查找的尺码组名称
        info=sgroup_info
        findCss(driver,"#stmSizeGroupToolbar > input.easyui-validatebox.validatebox-text").send_keys(info)
        sleep(0.5)

        #查找
        self.clickButton(u"查找")

        #判断页面是否刷新
        self.isRefreshed()

        #断言
        inos=findsCss(driver,"#stmSizeGroupAction table.datagrid-btable td[field='fdMemo']")
        searchAssert(self,inos,info)


        
    def test_7modify_SizeGroup(self):
        u'''修改尺码组'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码组
        self.to_SizeGroup()

        #查找
        code=sgroup_code
        self.searchbycode(code)

        #选择一个记录
        findCss(driver,"#stmSizeGroupAction table.datagrid-btable td[field='ck']").click()

        #修改
        self.clickButton(u"修改")

        #左移选择的尺码
        findCss(driver,"#ModifySizeForm > div.right > div > div > div > div.datagrid-view2 > div.datagrid-body > table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #左移
        findCss(driver,"#ModifySizeForm > div.middle > input.rightToLeft").click()

        #保存
        self.clickButton(u"保存")

        

    def test_8import_SizeGroup(self):
        u'''导入尺码组'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码组
        self.to_SizeGroup()

        #导入
        self.clickButton(u"导入")

    def test_9delete_SizeGroup(self):
        u'''删除尺码组'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入尺码组
        self.to_SizeGroup()

        #查找
        code=sgroup_code
        self.searchbycode(code)

        #选择一个记录
        findCss(driver,"#stmSizeGroupAction table.datagrid-btable td[field='ck']").click()


        #删除
        self.clickButton(u"删除")

    
    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_SizeGroup start--')
    suite=unittest.TestSuite()
    
    #suite.addTest(test_SizeGroup('test_0add_SizeGroup'))#添加尺码组
    suite.addTest(test_SizeGroup('test_1search_byCategory'))#按品类查找
    #suite.addTest(test_SizeGroup('test_2search_byBrand'))#按品牌查找
    #suite.addTest(test_SizeGroup('test_3search_byVersion'))#按版型查找
    #suite.addTest(test_SizeGroup('test_4search_bySGroupCode'))#按尺码组编码
    #suite.addTest(test_SizeGroup('test_5search_bySGroupName'))#按尺码组名称
    #suite.addTest(test_SizeGroup('test_6search_bySGroupInfo'))#按描述信息查找
    #suite.addTest(test_SizeGroup('test_7modify_SizeGroup'))#修改尺码组
    #suite.addTest(test_SizeGroup('test_8import_SizeGroup'))#导入尺码组
    #suite.addTest(test_SizeGroup('test_9delete_SizeGroup'))#删除尺码组

    
   

    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_SizeGroup end--')
        
