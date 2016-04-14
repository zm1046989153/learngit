# _*_ coding=utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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

#编码
strt=time.strftime("%H%M%S",time.localtime(time.time()))
code=u'EX_'+strt



class test_CustomExpress(unittest.TestCase):
    #自定义快递模块测试
    log.info(u"~~~自定义快递模块测试~~~")
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #获取测试地址
        url=root.getElementsByTagName("url")
        self.base_url=url[0].firstChild.data
        
    def to_CustomExpress(self):
        #自定义快递模块
        
        #获取登录帐号、密码
        logins=root.getElementsByTagName("login")
        username=logins[0].getAttribute("username")
        password=logins[0].getAttribute("password")
        
        driver=self.driver
        driver.get(self.base_url)
        #调用登录模块登录
        login.login(self,username,password)
        #进入自定义快递
        testModule(driver,u'系统管理',u'自定义快递')
        
        #判断页面是否刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmShippingTemplateAccordion > div:nth-child(1)  table.datagrid-btable  td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(1)

    
    def clickButton(self,button):
        '''点击各个按钮,并进行断言，需提供按钮名称'''
        driver=self.driver
        
        if button==u'添加' or button=='add':
            #点击添加按钮
            driver.find_element_by_css_selector('#stmShippingTemplateToolbar > a.easyui-linkbutton.addButton > span > span').click()
            sleep(1)
              
        elif button==u'查找' or button=='search':
            #点击“查找”按钮
            driver.find_element_by_css_selector('#stmShippingTemplateToolbar > a.easyui-linkbutton.findButton > span > span').click()
            #print findCss(driver,"#stmShippingTemplateAccordion > div:nth-child(1) > div.panel-body.accordion-body > div > div > div.datagrid-mask-msg").text
            WebWait(driver,"#stmShippingTemplateAccordion > div:nth-child(1) > div.panel-body.accordion-body > div > div > div.datagrid-mask-msg")
            sleep(1)

        elif button==u'查看' or button=='view':
            #点击“查看”按钮
            driver.find_element_by_css_selector('#stmShippingTemplateToolbar > a.easyui-linkbutton.viewButton > span > span').click()
            sleep(1)

            self.assertEqual(u"编辑",driver.find_element_by_css_selector("#stmShippingTemplateForm > div > a.easyui-linkbutton.saveButton > span > span > span").text)


        elif button==u'编辑' or button=='edit':
            #点击“编辑”按钮
            driver.find_element_by_css_selector('#stmShippingTemplateForm > div > a.easyui-linkbutton.saveButton > span > span > span').click()
            sleep(1)
            
        elif button==u'修改' or button=='modify':
            driver.find_element_by_css_selector('#stmShippingTemplateToolbar > a.easyui-linkbutton.editButton > span > span').click()
            sleep(1)
    

    
        elif button==u'删除' or button=='delete':
            #点击“删除”按钮
            driver.find_element_by_css_selector('#stmShippingTemplateToolbar > a.easyui-linkbutton.deleteButton > span > span').click()
            sleep(1)
            
            #点击确认，删除记录并断言
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
            sleep(1)
            dele_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text
            #print dele_text
            log.info(dele_text)
            self.assertEqual(u"删除成功",dele_text)
            sleep(1)
            
            #点击取消
            #driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2)").click()
                
        elif button==u'取消' or button=='cancel':
            #编辑界面，点击“取消”按钮
            driver.find_element_by_css_selector('#stmShippingTemplateForm > div > a.easyui-linkbutton.cancelButton > span > span').click()
            sleep(0.5)
            #取消
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(2) > span > span").click()
            
            sleep(1)
            

        elif button==u'保存' or button=='save':
            #编辑界面，点击保存按钮

            driver.find_element_by_css_selector("#stmShippingTemplateForm > div > a.easyui-linkbutton.saveButton > span > span > span").click()
            sleep(1)
            
            #获取断言信息
            
            success=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2)")
            tip_text=success.text
            sleep(0.5)
            
            #print tip_text
            log.info(tip_text)
            
            #确定,关闭提示框
            driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a > span > span").click()

            #断言是否保存成功
            self.assertEqual(u"保存成功！",tip_text)
            
        else:
            raise NameError('No Such Button,confirm again please')

    def selectstore(self):
        '''在部门界面选择部门'''
        driver=self.driver

        #等待部门选择界面刷新
        isRefreshed(driver,"div.zTreeDemoBackground.left")

        #菜单树选择部门
        findCss(driver,"ul.ztree.stmdeptTree > li:nth-child(1) > a > span").click()
        sleep(0.5)

        #选择门店
        findCss(driver,"body > div:nth-child(26) table.datagrid-btable td[field='fdName']").click()
        sleep(0.5)
        
        storename=findCss(driver,"body > div:nth-child(26) table.datagrid-btable td[field='fdName']").text

        #选择
        findCss(driver,"body > div:nth-child(26) > div.panel-body.panel-body-noborder.window-body.panel-noscroll > div > div.panel.layout-panel.layout-panel-center > div > div > div.panel.layout-panel.layout-panel-south > div > a.easyui-linkbutton.saveButtonDept > span > span > span").click()
        sleep(0.5)
        
        #返回选择的门店名称
        return storename
    
        
    """
    def test_0add_CustomExpress(self):
        u'''添加自定义快递'''
        
        driver=self.driver
        
        #进入自定义快递模块
        self.to_CustomExpress()

        #添加
        self.clickButton(u"添加")

        #编号
        global code
        strt=time.strftime("%H%M%S",time.localtime(time.time()))
        code=u'EX_'+strt
        findCss(driver,"#stmShippingTemplateForm  tr:nth-child(1) > td:nth-child(5) > input").send_keys(code)

        #门店名称
        findCss(driver,"#stmShippingTemplateForm tr:nth-child(1) > td:nth-child(7) > span > input.combo-text.validatebox-text").click()
        sleep(0.5)

        #选择门店
        storename=self.selectstore()


        #模版类型
        mtp=findCss(driver,"#stmShippingTemplateForm  tr:nth-child(2) > td:nth-child(2) > span > input.combo-text.validatebox-text.validatebox-invalid")
        mtp.click()
        sleep(0.5)
        mtp.send_keys(Keys.DOWN)
        sleep(0.5)
        mtp.send_keys(Keys.ENTER)
        sleep(0.5)


        #快递类型
        extp=findCss(driver,"#stmShippingTemplateForm  tr:nth-child(2) > td:nth-child(4) > span > input.combo-text.validatebox-text.validatebox-invalid")
        extp.click()
        sleep(0.5)
        extp.send_keys(Keys.DOWN)
        sleep(0.5)
        extp.send_keys(Keys.ENTER)
        sleep(0.5)


        #点击编辑模版按钮
        findCss(driver,"#stmShippingTemplateForm > div > a.easyui-linkbutton.editTemplateButton > span > span").click()
        sleep(1)

        #关闭窗口
        #findCss(driver,"html.panel-fit body.easyui-layout div.panel div.panel-header div.panel-tool a").click()
        #sleep(0.5)
        
        
        #点击编辑模版按钮
        findCss(driver,"#stmShippingTemplateForm > div > a.easyui-linkbutton.editTemplateButton > span > span").click()
        sleep(0.5)
        

        #选择参数
        Select(findCss(driver,"#stmShippingTemplateLodop div.titleSelect select.expressInputParameters")).select_by_value("[快递公司]")
        sleep(0.5)

        #点击添加参数
        findCss(driver,"#stmShippingTemplateLodop div.titleSelect input.expressInputButton").click()
        sleep(0.5)

        #点击保存
        findCss(driver,"#stmShippingTemplateLodop a.easyui-linkbutton span.l-btn-left span.l-btn-text").click()
        sleep(0.5)

        #获取页面警告信息
        alert=driver.switch_to_alert()
        #print falert.text
        sleep(0.5)
        alert.accept()
        sleep(1)


        #关闭窗口
        #findCss(driver,"html.panel-fit body.easyui-layout div.panel div.panel-header div.panel-tool a").click()
        sleep(1)

        #保存
        self.clickButton(u"保存")
        
      """

    def test_1search_byTemplateType(self):
        u'''按模版类型查找'''
        
        driver=self.driver
        
        #进入自定义快递模块
        self.to_CustomExpress()

        #选择模版类型
        findCss(driver,"#stmShippingTemplateToolbar > span:nth-child(2) > input.combo-text.validatebox-text").click()
        sleep(0.5)
        
        mtp_name=findCss(driver,"#stmShippingTemplateAccordion  table.datagrid-btable  td[field='typeKey']").text
        #print mtp_name
        sleep(0.5)
        mps=findsCss(driver,"body > div:nth-child(18) > div > div.combobox-item")
        n=0
       
        for mp in mps:
            n+=1
            if mp.text==mtp_name:
                findCss(driver,"body > div:nth-child(18) > div > div:nth-child("+str(n)+")").click()
                break
            continue
                    
        sleep(0.5)
        

        #查找
        self.clickButton(u"查找")
        sleep(2)

        #等待页面刷新
        log.info(u"等待页面刷新···")
        isRefreshed(driver,"#stmShippingTemplateAccordion > div:nth-child(1)  table.datagrid-btable  td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(0.5)

        #断言
        mtps=findsCss(driver,"#stmShippingTemplateAccordion > div:nth-child(1)  table.datagrid-btable  td[field='typeKey']")
        #for mtp in mtps:
            #print mtp.text
        searchAssert(self,mtps,mtp_name)
        

    def test_2search_byExpressType(self):
        u'''按快递类型查找'''
        
        driver=self.driver
        
        #进入自定义快递模块
        self.to_CustomExpress()

        #选择模版类型
        findCss(driver,"#stmShippingTemplateToolbar > span:nth-child(2) > input.combo-text.validatebox-text").click()
        

        
        sleep(0.5)
        #获取第一行数据的模版类型和快递类型
        mtp_name=findCss(driver,"#stmShippingTemplateAccordion  table.datagrid-btable  td[field='typeKey']").text
        #print mtp_name
        
        extp_name=findCss(driver,"#stmShippingTemplateAccordion  table.datagrid-btable  td[field='shippingKey']").text
        #print extp_name
        
        sleep(0.5)
        #选择模版类型
        
        mps=findsCss(driver,"body > div:nth-child(18) > div > div.combobox-item")     
        k=0
       
        for mp in mps:
            k+=1

            if mp.text==mtp_name:
                findCss(driver,"body > div:nth-child(18) > div > div:nth-child("+str(k)+")").click()
               
                break
            continue
                    
        sleep(0.5)
        
        #选择快递类型
        findCss(driver,"#stmShippingTemplateToolbar > span:nth-child(4) > input.combo-text.validatebox-text").click()
        sleep(0.5)

        #选择快递类型
        exs=findsCss(driver,"body > div:nth-child(19) > div > div.combobox-item")
        m=0
       
        for ex in exs:
            m+=1
            if ex.text==extp_name:
                findCss(driver,"body > div:nth-child(19) > div > div:nth-child("+str(m)+")").click()
                break
            continue
                    
        sleep(0.5)
        

        #查找
        self.clickButton(u"查找")
        sleep(2)

        #等待页面刷新
        log.info(u"等待页面刷新···")
        
        isRefreshed(driver,"#stmShippingTemplateAccordion > div:nth-child(1)  table.datagrid-btable  td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(0.5)

        #断言
        extps=findsCss(driver,"#stmShippingTemplateAccordion > div:nth-child(1)  table.datagrid-btable  td[field='shippingKey']")
        searchAssert(self,extps,extp_name)
        
        
        
    def test_3search_byStoreName(self):
        u'''按门店名称查找'''
        
        driver=self.driver
        
        #进入自定义快递模块
        self.to_CustomExpress()


        #选择门店
        findCss(driver,"#stmShippingTemplateToolbar > span:nth-child(6) > input.combo-text.validatebox-text").click()
        sleep(0.5)

        #选择门店
        storename=self.selectstore()

        #查找
        self.clickButton(u"查找")

         #等待页面刷新
        log.info(u"等待页面刷新···")
        
        isRefreshed(driver,"#stmShippingTemplateAccordion > div:nth-child(1)  table.datagrid-btable  td[field='ck']")
        
        log.info(u"刷新完成！！！")
        sleep(0.5)
        

        #断言
        sts=findsCss(driver,"#stmShippingTemplateAccordion > div:nth-child(1) table.datagrid-btable td[field='dptKeyName']")
        searchAssert(self,sts,storename)

    def test_4view_CustomExpress(self):
        u'''查看自定义快递'''
        
        driver=self.driver
        
        #进入自定义快递模块
        self.to_CustomExpress()

        #选择记录
        findCss(driver,"#stmShippingTemplateAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #查看
        self.clickButton(u"查看")

        #编辑
        self.clickButton(u"编辑")

        #保存
        self.clickButton(u"保存")

        
        

    def test_5modify_CustomExpress(self):
        u'''修改自定义快递'''

        driver=self.driver
        
        #进入自定义快递模块
        self.to_CustomExpress()

        #选择记录
        findCss(driver,"#stmShippingTemplateAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #修改
        self.clickButton(u"修改")

        #修改编号
        new_code=u"NEW_"+code
        cd=findCss(driver,"#stmShippingTemplateForm  tr:nth-child(1) > td:nth-child(5) > input")
        cd.clear()
        sleep(0.5)
        cd.send_keys(new_code)
        sleep(0.5)

        #保存
        self.clickButton(u"保存")

        #等待页面刷新完成
        WebWait(driver,"#stmShippingTemplateAccordion > div:nth-child(1) > div.panel-body.accordion-body > div > div > div.datagrid-mask-msg")

        #print findCss(driver,"#stmShippingTemplateAccordion > div:nth-child(1) table.datagrid-btable td[field='templateCode']").text

        self.assertEqual(new_code,findCss(driver,"#stmShippingTemplateAccordion > div:nth-child(1) table.datagrid-btable td[field='templateCode']").text)
        
        
    """
    def test_6delete_CustomExpress(self):
        u'''删除自定义快递'''

        driver=self.driver
        
        #进入自定义快递模块
        self.to_CustomExpress()

         #选择模版类型:到付模版
        findCss(driver,"#stmShippingTemplateToolbar > span:nth-child(2) > input.combo-text.validatebox-text").click()
        sleep(0.5)
        findCss(driver,"body > div:nth-child(18) > div > div:nth-child(2)").click()
        sleep(0.5)

        #查找
        self.clickButton(u"查找")
        sleep(3)

        #选择记录
        findCss(driver,"#stmShippingTemplateAccordion > div:nth-child(1) table.datagrid-btable td[field='ck']").click()
        sleep(0.5)

        #删除
        self.clickButton(u"删除")

       """
 
    def tearDown(self):
        log.info(u"该条用例执行完毕！！！")
        self.driver.close()
        self.driver.quit() 



if __name__=='__main__':
    
    
    #建立测试集
    log.info('test_CustomExpress start--')
    suite=unittest.TestSuite()
    
    #suite.addTest(test_CustomExpress('test_0add_CustomExpress'))#添加自定义快递
    #suite.addTest(test_CustomExpress('test_1search_byTemplateType'))#按模版类型查找
    #suite.addTest(test_CustomExpress('test_2search_byExpressType'))#按快递类型查找
    suite.addTest(test_CustomExpress('test_3search_byStoreName'))#按门店名称查找
    
    #suite.addTest(test_CustomExpress('test_4view_CustomExpress'))#查看自定义快递
    
    #suite.addTest(test_CustomExpress('test_5modify_CustomExpress'))#修改自定义快递
    
    #suite.addTest(test_CustomExpress('test_6delete_CustomExpress'))#删除自定义快递
    
    
    
   
   
    #执行测试
    
    runner=unittest.TextTestRunner()
    #runner.run(suite)

    unittest.main()
    log.info('test_CustomExpress end--')
        
