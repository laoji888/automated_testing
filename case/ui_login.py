from page.csms_home import Home
import time, unittest
from selenium import webdriver


class CsmsTest(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Remote(
         	       command_executor='http://106.13.132.197:8888/wd/hub',
         	       desired_capabilities={'browserName': 'firefox'}
         	       )
        self.url = "http://120.52.157.131:58080/#/home/cooperation"
        self.dr = Home(self.driver,self.url)

    def test_login(self):
        self.dr.login("qiaolin", "ChinaTower1234")
        time.sleep(1)
        xx = self.dr.find_element(*self.dr.element(3))
        self.assertIn("乔琳", xx.text,  msg='错误')

        self.dr.log_in_again("kh-laoji008", "ChinaTower1234*")
        time.sleep(5)
        self.assertIn("习近平", xx.text, msg='错误')
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()



