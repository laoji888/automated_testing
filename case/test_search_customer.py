from selenium import webdriver
from time import sleep
from page.home_page import ShouYe
import unittest
from page.client_management import client
from selenium.webdriver.common.by import By


# 测试客户管理搜索功能
class search_customer(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Remote(
        #  	       command_executor='http://106.13.132.197:8888/wd/hub',
        #  	       desired_capabilities={'browserName': 'firefox'}
        #  	       )

        self.driver = webdriver.Chrome()
        self.url = 'http://120.52.96.35:30088/page/login.html'


    def test_01(self):
        # 打开浏览器登录
        dr = ShouYe(self.driver,self.url)
        dr.open_b()
        dr.login("sugq")
        dr.wait()
        # 进入客户管理
        dr.to_setclient()
        dr.wait()
        # 验证页面跳转是否正确
        try:
            self.assertEqual(dr.aa().text,'客户管理')
            dr.log('判断页面是否跳转成功...')

        except:
            dr.log('断言失败，点前页面不是“客户管理”页面')

        else:
            dr.log('页面跳转成功')

            pass
        sleep(5)

        # 输入查询条件
        dr1 = client(self.driver,self.url)
        dr1.s_beijing()
        sleep(0.5)
        dr1.s_dongcheng()

        sleep(3)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

