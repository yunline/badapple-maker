from PIL import Image
import os
import numpy as np

from warnings import filterwarnings
filterwarnings("error",category=Warning)

siz=128
hq=True

anvil=Image.open('Anvil4096.png')
anvil=anvil.resize((siz,siz))

for i in os.walk('.\\ba\\'):
    fl=i[2]#fl是文件名的列表

def divide(arr,nam):
    im=Image.new('RGBA', (arr.shape[1], arr.shape[0]), (255,255,255,255))
    for y in range(0,arr.shape[1],siz):
        for x in range(0,arr.shape[0],siz):
            darr=arr[x-siz:x,y-siz:y]
            try:
                n=np.mean(darr)/255
            except:
                continue
            if hq==False:
                im2=anvil.resize((int(anvil.width*n)+1,int(anvil.height*n)+1))
            else:
                im2=anvil.resize((int(anvil.width*n)+1,int(anvil.height*n)+1),Image.ANTIALIAS)
            im.paste(im2,(int(y-n*siz/2),int(x-n*siz/2)))
    im.save('.\\r\\'+nam.replace('.jpg','.png'))

def pic(fl=fl):
    frl=[]#帧列表(PIL对象)
    for num in range(int(input("断点>>>")),len(fl)):
        i=fl[num]
        print(i)
        frl.append(Image.open('.\\ba\\'+i))
        arr=np.array(frl[-1])
        divide(arr,i)
        
pic()
