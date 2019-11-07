from PIL import Image,ImageDraw
import os
import numpy as np

from warnings import filterwarnings
filterwarnings("error",category=Warning)

siz=64
anvil=Image.open('Anvil4096.png')
anvil=anvil.resize((siz,siz))

for i in os.walk('.\\ba\\'):
    fl=i[2]#fl是文件名的列表


def divide(arr,nam):
    im=Image.new('RGBA', (arr.shape[1], arr.shape[0]), (0,0,0,255))
    draw=ImageDraw.Draw(im)
    for y in range(0,arr.shape[1],siz):
        for x in range(0,arr.shape[0],siz):
            darr=arr[x-siz:x,y-siz:y]
            try:
                n=np.mean(darr)/255
            except:
                continue
            im2=anvil.resize((int(anvil.width*n)+1,int(anvil.height*n)+1))
            draw.bitmap((y-n*siz/2-siz/2,x-n*siz/2-siz/2),im2)
    im.save('.\\r\\'+nam.replace('.jpg','.png'))
            
            
'''
def anv(s):
    return anvil.resize((int(anvil.width*s),int(anvil.height*s)),Image.ANTIALIAS)
'''


def pic(fl=fl):
    frl=[]#帧列表(PIL对象)
    for i in fl:
        print(i)
        frl.append(Image.open('.\\ba\\'+i))
        arr=np.array(frl[-1])
        divide(arr,i)
        
pic()
