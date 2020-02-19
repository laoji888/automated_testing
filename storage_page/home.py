from selenium import webdriver
from common.ui_base import base
from time import sleep


class home(base):

    # 打开浏览器
    def open_b(self):
        #self.log('正在打开浏览器...地址为 %s' % self.url)
        self.open()

    # 登录
    def login(self,user,pw):
        username = self.xl_tuple(0, 0, 1)  # 元素（用户名）
        self.send_keys(user,*username)
        pwd = self.xl_tuple(0, 1, 1)  #  元素（密码）
        self.send_keys(pw,*pwd)
        vv = self.xl_tuple(0, 2, 1)  #  元素（登录按钮）
        self.find_element_click(*vv)
        sleep(10)

        tz = self.xl_tuple(0, 6, 1)
        ll = self.xl_tuple(0, 7, 1)


        if self.find_element(*tz).is_displayed():
            self.s_frame(*tz)
            A = self.driver.find_element_by_xpath('//*[text()="确认已读"]')
            self.driver.execute_script("arguments[0].scrollIntoView();", A)
            sleep(2)
            self.driver.find_element_by_xpath('//*[text()="确认已读"]').click()
            #self.find_element_click(*ll)
            self.driver.switch_to.default_content()
        else:
            pass

    # 进入调拨管理下的创建调拨单
    def enter_foundTransfer(self):
        """
进入创建调拨单
        """
        e = self.xl_tuple(0, 5, 1)  # 库存管理
        e1= self.xl_tuple(1, 0, 1)  # 左侧菜单栏框架
        e2= self.xl_tuple(1, 1, 1)  # 调拨管理按钮
        e3= self.xl_tuple(1, 2, 1)  # 创建调拨单按钮
        e4 = self.xl_tuple(1, 20, 1)  # 右侧框架
        self.find_element_click(*e)
        sleep(3)
        self.s_frame(*e1)
        #  判断新建调拨单是否显示，如果显示就点击，不显示就点击调拨管理在点击创建调拨单
        if self.driver.find_element(*e3).is_displayed():
            self.find_element_click(*e3)
        else:
            self.find_element_click(*e2)
            sleep(1)
            self.find_element_click(*e3)

        self.s_frame(*e4)

    #  进入调拨单管理
    def enter_transferManage(self):
        """
进入调拨单管理
        """
        e = self.xl_tuple(0, 5, 1)  # 库存管理
        e1= self.xl_tuple(1, 0, 1)  # 左侧菜单栏框架
        e2= self.xl_tuple(1, 1, 1)  # 调拨管理按钮
        e3= self.xl_tuple(1, 3, 1)  # 调拨单管理按钮
        e4= self.xl_tuple(1, 20, 1)  # 右侧框架
        self.find_element_click(*e)
        sleep(3)
        self.s_frame(*e1)
        #  判断新建调拨单是否显示，如果显示就点击，不显示就点击调拨管理在点击创建调拨单
        if self.driver.find_element(*e3).is_displayed():
            self.find_element_click(*e3)
        else:
            self.find_element_click(*e2)
            sleep(1)
            self.find_element_click(*e3)

        self.s_frame(*e4)

    #  进入调拨单审批管理
    def enter_transferExamine(self):
        """
进入调拨单审批管理
        """
        e = self.xl_tuple(0, 5, 1)  # 库存管理
        e1= self.xl_tuple(1, 0, 1)  # 左侧菜单栏框架
        e2= self.xl_tuple(1, 1, 1)  # 调拨管理按钮
        e3= self.xl_tuple(1, 4, 1)  # 调拨单审批管理按钮
        e4 = self.xl_tuple(1, 20, 1)  # 右侧框架
        self.find_element_click(*e)
        sleep(3)
        self.s_frame(*e1)
        #  判断新建调拨单是否显示，如果显示就点击，不显示就点击调拨管理在点击创建调拨单
        if self.driver.find_element(*e3).is_displayed():
            self.find_element_click(*e3)
        else:
            self.find_element_click(*e2)
            sleep(1)
            self.find_element_click(*e3)

        self.s_frame(*e4)




if __name__ == '__main__':
    dr =  webdriver.Firefox()
    url = "http://120.52.96.35:8001/mgWeb/"
    d = home(dr,url)
    d.open_b()

    d.login("liqq","123456")
    d.enter_transferManage()
    d.enter_transferExamine()
    sleep(2)
    dr.quit()




