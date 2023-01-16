import requests
import os

def images(input:list):

    for count,info in enumerate(input):
        imgLink= info['data']
        loadImage(count,imgLink)



def loadImage(num:int,src:str):
    imageUrl = src
    img_data = requests.get(imageUrl).content
    curPath = os.getcwd()
    with open(f'{curPath}\static\images\pic{num}.jpg', 'wb') as handler:
        handler.write(img_data)