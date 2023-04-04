from googleScrape import googleScrape
from fbscrape import fbScrape
from maigret import maigrets
from infoga import infoga
import re
from pprint import pprint
import math
from imgChecker import *
from image import images    
from riskEval import calculateRisk
from linkedIn import search_linkedin
import shutil
import os

def main(x:str)->list:
    print(" _    _                _             \n| |  | |              | |            \n| |__| | __ ___      _| | _____ _ __ \n|  __  |/ _` \ \ /\ / / |/ / _ \ '__|\n| |  | | (_| |\ V  V /|   <  __/ |   \n|_|  |_|\__,_| \_/\_/ |_|\_\___|_|   ")
    # check weather the report folder is deleted in case yes make the reports folder
    isExist = os.path.exists('reports')
    if not isExist:
        os.mkdir('reports')
    
    usernames = [] #for keep username to use in maigret module

    # google module
    print("------------------------------------- google search start -------------------------------------")
    outputG,fbU,username,linkInLink =googleScrape(x)  
    print("------------------------------------- google search end   -------------------------------------")
    # add username to list uernames if usernamenot empty
    if username != "":
        usernames.append(username)
    # if not found facebook id account assume that the account is "firstname.lastname"
    if fbU == "":
        fbU = x.replace(" ",".")

    #facebook module
    print("------------------------------------- facebook module start -------------------------------------")
    outputfb,username=fbScrape(fbU)
    print("------------------------------------- facebook module end   -------------------------------------")
    # linkedin module
    print("------------------------------------- linkedin module start -------------------------------------")
    outLinked = search_linkedin(linkInLink)
    print("------------------------------------- linkedin module end   -------------------------------------")

    # "firstname.lastname" add to usernames if not found username in facebook module
    if  username == "":
        username =  x.replace(" ","")
        usernames.append(username)
    else:
        usernames.append(username)
        usernames.append(x.replace(" ",""))

    usernames = removeSymbol(usernames) #remove symbol from usernames
    usernames = list(dict.fromkeys(usernames)) #remove duplicate

    #maigrete module
    print("------------------------------------- Maigret module start -------------------------------------")
    outMaigrate,listOfWeb = maigrets(usernames)
    print("------------------------------------- Maigret module end   -------------------------------------")


    # merge all the result together
    output = merge(outputfb,outputG)
    output = merge(output,outLinked)
    finalOut = merge(output,outMaigrate)
    

    # check if email are breach by Infoga module
    print("------------------------------------- Infoga module start -------------------------------------")
    finalOut['email'] = infoga(finalOut['email'])
    print("------------------------------------- Infoga module end   -------------------------------------")
    # mask all of the contact information
    finalOut['email'] = maskData(finalOut['email'])
    finalOut['phoneNumber'] = maskData(finalOut['phoneNumber'])
    finalOut['ID']= maskData(finalOut['ID'])

    #load images 
    images(finalOut['picture'])

    # imgChecker module
    print("------------------------------------- duplichecker module start -------------------------------------")
    revLink = revImages(finalOut['picture']) 
    print("------------------------------------- duplichecker module end   -------------------------------------")


    # show final output
    print("-------------------------------------  final data   -------------------------------------")
    pprint(finalOut)
    print("------------------------------------- final listweb -------------------------------------")
    pprint(listOfWeb)
    print("------------------------------------- final listweb -------------------------------------")

    

    # revImages(finalOut['picture']) #do reverse image 
    riskLevel,suggestion = calculateRisk(finalOut)

    # remove reports folder(user data)
    shutil.rmtree("reports")

    return finalOut,listOfWeb,usernames[0],x,riskLevel,revLink,suggestion

# merge list in dict
def merge (dict_1:dict, dict_2:dict):
    for key, value in dict_2.items():
        if key in dict_1:
            if value:
                for i in value:
                    dict_1[key].append(i)  
        else:
            dict_1[key] = value

    return dict_1

# mask the data
def maskData (input:list) :
    for count,word in enumerate(input):
        temp = word['data']
        if '@' in temp : # incase of an email we wil mask the half first part of email
            s = temp.split('@')
            lens = len(s[0])
            maskNum = math.floor(lens/2)
            temp = temp.replace(temp[0:maskNum],'*'*maskNum,1)
            word['data']=temp
            input[count] = word    
        else: #any thing else we mask half of it
            lens = len(temp)
            maskNum = math.ceil(lens/2)
            temp = temp.replace(temp[0:maskNum],'*'*maskNum,1)
            word['data']=temp
            input[count] = word   

    return input

# remove all the symbol using regrex
def removeSymbol (input:list):

    for count,i in enumerate(input):
        input[count] = re.sub(r'[^\w]', '', i)

    return input


main("snowy")