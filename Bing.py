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

def revimg_search():
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

    url = input("image link: ")
    curPath = os.getcwd()
    driver = webdriver.Chrome(f"{curPath}/ggDriver/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.duplichecker.com/reverse-image-search.php")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,500)")
    inputlink = driver.find_element(By.XPATH, "//input[@id='url']")
    inputlink.send_keys(url)
    enter = driver.find_element(By.ID,"checkReverse")
    enter.click()
    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')
    for data in soup.find_all('div', class_='icon_svg'):
        for a in data.find_all('a'):
            print(a.get('href'))

revimg_search()
