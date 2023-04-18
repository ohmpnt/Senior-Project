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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def revImages(input :list):
    result = []
    #loop through each  image
    for i in input:
        temp = i['data']
        url = temp[temp.rfind("https"):] #start link with https incase of invalid link
        result.append(revimg_search(url)) # call revimg_search and put into result list

    return result

def revimg_search(url:str):
    caps = DesiredCapabilities().CHROME
    # caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
    # caps["pageLoadStrategy"] = "eager"  #  Waits for page to be interactive
    caps["pageLoadStrategy"] = "eager"   # Do not wait for full page load
    curPath = os.getcwd()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(f"{curPath}/ggDriver/chromedriver.exe", options=options,desired_capabilities=caps) #open google chrom web driver
    driver.maximize_window()
    driver.get("https://www.duplichecker.com/reverse-image-search.php") #get to the duplichecker site
    time.sleep(1)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(1)
    # driver.execute_script("window.scrollBy(0,500)") #scroll down in case of small screen
    inputlink = driver.find_element(By.XPATH, "//input[@id='url']")
    inputlink.send_keys(url) #send in the url
    inputlink.submit()
    # enter = driver.find_element(By.ID,"checkReverse")
    # enter.click() # click the search button
    time.sleep(1)
    src = driver.page_source #get the result page source
    soup = BeautifulSoup(src, 'html.parser')
    result = []
    #find all the reverse image links
    for data in soup.find_all('div', class_='icon_svg'):
        for a in data.find_all('a'):
            result.append(a.get('href'))
    dataLink = [result[0],result[1],result[2],result[3]]
    driver.close()
    return  dataLink #return the link

