import urllib
from bs4 import BeautifulSoup
import re
# 1.设置url路径
url = "http://www.yunzhonggexiaoshuo.com/"
# 2.设置用户代理
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
# 3.设置请求
req = urllib.request.Request(url,headers=headers)
# 4.打开请求
response = urllib.request.urlopen(req)
# 5.读取网页信息
html = response.read()
# 6.解析数据
soup = BeautifulSoup(html,"html.parser")
soup_text = str(soup.find_all("div"))
# 7.数据清理
first = re.findall(r'html">(.+?)</a>',soup_text)
#for i in first:
    #print(i)