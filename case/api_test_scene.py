import unittest, warnings, requests, time
from common.log import log

class scene(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

        # 合作伙伴登录信息
        self.url = "http://120.52.157.131:58080/apis/zznode-csm/cms/login"
        self.data = {'username': 'kh-laoji008', 'password': 'a92553fd8fdc9620f76c7651319bbdcd'}
        self.header = {}
        self.log = log().ll()

    # 登录后把token添加到请求头

    def login(self,url,data):
        r = requests.get(url = url, params = data)
        j = r.json()
        token = j['data']['token']
        self.header["token"] = token
        user = data["username"]
        self.log.info("用户：%s 登录成功,token已添加到请求头" %user)


    # 测试合作伙伴添加产品场景
    def test_add_commodity(self):
        self.log.info("开始执行合作伙伴添加商品")
        self.login(self.url, self.data)
        # 合作伙伴添加商品
        add_commodity_url = "http://120.52.157.131:58080/apis/zznode-flow/prodManage/addProd"
        data = {"proName": "api_test",
                "proCoverFlie": {"createTime": "2020-02-17 22:11:51", "fileCode": "s4PvBmJl", "fileFormat": ".png",
                                 "fileName": "548-336.png",
                                 "filePath": "/home/ftp/files/202002/043200217221151LwTYk.png", "fileSize": 30421,
                                 "fileUrl": "202002/043200217221151LwTYk.png", "id": 5298},
                "proType": ["fWAxMyIl"], "industryOne": ["B8IwLY9A"], "industryTwo": [], "area": ["ISovK2Zs"],
                "capactiy": ["iYmwusmL"],
                "videoFile": {"createTime": "2020-02-17 22:12:17", "fileCode": "M0QHndgb", "fileFormat": ".mp4",
                              "fileName": "mp4.mp4", "filePath": "/home/ftp/files/202002/918200217221217YhEMH.mp4",
                              "fileSize": 44102, "fileUrl": "202002/918200217221217YhEMH.mp4", "id": 5299},
                "aolutionFile": {"createTime": "2020-02-17 22:12:56", "fileCode": "A54eXxQP", "fileFormat": ".pdf",
                                 "fileName": "pdf.pdf", "filePath": "/home/ftp/files/202002/114200217221256NeNiL.pdf",
                                 "fileSize": 44102, "fileUrl": "202002/114200217221256NeNiL.pdf", "id": 5300},
                "proUse": "110", "proApplicationScenario": "110", "solution": "110", "proTrait": "110",
                "proAimsCilent": "110", "proCooperationMode": "110", "useCase": []}
        r1 = requests.post(url=add_commodity_url, json=data, headers=self.header)
        r1_json = r1.json()
        self.log.debug("合作伙伴添加商品成功")
        time.sleep(2)

        # 乔琳登录信息
        url = "http://120.52.157.131:58080/apis/zznode-csm/cms/login"
        data = {'username': 'qiaolin', 'password': '8579173b7f0ad165551bf8e892d3dee7'}
        self.login(url,data)

        # 搜索未审核的产品信息
        url1 = "http://120.52.157.131:58080/apis/zznode-flow/prodManage/queryProdList"
        j_data = {"pageSize":10,"pageNum":1,"proName":"api_test",
                  "companyNameCn":"","industryOne":[],"industryTwo":[],
                  "proStatus":"","queryType":"admin"}

        rr = requests.post(url=url1, json=j_data,headers=self.header)
        j = rr.json()
        x = j["data"]["rows"][0]["proName"]
        self.assertEqual(x, "api_test")
        self.log.debug("要审核的数据信息获取成功")

        # 获取的未审核的产品信息proCode,审核时添加到url和请求参数中
        x1 = j["data"]["rows"][0]["proCode"]

        u = "http://120.52.157.131:58080/apis/zznode-flow/prodManage/auditPro/"
        url2 = u + x1

        data_1 = {"remarks":"111", "auditResult":"pass", "proCode":x1}

        r6 = requests.patch(url=url2, data=data_1, headers=self.header)
        r_j = r6.json()
        self.assertEqual(r_j['resultStat'], 'SUCCESS')
        self.log.debug("新增产品审核成功")
        self.log.info("合作伙伴添加商品成功")




    def tearDown(self):
        pass


if __name__ == '__main__':
    r = scene()
    r.test_add_commodity()
