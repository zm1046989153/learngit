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

#分类编码
sort_code='zm'

#分类名称
sort_name=u'zm服装(自动化)'

#描述信息
sort_info=u'zm九牧王服装'

class test_CommoditySort(unittest.TestCase):
    #商品类别模块测试
    log.info(u"~~~商品类别模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_CommoditySort(self):
        #进入商品类别模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入商品类别
        testModule(driver,u'基础信息',u'商品类别')
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masPartClass table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        sleep(1)
    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#masPartClassToolbar a.easyui-linkbutton.addPartButton').click()
            sleep(1)
            
            
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#masPartClassToolbar a.easyui-linkbutton.findPartButton').click()
            sleep(1)

            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#masPartClassToolbar a.easyui-linkbutton.editButton').click()
            sleep(1)
            

        elif button==u'编辑' or button=='edit':
            #查看界面，点击“编辑”按钮
            driver.find_element_by_css_selector('#masPartClassToolbar a:nth-child(3)').click()
            sleep(0.5)
            

        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#masPartClassToolbar a.easyui-linkbutton.deleteZtreeButton').click()
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
            driver.find_element_by_css_selector('body div.panel-body.panel-body-noborder.window-body > div:nth-child(3) > a.cancelButton> span > span').click()
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

        
        
    def test_0add_Sort(self):
        u'''添加商品类别'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入商品类别
        self.to_CommoditySort()
        
        #点击添加按钮，进入添加界面
        self.clickButton(u'添加')
        
        
        #分类编码
        #获取当前时间作为分类编码
        strt=time.strftime('%H%M%S',time.localtime(time.time()))
        global sort_code
        sort_code='zm'+strt
        
        driver.find_element_by_css_selector("#ModifyPartClassForm tr:nth-child(3) > td.easyui-myText > input").send_keys(sort_code)
        sleep(0.5)
        
        #分类名称
        global sort_name
        sort_name=u'zm服装（自动化）'+strt
        driver.find_element_by_css_selector("#ModifyPartClassForm tr:nth-child(4) > td.easyui-myText > input").send_keys(sort_name)
        sleep(0.5)

        #描述信息
        driver.find_element_by_css_selector("#ModifyPartClassForm  tr:nth-child(5) > td.easyui-myText > input").send_keys(sort_info)

        #保存并断言
        self.clickButton(u'保存')

        
    def searchbycode(self,code):
        u'''此函数用于分类编码查找'''
        driver=self.driver
        driver.find_element_by_css_selector("#masPartClassToolbar > div:nth-child(1) > input:nth-child(3)").clear()
        sleep(0.5)
        driver.find_element_by_css_selector("#masPartClassToolbar > div:nth-child(1) > input:nth-child(3)").send_keys(code)
        sleep(0.5)
        self.clickButton(u'查找')
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masPartClass table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        sleep(0.5)
        
        #对查找结果断言
        cds=driver.find_elements_by_css_selector("#masPartClass table.datagrid-btable td[field='fdCode']")
        searchAssert(self,cds,code)
        
        
    def test_1search_BySortCode(self):
        u'''按分类编码查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入商品类别
        self.to_CommoditySort()
        
        #查找
        code=driver.find_element_by_css_selector("#masPartClass table.datagrid-btable td[field='fdCode']").text
        self.searchbycode(code)
        
        
        
        
    def test_2search_BySortName(self):
        u'''按分类名称查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入商品类别
        self.to_CommoditySort()
        sleep(1)

        #选择分类
        name=driver.find_element_by_css_selector("#masPartClass table.datagrid-btable td[field='fdName']").text
        st=driver.find_element_by_css_selector("#masPartClassToolbar > div:nth-child(1) > span > input.combo-text.validatebox-text")
        st.send_keys(name)
        sleep(0.5)
        st.send_keys(Keys.ENTER)
        sleep(0.5)
        
        #点击查找
        self.clickButton(u'查找')
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masPartClass table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        sleep(0.5)
        
        #对查找结果断言
        nes=driver.find_elements_by_css_selector("#masPartClass table.datagrid-btable td[field='fdName']")
        searchAssert(self,nes,name)
             
        
        
    def test_3search_BySortInfo(self):
        u'''按描述信息查找'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入商品类别
        self.to_CommoditySort()
        sleep(1)
        
        #输入查找的信息
        info=sort_info
        driver.find_element_by_css_selector("#masPartClassToolbar > div:nth-child(1) > input:nth-child(4)").send_keys(info)
        sleep(0.5)
        #点击查找
        self.clickButton(u'查找')

        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#masPartClass table.datagrid-btable td[field='ck']")
        log.info(u"刷新完成！！！")
        sleep(0.5)
        

        #对查找结果断言
        ifos=driver.find_elements_by_css_selector("#masPartClass table.datagrid-btable td[field='fdMemo']")
        searchAssert(self,ifos,info)
            
        

    def test_4modify_Sort(self):
        u'''修改商品分类'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入商品类别
        self.to_CommoditySort()
        sleep(1)
        
        #按编码查找分类
        code=sort_code
        self.searchbycode(code)
        #勾选记录
        driver.find_element_by_css_selector("#masPartClass table.datagrid-btable td[field='ck']").click()
        #修改
        self.clickButton(u'修改')
        sleep(1)
        
        #修改分类名称
        new_sortname='NEW_'+sort_name
        sn=driver.find_element_by_css_selector("#ModifyPartClassForm tr:nth-child(4) > td.easyui-myText > input")
        sn.clear()
        sleep(0.5)
        #编辑新名称
        sn.send_keys(new_sortname)
        sleep(0.5)
        #点击保存
        self.clickButton(u'保存')
        
       
        #按编码查找分类
        
        self.searchbycode(code)
        
        #断言分类名称是否和修改的一致
        self.assertEqual(new_sortname,driver.find_element_by_css_selector("#masPartClass table.datagrid-btable td[field='fdName']").text)
        


    def test_5delete_Sort(self):
        u'''删除商品分类'''
        log.info(u"开始执行用例...")
        
        driver=self.driver
        #进入商品类别
        self.to_CommoditySort()
        sleep(1)

        #按编码查找分类
        code=sort_code
        self.searchbycode(code)
        
        #断言并勾选记录
        if code not in driver.find_element_by_css_selector("#masPartClass table.datagrid-btable td[field='fdCode']").text:
            raise NameError('Search Failed,please try again')
        driver.find_element_by_css_selector("#masPartClass table.datagrid-btable td[field='ck']").click()
        sleep(0.5)
        
        #删除并断言
        self.clickButton(u'删除')   

    def tearDown(self):
        log.info(u"该条用例执行完毕")
        self.driver.close()
        self.driver.quit()




if __name__=='__main__':
    
    #建立测试集
    suite=unittest.TestSuite()
    
    #suite.addTest(test_CommoditySort('test_0add_Sort'))#添加商品类别
    #suite.addTest(test_CommoditySort('test_1search_BySortCode'))#按分类编码查找
    #suite.addTest(test_CommoditySort('test_2search_BySortName'))#按分类名称查找
    #suite.addTest(test_CommoditySort('test_3search_BySortInfo'))#按描述信息查找
    suite.addTest(test_CommoditySort('test_4modify_Sort'))#修改商品分类
    #suite.addTest(test_CommoditySort('test_5delete_Sort'))#删除商品分类
    
    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)

    #unittest.main()
        
        
