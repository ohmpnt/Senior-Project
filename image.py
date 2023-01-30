import requests
import os

def images(input:list):

    for count,info in enumerate(input):
        imgLink= info['data']
        loadImage(count,imgLink)



def loadImage(num:int,src:str):
    imageUrl = src
    url = imageUrl[imageUrl.rfind("https"):]
    img_data = requests.get(url).content
    curPath = os.getcwd()
    with open(f'{curPath}\static\images\pic{num}.jpg', 'wb') as handler:
        handler.write(img_data)



loadImage(1,"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSO_43PPSdPKYlNrjSXcf1fLzruLzbgEDmjhSqE-XJpLGso3vTl")