# -*-coding:utf-8-*-
import requests
from pytesseract import *
from bs4 import BeautifulSoup
from PIL import Image


url = 'http://app.szzfgjj.com:7001/accountQuery'
url_verify = "http://app.szzfgjj.com:7001/pages/code.jsp?yzm="
session = requests.Session()
ad = "d:\\py\\pc\\tieba\\"
path = ad + "557" + ".jpg"
accnum = input("请输入电脑号或者公积金账号：")
certinum = input("请输入身份证号码：")
def verify_code():
    r = session.get(url_verify)
    with open(path, "wb") as fd:
        for chunk in r.iter_content(100):
            fd.write(chunk)
            #下载图片 data=urllib.request.urlretrieve(urlyzm,path)
    im = Image.open(path)
    verify_x = pytesseract.image_to_string(im)
    return verify_x


def query_data(verify):

    if len(accnum) == 11:
        data_a = {
            "accnum": accnum,
            "certinum": certinum,
            "qryflag": 1,
            "verify": verify
        }
    elif len(accnum)==9:
        data_a = {
            "accnum": accnum,
            "certinum": certinum,
            "qryflag": 0,
            "verify": verify
        }
    #y有公积金账号和电脑号查询两种方式
    else:
        print("请重新输入公积金账号或者电脑号：")
    return data_a

def query(data1):
    rr = session.post(url, data=data1)
    soup = BeautifulSoup(rr.text, "html.parser")
    return soup

if __name__ == '__main__':
    i = 1
    for i in range(10):
        verify = verify_code()
        data1 = query_data(verify=verify)
        soup = query(data1=data1)
        if "验证码错误" in str(soup):
            print("验证码错误")
        else:
            print(soup)
            break
        i += 1


