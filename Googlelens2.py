from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from pprint import pprint
import os 
import requests
import time
import re
def search_picture_link(URL :str):


    curPath = os.getcwd()
    print(curPath)
    driver = webdriver.Chrome(f"{curPath}/ggDriver/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://images.google.com/")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "nDcEnd").click()
    time.sleep(1)
    element = driver.find_element(By.CLASS_NAME, "cB9M7")
    element.send_keys(URL)
    element.send_keys(Keys.RETURN)
    
    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')
    link = soup.findAll("img",{"src":True}, class_ = "wETe9b jFVN1")

    # pprint(link)
    count = 0
    revImages = []
    for image in link:
        # print("Link: " + image['src'])
        if image['src'].startswith("data:") :
            revImages.append(image['data-src'])
        else:
            revImages.append(image['src'])
        if count == 2 :
            break
        count+=1
    
    return revImages
    # pprint(link)

def revImages(input :list):

    result = []
    for i in input:
        result.append(search_picture_link(i['data']))

    # print(result)
    for count,images in enumerate(result):
        
        for count1,image in enumerate(images):
            loadRevImage(count,count1,image)




def loadRevImage(num:int,numImg :int ,src:str):
    imageUrl = src
    img_data = requests.get(imageUrl).content
    curPath = os.getcwd()
    with open(f'{curPath}\static\RevImage\pic{num}{numImg}.jpg', 'wb') as handler:
        handler.write(img_data)


# revImages([{"data":"https://static-cdn.jtvnw.net/user-default-pictures-uv/13e5fa74-defa-11e9-809c-784f43822e80-profile_image-150x150.png"}])


# revImages([{'data': 'https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/299835346_10222653853429438_238771487539892262_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=100&ccb=1-7&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=awbjDUKkV1gAX-VawxL&tn=-DFwpzWxTywRKSgz&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfDt6-GkMu0wBy5H7EesMAERLbrIZCavmIkz9yt67eYpzw&oe=63DCF325&manual_redirect=1',
#               'tag': 'social network',
#               'url': 'https://www.facebook.com/Songpon.te/about'},
#              {'data': 'https://secure.gravatar.com/avatar/744cafe0ee73effe8284b5edaaacb668?s=80&d=identicon',
#               'sitename': 'GitLab',
#               'tag': 'coding',
#               'url': 'https://gitlab.com/teerakanok'}])