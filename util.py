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
    pprint(listOfWeb)
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

# def test():
#     x = {'DOB': [],
#         'ID': [],
#         'address': [{'data': '',
#                     'tag': 'social network',
#                     'url': 'https://www.facebook.com/Songpon.te/about'}],
#         'education': [],
#         'email': [{'data': '*ct@mahidol.ac.th (not breach)',
#                     'tag': 'unknow',
#                     'url': 'https://www.ict.mahidol.ac.th/people/staff-contact/songpon-teerakanok/'}],
#         'fName': [],
#         'familyMember': [],
#         'fullName': [{'data': '',
#                     'tag': 'social network',
#                     'url': 'https://www.facebook.com/Songpon.te/about'}],
#         'gender': [{'data': '',
#                     'tag': 'social network',
#                     'url': 'https://www.facebook.com/Songpon.te/about'}],
#         'lName': [],
#         'name': [],
#         'occupation': [],
#         'phoneNumber': [],
#         'picture': [{'data': 'https://scontent.fbkk22-1.fna.fbcdn.net/v/t39.30808-6/299835346_10222653853429438_238771487539892262_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=100&ccb=1-7&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=CcGPeRZCb-wAX9QzHZz&tn=-DFwpzWxTywRKSgz&_nc_ht=scontent.fbkk22-1.fna&oh=00_AfBApN3rT1-ykUiFiYaehxjal1iVRuq7fW8YgRnoc6dKIg&oe=63D30FE5&manual_redirect=1',
#                     'tag': 'social network',
#                     'url': 'https://www.facebook.com/Songpon.te/about'}],
#         'relationship': [],
#         'username': [],
#         'workPlace': [{'data': '',
#                         'tag': 'social network',
#                         'url': 'https://www.facebook.com/Songpon.te/about'}]}

#     y = [{'sitename': 'SlideShare', 'url': 'https://slideshare.net/songponteerakanok'},
#         {'sitename': 'Pinterest',
#         'url': 'https://www.pinterest.com/songponteerakanok/'},
#         {'sitename': 'Strava',
#         'url': 'https://www.strava.com/athletes/songponteerakanok'},
#         {'sitename': 'F6S', 'url': 'https://www.f6s.com/songponteerakanok'},
#         {'sitename': 'TJournal',
#         'url': 'https://tjournal.ru/search/v2/subsite/relevant?query=songponteerakanok'},
#         {'sitename': 'DonationsAlerts',
#         'url': 'https://www.donationalerts.com/r/songponteerakanok'}]

#     return x,y,'songponteerakanok'

# main("songpon teerakanok")