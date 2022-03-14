import re

import requests
from bs4 import BeautifulSoup


def main():
    s=requests.session() #创建会话
    reseturl="https://service.jiangsugqt.org/youth/lesson" #江苏省青年大学习接口

    headers={ #构造请求头
    'User-Agent':"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001234) NetType/WIFI Language/zh_CN",
    'Cookie':"laravel_session=8rAucTd84mpMLxilmCjeWO08rbtC7opDnrwo9YvJ" #抓包获取
    # 'Cookie':"8rAucTd84mpMLxilmCjeWO08rbtC7opDnrwo9YvJ"
    # 8rAucTd84mpMLxilmCjeWO08rbtC7opDnrwo9YvJ 周良宇 003831928
    # esX66JF8QROB5yx89KMpFBwnF2eNrVUbSpx8FVUX 姜宇 008629871
    # vf6yckniFRDqepGNSaSD2SN4IhCv1wj6LPPqfh74 李
    }
    login=s.get(reseturl,headers=headers)
    # data=login.text
    # # print(res1.text)
    # print(data)
    # res=res1.text.find("token")
    # print(res)
    # html=res1
    # # html = BeautifulSoup(data.text, "html.parser")
    token = re.findall(r'var token ?= ?"(.*?)"', login.text) #获取js里的token
    print(token)
    # # print(pattern.search(script.text).group(1))
    # print(token)
    # # print(soup)

    finalurl="https://service.jiangsugqt.org/youth/lesson/confirm"
    params={
        "_token":token,
        "lesson_id":"120"
    }
    res2=s.post(url=finalurl,params=params)
    res=res2.json()
    print(res)
    if res["status"]==1:
        print("青年大学习已完成")
    else:
        print("错误")


if __name__ == '__main__':
    main()