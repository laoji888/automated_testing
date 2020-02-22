#coding:utf-8
import datetime
import pymysql
import requests,json,xlrd,time



# 测试json传参
from selenium.webdriver.common.keys import Keys


def post_json():



    a = xlrd.open_workbook("parameter/single.xlsx")
    b = a.sheet_by_index(6)

    cc = b.row_values(1)
    xc = str(cc)
    xc = xc.strip("[]")
    xc = xc.strip("'")
    vf = json.loads(xc)
    print(type(vf))
    vf["endTime"] = "2020"
    print(vf)


    #
    # now_time = datetime.datetime.now()
    # time1 = now_time.strftime("%Y-%m-%d %H:%M:%S")
    # time2 = (now_time + datetime.timedelta(seconds=+20)).strftime("%Y-%m-%d %H:%M:%S")
    # print(vf["releaseTime"])
    # vf["releaseTime"] = time2
    # print(vf["releaseTime"])

    # 申请招募是json传参，发布公告是data，要实现改字典字段的时间，和格式化字典是的时间
    # aa = {"adjunctId":"","endTime":"2020-02-17 00:00:00","firstReviewLoginName":"yjsp","releaseTime":"2020-02-16 19:22:53","remarks":"","reviewType":"逐级审批","secondReviewLoginName":"","title":"2012","description":"<p class=\"text poem-item\" style=\"margin-top: 0px; margin-bottom: 8px; margin-left: 8px; padding: 0px; color: rgb(51, 51, 51); font-size: 14px; line-height: 24px; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\">李白乘舟将欲行，忽闻岸上踏歌声。</p><p class=\"text poem-item\" style=\"margin-top: 0px; margin-bottom: 8px; margin-left: 8px; padding: 0px; color: rgb(51, 51, 51); font-size: 14px; line-height: 24px; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\">桃花潭水深千尺，不及汪伦送我情</p><p><br/></p>","tempId":185}
    #
    # print(xc)
    # print(type(xc))
    # # 接口是添加需求接口
    # u = "http://120.52.157.131:58080/apis/zznode-flow/recruit/notice/save"
    # heder = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    #         'Accept': 'application/json, text/javascript, */*',
    #         "Content-Type": "application/json",
    #         "token":"eyJhbGciOiJIUzI1NiIsInppcCI6IkRFRiJ9.eNqEkMtKw0AUht_lrGdgZjqZS7ax4EIr2O5EwphMcXohIRcQSpeC0I1bqeDKN-iyvk3ic5ghKFhq3f6383FWUNZ3EML8Hi9MNnOEKEBQl7aIXQqhDligEJRJllsIb1bgRY6gyBZ2ZJadBu3zU_Px2uxfmv0OeufMlUcMuzTF_IhR56mp7MT5NRoIwrVgA0UI6ceiLPVnovPRJBpfjuPrq4thzGGNehj9C-Zzs203b-3je7vd_Ql2KvQDeSJ0AMy4ZEr9A6xhfYvAPuS-orUUVAwoAmcqLyj6Lcwq13WFEknQ_R5bISnmWibYJCTA2sgpU3aqFOs-8AUAAP__.ZHJTbGpaCredUvxFgxr8H_VGQ5m185b_xHhReD0ut9k"}
    #
    # r = requests.post(url=u,json=aa,headers=heder)
    # print(r.json())


# 上传接口
def upload():

    heder = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*',
            'token':'eyJhbGciOiJIUzI1NiIsInppcCI6IkRFRiJ9.eNqEjs1Kw0AUhd_lricwM5nJzGQbCy60gu1OJMwkI05_SMgPCCVLQejGrVRw5Rt0Wd8m8TlsCAqWWrffuefcbwVlbSCE-b230NnMYSwBQV3aInYphIpTLhGUSZZbCG9W0EOGoMgWdqyXewbd81P78druXtrdFobkzJVHArvUxfxIUOepruzU9WuEB5ipgPoSYzyMRVnav4nOx9NocjmJr68uRjGDBg0y6pfM53rTrd-6x_dus_1T7NTRj-SJowNhygSV8h9hBc0tAvuQ9xWlhCCCEwROVz2Q5BvMKrfvahxgY33tKRMwjxHieybRxEsk4z6VTJk7Ac0XAAAA__8.rcfv6-P0CPyWCcdgOV-JeL4N0_RH272bP1VOHpT6imk',
            'Content - Type': 'multipart/form-data'
            }

    url = "http://120.52.157.131:58080/apis/zznode-file/upload"
    file ={'file': open("./uploads/file.txt", 'rb')}
    data = {"file": "(binary)"}

    r = requests.post(url=url,data=data,files=file)
    x =r.json()
    print(x)

# 时间处理
def t():
    now_time = datetime.datetime.now()
    time1 = now_time.strftime("%Y-%m-%d %H:%M:%S")
    time2 = (now_time + datetime.timedelta(seconds=+20)).strftime("%Y-%m-%d %H:%M:%S")
    print(time1)
    print(time2)

# 格式化字典
def set_dict():
    qw = {"a": "qwe", "b": "12", "c": "time"}
    t = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())

    for k in list(qw.keys()):
        if not qw[k]:

            del qw[k]

    for k in list(qw.keys()):
        if qw[k] == 'null':
            qw[k] = ''


    for k in list(qw.keys()):
        if qw[k] == 'time':
            qw[k] = t


    for k,v in qw.items():
        print(k + "=" + v)


# 截取json
def aaa():
    x = {"adjunctId":"","endTime":"2020-02-17 00:00:00","firstReviewLoginName":"yjsp","releaseTime":"2020-02-16 18:05:34","remarks":"","reviewType":"逐级审批","secondReviewLoginName":"","title":"api_2021","description":"<p class=\"text poem-item\" style=\"margin-top: 0px; margin-bottom: 8px; margin-left: 8px; padding: 0px; color: rgb(51, 51, 51); font-size: 14px; line-height: 24px; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\">黄葛生洛溪，黄花自绵幂。</p><p class=\"text poem-item\" style=\"margin-top: 0px; margin-bottom: 8px; margin-left: 8px; padding: 0px; color: rgb(51, 51, 51); font-size: 14px; line-height: 24px; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\">青烟蔓长条，缭绕几百尺。</p><p class=\"text poem-item\" style=\"margin-top: 0px; margin-bottom: 8px; margin-left: 8px; padding: 0px; color: rgb(51, 51, 51); font-size: 14px; line-height: 24px; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\">闺人费素手，采缉作絺绤。</p><p class=\"text poem-item\" style=\"margin-top: 0px; margin-bottom: 8px; margin-left: 8px; padding: 0px; color: rgb(51, 51, 51); font-size: 14px; line-height: 24px; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\">缝为绝国衣，远寄日南客。</p><p class=\"text poem-item\" style=\"margin-top: 0px; margin-bottom: 8px; margin-left: 8px; padding: 0px; color: rgb(51, 51, 51); font-size: 14px; line-height: 24px; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\">苍梧大火落，暑服莫轻掷。</p><p class=\"text poem-item\" style=\"margin-top: 0px; margin-bottom: 8px; margin-left: 8px; padding: 0px; color: rgb(51, 51, 51); font-size: 14px; line-height: 24px; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\">此物虽过时，是妾手中迹。</p><p><br/></p>","tempId":183}
    a = json.dumps(x)
    print(x['title'])



def msql(sql):
    conn = pymysql.connect(
        host='127.0.0.1',
        user = 'root',
        passwd="000000",
        port= 3306,
        db='test',
        charset='utf8')

    curso = conn.cursor()
    cursor = curso.execute(sql)
    print(cursor)
    print(curso)
    curso.close()

from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
dr.get("http://120.52.157.131:58080/#/home/cooperation")
sleep(10)





