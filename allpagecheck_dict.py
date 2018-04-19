# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup
import sys

charalist = [chr(i) for i in range(65,65+26)]
nonlist = []
t = 0

for s1 in charalist:
    for s2 in charalist:
        query = s1+s2
        t = t + 1
        print("現在:" + str(t) + "/676件目")
        time.sleep(1)

        # HTML を取得
        html = urllib.request.urlopen("https://dic.yahoo.co.jp/search/?ei=UTF-8&fr=kb&p=" + query + "&dic_id=all&stype=full").read().decode("utf-8")

        # 解析用の BeautifulSoup オブジェクトを作成
        soup = BeautifulSoup(html, "lxml")

        # <div class="plainlinks">のタグをチェック
        tag = soup.find("div", attrs={"class": "plainlinks"})

        if not isinstance(tag, type(None)):
            flg = tag.string
        else:
            flg = ""
