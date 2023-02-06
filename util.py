from googleScrape import googleScrape
from fbscrape import fbScrape
from maigret import maigrets
from infoga import infoga
import re
from pprint import pprint
import math
from image import images    
from Googlelens2 import *
from riskEval import calculateRisk
import shutil


def main(x:str)->list:
    # google 
    isExist = os.path.exists('reports')
    if not isExist:
        os.mkdir('reports')
    
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
        usernames.append(x.replace(" ",""))

    usernames = removeSymbol(usernames) #remove symbol from username
    usernames = list(dict.fromkeys(usernames)) #remove duplicate
    #maigrete
    outMaigrate,listOfWeb = maigrets(usernames) 
    # merge all the result together
    output = merge(outputfb,outputG)
    finalOut = merge(output,outMaigrate)

    # check if email are breach?
    finalOut['email'] = infoga(finalOut['email'])
    # mask contact information
    finalOut['email'] = maskData(finalOut['email'])
    finalOut['phoneNumber'] = maskData(finalOut['phoneNumber'])
    finalOut['ID']= maskData(finalOut['ID'])
    pprint(finalOut)
    pprint(listOfWeb)
    images(finalOut['picture'])  #load images 
    revImages(finalOut['picture']) #do reverse image 
    riskLevel = calculateRisk(finalOut)
    print(riskLevel)
    shutil.rmtree("reports")

    return finalOut,listOfWeb,usernames[0],x,riskLevel


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
#  'ID': [],
#  'address': [{'data': '',
#               'tag': 'social network',
#               'url': 'https://www.facebook.com/fubuki.tang/about'}],
#  'education': [],
#  'email': [{'data': 'kantaponsrigadphach@gmail.com',
#             'tag': 'social network',
#             'url': 'https://www.ict.mahidol.ac.th/'}],
#  'fName': [],
#  'familyMember': [],
#  'fullName': [{'data': '',
#                'tag': 'social network',
#                'url': 'https://www.facebook.com/fubuki.tang/about'},
#               {'data': 'Kantapon Srigadphach',
#                'sitename': 'GitHub',
#                'tag': 'coding',
#                'url': 'https://github.com/Tangkantapon'},
#               {'data': 'tangkantapon',
#                'sitename': 'Twitch',
#                'tag': 'streaming',
#                'url': 'https://www.twitch.tv/Tangkantapon'}],
#  'gender': [{'data': '',
#              'tag': 'social network',
#              'url': 'https://www.facebook.com/fubuki.tang/about'}],
#  'lName': [],
#  'name': [],
#  'occupation': [],
#  'phoneNumber': [],
#  'picture': [{'data': 'https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/290501684_5219335674825610_671348912778975975_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=104&ccb=1-7&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=4TgaNVBJHsIAX9BDE4c&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfAS0G6utvxTTlCYKcGtjxTGSk0DuPwArCSimopMbQ_NLw&oe=63E5AB28&manual_redirect=1',
#               'tag': 'social network',
#               'url': 'https://www.facebook.com/fubuki.tang/about'},
#              {'data': 'https://avatars.githubusercontent.com/u/51602945?v=4',
#               'sitename': 'GitHub',
#               'tag': 'coding',
#               'url': 'https://github.com/Tangkantapon'},
#              {'data': 'https://static-cdn.jtvnw.net/user-default-pictures-uv/ebe4cd89-b4f4-4cd9-adac-2f30151b4209-profile_image-150x150.png',
#               'sitename': 'Twitch',
#               'tag': 'streaming',
#               'url': 'https://www.twitch.tv/Tangkantapon'},
#              {'data': 'flex: 0 0 '
#                       '80px;https://cuad.ask.fm/assets2/154/971/066/880/normal/avatar.jpg',
#               'sitename': 'AskFM',
#               'tag': 'eg',
#               'url': 'https://ask.fm/Tangkantapon'}],
#  'relationship': [{'data': '',
#                    'tag': 'social network',
#                    'url': 'https://www.facebook.com/fubuki.tang/about'}],
#  'username': [{'data': '',
#                'tag': 'social network',
#                'url': 'https://www.facebook.com/fubuki.tang/about'},
#               {'data': 'tangkantapon',
#                'sitename': 'Twitch',
#                'tag': 'streaming',
#                'url': 'https://www.twitch.tv/Tangkantapon'}],
#  'workPlace': []}


#     y = [{'img': 'Twitch.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'Twitch',
#   'url': ['https://www.twitch.tv/Tangkantapon']},
#  {'img': 'GitHub.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'GitHub',
#   'url': ['https://github.com/Tangkantapon']},
#  {'img': 'Tumblr.png',
#   'name': ['@tangktp'],
#   'sitename': 'Tumblr',
#   'url': ['https://tangktp.tumblr.com/']},
#  {'img': 'Pinterest.png',
#   'name': ['@tangktp', '@Tangkantapon'],
#   'sitename': 'Pinterest',
#   'url': ['https://www.pinterest.com/tangktp/',
#           'https://www.pinterest.com/Tangkantapon/']},
#  {'img': 'K.png',
#   'name': ['@tangktp'],
#   'sitename': 'Kaggle',
#   'url': ['https://www.kaggle.com/tangktp']},
#  {'img': 'S.png',
#   'name': ['@tangktp'],
#   'sitename': 'Strava',
#   'url': ['https://www.strava.com/athletes/tangktp']},
#  {'img': 'P.png',
#   'name': ['@tangktp', '@Tangkantapon'],
#   'sitename': 'Picuki',
#   'url': ['https://www.picuki.com/profile/tangktp',
#           'https://www.picuki.com/profile/Tangkantapon']},
#  {'img': 'P.png',
#   'name': ['@tangktp', '@Tangkantapon'],
#   'sitename': 'Pixwox',
#   'url': ['https://www.pixwox.com/profile/tangktp/',
#           'https://www.pixwox.com/profile/Tangkantapon/']},
#  {'img': 'D.png',
#   'name': ['@tangktp', '@Tangkantapon'],
#   'sitename': 'DonationsAlerts',
#   'url': ['https://www.donationalerts.com/r/tangktp',
#           'https://www.donationalerts.com/r/Tangkantapon']},
#  {'img': 'G.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'GitHubGist',
#   'url': ['https://gist.github.com/Tangkantapon']},
#  {'img': 'N.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'Nitter',
#   'url': ['https://nitter.net/Tangkantapon']},
#  {'img': 'R.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'Roblox',
#   'url': ['https://www.roblox.com/user.aspx?username=Tangkantapon']},
#  {'img': 'g.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'giphy.com',
#   'url': ['https://giphy.com/channel/Tangkantapon']},
#  {'img': 'A.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'Academia.edu',
#   'url': ['https://independent.academia.edu/Tangkantapon']},
#  {'img': 'V.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'VSCO',
#   'url': ['https://vsco.co/Tangkantapon']},
#  {'img': 'A.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'AskFM',
#   'url': ['https://ask.fm/Tangkantapon']},
#  {'img': 'g.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'giters.com',
#   'url': ['https://giters.com/Tangkantapon']},
#  {'img': 'D.png',
#   'name': ['@Tangkantapon'],
#   'sitename': 'Dumpor',
#   'url': ['https://dumpor.com/v/Tangkantapon']}]

#     return x,y,'Tang kantapon','Tang'


# main("Tang kantapon")
