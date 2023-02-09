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
def revImages(input :list):
    result = []
    for i in input:
        temp = i['data']
        url = temp[temp.rfind("https"):]
        result.append(revimg_search(url))

    return result

def revimg_search(url:str):
    # # url = input("input link: ")
    # url = "https://scontent.fbkk2-6.fna.fbcdn.net/v/t39.30808-6/290501684_5219335674825610_671348912778975975_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=4TgaNVBJHsIAX9Gzmyh&_nc_ht=scontent.fbkk2-6.fna&oh=00_AfAx7BXzVXykonCbkqCYPJP_5NJBgHY04W2TAP_WtoaNDw&oe=63E7A568"
    # curPath = os.getcwd()
    # driver = webdriver.Chrome(f"{curPath}/ggDriver/chromedriver.exe")
    # driver.maximize_window()
    # driver.get("https://yandex.com/images/")
    # time.sleep(1)
    # # driver.find_element(By.CLASS_NAME, "input__cbir-button").click()
    # searchbutton = driver.find_element(By.CSS_SELECTOR, "button.button2_theme_clear")
    # searchbutton.click()
    # time.sleep(1)
    # element = driver.find_element(By.XPATH, "//input[@class='Textinput-Control']")
    # element.send_keys(url)
    # # element.send_keys(Keys.RETURN)
    # enter = driver.find_element(By.XPATH, "//button[@class='CbirPanel-UrlFormButton']")
    # enter.click()
    # get_url = driver.current_url
    # print(get_url)

    
    curPath = os.getcwd()
    driver = webdriver.Chrome(f"{curPath}/ggDriver/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.duplichecker.com/reverse-image-search.php")
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0,500)")
    inputlink = driver.find_element(By.XPATH, "//input[@id='url']")
    inputlink.send_keys(url)
    enter = driver.find_element(By.ID,"checkReverse")
    enter.click()
    time.sleep(1)
    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')
    result = []
    for data in soup.find_all('div', class_='icon_svg'):
        for a in data.find_all('a'):
            result.append(a.get('href'))

    print(result)
    dataLink = [result[0],result[1],result[2],result[3]]

    return  dataLink


# i =revimg_search('https://scontent.fbkk2-6.fna.fbcdn.net/v/t39.30808-6/290501684_5219335674825610_671348912778975975_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=4TgaNVBJHsIAX9Gzmyh&_nc_ht=scontent.fbkk2-6.fna&oh=00_AfAx7BXzVXykonCbkqCYPJP_5NJBgHY04W2TAP_WtoaNDw&oe=63E7A568')
# print(i)

# out = revImages([{'data': 'https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/290501684_5219335674825610_671348912778975975_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=104&ccb=1-7&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=DQVM3C4CUaIAX_gsdS1&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfAsd0d4H_tQUe6iK9DQyhrcvxad7RuK9VCF-FURv608OQ&oe=63E99FA8&manual_redirect=1',
#               'sitename': 'facebook',
#               'tag': 'social network',
#               'url': 'https://www.facebook.com/fubuki.tang/about'},
#              {'data': 'https://avatars.githubusercontent.com/u/51602945?v=4',
#               'sitename': 'GitHub',
#               'tag': 'coding',
#               'url': 'https://github.com/tangkantapon'},
#              {'data': 'https://static-cdn.jtvnw.net/user-default-pictures-uv/ebe4cd89-b4f4-4cd9-adac-2f30151b4209-profile_image-150x150.png',
#               'sitename': 'Twitch',
#               'tag': 'streaming',
#               'url': 'https://www.twitch.tv/tangkantapon'},
#              {'data': 'flex: 0 0 '
#                       '80px;https://cuad.ask.fm/assets2/154/971/066/880/normal/avatar.jpg',
#               'sitename': 'AskFM',
#               'tag': 'eg',
#               'url': 'https://ask.fm/tangkantapon'}])

# print(out)