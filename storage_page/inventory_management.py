from selenium import webdriver
from common.ui_base import base
from time import sleep
from storage_page.home import home
from selenium.webdriver.common.action_chains import ActionChains as a

class InventoryManagement(base):


    #  新建调拨单下搜索功能
    def new_transfer_seatch(self):
        """
新建调拨单下的搜索功能，济南分公司，工程库，物料编码是01240102050601
        """
        e1 = self.xl_tuple(1,6,1)  # 选择地市下拉框
        e2 = self.xl_tuple(1,7,1)  # 地市下济南分公司
        e3 = self.xl_tuple(1,8,1)  # 下拉框逻辑库
        e4 = self.xl_tuple(1,9,1)  # 逻辑库下的工程物资库
        e5 = self.xl_tuple(1,10,1)  # 输入框物料编码
        e6 = self.xl_tuple(1,11,1)  # 查新按钮

        self.find_element_click(*e1)
        self.find_element_click(*e2)
        self.find_element_click(*e3)
        self.find_element_click(*e4)
        self.send_keys('01240102050601', *e5)
        self.find_element_click(*e6)

    # 新建调拨单，调拨至德州工程逻辑库
    def new_transfer(self):
        """
新建调拨单，调拨至德州工程逻辑库
        """
        e = self.xl_tuple(1, 12, 1)  # 调拨数量
        e1 = self.xl_tuple(1, 13, 1)  # 下拉框目标地市
        e2 = self.xl_tuple(1, 14, 1)  # 目标地市下的德州分公司
        e3 = self.xl_tuple(1, 15, 1)  # 目标逻辑库下拉框
        e4 = self.xl_tuple(1, 16, 1)  # 目标逻辑库工程库
        e5 = self.xl_tuple(1, 17, 1)  # 新建页面第一条数据
        e6 = self.xl_tuple(1, 18, 1)  # 创建调拨申请


        self.send_keys('1', *e)
        self.find_element_click(*e1)
        self.find_element_click(*e2)
        self.find_element_click(*e3)
        self.find_element_click(*e4)
        self.find_element_click(*e5)

        # 滚动条滚动到指定位置
        A = self.driver.find_element_by_xpath('//button[@class="inp-print-btn btn-size-s'
                                              ' layui-btn" and @name="addAllotPlan"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", A)

        sleep(0.5)
        self.js("$('[name=\"addAllotPlan\"]').click()")  # 点击创建调拨申请
        sleep(3)
        self.driver.switch_to.alert.accept()
        sleep(10)
        self.driver.switch_to.alert.accept()


    # 在调拨单管理界面提交审批
    def submit_inspect(self):
        """
审批人选择姜嘉功，并提交审批
        """
        e1 = self.xl_tuple(1,21,1)  # 下拉框-下一审批人
        e2 = self.xl_tuple(1,22,1)  # 审批人姜嘉功
        e3 = self.xl_tuple(1,23,1)  # 保存调拨单号
        e4 = self.xl_tuple(1,24,1)  # 提交审批按钮
        e5 = self.xl_tuple(1,25,1)  # 第一条数据

        self.find_element_click(*e1)
        self.find_element_click(*e2)
        code = self.find_element(*e3).text
        self.transfer_code = code
        self.find_element_click(*e5)
        ele = self.find_element(*e4)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        self.js("$('#submittedforapproval').click()")
        sleep(3)
        self.driver.switch_to.alert.accept()
        sleep(4)
        self.driver.switch_to.alert.accept()

    #  审批调拨单
    def transfer_inspect(self):
        e = self.xl_tuple(1, 27, 1)  # 项目编号输入框
        e1 = self.xl_tuple(1, 30, 1)  # 查询按钮
        e2 = self.xl_tuple(1, 28, 1)  # 第一条数据
        e3 = self.xl_tuple(1, 29, 1)  # 审批通过按钮

        self.send_keys(self.transfer_code,*e)
        self.find_element_click(*e1)
        self.find_element_click(*e2)
        self.find_element_click(*e3)
        sleep(1)
        self.driver.switch_to.alert.accept()
        sleep(4)
        self.driver.switch_to.alert.accept()






if __name__ == '__main__':
    driver = webdriver.Firefox()
    url = "http://120.52.96.35:8001/mgWeb/"


    dr = home(driver,url)
    dr.open_b()
    dr.login('zhaolei', '123456')
    dr.enter_foundTransfer()
    sleep(3)

    dr1 = InventoryManagement(driver,url)
    dr1.new_transfer_seatch()
    dr1.new_transfer()
    sleep(1)
    driver.switch_to.default_content()

    dr.enter_transferManage()
    dr1.submit_inspect()
    sleep(3)
    driver.quit()


