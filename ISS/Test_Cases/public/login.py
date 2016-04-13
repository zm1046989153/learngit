# -*- coding: utf-8 -*-

#登录
def login(self,username,password):
    driver=self.driver
    driver.find_element_by_name("stmUserPwd.fdName").send_keys(username)
    driver.find_element_by_name("stmUserPwd.fdPassword").send_keys(password)
    
    #driver.find_element_by_css_selector("#loginForm > div:nth-child(1) > input[name='stmUserPwd.fdName']").send_keys(username)
    #driver.find_element_by_css_selector("#loginForm > div:nth-child(2) > input[name='stmUserPwd.fdPassword']").send_keys(password)
    driver.find_element_by_xpath(".//*[@id='buttonLogin']").click()



#退出
def logout(self):
    driver=self.driver
    driver.find_element_by_xpath("html/body/div[1]/div/div/a[2]/span").click()
    driver.find_element_by_xpath("html/body/div[13]/div[2]/div[4]/a[1]").click()
    
    
      
