import requests
from time import sleep
from PIL import Image
import os
import tool

def down_img(url,j):
    tool.exist_file(r'img')
    tool.exist_file(r'ori_img')
    try:
        pic = requests.get(url,timeout=20)
        sleep(2)
    except:
        print(url)
        print("error")

    if url[-3:] == 'jpg' :
        with open(r'temp.jpg','wb') as f:
            f.write(pic.content)
        img = Image.open(r'temp.jpg')
        path = os.path.join(r'ori_img', str(j) + '.jpg')
        img.save(path)
        img = img.resize((200,200))
        path = os.path.join(r'img',str(j)+'.jpg')
        img.save(path)
    else:
        with open(r'temp.png','wb') as f:
            f.write(pic.content)
        img = Image.open(r'temp.png')
        path = os.path.join(r'ori_img', str(j) + '.png')
        img.save(path)
        img = img.resize((200,200))
        img = img.convert('RGB')
        path = os.path.join(r'img', str(j) + '.jpg')
        img.save(path)
    print('temp.jpg ----->ok')

if __name__ == '__main__':
    # down_img(r'https://g-search1.alicdn.com/img/bao/uploaded/i4/i2/2878528631/O1CN0164IEVV2Dd34s9MPcj_!!0-item_pic.jpg')
    # path = r'https://g-search1.alicdn.com/img/bao/uploaded/i4/i2/2878528631/O1CN0164IEVV2Dd34s9MPcj_!!0-item_pic.jpg'
    # print(path[-3:])
    pass