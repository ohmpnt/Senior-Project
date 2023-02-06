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


def test():
    x = {'DOB': [],
 'ID': [],
 'address': [{'data': '',
              'tag': 'social network',
              'url': 'https://www.facebook.com/fubuki.tang/about'}],
 'education': [],
 'email': [{'data': 'kantaponsrigadphach@gmail.com',
            'tag': 'social network',
            'url': 'https://www.ict.mahidol.ac.th/'}],
 'fName': [],
 'familyMember': [],
 'fullName': [{'data': '',
               'tag': 'social network',
               'url': 'https://www.facebook.com/fubuki.tang/about'},
              {'data': 'tangkantapon',
               'sitename': 'Twitch',
               'tag': 'streaming',
               'url': 'https://www.twitch.tv/Tangkantapon'},
              {'data': 'Kantapon Srigadphach',
               'sitename': 'GitHub',
               'tag': 'coding',
               'url': 'https://github.com/Tangkantapon'}],
 'gender': [{'data': '',
             'tag': 'social network',
             'url': 'https://www.facebook.com/fubuki.tang/about'}],
 'lName': [],
 'name': [],
 'occupation': [],
 'phoneNumber': [],
 'picture': [{'data': 'https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/290501684_5219335674825610_671348912778975975_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=104&ccb=1-7&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=wwQbyMhXm9QAX8ePY_W&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfCq0r-N4aV5ckhtVVoxq3LZOFFOGs6h_xfe0KkpaTEamg&oe=63DDC228&manual_redirect=1',
              'tag': 'social network',
              'url': 'https://www.facebook.com/fubuki.tang/about'},
             {'data': 'https://static-cdn.jtvnw.net/user-default-pictures-uv/ebe4cd89-b4f4-4cd9-adac-2f30151b4209-profile_image-150x150.png',
              'sitename': 'Twitch',
              'tag': 'streaming',
              'url': 'https://www.twitch.tv/Tangkantapon'},
             {'data': 'https://avatars.githubusercontent.com/u/51602945?v=4',
              'sitename': 'GitHub',
              'tag': 'coding',
              'url': 'https://github.com/Tangkantapon'},
             {'data': 'flex: 0 0 '
                      '80px;https://cuad.ask.fm/assets2/154/971/066/880/normal/avatar.jpg',
              'sitename': 'AskFM',
              'tag': 'eg',
              'url': 'https://ask.fm/Tangkantapon'}],
 'relationship': [{'data': '',
                   'tag': 'social network',
                   'url': 'https://www.facebook.com/fubuki.tang/about'}],
 'username': [{'data': '',
               'tag': 'social network',
               'url': 'https://www.facebook.com/fubuki.tang/about'},
              {'data': 'tangkantapon',
               'sitename': 'Twitch',
               'tag': 'streaming',
               'url': 'https://www.twitch.tv/Tangkantapon'}],
 'workPlace': []}


    y = [{'img': 'Youtube_grey.png', 'sitename': 'Youtube', 'url': ''},
 {'img': 'Facebook_grey.png', 'sitename': 'Facebook', 'url': ''},
 {'img': 'Amazon_grey.png', 'sitename': 'Amazon', 'url': ''},
 {'img': 'Reddit_grey.png', 'sitename': 'Reddit', 'url': ''},
 {'img': 'VK_grey.png', 'sitename': 'VK', 'url': ''},
 {'img': 'Instagram_grey.png', 'sitename': 'Instagram', 'url': ''},
 {'img': 'Twitch_grey.png', 'sitename': 'Twitch', 'url': ''},
 {'img': 'Ebay_grey.png', 'sitename': 'Ebay', 'url': ''},
 {'img': 'Twitter_grey.png', 'sitename': 'Twitter', 'url': ''},
 {'img': 'Wordpress_grey.png', 'sitename': 'Wordpress', 'url': ''},
 {'img': 'Pornhub_grey.png', 'sitename': 'Pornhub', 'url': ''},
 {'img': 'Github_grey.png', 'sitename': 'Github', 'url': ''},
 {'img': 'Spotify_grey.png', 'sitename': 'Spotify', 'url': ''},
 {'img': 'Tiktok_grey.png', 'sitename': 'Tiktok', 'url': ''},
 {'img': 'Xvideos_grey.png', 'sitename': 'Xvideos', 'url': ''},
 {'img': 'Tumblr.png',
  'sitename': 'Tumblr',
  'url': 'https://tangktp.tumblr.com/'},
 {'img': 'Pinterest.png',
  'sitename': 'Pinterest',
  'url': 'https://www.pinterest.com/tangktp/'},
 {'img': 'Patreon_grey.png', 'sitename': 'Patreon', 'url': ''},
 {'img': 'K.png',
  'sitename': 'Kaggle',
  'url': 'https://www.kaggle.com/tangktp'},
 {'img': 'P.png',
  'sitename': 'Picuki',
  'url': 'https://www.picuki.com/profile/tangktp'},
 {'img': 'S.png',
  'sitename': 'Strava',
  'url': 'https://www.strava.com/athletes/tangktp'},
 {'img': 'F.png', 'sitename': 'F6S', 'url': 'https://www.f6s.com/tangktp'},
 {'img': 'P.png',
  'sitename': 'Pixwox',
  'url': 'https://www.pixwox.com/profile/tangktp/'},
 {'img': 'T.png',
  'sitename': 'TJournal',
  'url': 'https://tjournal.ru/search/v2/subsite/relevant?query=tangktp'},
 {'img': 'D.png',
  'sitename': 'DonationsAlerts',
  'url': 'https://www.donationalerts.com/r/tangktp'},
 {'img': 'Youtube_grey.png', 'sitename': 'Youtube', 'url': ''},
 {'img': 'Facebook_grey.png', 'sitename': 'Facebook', 'url': ''},
 {'img': 'Amazon_grey.png', 'sitename': 'Amazon', 'url': ''},
 {'img': 'Reddit_grey.png', 'sitename': 'Reddit', 'url': ''},
 {'img': 'VK_grey.png', 'sitename': 'VK', 'url': ''},
 {'img': 'Instagram_grey.png', 'sitename': 'Instagram', 'url': ''},
 {'img': 'Twitch.png',
  'sitename': 'Twitch',
  'url': 'https://www.twitch.tv/Tangkantapon'},
 {'img': 'Ebay_grey.png', 'sitename': 'Ebay', 'url': ''},
 {'img': 'Twitter_grey.png', 'sitename': 'Twitter', 'url': ''},
 {'img': 'Wordpress_grey.png', 'sitename': 'Wordpress', 'url': ''},
 {'img': 'Pornhub_grey.png', 'sitename': 'Pornhub', 'url': ''},
 {'img': 'Github_grey.png', 'sitename': 'Github', 'url': ''},
 {'img': 'Spotify_grey.png', 'sitename': 'Spotify', 'url': ''},
 {'img': 'Tiktok_grey.png', 'sitename': 'Tiktok', 'url': ''},
 {'img': 'Xvideos_grey.png', 'sitename': 'Xvideos', 'url': ''},
 {'img': 'Tumblr_grey.png', 'sitename': 'Tumblr', 'url': ''},
 {'img': 'Pinterest.png',
  'sitename': 'Pinterest',
  'url': 'https://www.pinterest.com/Tangkantapon/'},
 {'img': 'Patreon_grey.png', 'sitename': 'Patreon', 'url': ''},
 {'img': 'G.png',
  'sitename': 'GitHubGist',
  'url': 'https://gist.github.com/Tangkantapon'},
 {'img': 'G.png',
  'sitename': 'GitHub',
  'url': 'https://github.com/Tangkantapon'},
 {'img': 'N.png',
  'sitename': 'Nitter',
  'url': 'https://nitter.net/Tangkantapon'},
 {'img': 'g.png',
  'sitename': 'giphy.com',
  'url': 'https://giphy.com/channel/Tangkantapon'},
 {'img': 'R.png',
  'sitename': 'Roblox',
  'url': 'https://www.roblox.com/user.aspx?username=Tangkantapon'},
 {'img': 'P.png',
  'sitename': 'Picuki',
  'url': 'https://www.picuki.com/profile/Tangkantapon'},
 {'img': 'A.png',
  'sitename': 'Academia.edu',
  'url': 'https://independent.academia.edu/Tangkantapon'},
 {'img': 'S.png',
  'sitename': 'Strava',
  'url': 'https://www.strava.com/athletes/Tangkantapon'},
 {'img': 'F.png', 'sitename': 'F6S', 'url': 'https://www.f6s.com/Tangkantapon'},
 {'img': 'T.png',
  'sitename': 'TJournal',
  'url': 'https://tjournal.ru/search/v2/subsite/relevant?query=Tangkantapon'},
 {'img': 'P.png',
  'sitename': 'Pixwox',
  'url': 'https://www.pixwox.com/profile/Tangkantapon/'},
 {'img': 'A.png', 'sitename': 'AskFM', 'url': 'https://ask.fm/Tangkantapon'},
 {'img': 'g.png',
  'sitename': 'giters.com',
  'url': 'https://giters.com/Tangkantapon'},
 {'img': 'D.png',
  'sitename': 'DonationsAlerts',
  'url': 'https://www.donationalerts.com/r/Tangkantapon'},
 {'img': 'D.png',
  'sitename': 'Dumpor',
  'url': 'https://dumpor.com/v/Tangkantapon'},
 {'img': 'T.png',
  'sitename': 'TRASHBOX.RU',
  'url': 'https://trashbox.ru/users/Tangkantapon'}]

    return x,y,'Tang kantapon','Tang'


# main("Tang kantapon")
