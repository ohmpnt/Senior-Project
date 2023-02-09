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
import shutil
import os

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
    images(finalOut['picture'])
      #load images 
    revLink = revImages(finalOut['picture']) #do reverse image 

    # revImages(finalOut['picture']) #do reverse image 
    riskLevel,suggestion = calculateRisk(finalOut)
    pprint(suggestion)
    shutil.rmtree("reports")

    return finalOut,listOfWeb,usernames[0],x,riskLevel,revLink,suggestion


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

# def listTag(input:dict) :
#     data = []
#     for key,value in dict.items(input):
#         if value != []:
#             data.append(key)
#     useTag = ['gaming', 'music', 'art', 'dating', 'movies', 'hobby', 'sport','forum','porn','social network','coding', 'news', 'blog', 'shopping', 'stock','education','career','trading', 'photo', 'finance','business','medicine','streaming']
#     tag = []
#     for  i in input :
#         temp = input[i]
#         for j in temp :
#             if j['tag'] in useTag:
#                 tag.append(j['tag'])

#     tag = list(dict.fromkeys(tag))

#     return data,tag


def test():
    x={'DOB': [],
 'ID': [],
 'address': [{'data': '',
              'sitename': 'facebook',
              'tag': 'social network',
              'url': 'https://www.facebook.com/fubuki.tang/about'}],
 'education': [],
 'email': [],
 'fName': [],
 'familyMember': [],
 'fullName': [{'data': '',
               'sitename': 'facebook',
               'tag': 'social network',
               'url': 'https://www.facebook.com/fubuki.tang/about'},
              {'data': 'tangkantapon',
               'sitename': 'Twitch',
               'tag': 'streaming',
               'url': 'https://www.twitch.tv/tangkantapon'},
              {'data': 'Kantapon Srigadphach',
               'sitename': 'GitHub',
               'tag': 'coding',
               'url': 'https://github.com/tangkantapon'}],
 'gender': [{'data': '',
             'sitename': 'facebook',
             'tag': 'social network',
             'url': 'https://www.facebook.com/fubuki.tang/about'}],
 'lName': [],
 'name': [],
 'occupation': [],
 'phoneNumber': [],
 'picture': [{'data': 'https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/290501684_5219335674825610_671348912778975975_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=104&ccb=1-7&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=DQVM3C4CUaIAX_gsdS1&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfAsd0d4H_tQUe6iK9DQyhrcvxad7RuK9VCF-FURv608OQ&oe=63E99FA8&manual_redirect=1',
              'sitename': 'facebook',
              'tag': 'social network',
              'url': 'https://www.facebook.com/fubuki.tang/about'},
             {'data': 'https://static-cdn.jtvnw.net/user-default-pictures-uv/ebe4cd89-b4f4-4cd9-adac-2f30151b4209-profile_image-150x150.png',
              'sitename': 'Twitch',
              'tag': 'streaming',
              'url': 'https://www.twitch.tv/tangkantapon'},
             {'data': 'https://avatars.githubusercontent.com/u/51602945?v=4',
              'sitename': 'GitHub',
              'tag': 'coding',
              'url': 'https://github.com/tangkantapon'},
             {'data': 'flex: 0 0 '
                      '80px;https://cuad.ask.fm/assets2/154/971/066/880/normal/avatar.jpg',
              'sitename': 'AskFM',
              'tag': 'eg',
              'url': 'https://ask.fm/tangkantapon'}],
 'relationship': [{'data': '',
                   'sitename': 'facebook',
                   'tag': 'social network',
                   'url': 'https://www.facebook.com/fubuki.tang/about'}],
 'username': [{'data': '',
               'sitename': 'facebook',
               'tag': 'social network',
               'url': 'https://www.facebook.com/fubuki.tang/about'},
              {'data': 'tangkantapon',
               'sitename': 'Twitch',
               'tag': 'streaming',
               'url': 'https://www.twitch.tv/tangkantapon'}],
 'workPlace': []}
    y=[{'img': 'GitHub.png',
  'name': ['tangkantapon'],
  'sitename': 'GitHub',
  'url': ['https://github.com/tangkantapon']},
 {'img': 'Twitch.png',
  'name': ['tangkantapon'],
  'sitename': 'Twitch',
  'url': ['https://www.twitch.tv/tangkantapon']},
 {'img': 'Tumblr.png',
  'name': ['tangktp'],
  'sitename': 'Tumblr',
  'url': ['https://tangktp.tumblr.com/']},
 {'img': 'Pinterest.png',
  'name': ['tangktp', 'tangkantapon'],
  'sitename': 'Pinterest',
  'url': ['https://www.pinterest.com/tangktp/',
          'https://www.pinterest.com/tangkantapon/']},
 {'img': 'K.png',
  'name': ['tangktp'],
  'sitename': 'Kaggle',
  'url': ['https://www.kaggle.com/tangktp']},
 {'img': 'P.png',
  'name': ['tangktp', 'tangkantapon'],
  'sitename': 'Picuki',
  'url': ['https://www.picuki.com/profile/tangktp',
          'https://www.picuki.com/profile/tangkantapon']},
 {'img': 'S.png',
  'name': ['tangktp', 'tangkantapon'],
  'sitename': 'Strava',
  'url': ['https://www.strava.com/athletes/tangktp',
          'https://www.strava.com/athletes/tangkantapon']},
 {'img': 'T.png',
  'name': ['tangktp', 'tangkantapon'],
  'sitename': 'TJournal',
  'url': ['https://tjournal.ru/search/v2/subsite/relevant?query=tangktp',
          'https://tjournal.ru/search/v2/subsite/relevant?query=tangkantapon']},
 {'img': 'D.png',
  'name': ['tangktp', 'tangkantapon'],
  'sitename': 'Dumpor',
  'url': ['https://dumpor.com/v/tangktp', 'https://dumpor.com/v/tangkantapon']},
 {'img': 'D.png',
  'name': ['tangktp', 'tangkantapon'],
  'sitename': 'DonationsAlerts',
  'url': ['https://www.donationalerts.com/r/tangktp',
          'https://www.donationalerts.com/r/tangkantapon']},
 {'img': 'G.png',
  'name': ['tangkantapon'],
  'sitename': 'GitHubGist',
  'url': ['https://gist.github.com/tangkantapon']},
 {'img': 'N.png',
  'name': ['tangkantapon'],
  'sitename': 'Nitter',
  'url': ['https://nitter.net/tangkantapon']},
 {'img': 'R.png',
  'name': ['tangkantapon'],
  'sitename': 'Roblox',
  'url': ['https://www.roblox.com/user.aspx?username=tangkantapon']},
 {'img': 'g.png',
  'name': ['tangkantapon'],
  'sitename': 'giphy.com',
  'url': ['https://giphy.com/channel/tangkantapon']},
 {'img': 'A.png',
  'name': ['tangkantapon'],
  'sitename': 'Academia.edu',
  'url': ['https://independent.academia.edu/tangkantapon']},
 {'img': 'A.png',
  'name': ['tangkantapon'],
  'sitename': 'AskFM',
  'url': ['https://ask.fm/tangkantapon']},
 {'img': 'V.png',
  'name': ['tangkantapon'],
  'sitename': 'VSCO',
  'url': ['https://vsco.co/tangkantapon']},
 {'img': 'g.png',
  'name': ['tangkantapon'],
  'sitename': 'giters.com',
  'url': ['https://giters.com/tangkantapon']}]

    sug = [['photo',
  'GitHub',
  ['● Observe on your account and may consider changing the privacy settings',
   '● Be careful when uploading a photo in unreliable sources'],
  'https://github.com/Tangkantapon'],
 ['address',
  'Facebook',
  ['● Observe on your account and may consider changing the privacy settings',
   '● Be careful when filling in address information in unreliable sources'],
  'https://www.facebook.com/fubuki.tang/about'],
 ['full name',
  'GitHub',
  ['● Observe on your account and may consider changing the privacy settings',
   '● Be careful when filling in full name information in unreliable sources'],
  'https://github.com/Tangkantapon'],
 ['photo',
  'Facebook',
  ['● Observe on your account and may consider changing the privacy settings',
   '● Be careful when uploading a photo in unreliable sources'],
  'https://www.facebook.com/fubuki.tang/about'],
 ['photo',
  'Twitch',
  ['● Observe on your account and may consider changing the privacy settings',
   '● Be careful when uploading a photo in unreliable sources'],
  'https://www.twitch.tv/Tangkantapon']]
    revLink = [['https://lens.google.com/uploadbyurl?url=https%3A%2F%2Fscontent.fbkk28-1.fna.fbcdn.net%2Fv%2Ft39.30808-6%2F290501684_5219335674825610_671348912778975975_n.jpg%3Fstp%3Dcp0_dst-jpg_e15_fr_q65%26_nc_cat%3D104%26ccb%3D1-7%26_nc_sid%3D85a577%26efg%3DeyJpIjoidCJ9%26_nc_ohc%3DDQVM3C4CUaIAX_gsdS1%26_nc_ht%3Dscontent.fbkk28-1.fna%26oh%3D00_AfAsd0d4H_tQUe6iK9DQyhrcvxad7RuK9VCF-FURv608OQ%26oe%3D63E99FA8%26manual_redirect%3D1', 
                'https://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=https%3A%2F%2Fscontent.fbkk28-1.fna.fbcdn.net%2Fv%2Ft39.30808-6%2F290501684_5219335674825610_671348912778975975_n.jpg%3Fstp%3Dcp0_dst-jpg_e15_fr_q65%26_nc_cat%3D104%26ccb%3D1-7%26_nc_sid%3D85a577%26efg%3DeyJpIjoidCJ9%26_nc_ohc%3DDQVM3C4CUaIAX_gsdS1%26_nc_ht%3Dscontent.fbkk28-1.fna%26oh%3D00_AfAsd0d4H_tQUe6iK9DQyhrcvxad7RuK9VCF-FURv608OQ%26oe%3D63E99FA8%26manual_redirect%3D1', 
                'https://yandex.com/images/search?source=collections&&url=https%3A%2F%2Fscontent.fbkk28-1.fna.fbcdn.net%2Fv%2Ft39.30808-6%2F290501684_5219335674825610_671348912778975975_n.jpg%3Fstp%3Dcp0_dst-jpg_e15_fr_q65%26_nc_cat%3D104%26ccb%3D1-7%26_nc_sid%3D85a577%26efg%3DeyJpIjoidCJ9%26_nc_ohc%3DDQVM3C4CUaIAX_gsdS1%26_nc_ht%3Dscontent.fbkk28-1.fna%26oh%3D00_AfAsd0d4H_tQUe6iK9DQyhrcvxad7RuK9VCF-FURv608OQ%26oe%3D63E99FA8%26manual_redirect%3D1&rpt=imageview', 
                'https://www.tineye.com/search/?&url=https%3A%2F%2Fscontent.fbkk28-1.fna.fbcdn.net%2Fv%2Ft39.30808-6%2F290501684_5219335674825610_671348912778975975_n.jpg%3Fstp%3Dcp0_dst-jpg_e15_fr_q65%26_nc_cat%3D104%26ccb%3D1-7%26_nc_sid%3D85a577%26efg%3DeyJpIjoidCJ9%26_nc_ohc%3DDQVM3C4CUaIAX_gsdS1%26_nc_ht%3Dscontent.fbkk28-1.fna%26oh%3D00_AfAsd0d4H_tQUe6iK9DQyhrcvxad7RuK9VCF-FURv608OQ%26oe%3D63E99FA8%26manual_redirect%3D1'], 
                ['https://lens.google.com/uploadbyurl?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F51602945%3Fv%3D4', 
                'https://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F51602945%3Fv%3D4', 
                'https://yandex.com/images/search?source=collections&&url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F51602945%3Fv%3D4&rpt=imageview', 
                'https://www.tineye.com/search/?&url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F51602945%3Fv%3D4'], 
                ['https://lens.google.com/uploadbyurl?url=https%3A%2F%2Fstatic-cdn.jtvnw.net%2Fuser-default-pictures-uv%2Febe4cd89-b4f4-4cd9-adac-2f30151b4209-profile_image-150x150.png', 
                'https://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=https%3A%2F%2Fstatic-cdn.jtvnw.net%2Fuser-default-pictures-uv%2Febe4cd89-b4f4-4cd9-adac-2f30151b4209-profile_image-150x150.png', 
                'https://yandex.com/images/search?source=collections&&url=https%3A%2F%2Fstatic-cdn.jtvnw.net%2Fuser-default-pictures-uv%2Febe4cd89-b4f4-4cd9-adac-2f30151b4209-profile_image-150x150.png&rpt=imageview', 
                'https://www.tineye.com/search/?&url=https%3A%2F%2Fstatic-cdn.jtvnw.net%2Fuser-default-pictures-uv%2Febe4cd89-b4f4-4cd9-adac-2f30151b4209-profile_image-150x150.png'], 
                ['https://lens.google.com/uploadbyurl?url=https%3A%2F%2Fcuad.ask.fm%2Fassets2%2F154%2F971%2F066%2F880%2Fnormal%2Favatar.jpg', 
                'https://www.bing.com/images/searchbyimage?FORM=IRSBIQ&cbir=sbi&imgurl=https%3A%2F%2Fcuad.ask.fm%2Fassets2%2F154%2F971%2F066%2F880%2Fnormal%2Favatar.jpg', 
                'https://yandex.com/images/search?source=collections&&url=https%3A%2F%2Fcuad.ask.fm%2Fassets2%2F154%2F971%2F066%2F880%2Fnormal%2Favatar.jpg&rpt=imageview', 
                'https://www.tineye.com/search/?&url=https%3A%2F%2Fcuad.ask.fm%2Fassets2%2F154%2F971%2F066%2F880%2Fnormal%2Favatar.jpg']]

    return x,y,'Tang kantapon','Tang',1,revLink,sug


# main("Tang kantapon")
