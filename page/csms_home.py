from selenium import webdriver
from common.ui_base import base
from time import sleep
import time


class Home(base):

    # 获取元素信息
    def element(self, rows):
        element =  self.element_info("elements/csms_elements.xlsx", 0, rows, clos=1, ty=1)
        return element

    # 登录
    def login(self, name, pwd):
        self.open()
        self.send_keys(name,*self.element(0))
        self.send_keys(pwd,*self.element(1))
        self.find_element_click(*self.element(2))
    #
    def log_in_again(self, name, pwd):
        self.action_chains_1(*self.element(6))
        self.action_chains_1(*self.element(4))
        self.find_element_click(*self.element(5))
        self.send_keys(name, *self.element(0))
        self.send_keys(pwd, *self.element(1))
        self.find_element_click(*self.element(2))












