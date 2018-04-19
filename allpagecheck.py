# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import sys
import time

charalist = [chr(i) for i in range(65,65+26)]
nonlist = []
t = 0

for s1 in charalist:
    for s2 in charalist:
        query = s1+s2
        t = t + 1
        print("現在:" + str(t) + "/676件目")
        time.sleep(1)

        try:
            page = urllib.request.urlopen("https://ja.wikipedia.org/wiki/" + query)
        except urllib.error.HTTPError as e:
            nonlist.append(query)

# 結果出力
if nonlist == []:
    print("676通り全ての記事の確認が出来ました！")
else:
    print("記事の存在しない２文字は、以下の" + str(len(nonlist)) + "件です。")
    for item in nonlist:
        print(item)
