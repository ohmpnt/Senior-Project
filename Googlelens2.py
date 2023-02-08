from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from pprint import pprint
import os 
import requests
import time
import re
def search_picture_link(url :str):
    url = url[url.rfind("https"):]
    curPath = os.getcwd()
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # , options=chrome_options
    driver = webdriver.Chrome(f"{curPath}/ggDriver/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://images.google.com/")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "nDcEnd").click()
    time.sleep(1)
    element = driver.find_element(By.CLASS_NAME, "cB9M7")
    element.send_keys(url)
    element.send_keys(Keys.RETURN)
    time.sleep(3)
    
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
    
    print(revImages)
    return revImages
    # pprint(link)

def revImages(input :list):
    result = []
    for i in input:
        result.append(search_picture_link(i['data']))

    print(result)
    for count,images in enumerate(result):
        
        for count1,image in enumerate(images):
            loadRevImage(count,count1,image)


def loadRevImage(num:int,numImg :int ,src:str):
    imageUrl = src
    img_data = requests.get(imageUrl).content
    curPath = os.getcwd()
    with open(f'{curPath}\static\RevImage\pic{num}{numImg}.jpg', 'wb') as handler:
        handler.write(img_data)


# revImages([{"data":"https://scontent.fbkk2-6.fna.fbcdn.net/v/t39.30808-6/290501684_5219335674825610_671348912778975975_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=4TgaNVBJHsIAX9Gzmyh&_nc_ht=scontent.fbkk2-6.fna&oh=00_AfAx7BXzVXykonCbkqCYPJP_5NJBgHY04W2TAP_WtoaNDw&oe=63E7A568"}])


# revImages([{'data': 'https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/290501684_5219335674825610_671348912778975975_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=104&ccb=1-7&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=wwQbyMhXm9QAX8ePY_W&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfCq0r-N4aV5ckhtVVoxq3LZOFFOGs6h_xfe0KkpaTEamg&oe=63DDC228&manual_redirect=1',
#               'tag': 'social network',
#               'url': 'https://www.facebook.com/fubuki.tang/about'},
#              {'data': 'https://static-cdn.jtvnw.net/user-default-pictures-uv/ebe4cd89-b4f4-4cd9-adac-2f30151b4209-profile_image-150x150.png',
#               'sitename': 'Twitch',
#               'tag': 'streaming',
#               'url': 'https://www.twitch.tv/Tangkantapon'},
#              {'data': 'https://avatars.githubusercontent.com/u/51602945?v=4',
#               'sitename': 'GitHub',
#               'tag': 'coding',
#               'url': 'https://github.com/Tangkantapon'},
#              {'data': 'flex: 0 0 '
#                       '80px;https://cuad.ask.fm/assets2/154/971/066/880/normal/avatar.jpg',
#               'sitename': 'AskFM',
#               'tag': 'eg',
#               'url': 'https://ask.fm/Tangkantapon'}])