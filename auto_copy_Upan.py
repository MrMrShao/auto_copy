from time import sleep
import os, shutil
usb_path="H://"
x=True
while x:
    try:
        content=os.listdir(usb_path)
    except:
        sleep(3)
       # print('No such file,trying...')
        pass
    else:
        x=False
#print(content)
shutil.copytree(usb_path, r'E:\python\new')
