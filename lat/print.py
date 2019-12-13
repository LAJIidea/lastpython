# 导入图象输出模块
import tkinter
# 导入tk的响应输出模块
from  tkinter.messagebox import showinfo
# 导入爬取的目录
from lat import catalogue
# 用来存储目录按钮
button = []
# 用来存储文章内容
#text = []
n = 0
a = 0
# 生成一个窗口
top = tkinter.Tk()
# 响应按钮事件，输出对应的文章内容
def reply(n):
    c = n+245
    f = open(str(c) + ".txt", "r", encoding="utf-8")
    text = f.read()
    showinfo(title="新窗口",message=text)

'''
def reply():
    showinfo(title="新窗口",message="!")
'''

# 创建目录按钮
for i in catalogue.first:
    # 用lamda函数来调用reply()函数，注意lambda在循环中的问题
    button.append(tkinter.Button(top,text = i,command=lambda s=n:reply(s)))
    button[n].pack()
    n += 1
# 窗口持续存在
top.mainloop()