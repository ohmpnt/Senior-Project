import requests
import os

def images(input:list):
    #loop through each image and put into loadimage function
    for count,info in enumerate(input):
        imgLink= info['data']
        loadImage(count,imgLink)



def loadImage(num:int,src:str):
    imageUrl = src
    url = imageUrl[imageUrl.rfind("https"):]  #start link with https incase of invalid link
    img_data = requests.get(url).content #get the image content
    curPath = os.getcwd()
    #save in folder \static\images\pic
    with open(f'{curPath}\static\images\pic{num}.jpg', 'wb') as handler:
        handler.write(img_data)



