import urllib
from bs4 import BeautifulSoup
def getHtml(index):
    # 1.设置URL路径
    url = "http://www.yunzhonggexiaoshuo.com/"+str(index)+".html"
    # 2.打开网页爬取网页信息
    response = urllib.request.urlopen(url)
    # 3.读取响应文件内容
    html = response.read()
    # 4.解析文件
    soup = BeautifulSoup(html, "html.parser")
    soup_text = str(soup.find_all('div',id="BookText"))
    # 5.数据清理
    first = soup_text.replace("<br/><br/>","\n")
    second = first.replace('<div id="p_ad_t3"><script language="javascript" src="/2.js" type="text/javascript"></script></div></div>]',' ')
    final = second.replace('[<div class="bookcontent clearfix" id="BookText">',' ')
    # 6.存储文件
    fileName = str(index) + ".txt"
    f = open(fileName, "w", encoding="utf-8")
    f.write(final)
    f.close()
# 爬取所有章节
if __name__ == '__main__':
    for index in range(245,305):
        getHtml(index)


