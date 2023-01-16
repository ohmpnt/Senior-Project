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
    outputG,fbU,username =googleScrape(x)  

    if fbU == "":
        fbU = x.replace(" ",".")

    #facebook    
    outputfb,username=fbScrape(fbU)

    if  username == "":
        username =  x.replace(" ","")
    username=re.sub(r'[^\w]', '', username) #remove symbol from username

    #maigrete
    outMaigrate,listOfWeb = maigret(username) 

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




main('tang kantapon')

# x = [{'data': 'ohmsnow@gmail.com'},{'data':'dasdaSssvbmm@gmail.com'},{'data':'ict@gmail.com'}]
# y = [{'data': '0971515951','lol':'kkasld'},{'data':'0851228378','lol':'kkasld'},{'data':'67123123123','lol':'kkasld'}]
# massData(y)