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
    # vf6yckniFRDqepGNSaSD2SN4IhCv1wj6LPPqfh74 李靖翔
    }
    login=s.get(reseturl,headers=headers) #登录
    # print(login.text)
    login_soup = BeautifulSoup(login.text, 'html.parser') #解析信息确认页面
    # print(soup.select(".confirm-user-info"))
    userinfo=login_soup.select(".confirm-user-info p") #找到用户信息div 课程姓名编号单位
    # print(userinfo)
    dict={}
    for i in userinfo:
        # print(i)
        info_soup=BeautifulSoup(str(i), 'html.parser') #分布解析课程姓名编号单位信息
        # print(info_soup.get_text())
        item=info_soup.get_text()
        # print(item[:4],item[5:])
        dict[item[:4]]=item[5:]
    print(dict)
        #
        # span_soup=info_soup.find_all('span')
        # no_span=BeautifulSoup(str(span_soup[0]), 'html.parser')
        # item=no_span.get_text()[:-1] #key
        # print(item)
        # print(info_soup.get_text())
    # info_soup=BeautifulSoup(str(userinfo[0]), 'html.parser') #解析用户信息
    # print(info_soup)
    # print(info_soup.get_text())
    # info=info_soup.get_text()
    # print(info)
    # print(info_soup.find_all('p'))

    # for i in userinfo:
    #     print(i)
    # info = BeautifulSoup(str(userinfo[0]), 'lxml') #解析用户信息div

    # print(info)
    # soup1 = BeautifulSoup(info.text, 'html.parser')
    # print(soup1)
    # infoitem = soup1.select('p')
    # print(infoitem)
    # for i in infoitem:
    #    print(i)
    token = re.findall(r'var token ?= ?"(.*?)"', login.text) #获取js里的token
    lesson_id = re.findall(r"'lesson_id':(.*)", login.text)  # 获取js里的token
    print("token:%s"%token[0])
    print("lesson_id:%s"%lesson_id[0])
    # # print(pattern.search(script.text).group(1))
    # print(token)
    # # print(soup)

    finalurl="https://service.jiangsugqt.org/youth/lesson/confirm"
    params={
        "_token":token[0],
        "lesson_id":lesson_id[0]
    }
    res2=s.post(url=finalurl,params=params)
    res=res2.json()
    print("返回结果:%s"%res)
    if res["status"]==1:
        print("青年大学习已完成")
    else:
        print("错误")


if __name__ == '__main__':
    main()