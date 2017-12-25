# -*- coding: utf-8 -*-
import requests, re
from bs4 import BeautifulSoup

baseUrl = "https://www.v2ex.com"
cookie = ''


class V2ex(object):

    def url(self, urlList):
        return '/'.join(urlList)

    def headers(self):
        headers = {
            'cookie':
            cookie,
            'user-agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
        }
        return headers

    def start(self):
        url = self.url([baseUrl, "mission", "daily"])
        response = requests.get(url, headers=self.headers())
        soup = BeautifulSoup(response.text, "lxml")
        con = soup.find(
            "input", attrs={
                "class": "super normal button"
            }).get("onclick")
        href = re.search(u"('/)(.*)(')", con, re.S).group(2)
        url = self.url([baseUrl, href])
        response = requests.get(url, headers=self.headers())
        if response.status_code == 200:
            print("签到成功！")
        else:
            print("签到失败！")
        exit()


if __name__ == '__main__':
    V2ex = V2ex()
    V2ex.start()