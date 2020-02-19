from selenium import webdriver
from time import sleep
from common.ui_base import base
from selenium.webdriver.common.by import By
from page.home_page import ShouYe



# 注册省份按钮
province = (By.XPATH, '//*[@id="e-content"]/div[2]/div/div/div[2]/form/div[1]/div/div/div[1]')
# 北京
beijing = (By.XPATH, '/html/body/div[2]/div/div[1]/ul/li[1]/span')
# 天津
tianjin = (By.XPATH, '/html/body/div[2]/div/div[1]/ul/li[2]')
# 河北省
hebei = (By.XPATH, '/html/body/div[2]/div/div[1]/ul/li[3]')

# 注册地市
place = (By.XPATH, '/html/body/div/div[4]/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/input')
# 东城
dongcheng = (By.XPATH, '/html/body/div[3]/div/div[1]/ul/li[1]/span')
# 新增客户按钮
add = (By.XPATH, '//*[@id="e-content"]/div[2]/div/div/div[2]/form/div[8]/div/div/button[2]')


# 首页-->客户管理-->客户管理页面
class client(base):

    # 省份选择北京
    def s_beijing(self):
        self.log('省分选择北京...')
        self.find_element_click(*province)
        self.find_element_click(*beijing)

    # 注册地选择东城
    def s_dongcheng(self):
        self.log('注册地选择东城区...')
        self.find_element_click(*place)
        self.find_element_click(*dongcheng)


if __name__ == '__main__':
    dr = webdriver.Chrome()
    url = "http://120.52.96.35:30088/page/login.html"

    x = ShouYe(dr, url)
    x.open_b()
    x.login()
    sleep(3)
    x.to_setclient()
    y = client(dr, url)
    sleep(3)
    y.s_beijing()
    sleep(1)
    y.s_dongcheng()

    sleep(5)
    dr.quit()
