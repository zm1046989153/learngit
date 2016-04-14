# _*_ coding=utf-8 _*_

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
from time import sleep
import unittest,time
import logging

################################################################################
#本函数用于屏幕截图
def screenshot(driver,name=''):
    driver.get_screenshot_as_file("D:\\ISS\Report\\screenshot\\"+time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))+name+".png")
    

###############################################################################################################################################################
now=time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
log_file="D:\\ISS\\Report\\"+now+"_ISS_LOG.log"

log=logging.getLogger()

#配置日志的输出格式及方式
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(filename)s [Test Case:%(funcName)s] [line:%(lineno)d]%(levelname)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename = log_file,
                    filemode='w')


###############################################################################################################################################################

#当界面中的某个元素不存在时才继续执行程序
def WebWait(driver,css,waittime=15):
    '''页面等待'''

    try:
        #print time.time()
        driver.implicitly_wait(0)
        a=WebDriverWait(driver,waittime).until_not(lambda x:x.find_element_by_css_selector(css).is_displayed())
        sleep(1)
        #print a
        #div.datagrid-mask-msg
        
    except:
        log.info(u"页面无法刷新！！！")
        raise NameError("Wait Timeout!")

    finally:
        
        driver.implicitly_wait(30)
        #print time.time()
            


###############################################################################################################################################################
#等待界面刷新直到界面出现某个元素
def isRefreshed(driver,css,waittime=10):
    '''等待页面刷新'''
    
    try:
        driver.implicitly_wait(0)
        wait=WebDriverWait(driver,waittime)
        local=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css)))
        
    except:
        log.error(u"当前界面未刷新")
        local=None
        raise NameError (u"当前界面未刷新")
        
    finally:
        driver.implicitly_wait(30)
        return local
        
###############################################################################################################################################################

def toTime(formats,tran_time):
    '''本函数用于将时间字符串转换为时间戳'''
    tt=time.strptime(tran_time,formats)
    strt=time.mktime(tt)
    return strt




###############################################################################################################################################################

'''定位单个元素封装'''

def findId(driver,id):
    f=driver.find_element_by_id(id)
    return f

def findName(driver,name):
    f=driver.find_element_by_name(name)
    return f

def findClassName(driver,name):
    f=driver.find_element_by_class_name(name)
    return f

def findTagName(driver,name):
    f=driver.find_element_by_tag_name(name)
    return f

def findLinkText(driver,text):
    f=driver.find_element_by_link_text(text)
    return f

def findPLinkText(driver,text):
    f=driver.find_element_by_partial_link_text(text)
    return f

def findXpath(driver,xpath):
    f=driver.find_element_by_xpath(xpath)
    return f

def findCss(driver,css):
    f=driver.find_element_by_css_selector(css)
    return f
###############################################################################################################################################################
'''定位一组元素封装'''

def findsId(driver,id):
    f=driver.find_elements_by_id(id)
    return f

def findsName(driver,name):
    f=driver.find_elements_by_name(name)
    return f

def findsClassName(driver,name):
    f=driver.find_elements_by_class_name(name)
    return f

def findsTagName(driver,name):
    f=driver.find_elements_by_tag_name(name)
    return f

def findsLinkText(driver,text):
    f=driver.find_elements_by_link_text(text)
    return f

def findsPLinkText(driver,text):
    f=driver.find_elements_by_partial_link_text(text)
    return f

def findsXpath(driver,xpath):
    f=driver.find_elements_by_name(xpath)
    return f

def findsCss(driver,css):
    f=driver.find_elements_by_css_selector(css)
    return f


###############################################################################################################################################################


kys=''
def searchAssert(self,paths,assert_text=""):
        '''本函数用于对查找结果断言,提供断言路径和断言信息'''
        
        n=len(paths)
        
        #print n
        driver=self.driver
        
        if n==0:
            #未查找到数据，抛出异常
            raise NameError("Without Data be Searched")
        
        #判断查找到的数据是否正确 
        for path in paths:
            #print path.text
                self.assertIn(assert_text,path.text)

###############################################################################################################################################################            
def funcButton(driver,button):
    
    '''点击各个按钮,并进行断言，需提供按钮名称'''
    #driver=self.driver
    #print kys
        
    if button==u'添加' or button=='add':
        #点击添加按钮
        driver.find_element_by_css_selector('#'+str(kys)+'Toolbar > a.easyui-linkbutton.addButton').click()
        #masPartHdToolbar > a.easyui-linkbutton.addButton.\30 03014A03.l-btn.l-btn-plain > span > span
        #masPartClassToolbar > div:nth-child(2) > a.easyui-linkbutton.addPartButton.\30 03015A03.l-btn.l-btn-plain > span > span   
        sleep(1)
            
            
    elif button==u'查找' or button=='search':
        #点击“查找”按钮
        driver.find_element_by_css_selector('#'+str(kys)+'Toolbar> a.easyui-linkbutton.findButton').click()
        sleep(1)

            
    elif button==u'修改' or button=='modify':
        driver.find_element_by_css_selector('#'+str(kys)+'Toolbar > a.easyui-linkbutton.editButton').click()
        sleep(1)
            

    elif button==u'导入' or button=='import':
        #查看界面，点击“编辑”按钮
        driver.find_element_by_css_selector('#'+str(kys)+'Toolbar > a.easyui-linkbutton.importButton ').click()
        sleep(0.5)
            

    elif button==u'删除' or button=='delete':
        #点击“删除”按钮
        driver.find_element_by_css_selector('#'+str(kys)+'Toolbar > a.easyui-linkbutton.deleteButton').click()
        sleep(1)
            
        #点击确认，删除记录并断言
        driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a:nth-child(1) > span > span").click()
        sleep(1)
        dele_text=driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(1)").text
        #print dele_text
        self.assertEqual(u"删除成功",dele_text)
            
    
###############################################################################################################################################################

def testModule(driver,module0,module):
    '''
    本函数用于自动进入全渠道后台要测试的模块，需提供大模块module0、小模块名称module
    
    模块：
    
    订单管理》订制订单、量体工单
    
    会员管理》会员信息、量体数据、储值卡制成投放、储值卡类别、会员卡制成投放、会员成长值规则、会员档案
            会员属性、发卡规则、会员等级
    
    基础信息》成衣商品、辅料信息、商品档案、商品类别、SKU设置、量体项目、BOM管理、着装组合、颜色配置
            颜色组配置、尺码配置、尺码组配置、广告主题、商品库存、附加属性、商品季、销售季、商品主题
            品牌故事、风格配置、商品系列、版型配置、商品品牌、部件管理、面料信息、商品价格带、工艺档案
    
    系统管理》用户信息、销售组织管理、常数配置、字典配置、默认快递、自定义快递、用户配置、角色信息、报表配置
           系统配置、Json配置、地区编码、设备信息、支付账号信息、人员信息、图表样式、会员系统参数设置
           会员自定义属性设置、会员档案设置
    
    促销方案管理》触发式促销、线上促销、线上促销关系、线下促销、线下促销关系
    
    系统报表》会员消费情况查询、量体项目-着装人体型、量体项目-明细表、加入购物车汇总报表、加入购物车操作明细
          店铺销售分析-店铺业绩、预约量体、订单跟踪


    '''
    global kys
    d={u'颜色配置':'stmColor',u'商品类别':'masPartHd'}
    #kys=d[module]
    #print kys
        
    
    
    sleep(2)
    if module0==u'订单管理':
        k=1
    elif module0==u'会员管理':
        k=2
        driver.find_element_by_css_selector("#menuAccordion>div:nth-child(2)>div:nth-child(1)").click()
        
    elif module0==u'基础信息':
        k=3
        driver.find_element_by_css_selector("#menuAccordion>div:nth-child(3)>div:nth-child(1)").click()
        
    elif module0==u'系统管理':
        k=4
        driver.find_element_by_css_selector("#menuAccordion>div:nth-child(4)>div:nth-child(1)").click()
        
    elif module0==u'平台运营管理':
        k=5
        driver.find_element_by_css_selector("#menuAccordion>div:nth-child(5)>div:nth-child(1)").click()
        
    elif module0==u'促销方案管理':
        k=6
        driver.find_element_by_css_selector("#menuAccordion>div:nth-child(6)>div:nth-child(1)").click()
        
    elif module0==u'系统报表':
        k=7
        driver.find_element_by_css_selector("#menuAccordion>div:nth-child(7)>div:nth-child(1)").click()
        
    else:
        raise NameError("No Such Module"+module0)
    
    sleep(1)
    
    litags=driver.find_elements_by_css_selector('#menuAccordion>div:nth-child('+str(k)+') #menuTree > li span.tree-title')
    n=len(litags)
    i=0
    pa=''#用于存储模块位置元素路径
    
    for litag in litags:
        if i<n:
            i+=1
            #print litag.text
            if litag.text==module:
                pa='#menuAccordion>div:nth-child('+str(k)+') #menuTree > li:nth-child('+str(i)+') > div > span.tree-title'
                break
            continue
        break
    
    if pa=='':
        raise NameError('No Such Module!'+module1)
    #sleep(0.5)    
    #进入要测试的模块
    driver.find_element_by_css_selector(pa).click()


    


'''

#订制订单
#localtion.findCss(driver,'#menuTree > li:nth-child(1) > div').click()
#print driver.find_element_by_css_selector("#menuAccordion #menuTree > li:nth-child(1) > div)").text
#menuTree > li:nth-child(1) > div > span.tree-title

#量体工单
#print driver.find_element_by_css_selector("#menuTree > li:nth-child(2) > div ").text
#driver.find_element_by_css_selector("#menuTree > li:nth-child(1)")
#会员管理
sleep(0.5)
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(2)>div:nth-child(1)").click()
#print driver.find_element_by_selector("#menuAccordion > div:nth-child(2) > div:nth-child(1) div.panel-title").text
sleep(0.5)

#会员信息
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(2) #menuTree > li:nth-child(1) > div > span.tree-title").click()
sleep(1)
#量体数据
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(2) #menuTree > li:nth-child(2) > div > span.tree-title").click()
sleep(1)
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(2) #menuTree > li:nth-child(3) > div > span.tree-title").click()
sleep(1)
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(2) #menuTree > li:nth-child(4) > div > span.tree-title").click()
sleep(1)
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(2) #menuTree > li:nth-child(5) > div > span.tree-title").click()
sleep(1)
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(2) #menuTree > li:nth-child(6) > div > span.tree-title").click()
sleep(1)
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(2) #menuTree > li:nth-child(7) > div > span.tree-title").click()
sleep(1)
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(2) #menuTree > li:nth-child(8) > div > span.tree-title").click()
sleep(1)
'''
'''
#基础信息
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(3)>div").click()
sleep(1)

driver.find_element_by_css_selector("#menuAccordion>div:nth-child(4)>div").click()
sleep(1)
driver.find_element_by_css_selector("#menuAccordion>div:nth-child(5)>div").click()
sleep(1)
'''
if __name__=='__main__':
    
    sys.path.append('D:\\ISS\\Test_Cases\\public')
    import localtion
    kys=''
   
    driver=webdriver.Firefox()
    driver.get('http://192.168.1.172:8080/ISS10/index.jsp')
    driver.maximize_window()

    #填写帐号、密码
    localtion.findCss(driver,'#loginForm > div:nth-child(1) > input[type="text"]').send_keys('JOE_ADMIN')
    localtion.findCss(driver,'#loginForm > div:nth-child(2) > input[type="password"]').send_keys('qs8888')

    #点击登录按钮
    localtion.findCss(driver,'#buttonLogin > span > span').click()
  
    
    testModule(driver,u'基础信息',u'颜色配置')#调用进入模块函数

    funcButton(driver,u'添加')
    
