
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import xlrd
from selenium.webdriver.common.by import By


# 封装公用方法
class base():

    # 初始化方法
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
        self.transfer_code = '123'

    # 打开浏览器并最大化
    def open(self):
        """
打开浏览器
        :param url: 要打开的地址
        """
        self.driver.get(self.url)
        sleep(1)
        self.driver.maximize_window()

    # 日志输入文件并显示在控制台
    # def log(self,v):
    #     return log.info(v)

    # 给操作元素添加样式（红框）
    def add_style(self,*loc):
        """
为元素添加红色的外框
        :param loc: 元素信息（元祖）
        """
        ele = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                                   ele, "border: 2px solid red;")

    # 操作元素后吧红框改成蓝框
    def set_style(self,*loc):
        """
为元素添加蓝色的框
        :param loc: 元素信息（元祖）
        """
        ele = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                                   ele, "border: 2px solid blue;")


    # 等待页面全部加载，加载完则通过，否则刷新当前页面
    def wait(self):
        """
等待页面元素加载完成，默认15秒，如果超时则刷新页面
        """
        try:
            # base.log(self,'等待页面加载......')
            self.driver.implicitly_wait(15)
        except:
            self.driver.refresh()
            # base.log(self,'等待时间超时，正在刷新页面......')

        else:
            # base.log(self,'页面加载完毕......')
            pass

    # 定位单个元素并点击
    def find_element_click(self,*loc):
        """
定位元素并单击元素
        :param loc: 元素信息（元祖）
        """
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
            # sleep(1)
            self.add_style(*loc)
        except NoSuchElementException:
            # base.log(self, '页面元素未找到: %s" %(loc,)')
            pass
        else:
            self.driver.find_element(*loc).click()
            self.set_style(*loc)

    # 定位单个元素返回对象
    def find_element(self,*loc):
        """
定位元素并返回元素对象
        :param loc:
        :return:
        """
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
            self.add_style(*loc)
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            # base.log(self,"页面元素未找到: %s" %(loc,))
            pass

    # 定位列表并以下标选择元素
    def find_elements(self,index,*loc):
        """
在元素列表中用下标选择元素
        :param index: 元素下标
        :param loc: 元素信息（元祖）
        """
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
            self.add_style(*loc)
            self.driver.find_elements(*loc)[index].click()
            self.set_style(*loc)
        except NoSuchElementException:
            # base.log(self,"页面元素未找到: %s" %(loc,))
            pass

    # 下拉类表选择
    def select(self,index,*loc):
        """
用下标选择select元素
        :param index:元素下标
        :param loc: 元素信息（元祖）
        """
        self.add_style(*loc)
        ele = self.driver.find_element(*loc)
        Select(ele).select_by_index(index)

    # 调用js
    def js(self,ele):
        self.driver.execute_script(ele)

    # 清空并输入数据
    def send_keys(self,value,*loc):
        """
定位元素后清空并输入数据
        :param value: 输入的数据
        :param loc: 元素信息
        """
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
            self.add_style(*loc)
            self.driver.find_element(*loc).clear()
            self.driver.find_element(*loc).send_keys(value)
            self.set_style(*loc)
        except NoSuchElementException:
            # base.log(self,"页面元素未找到: %s 数据输入失败..." %(loc,))
            pass
        else:
            # base.log(self, "数据输入成功，输入的数据为 %s" % value)
            pass

    # 切换frame
    def s_frame(self,*frame_id):
        """
切换frame框架
        :param frame_id: frame框架元素信息（元祖）
        """
        ele = self.driver.find_element(*frame_id)
        self.driver.switch_to.frame(ele)
        # base.log(self, "frame切换成功" )

    # 鼠标悬停
    def action_chains_1(self,*loc):
        """
鼠标悬停一次
        :param loc: 元素信息（元祖）
        """
        ele = self.driver.find_element(*loc)
        self.add_style(*loc)
        # base.log(self, "正在进行鼠标悬停..")
        ActionChains(self.driver).move_to_element(ele).perform()
        self.set_style(*loc)
        sleep(2)


    # 连续鼠标悬停
    def action_chains_2(self,*loc):
        """

        :param loc:
        """
        a = ActionChains(self.driver)
        a.move_to_element(*loc)
        a.pause(1)
        a.move_to_element(*loc)
        a.pause(1)
        a.perform()

    # 读取xlsx,ty=1是返回元祖，ty=2时先转换成整形在转换成字符串，ty=3时转换成字符串
    def xl_tuple(self,sheet_index,rows,clos,ty=1):
        """
读取xlsx,ty=1是返回元祖，ty=2时先转换成整形在转换成字符串，ty=3时转换成字符串
        :param sheet_index: sheet页
        :param rows: 行号（下标）
        :param clos: 列号（下标）
        :param ty: 返回的数据类型
        :return:
        """
        elepath = "../elements/elements.xlsx"
        page = xlrd.open_workbook(elepath)  # 打开文件
        table = page.sheet_by_index(sheet_index)  # 获取sheet页
        e = table.cell_value(rows,clos)

        if ty == 1:
            ele = eval(e)
            return ele
        elif ty == 2:
            x = int(e)
            y = str(x)
            return y
        elif ty == 3:
            z = str(e)
            return z





















