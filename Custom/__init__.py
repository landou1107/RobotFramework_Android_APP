# -*- coding:utf-8 -*-

from adbshell import AdbShell

__version__ = '0.1'

class Custom(AdbShell):
    u'''
    这是一个AdbShell库，输入包名信息，进行安装卸载相关操作。
	'''
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
