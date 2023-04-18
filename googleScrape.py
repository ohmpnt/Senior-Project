from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint

def googleScrape (input:str):
    #all the information we try to find
    output = {
        "email" : [],
        "phoneNumber" : [],
        "ID": [],

    }
    src =search(input, tld="com" , num=10, stop=10, pause =2) # call the google search tool get the result as generator
    links = []
    #loop throgh each link we found
    for link in src:
        links.append(link)
        try:
            result = requests.get(link, timeout=5).text #request source of the page
            soup = BeautifulSoup(result,"html.parser")
            #use regrex to check pattern information (email,identification number,phone number)
            email = soup.find_all(text= re.compile('\s[\w\.-]+@[\w\.-]+\.\w{2,4}\s'))
            phoneNumber = soup.find_all(text= re.compile('\s0\d\d[\s-]\d\d\d[\s-]\d\d\d\d\s'))
            iden = soup.find_all(text= re.compile('\s\d[\s-]\d\d\d\d[\s-]\d\d\d\d\d[\s-]\d\d[\s-]\d\s'))
            #delete symbol in data we found
            email = delSymbol(email) 
            phoneNumber = delSymbol(phoneNumber)
            iden = delSymbol(iden)

            #loop through each data we found and add to output as json format
            for i in email:
                if email:
                    match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', i) #check again
                    output["email"].append({
                                    "sitename" :'unknow',
                                    "url" : link,
                                    "data":  str(match.group(0)),
                                    "tag" : "unknow"
                                    }) 
            for i in phoneNumber:
                if phoneNumber:
                    match = re.search(r'0\d\d[\s-]\d\d\d[\s-]\d\d\d\d', i) #check again
                    output["phoneNumber"].append({
                                    "sitename" :'unknow',
                                    "url" : link,
                                    "data":  str(match.group(0)) ,
                                    "tag" : "unknow"
                                    }) 
            for i in iden:
                if iden:
                    match = re.search(r'\d[\s-]\d\d\d\d[\s-]\d\d\d\d\d[\s-]\d\d[\s-]\d', i) #check again
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
    #try to find username
    usernames= username(links)
    # try to find linkedin link
    linkedin = linkedInSearch(input+" linkedin")
    return output,fbID,usernames,linkedin
    
    

#find facebook id
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

#find posible username
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

#delete the symbol
def delSymbol (input:list):

    for count,data in enumerate(input): 
        data = re.sub('\s+', '', data)
        input[count]=data

    return input
#find linkedin account profile page link
def linkedInSearch (input: str) :
    src =search(input, tld="com" , num=10, stop=10, pause =2) 
    links = []
    for i in src:
        links.append(i)

    if links:
        return links[0]
    else :
        return None
    

