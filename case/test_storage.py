from selenium import webdriver
from time import sleep
from page.home import home
import unittest, time
from selenium.webdriver.common.by import By
from page.inventory_management import InventoryManagement


class storage_case(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Remote(
        #  	       command_executor='http://106.13.132.197:8888/wd/hub',
        #  	       desired_capabilities={'browserName': 'firefox'}
        #  	       )
        # self.elepath = './elements/elements.xlsx'
        self.driver = webdriver.Firefox()
        self.url = 'http://120.52.96.35:8001/mgWeb/'
        self.t = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))  # 当前时间


    def test_001(self):

        try:
            #  登录
            dr = home(self.driver,self.url)
            dr.open_b()
            dr.login("zhaolei", "123456")  # 赵雷登录
            self.assertEquals(self.driver.title,"中国铁塔仓储管理系统")
            dr.enter_foundTransfer()  # 进入调拨管理下的创建调拨单
            dr1 = InventoryManagement(self.driver,self.url)
            dr1.new_transfer_seatch()  # 新建调拨单下搜索功能
            dr1.new_transfer()  # 新建调拨单，调拨至德州工程逻辑库
            self.driver.switch_to.default_content()  # 切换到默认框架
            dr.enter_transferManage()  # 进入调拨单管理
            dr1.submit_inspect()  # 在调拨单管理界面提交审批
            self.driver.close()
            dr2 = home(self.driver,self.url)
            dr2.login("zhaolei", "123456")

        except Exception as e:
            print(e)
            self.driver.save_screenshot("./error_imgs/" + self.t + '.png')
        else:
            self.driver.get_screenshot_as_file("./win_imgs/" + self.t + '.png')



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    storage_case().test_001()

