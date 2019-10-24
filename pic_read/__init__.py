import base64
import os
from time import time
from urllib.request import Request, urlopen

from future.backports.urllib import parse

from sqlite import Sql

orc_baidu_token = None


class BaiduApi(object):
    baidu_config = {}
    sqlConnect = None
    headers = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
            'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
            'Connection': 'keep-alive'
        }
    def __init__(self):
        self.sqlConnect = Sql()

    def __token__(self):
        result = self.sqlConnect.search("SELECT token, expire from TOKEN where ID=1")
        if(result.rowcount<=0):
            return self.__new_token__(True)
        for row in result:
            if(int(time())>row[1]):
                return self.__new_token__(False)
            return row[0]




    def __new_token__(self, insert):
        api_key = os.getenv("API_KEY")
        secret_key = os.getenv("SECRET_KEY")
        # coding:utf-8

        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
        api_key, secret_key)
        print("host is : %s " % host)
        request = Request(host, headers=self.headers)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urlopen(request)
        content = response.read()
        if (content):
            orc_baidu_token_map = eval(bytes.decode(content))
            orc_baidu_token = orc_baidu_token_map["access_token"]
            orc_baidu_token_expire = int(orc_baidu_token_map["expires_in"]) + int(time())
            if(insert):
                print("insert a new baidu orc token")
                self.sqlConnect.insert("INSERT INTO TOKEN (ID,token,expire) VALUES (1, '%s', %d)" % (orc_baidu_token, orc_baidu_token_expire))
            else:
                print("update a new baidu orc token")
                self.sqlConnect.update("UPDATE TOKEN set token='%s', expire=%d where ID=1" % (orc_baidu_token, orc_baidu_token_expire))
            return orc_baidu_token

    def hands_pic_to_words(self, picPath):
        access_token = self.__token__() if orc_baidu_token is None else orc_baidu_token
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting?access_token=' + access_token
        # 二进制方式打开图文件
        f = open(picPath, 'rb')
        # 参数image：图像base64编码
        img = base64.b64encode(f.read())
        params = {"image": img}
        params = parse.urlencode(params).encode("utf-8")

        self.headers["Content-Type"] = 'application/x-www-form-urlencoded'
        request = Request(url, data=params, headers=self.headers)
        response = urlopen(request)
        content = response.read()
        result = ""
        if (content):
            words_result = (eval(bytes.decode(content))["words_result"])
            for word in words_result:
                result = result+word["words"]
        print(result)
        return result

    def person_card_to_words(self, picPath):
        access_token = self.__token__() if orc_baidu_token is None else orc_baidu_token
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/idcard?access_token=' + access_token
        # 二进制方式打开图文件
        f = open(picPath, 'rb')
        # 参数image：图像base64编码
        img = base64.b64encode(f.read())
        params = {"image": img, "id_card_side":"front","detect_direction":"true","detect_risk":"true"}
        params = parse.urlencode(params).encode("utf-8")
        self.headers["Content-Type"] = 'application/x-www-form-urlencoded'
        request = Request(url, data=params, headers=self.headers)
        response = urlopen(request)
        content = response.read()
        result = {}
        if (content):
            words_result = (eval(bytes.decode(content))["words_result"])
            for key in words_result:
                result[key] = words_result[key]["words"]
        print(result)
        return result

    def bank_card_to_words(self, picPath):
        access_token = self.__token__() if orc_baidu_token is None else orc_baidu_token
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard?access_token=' + access_token
        # 二进制方式打开图文件
        f = open(picPath, 'rb')
        # 参数image：图像base64编码
        img = base64.b64encode(f.read())
        params = {"image": img}
        params = parse.urlencode(params).encode("utf-8")
        self.headers["Content-Type"] = 'application/x-www-form-urlencoded'
        request = Request(url, data=params, headers=self.headers)
        response = urlopen(request)
        content = response.read()
        result=""
        if (content):
            words_result = (eval(bytes.decode(content))["result"])
            result = words_result
        print(result)
        return result

#BaiduApi().person_card_to_words(os.path.abspath("../temp/card.jpg"))