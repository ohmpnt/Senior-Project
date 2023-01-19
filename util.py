from googleScrape import googleScrape
from fbscrape import fbScrape
from maigret import maigret
from infoga import infoga
import re
from pprint import pprint
import math
from image import images    




def main(x:str)->list:
    # google 
    usernames = []
    outputG,fbU,username =googleScrape(x)  
    if username != "":
        usernames.append(username)

    if fbU == "":
        fbU = x.replace(" ",".")

    #facebook    
    outputfb,username=fbScrape(fbU)
    
    if  username == "":
        username =  x.replace(" ","")
        usernames.append(username)
    else:
        usernames.append(username)

    usernames = removeSymbol(usernames) #remove symbol from username

    #maigrete
    outMaigrate,listOfWeb = maigret(usernames[0]) 
    # merge all the result together
    output = merge(outputfb,outputG)
    finalOut = merge(output,outMaigrate)

    # check if email are breach?
    finalOut['email'] = infoga(finalOut['email'])
    # mask contact information
    finalOut['email'] = maskData(finalOut['email'])
    finalOut['phoneNumber'] = maskData(finalOut['phoneNumber'])
    finalOut['ID']= maskData(finalOut['ID'])
    images(finalOut['picture'])
    pprint(finalOut)
    return finalOut,listOfWeb,username


def merge (dict_1:dict, dict_2:dict):
    for key, value in dict_2.items():
        if key in dict_1:
            if value:
                for i in value:
                    dict_1[key].append(i)  
        else:
            dict_1[key] = value

    return dict_1


def maskData (input:list) :
    for count,word in enumerate(input):
        temp = word['data']
        if '@' in temp :
            s = temp.split('@')
            lens = len(s[0])
            maskNum = math.floor(lens/2)
            temp = temp.replace(temp[0:maskNum],'*'*maskNum,1)
            word['data']=temp
            input[count] = word    
        else:
            lens = len(temp)
            maskNum = math.ceil(lens/2)
            temp = temp.replace(temp[0:maskNum],'*'*maskNum,1)
            word['data']=temp
            input[count] = word   

    return input

def removeSymbol (input:list):

    for count,i in enumerate(input):
        input[count] = re.sub(r'[^\w]', '', i)

    return input

# main("Kantapon Srigadphach")