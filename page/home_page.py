
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.ui_base import base
from time import sleep




# 用户名输入框
username = (By.XPATH,'//*[@id="esc-login-head"]/div/div[2]/ul/li[2]/input')
# 登录按钮
betn = (By.XPATH,'//*[@id="esc-login-head"]/div/div[2]/ul/li[3]/a/img')


# 我的工作台
myjob = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[2]/div')
# 我的待办
rough = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[2]/ul/li[1]')
# 我的已办
done = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[2]/ul/li[2]')
# 公告查询
notice = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[2]/ul/li[3]')
# 我的客户
client = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[2]/ul/li[4]')
# 用户名

# 客户管理
set_client = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[3]')
# 客户管理
set_client1 = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[3]/ul/li[1]')
#set_client1 = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[3]/ul/li[1]/span')


# 商机管理
ShangJiGuanLi = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[4]')

# 商机获取
chance = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[4]/ul/li[1]')
# 任务协同
RenWuXieTong = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[4]/ul/li[2]')
# 需求管理
XuQiuGuanLi = (By.XPATH,'//*[@id="vm"]/div[3]/div/div[2]/ul/li[4]/ul/li[4]')


# 页面跳转断言：是否跳转到需求管理页面
dy = (By.XPATH,'//*[@id="e-content"]/div[2]/div/div/div[1]/span/span[6]')
elepa = './elements/elements.xlsx'
# 首页
class ShouYe(base):

    # 打开浏览器
    def open_b(self):
        self.log('正在打开浏览器...地址为 %s' %self.url)
        self.open(self.url)

    # 输入用户名并点击
    def login(self,v):
        self.log('正在输入用户名并点击登录按钮...')
        x=self.xl_tuple(elepa,0,0,1)
        self.send_keys(v,*x)
        #self.send_keys(v,*username)
        self.find_element_click(*betn)

    # 进入我的代办事项
    def to_rough(self):
        self.log('进入我的代办事项...')
        self.action_chains_1(*myjob)
        self.find_element_click(*rough)

    # 进入我的已办事项
    def to_done(self):
        self.log('进入我的已办事项...')
        self.action_chains_1(*myjob)
        self.find_element_click(*done)

    # 进入客户管理
    def to_setclient(self):
        self.log('进入客户管理页面...')
        self.action_chains_1(*set_client)
        sleep(2)
        self.find_element_click(*set_client1)

    def aa(self):
        return self.find_element(*dy)

    # 进入商机管理
    def to_shangji(self):
        self.log('进入商机管理...')
        self.action_chains_1(*ShangJiGuanLi)
        self.find_element_click(*chance)

    # 进入任务协同
    def to_xietong(self):
        self.log('进入任务协同...')
        self.action_chains_1(*ShangJiGuanLi)
        self.find_element_click(*RenWuXieTong)

    # 进入需求管理
    def to_xuqiu(self):
        self.log('进入需求管理...')
        self.action_chains_1(*ShangJiGuanLi)
        self.find_element_click(*XuQiuGuanLi)







if __name__ == '__main__':
    dr = webdriver.Chrome()
    url = "http://120.52.96.35:30088/page/login.html"

    x = ShouYe(dr,url)
    x.open_b()
    x.login('sugq')
    x.wait()
    x.to_setclient()
    x.wait()
    A = dr.find_element_by_xpath('//*[@id="e-content"]/div[2]/div/div/div[4]/button[2]')
    dr.execute_script("arguments[0].scrollIntoView();", A)
    sleep(5)
    dr.quit()



