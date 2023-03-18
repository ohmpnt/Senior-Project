import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import os
from pprint import pprint
def search_linkedin(URL:str):
    print(URL)
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
    # try:
    curPath = os.getcwd()
    driver = webdriver.Chrome(f"{curPath}/ggDriver/chromedriver.exe")
    driver.get(URL)
    time.sleep(1)
    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')
    fullname = soup.find("h1")
    bio = soup.find_all("div", class_ = "break-words")
    address = soup.find("div", class_ = "top-card__subline-item")
    experience = soup("span", class_ = "top-card-link__description")
    education = soup("span", class_ = "top-card-link__description")

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
    
    # except:
    #     return data
    # print("Full-name: " + fullname.text.strip())
    # for text in bio:
    #     print("Bio: " + text.get_text().strip())
    #     break
    # print("Address: " + address.text.strip())
    # print("Experience: " + experience[0].text.strip())
    # print("Education: " + education[1].text.strip())
    # print(soup.prettify())

    # print('linked in')
    # pprint(data)
    return data

# search_linkedin('https://th.linkedin.com/in/kantapon-srigadphach-1498b0204')