# -*- coding: utf-8 -*-
import unittest,time,os,sys
import threading
import HTMLTestRunner



#查找含有thread的文件，文件夹
def EEEcreatsuit():
    casedir=[]
    listaa=os.listdir('D:\\ISS\\Test_Cases')
    test_dir='D:\\ISS\\Test_Cases'
    for xx in listaa:
        if "thread" in xx:
            casedir.append(xx)
            
    suite=[]

    for n in casedir:
        testunit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(test_dir+'\\'+n,pattern='test*.py',top_level_dir=test_dir+'\\'+n)
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTest(test_case)
        suite.append(testunit)
    return suite,casedir

#多线程运行测试套件，将结果写入HTMLTestRunner报告
def EEEEEmultiRunCase(suite,casedir):
    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
    filename = 'D:\\ISS\\Report\\'+now+u' ISS项目报告.html'
    fp = file(filename, 'wb')
    proclist=[]
    s=0
    for i in suite:       
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=str(casedir[s])+u'测试报告',description=u'用例执行情况：')
        proc = threading.Thread(target=runner.run,args=(i,))
        proclist.append(proc)
        s=s+1
    for proc in proclist:proc.start()
    for proc in proclist:proc.join()
    fp.close()

if __name__ == '__main__':
            
        runtmp=EEEcreatsuit()
        EEEEEmultiRunCase(runtmp[0],runtmp[1])
      
            
        
            
