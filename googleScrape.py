from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint
def googleScrape (input:str):
    output = {
        "email" : [],
        "phoneNumber" : [],
        "ID": [],

    }
    src =search(input, tld="com" , num=10, stop=10, pause =2) 
    links = []
    for link in src:
        links.append(link)
        try:
            result = requests.get(link, timeout=5).text
            soup = BeautifulSoup(result,"html.parser")
            email = soup.find_all(text= re.compile('\s[\w\.-]+@[\w\.-]+\.\w{2,4}\s'))
            phoneNumber = soup.find_all(text= re.compile('\s0\d\d[\s-]\d\d\d[\s-]\d\d\d\d\s'))
            iden = soup.find_all(text= re.compile('\s\d[\s-]\d\d\d\d[\s-]\d\d\d\d\d[\s-]\d\d[\s-]\d\s'))
            email = delSymbol(email)
            phoneNumber = delSymbol(phoneNumber)
            iden = delSymbol(iden)
            for i in email:
                if email:
                    match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', i)
                    output["email"].append({
                                    "sitename" :'unknow',
                                    "url" : link,
                                    "data":  str(match.group(0)),
                                    "tag" : "unknow"
                                    }) 
            for i in phoneNumber:
                if phoneNumber:
                    match = re.search(r'0\d\d[\s-]\d\d\d[\s-]\d\d\d\d', i)
                    output["phoneNumber"].append({
                                    "sitename" :'unknow',
                                    "url" : link,
                                    "data":  str(match.group(0)) ,
                                    "tag" : "unknow"
                                    }) 
            for i in iden:
                if iden:
                    match = re.search(r'\d[\s-]\d\d\d\d[\s-]\d\d\d\d\d[\s-]\d\d[\s-]\d', i)
                    output["ID"].append({
                                    "sitename" :'unknow',
                                    "url" : link,
                                    "data":  str(match.group(0)) ,
                                    "tag" : "unknow"
                                    }) 
        except:
            continue
    
    # try to find  facebook id or facebook username
    fbID = fbUsername(links)
    usernames= username(links)
    linkedin = linkedInSearch(input+" linkedin")
    return output,fbID,usernames,linkedin
    
    


def fbUsername (input:list):
    fbID = ""
    flag= False
    for i in input:
        temp = i
        temp =temp.split("/")
        for count,word in enumerate(temp):
            if "facebook" in word :
                flag= True
                fbID = temp[count+1]
        if flag == True:
            break
    return fbID

    
def username (input:list):
    flag= False
    username=""
    for i in input:
        temp = i
        temp =temp.split("/")
        for count,word in enumerate(temp):
            if "instagram" in word:
                flag = True
                username = temp[count+1]
        if flag == True:
            break
    return username


def delSymbol (input:list):

    for count,data in enumerate(input): 
        data = re.sub('\s+', '', data)
        input[count]=data

    return input

def linkedInSearch (input: str) :
    src =search(input, tld="com" , num=10, stop=10, pause =2) 
    links = []
    for i in src:
        links.append(i)

    if links:
        return links[0]
    else :
        return None