import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import os
from pprint import pprint
import re

def search_linkedin(URL:str):
    data = {
        "DOB" : [],
        "fName" : [],
        "lName": [],
        "username": [],
        "phoneNumber": [],
        "email": [],
        "fullName": [],
        "picture": [],
        "address": [],
        "occupation": [],
        "education": [],
        "name":  [],
        "workPlace" : []
    }
    if URL is None:
        return data
    curPath = os.getcwd()
    # Create Chromeoptions instance 
    options = webdriver.ChromeOptions() 
 
    # Adding argument to disable the AutomationControlled flag 
    options.add_argument("--disable-blink-features=AutomationControlled") 
 
    # Exclude the collection of enable-automation switches 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
    # Turn-off userAutomationExtension 
    options.add_experimental_option("useAutomationExtension", False) 
    curPath = os.getcwd()
    driver = webdriver.Chrome(f"{curPath}/ggDriver/chromedriver.exe",options=options) # open google chrome webdriver
    driver.get(URL) #get to the url
    time.sleep(1)
    src = driver.page_source #get the page source
    soup = BeautifulSoup(src, 'html.parser')
    # try to find the information on page source
    fullname = soup.find("h1")
    bio = soup.find_all("div", class_ = "break-words")
    address = soup.find("div", class_ = "top-card__subline-item")
    experience = soup("span", class_ = "top-card-link__description")
    education = soup("span", class_ = "top-card-link__description")
    # add the information we found into dict
    # Fullname
    try:
        data['fullName'].append({
                                    'sitename': 'LinkedIn', 
                                    'url' : URL,
                                    'data': fullname.text.strip(),
                                    'tag' : 'social network'
                                })
    except:
        pass
    # Address
    try:
        data['address'].append({
                                    'sitename': 'LinkedIn', 
                                    'url' : URL,
                                    'data': address.text.strip(),
                                    'tag' : 'social network'
                                })
    except:
        pass
    # Workplace
    try:
        data['workPlace'].append({
                                    'sitename': 'LinkedIn', 
                                    'url' : URL,
                                    'data': experience[0].text.strip(),
                                    'tag' : 'social network'
                                })
    except:
        pass
    # Education
    try:
        data['education'].append({
                                    'sitename': 'LinkedIn', 
                                    'url' : URL,
                                    'data': education[1].text.strip(),
                                    'tag' : 'social network'
                                })
    except:
        pass
    # profile picture
    try:
        pic = []
        for link in soup.find_all('img',attrs={'data-delayed-url': re.compile("^https://media.licdn.com")}):
    
            pic.append(link.get('data-delayed-url'))  

        data['picture'].append({
                                    'sitename': 'LinkedIn', 
                                    'url' : URL,
                                    'data': pic[0],
                                    'tag' : 'social network'
                                })
    except:
        pass
    return data
