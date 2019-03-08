# encoding=utf8

import os, re, logging, subprocess, threading, socket, time, sys, thread
import AppiumInstance
import platform


class ParalleAppiumLib():

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    serverCount = int(2)
    serverList = []
    threadList = []

    reload(sys)  
    sys.setdefaultencoding('utf8') 

    # 1 setServerCount(count)
    # 2 addServer (serverNum, deviceName, packageName, activityName) **each server a tine
    # 3 startServers

    def addInstance(self, deviceName, app, appiumPort, bootstrapPort, platformName, platformVersion, packageName,
                    activityName, browserName=None, xcodeOrgId=None, bundleID=None):
        x = AppiumInstance.appiumInstance()
        x.setDeviceName(deviceName)
        x.setAppPath(app)
        x.setPort(appiumPort)
        x.setBoostrapPort(bootstrapPort)
        x.setAppPackage(packageName)
        x.setAppActivity(activityName)
        x.setBrowserName(browserName)
        x.setPlatform(platformName)
        x.setVersion(platformVersion)
        x.setBundleId(bundleID)
        x.setXcodeOrgId(xcodeOrgId)
        x.setXcodeSigningId("iPhone developer")
        # print self.serverList.append(x)
        self.serverList.append(x)
        self.threadList.append(None)
        return

    def startServers(self, withClient=False):
        self.serverList, self.serverCount
        for i in range(int(self.serverCount)):
            self.threadList[i] = threading.Thread(target=self.serverList[i].appiumInstance(withClient))
            # print withClient
            self.threadList[i].start()
        j = int(0)
        while self.serverList[j] == None and j < self.serverCount:
            time.sleep(2)
            if self.serverList[j] != None:
                j += 1

        time.sleep(5)
        return

    def startClients(self):
        return

    def stopAppiumServers(self):
        for k in range(int(self.serverCount)):
            self.serverList[k].stopInstance()
            #self.threadList[k].join()
        os.system("killall node")

    def killNameServer(self):
        os.system("killall node")

    def killPidServer(self,port):
        if(platform.system()=='windows'):
            #查找对应端口的pid
            cmd_find='netstat -aon | findstr %s' %port
            print(cmd_find)

            result = os.popen(cmd_find)
            text = result.read()
            pid=text[-5:-1]

            #执行被占用端口的pid
            cmd_kill='taskkill -f -pid %s' %pid
            print(cmd_kill)
            os.popen(cmd_kill)
        else:
            #查找对应端口的pid
            # https://tonydeng.github.io/2016/07/07/use-lsof-to-replace-netstat/
            pid=os.popen("lsof -nP -iTCP:%s |grep LISTEN|awk '{print $2;}'" %port).read()
            # pid=os.popen("lsof -nP -iTCP:%s |grep LISTEN|awk '{print $2;}'" %port).read().split('/')[0] 
            print pid

            #执行被占用端口的pid
            cmd_kill='kill %s' %pid
            print(cmd_kill)
            os.popen(cmd_kill)

    def setServerCount(self, count):
        self.serverCount = int(count)

###########FIND
    def find_element_by_accessibility_id(self, num, id):
        return  self.serverList[int(num)]._find_element_by_accessibility_id(id)

    def find_element_by_id(self, num, id):
        return  self.serverList[int(num)]._find_element_by_id(id)

    def find_element_by_xpath(self, num, xpath):
        return  self.serverList[int(num)]._find_element_by_xpath(xpath)

    def find_element_by_class_name(self, num, className):
        return  self.serverList[int(num)]._find_element_by_class_name(className)

    def find_element_by_name(self, num, name):
        return self.serverList[int(num)]._find_element_by_name(name)

##########CLICK

    def click_element_by_accessibility_id(self, num, id):
        self.serverList[int(num)]._click_element_by_accessibility_id(id)

    def click_element_by_id(self, num, id):
        self.serverList[int(num)]._click_element_by_id(id)

    def click_element_by_xpath(self, num, xpath):
        self.serverList[int(num)]._click_element_by_xpath(xpath)

    def click_element_by_class_name(self, num, className):
        self.serverList[int(num)]._click_element_by_class_name(className)

    def click_element_by_name(self, num, name):
        self.serverList[int(num)]._click_element_by_name(name)

    def tap_coordinate(self, num, x, y, duration):
        self.serverList[int(num)]._tap_coordinate(x, y, duration)

    def swipe_custom(self, num, x1, y1, x2, y2, duration):
        self.serverList[int(num)]._swipe_custom(x1, y1, x2, y2, duration)

##########TEXT
    def input_text_by_id(self, num, id, text):
        self.serverList[int(num)]._input_text_by_id(id, text)

    def input_text_by_xpath(self, num, xpath, text):
        self.serverList[int(num)]._input_text_by_xpath(xpath, text)

    def input_text_by_class_name(self, num, className, text):
        self.serverList[int(num)]._input_text_by_class_name(className, text)

    def input_text_by_name(self, num, name, text):
        self.serverList[int(num)]._input_text_by_name(name, text)

##########WAIT

    def wait_until_page_contains_accessibility_id(self, num, id, timeout=30):
        self.serverList[int(num)]._wait_until_page_contains_accessibility_id(id, timeout)

    def wait_until_page_contains_id(self, num, id, timeout=30):
        self.serverList[int(num)]._wait_until_page_contains_id(id, timeout)

    def wait_until_page_contains_xpath(self, num, xpath, timeout=30):
        self.serverList[int(num)]._wait_until_page_contains_xpath(xpath, timeout)

    def wait_until_page_contains_class_name(self, num, className, timeout=30):
        self.serverList[int(num)]._wait_until_page_contains_class_name(className, timeout)

    def wait_until_page_contains_name(self, num, name, timeout=30):
        self.serverList[int(num)]._wait_until_page_contains_name(name, timeout)

    def goToURL(self, num, URL):
        self.serverList[int(num)]._goToURL(URL)
# ios_webkit_debug_proxy -c 607dd2124bfe2b5f95929539bf41e68265009de7:27753 -d


if __name__ == '__main__':
    a =ParalleAppiumLib()
    # print os.path.abspath(os.path.dirname(os.getcwd()))
    a.killPidServer('4723')

    # a.addInstance('LE67A06310133286','4723','4024','Android','6.0','com.tianyancha.skyeye','.SplashPage','None','None','None')