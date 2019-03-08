# -*- coding:utf-8 -*-

__version__ = '0.1'

import os
# 使用正则表达式筛选设备 id
import re
import sys
import time

class AdbShell(object):

    def adb_install_package(self, deviceId, apk=None, package_name=None):
        u'''
        Install packages through ADB command.
        Examples:
        |     Adb Install Package    | ${apk_name} | ${package_name} |
        '''
        if apk == None:
            apk = os.getenv('G_APPIUM_APP_APK')
        else:
            apk = os.path.join(os.getenv('G_APPIUM_APP_DIR'), apk)
            print apk
        if package_name == None:
            package_name = os.getenv('G_APPIUM_APP_PACKAGE')
        if self.is_package_installed(deviceId, package_name):
            self.adb_uninstall_package(deviceId, package_name)
        try:
            # devices = self.get_android_deviceId()
            # cmd = 'adb -s {} install {}'.format(os.getenv('U_APPIUM_DEVICE_NAME'), apk)
            cmd = 'adb -s {} install -r -d {}'.format(deviceId, apk)
            print cmd
            text = os.popen(cmd)
            content = text.read()
            print content
            if 'Success' in content:
                print 'Pass: Install {} succeeded. \nVersion: {}'.format(package_name, apk)
            else:
                # self.__raiseError('Fail: Could NOT intall {}'.format(package_name))
                print 'Fail: Could NOT intall {}'.format(package_name)
        except Exception, e:
            print str(e)

    def get_android_logcat(self, deviceId):
    	u'''
        获取当前设备的logcat，通过adb logcat命令输出日志
        | Get Android LogCat | adb logcat |
        '''
        # 获取上级目录
        path = os.path.abspath(os.path.dirname(os.getcwd()))
  #       # MonkeyRunner下获取运行的文件所在的路径
		# rootpath = os.path.split(os.path.realpath(sys.argv[0]))[0]
        logcat_path = path + "/android_logcat/"
        if not os.path.isdir(logcat_path):
    		os.mkdir(logcat_path)

        old_stdout = sys.stdout
        currentTime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        logcat_format = '{}{}_{}_android_logcat.txt'.format(logcat_path,deviceId,currentTime)
        cmd = 'adb -s {} logcat -d -v threadtime > {}'.format(deviceId,logcat_format)
    	# adb -s LE67A06310133286 logcat -d -v threadtime
        print cmd
        os.popen(cmd)

    def get_android_deviceId(self):
        u'''
        读取设备id，通过ADB命令，正则表达式匹配出id信息
        | Get Android DeviceId | adb devices |
        '''
        readDeviceId = list(os.popen('adb devices').readlines())
        deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
        return deviceId

    def get_android_version(self):
        u'''
        读取设备系统版本号,通过ADB命令'adb shell getprop ro.build.version.release'
        |    Get Android Version    | ro.build.version.release |
        '''
        deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
        deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
        return deviceVersion

    def adb_uninstall_package(self, deviceId, package_name=None):
        u'''
        Uninstall packages through ADB command.
        Examples:
        |    Adb Uninstall Package    | ${package_name} |
        '''
        if package_name == None:
            package_name = os.getenv('G_APPIUM_APP_PACKAGE')
        if not self.is_package_installed(deviceId, package_name):
            # self.__raiseError('Fail: APP {} is not installed.'.format(package_name))
            print 'Fail: APP {} is not installed.'.format(package_name)
        try:
            # devices = self.get_android_deviceId()
            # cmd = 'adb -s {} uninstall {}'.format(os.getenv('U_APPIUM_DEVICE_NAME'), package_name)
            cmd = 'adb -s {} uninstall {}'.format(deviceId, package_name)
            print cmd
            text = os.popen(cmd)
            content = text.read()
            print content
            if 'Success' in content:
                print 'Pass: Uninstall {} succeeded.'.format(package_name)
            else:
                # self.__raiseError('Fail: Could NOT unintall {}'.format(package_name))
                print 'Fail: Could NOT unintall {}'.format(package_name)
        except Exception as e:
            print str(e)

    def is_package_installed(self, deviceId, package_name):
        u'''
        Check target package is installed through ADB command.
        Examples:
        | ${status} | Is Package Installed |
        '''
        packages = self.get_third_party_packages(deviceId)
        if package_name in packages:
            return True
        else:
            return False

    def get_third_party_packages(self, deviceId):
        u'''
        Get Third-party packages through ADB command.
        Examples:
        | ${apk_name} | Get Third Party Packages |
        '''
        apks = []
        try:
            f = os.popen('adb -s {} shell pm list package -3'.format(deviceId))
            for x in f.readlines():
                apks.append(x.strip().split(':')[1])
            return apks
        except Exception, e:
            print str(e)

if __name__ == '__main__':
    a = AdbShell()
    # a.get_android_logcat('LE67A06310133286')
    # print a.get_android_deviceI
    # print a.get_android_version()
    a.adb_install_package('LE67A06310133286','/Users/lishuang/Work/RobotframeworkProject/robotframework_tyc_8.5.1/demoapp/华为市场包_signed.apk','com.tianyancha.skyeye')
    # print a.is_package_installed('LE67A06310133286','com.tianyancha.skyeye')
    # a.adb_uninstall_package('LE67A06310133286','com.tianyancha.skyeye')
    # a.adb_uninstall_package()
