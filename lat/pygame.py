import pygame,sys
from pygame.locals import *
# 初始化pygame模块
pygame.init()
# 设定窗口大小
DISPLAY = pygame.display.set_mode(400,300)
# 在窗口中输出文字
pygame.display.set_caption("hello")
# 设定颜色方便调用
BLACK = (0,0,0)  #pygame中(0，0，0)表示黑色

GREEN = (0,255,0)

BLUE = (0,0,128)
# 设定字体样式
fontobj = pygame.font.Font('waterlily-script.woff.ttf',32)
# render方法返回Surface对象
textSurface = fontobj.render('hello',True,GREEN)
# get_rect()方法返回rect对象
textRect = textSurface.get_rect()
# 将文本居中显示
textRect.center=(200,150)

while True:
    # 设定窗口背景颜色
    DISPLAY.fill(BLACK)
    # 建立文字像素块
    DISPLAY.blit(textSurface,textRect)
    for event in pygame.event.get():
        # 设置退出方式，当点击x号或者按下esc退出程序
        if event.type()==QUIT:
            pygame.quit()
            sys.exit()
    # 刷新窗口，让窗口一直显示
    pygame.display.update()