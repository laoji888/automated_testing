
import datetime
from common.log import log
import xlrd, requests, unittest, time, json, pymysql

log = log().ll("./logs/api_log.log")


# now_time = datetime.datetime.now() 获取时间
# t1 = (now_time + datetime.timedelta(seconds=+3)).strftime("%Y-%m-%d %H:%M:%S") # 当前时间+3
# t2 = (now_time + datetime.timedelta(seconds=+15)).strftime("%Y-%m-%d %H:%M:%S") # 当前时间+15


# 接口测试类
class base():

    #  初始化方法
    def __init__(self, s_url, s_data, filepath, param_sheet, assert_sheet):
        """
        初始化方法
        :param self.dir_case: 参数文件存放路径
        :param s_url: 登录接口url
        :param s_data: 登录接口的参数
        :param url: 请求地址
        :param filepath:  存放参数的Excel文件名及后缀
        :param param_sheet: 要遍历的参数sheet页下标
        :param asset: 要遍历的断言sheet页下标
        """
        self.dir_case = './parameter/' + filepath
        self.s_url = s_url
        self.s_data = s_data
        self.filepath = filepath
        self.param = param_sheet
        self.assert_sheet = assert_sheet
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*'}

        self.nrow = 1
        self.ast = unittest.TestCase()  # 使用unittest框架下的断言

    # 连接数据库
    def msql(self,sql):
        conn = pymysql.connect(
            host='127.0.0.1',
            user = 'root',
            password='000000',
            port= 3306,
            db='test',
            charset='utf8')

        curso = conn.cursor()
        curso.execute(sql)
        xx = curso.fetchone()
        conn.commit()
        curso.close()
        conn.close()
        return xx[0]

    # 获取url
    def get_url(self, nrows=0, ncols=0):
        """
        获取url地址
        :param nrows: 行
        :param ncols: 列
        :return:
        """
        data = xlrd.open_workbook(self.dir_case)
        table = data.sheets()[self.assert_sheet]
        url = table.cell_value(nrows, ncols)
        log.debug("打开路径为： %s 的文件第：%s页，获取到的数据是：%s" % (self.dir_case, self.assert_sheet, url))
        log.info("获取url路径成功，地址第：%s" % url)
        return url

    # 遍历xlsx文件的参数，并以字典类型输出
    def get_data(self):
        """
        读取Excel里配置好的接口参数，以字典的方式存放
        """
        data = xlrd.open_workbook(self.dir_case)
        table = data.sheets()[self.param]
        log.debug("参数文件路径是:%s,打开文件第:%s页" % (self.dir_case, self.param))
        nor = table.nrows  # 行
        nol = table.ncols  # 列
        dict = {}

        for i in range(1, nor):
            for j in range(nol):
                title = table.cell_value(0, j)
                value = table.cell_value(i, j)

                value_type = table.cell(i, j).ctype
                if value_type == 2 and value % 1 == 0.0:  # 如果ctype为2且取余于1等于0.0，转换成整型
                    value = int(value)
                    log.debug("获取到的参数是小数：%s,已转换成整型" % value)
                    if value == 0.0:
                        value = int(value)
                    log.debug("获取到的参数是：%s，已转换成整型" % value)
                else:
                    pass
                dict[title] = value
                log.debug("获取到的参数名是:%s,参数值是:%s" % (title, value))
            yield dict
        log.info("参数读取成功")

    # 读取excl，获得实际结果命令和预期结果
    def get_assert(self, nrow, ncol=0):
        """
        读取接口的预期结果和获取实际结果的命令
        :param nrow: 要读取的行数
        :param ncol: 要读取的列数，默认是0
        :return: 返回读取的数据
        """
        data = xlrd.open_workbook(self.dir_case)
        table = data.sheet_by_index(self.assert_sheet)
        log.debug("打开文件:%s的第%s页获取断言信息" % (self.dir_case, self.assert_sheet))
        value = table.cell_value(nrow, ncol)

        value_type = table.cell(nrow, ncol).ctype
        if value_type == 2 and value % 1 == 0.0:  # 如果ctype为2且取余于1等于0.0，转换成整型
            log.debug("获取到的断言类型是小数：%s,已装换成整型" % value)
            value = int(value)
            if value == 0.0:
                value = int(value)
            log.debug("获取到的断言是0.0，已转换成整型")
        log.info("断言信息获取成功：%s" % value)
        return value

    # 遍历字典的值是否为空或null，如果为空就删除该键值对，如果为null就把该键改成 “”。如果不传参数Excel为空即可，如果想参数值为空就写null。
    def set_dict(self, data):
        """
        遍历字典的值是否为空或null，如果为空就删除该键值对，如果为null就把该键改成 “”，空值不等于null,如果读取的值是time就转换成当前时间
        :param data: 要遍历的字典
        :return: 返回删除空值的键值对后的字典
        """


        t = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        xx = data
        for k in list(data.keys()):
            if not data[k]:
                log.debug("获取到的键：%s 的值为空，删除该键值对" % data[k])
                del data[k]

            elif data[k] == 'null':
                data[k] = ''
                log.debug("获取到的键：%s 的值为 null，把该键的值设置为空" % data[k])

            elif data[k] == 'time':
                data[k] = t
                log.debug("获取到的键：%s 的值为 time，把该键的值设置为当前时间" % data[k])
        log.info("参数格式化成功")

        return xx

    # 创建会话对象
    def add_session(self):

        log.debug("获取到登录url为：%s" % (self.s_url))
        log.debug("获取到登录的参数为：%s" % (self.s_data))
        s = requests.session()
        log.debug("登录请求成功")
        response = s.get(url=self.s_url, params=self.s_data)
        response_json = response.json()


        try:
            token = response_json['data']['token']
            self.header['token'] = token
            log.debug("获取到的token是：%s" % token)
            log.info("token已添加到heder")
        except:
            log.debug("返回值中没有token")
            pass

        return s

    # 运行get请求
    def run_get(self):
        s = self.add_session()
        for i in base.get_data(self):
            url = self.get_url()
            data = base.set_dict(self, i)
            response = s.get(url, params=data, headers=self.header)
            result = self.get_assert(self.nrow)  # 实际结果命令
            expect = self.get_assert(self.nrow, 1)  # 预期结果
            self.nrow = self.nrow + 1
            ast = self.nrow - 1  # 现在调用的行数
            if response.text == expect:  # 判断返回的类型，根据不同的类型做出相应的判断
                log.debug("返回值类型是text：%s，text断言成功" % response.text)
            else:
                response_json = response.json()
                cmd = eval(result)
                log.info("断言成功第%s页的%s行" % (self.assert_sheet, ast))
                self.ast.assertEqual(cmd, expect)
            log.info("get请求成功")

    # 运行post请求
    def run_post(self):
        s = self.add_session()
        for i in base.get_data(self):
            url = self.get_url()
            data = base.set_dict(self, i)  # 调用函数，清除值为空的键值对
            response = s.post(url, data=data)
            result = self.get_assert(self.nrow)  # 获取实际结果的命令
            expect = self.get_assert(self.nrow, 1)  # 预期结果
            log.info("调用第%s行，命令是：%s，预期结果是：%s" % (self.nrow, result, expect))
            self.nrow = self.nrow + 1
            ast = self.nrow - 1

            if response.text == expect:  # 判断返回的类型，根据不同的类型做出相应的判断
                log.debug("返回值类型是text：%s，text断言成功" % response.text)
            else:
                response_json = response.json()
                cmd = eval(result)
                log.info("断言成功第%s页的%s行" % (self.assert_sheet, ast))
                self.ast.assertEqual(cmd, expect)
            log.info("post请求成功")

    # 运行post请求，参数为json
    def run_post_json(self):
        """
        post请求，请求参数为json，参数以字典的方式存在每行的第一列
        :return:
        """
        self.header['Content-Type'] = "application/json;charset=UTF-8"
        s = self.add_session()
        data = xlrd.open_workbook(self.dir_case)
        table = data.sheets()[self.param]
        nrows = table.nrows
        url = self.get_url()



        for i in range(1, nrows):
            data_list = table.row_values(i)
            data_str = str(data_list)
            data_str = data_str.strip("[]")
            data_str = data_str.strip("'")
            data_dict = json.loads(data_str)

            response = s.post(url=url, json=data_dict, headers=self.header)
            result = self.get_assert(self.nrow)  # 获取实际结果的命令
            expect = self.get_assert(self.nrow, 1)  # 预期结果
            log.info("调用第%s行，命令是：%s，预期结果是：%s" % (self.nrow, result, expect))
            self.nrow = self.nrow + 1
            ast = self.nrow - 1
            log.info(response.json())
            log.info(response.text)

            if response.text == expect:  # 判断返回的类型，根据不同的类型做出相应的判断
                log.debug("返回值类型是text：%s，text断言成功" % response.text)
            else:
                response_json = response.json()
                cmd = eval(result)
                log.info("断言成功第%s页的%s行" % (self.assert_sheet, ast))
                self.ast.assertEqual(cmd, expect)
            log.info("post请求成功")

    # post请求，上传文件
    def run_post_upload(self, file="file.txt"):
        """
        上传文件
        :param file: 上传的文件名
        """
        s = self.add_session()
        for i in base.get_data(self):
            url = self.get_url()
            data = base.set_dict(self, i)  # 调用函数，清除值为空的键值对
            filePate = "./uploads/" + file
            file = {'file': open(filePate, 'rb')}
            response = s.post(url=url, data=data, files=file)
            result = self.get_assert(self.nrow)  # 获取实际结果的命令
            expect = self.get_assert(self.nrow, 1)  # 预期结果
            log.info("调用第%s行，命令是：%s，预期结果是：%s" % (self.nrow, result, expect))
            self.nrow = self.nrow + 1
            ast = self.nrow - 1

            if response.text == expect:  # 判断返回的类型，根据不同的类型做出相应的判断
                log.debug("返回值类型是text：%s，text断言成功" % response.text)
            else:
                response_json = response.json()
                cmd = eval(result)
                log.info("断言成功第%s页的%s行" % (self.assert_sheet + 1, ast))
                self.ast.assertEqual(cmd, expect)
            log.info("post请求成功")


if __name__ == '__main__':
    u = "http://120.52.157.131:58080/apis/zznode-csm/cms/login"
    dat = {'username': 'qiaolin', 'password': '8579173b7f0ad165551bf8e892d3dee7'}
    run = base(u, dat, 'single.xlsx', 0, 1)
    run.run_get()

    # url = "http://120.52.157.131:58080/apis/zznode-csm/cms/login"
    # data = {'username': 'qiaolin', 'password': '8579173b7f0ad165551bf8e892d3dee7'}
    # run = base(url, data, 'single.xlsx', 2, 3)
    # run.run_post()

    # url = "http://120.52.157.131:58080/apis/zznode-csm/cms/login"
    # run = base(url, 'single.xlsx', 3, 2)
    # for i in run.get_data():
    #     print(i,type(i))
