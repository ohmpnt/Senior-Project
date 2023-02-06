
import os
import json
from pprint import pprint



def maigrets(input: list):
    newOut = {}
    listWebOut = []
    for i in input:
        temp,listWeb =profileSearch(i)
        newOut = merge(newOut,temp)
        listWebOut= listMerge(listWebOut,listWeb)
    listWebOut = sortIcon(listWebOut)
    listWebOut = removeTrash(listWebOut)
    return newOut,listWebOut

def listMerge (list1:list,list2:list) ->list :
    
    for i in list2:
        if i not in list1:
            list1.append(i)


    return list1

def profileSearch(input:str):

    print(input)
    curPath = os.getcwd()
    os.system(f'python "{curPath}/maigret/maigret.py" {input} --json ndjson --timeout 8 ')

    try : 
        file = open(f'reports/report_{input}_ndjson.json')
        datas = file.readlines()
        output= []
        for data in datas:
            output.append(json.loads(data))
        file.close()
        # pprint(output)
        # print("----------------------------------------------------------------------------------------------------------------------------------------")
        data = pageData(output)
        weblist = listWeb(output)
        return data,weblist
    except :
        print('something worng!')
    



def pageData (input:list):
    target = [
        ["username","username"],
        ["fullname","fullName"],
        ["image", "picture"],
        ["location","address"],
        ["occupation","occupation"],
        ["patreon_username","username"],
        ["flickr_username","username"],
        ["pinterest_username","username"],
        ["reddit_username","username"],
        ["tiktok_username","username"],
        ["disqus_username","username"],
        ["periscope_username","username"],
        ["imgur_username","username"],
        ["tinder_username","username"],
        ["facebook_username","username"],
        ["instagram_username","username"],
        ["telegram_username","username"],
        ["twitter_username","username"],
        ["vk_username","username"],
        ["first_name","fName"],
        ["last_name","lName"],
        ["email","email"],
        ["business_email","email"],
        ["birthday","DOB"],
        ["birthday_at","DOB"],
        ["birth_date","DOB"],
        ["city","address"],
        ["country","address"],
        ["github_username","username"],
        ["reddit_username","username"],
        ["hackernews_username","username"],
        ["phone","phoneNumber"],
        ["education","education"],
        ["college","education"],
        ["name","name"],
        ["nickname","name"]
    ]

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
        "name":  []
    }

    for i in input:
        temp = i
        status = temp['status']
        ids = status['ids']
        tags = status['tags'] 
        for j in target:
            tempj = j
            try:
                data[tempj[1]].append({
                                            'sitename': temp['sitename'], 
                                            'url' : temp['url_user'],
                                            'data': ids[tempj[0]],
                                            'tag' : tags[0]
                                    })
            except KeyError:
                continue
        
    return data



def merge (dict_1:dict, dict_2:dict):
    for key, value in dict_2.items():
        if key in dict_1:
            if value:
                for i in value:
                    dict_1[key].append(i)  
        else:
            dict_1[key] = value

    return dict_1

def listWeb (input):

    showsite = ["Youtube","Facebook","Amazon","Reddit","VK","Instagram","Twitch","Ebay","Twitter","Wordpress","Pornhub","GitHub","Spotify","Tiktok","Xvideos","Tumblr","Pinterest","Patreon"]
    # listOfWeb = [{'sitename' : temp['sitename'], 
    #                     'url' : temp['url_user'],
    #                     "img" : f"{firstLetter}.png"}]
    # listOfWeb=[{'sitename' : "Youtube", 
    #                    'url' : '',
    #                     "img" : "Youtube_grey.png"},
    #             {'sitename' : "Facebook", 
    #                    'url' : '',
    #                     "img" : "Facebook_grey.png"},
    #             {'sitename' : "Amazon", 
    #                    'url' : '',
    #                     "img" : "Amazon_grey.png"},
    #             {'sitename' : "Reddit", 
    #                    'url' : '',
    #                     "img" : "Reddit_grey.png"},
    #             {'sitename' : "VK", 
    #                    'url' : '',
    #                     "img" : "VK_grey.png"},
    #             {'sitename' : "Instagram", 
    #                    'url' : '',
    #                     "img" : "Instagram_grey.png"},
    #             {'sitename' : "Twitch", 
    #                    'url' : '',
    #                     "img" : "Twitch_grey.png"},
    #             {'sitename' : "Ebay", 
    #                    'url' : '',
    #                     "img" : "Ebay_grey.png"},
    #             {'sitename' : "Twitter", 
    #                    'url' : '',
    #                     "img" : "Twitter_grey.png"},
    #             {'sitename' : "Wordpress", 
    #                    'url' : '',
    #                     "img" : "Wordpress_grey.png"},
    #             {'sitename' : "Pornhub", 
    #                    'url' : '',
    #                     "img" : "Pornhub_grey.png"},
    #             {'sitename' : "GitHub", 
    #                    'url' : '',
    #                     "img" : "Github_grey.png"},
    #             {'sitename' : "Spotify", 
    #                    'url' : '',
    #                     "img" : "Spotify_grey.png"},
    #             {'sitename' : "Tiktok", 
    #                    'url' : '',
    #                     "img" : "Tiktok_grey.png"},
    #             {'sitename' : "Xvideos", 
    #                    'url' : '',
    #                     "img" : "Xvideos_grey.png"},
    #             {'sitename' : "Tumblr", 
    #                    'url' : '',
    #                     "img" : "Tumblr_grey.png"},
    #             {'sitename' : "Pinterest", 
    #                    'url' : '',
    #                     "img" : "Pinterest_grey.png"},
    #             {'sitename' : "Patreon", 
    #                    'url' : '',
    #                     "img" : "Patreon_grey.png"}]
    listOfWeb = []
    for i in input:
        
        temp = i
        sitename = temp['sitename']
        firstLetter = sitename[0:1]
        if sitename in showsite:

            listOfWeb.append({'sitename' : temp['sitename'], 
                            'url' : temp['url_user'],
                            "img" : f"{sitename}.png"})
        else:
            listOfWeb.append({'sitename' : temp['sitename'], 
                            'url' : temp['url_user'],
                            "img" : f"{firstLetter}.png"})

    return listOfWeb  

def sortIcon(input:list):
    showsite = ["Youtube","Facebook","Amazon","Reddit","VK","Instagram","Twitch","Ebay","Twitter","Wordpress","Pornhub","GitHub","Spotify","Tiktok","Xvideos","Tumblr","Pinterest","Patreon"]
    for i in input:
        if i['sitename'] in showsite:
            input.insert(0, input.pop(input.index(i)))
    pprint(input)
    return input

def removeTrash(input:list):
    trash = ['F6S','TJournal','Pixwox','TRASHBOX.RU']
    for i in input:
        if i['sitename'] in trash:
            input.pop(input.index(i))
    return input
# def checkdupe(input :list ,sitename:str):

#     for count,data in enumerate(input):
#         if sitename == data['sitename']:
#             return count


# maigret('ohmsnow')
#  {'img': 'g.png',
#  {'img': 'Reddit_grey.png', 'sitename': 'Reddit', 'url': ''},
#  {'img': 'VK_grey.png', 'sitename': 'VK', 'url': ''},
#  {'img': 'Instagram_grey.png', 'sitename': 'Instagram', 'url': ''},
#  {'img': 'Twitch_grey.png', 'sitename': 'Twitch', 'url': ''},
#  {'img': 'Ebay_grey.png', 'sitename': 'Ebay', 'url': ''},
#  {'img': 'Twitter_grey.png', 'sitename': 'Twitter', 'url': ''},
#  {'img': 'Wordpress_grey.png', 'sitename': 'Wordpress', 'url': ''},
#  {'img': 'Pornhub_grey.png', 'sitename': 'Pornhub', 'url': ''},
#  {'img': 'Github_grey.png', 'sitename': 'Github', 'url': ''},
#  {'img': 'Spotify_grey.png', 'sitename': 'Spotify', 'url': ''},
#  {'img': 'Tiktok_grey.png', 'sitename': 'Tiktok', 'url': ''},
#  {'img': 'Xvideos_grey.png', 'sitename': 'Xvideos', 'url': ''},
#  {'img': 'Tumblr.png',
#   'sitename': 'Tumblr',
#   'url': 'https://tangktp.tumblr.com/'},
#  {'img': 'Pinterest.png',
#   'sitename': 'Pinterest',
#   'url': 'https://www.pinterest.com/tangktp/'},
#  {'img': 'Patreon_grey.png', 'sitename': 'Patreon', 'url': ''},
#  {'img': 'K.png',
#   'sitename': 'Kaggle',
#   'url': 'https://www.kaggle.com/tangktp'},
#  {'img': 'P.png',
#   'sitename': 'Picuki',
#   'url': 'https://www.picuki.com/profile/tangktp'},
#  {'img': 'S.png',
#   'sitename': 'Strava',
#   'url': 'https://www.strava.com/athletes/tangktp'},
#  {'img': 'F.png', 'sitename': 'F6S', 'url': 'https://www.f6s.com/tangktp'},
#  {'img': 'P.png',
#   'sitename': 'Pixwox',
#   'url': 'https://www.pixwox.com/profile/tangktp/'},
#  {'img': 'T.png',
#   'sitename': 'TJournal',
#   'url': 'https://tjournal.ru/search/v2/subsite/relevant?query=tangktp'},
#  {'img': 'D.png',
#   'sitename': 'DonationsAlerts',
#   'url': 'https://www.donationalerts.com/r/tangktp'},
#  {'img': 'Youtube_grey.png', 'sitename': 'Youtube', 'url': ''},
#  {'img': 'Facebook_grey.png', 'sitename': 'Facebook', 'url': ''},
#  {'img': 'Amazon_grey.png', 'sitename': 'Amazon', 'url': ''},
#  {'img': 'Reddit_grey.png', 'sitename': 'Reddit', 'url': ''},
#  {'img': 'VK_grey.png', 'sitename': 'VK', 'url': ''},
#  {'img': 'Instagram_grey.png', 'sitename': 'Instagram', 'url': ''},
#  {'img': 'Twitch.png',
#   'sitename': 'Twitch',
#   'url': 'https://www.twitch.tv/Tangkantapon'},
#  {'img': 'Ebay_grey.png', 'sitename': 'Ebay', 'url': ''},
#  {'img': 'Twitter_grey.png', 'sitename': 'Twitter', 'url': ''},
#  {'img': 'Wordpress_grey.png', 'sitename': 'Wordpress', 'url': ''},
#  {'img': 'Pornhub_grey.png', 'sitename': 'Pornhub', 'url': ''},
#  {'img': 'Github_grey.png', 'sitename': 'Github', 'url': ''},
#  {'img': 'Spotify_grey.png', 'sitename': 'Spotify', 'url': ''},
#  {'img': 'Tiktok_grey.png', 'sitename': 'Tiktok', 'url': ''},
#  {'img': 'Xvideos_grey.png', 'sitename': 'Xvideos', 'url': ''},
#  {'img': 'Tumblr_grey.png', 'sitename': 'Tumblr', 'url': ''},
#  {'img': 'Pinterest.png',
#   'sitename': 'Pinterest',
#   'url': 'https://www.pinterest.com/Tangkantapon/'},
#  {'img': 'Patreon_grey.png', 'sitename': 'Patreon', 'url': ''},
#  {'img': 'G.png',
#   'sitename': 'GitHubGist',
#   'url': 'https://gist.github.com/Tangkantapon'},
#  {'img': 'G.png',
#   'sitename': 'GitHub',
#   'url': 'https://github.com/Tangkantapon'},
#  {'img': 'N.png',
#   'sitename': 'Nitter',
#   'url': 'https://nitter.net/Tangkantapon'},
#  {'img': 'g.png',
#   'sitename': 'giphy.com',
#   'url': 'https://giphy.com/channel/Tangkantapon'},
#  {'img': 'R.png',
#   'sitename': 'Roblox',
#   'url': 'https://www.roblox.com/user.aspx?username=Tangkantapon'},
#  {'img': 'P.png',
#   'sitename': 'Picuki',
#   'url': 'https://www.picuki.com/profile/Tangkantapon'},
#  {'img': 'A.png',
#   'sitename': 'Academia.edu',
#   'url': 'https://independent.academia.edu/Tangkantapon'},
#  {'img': 'S.png',
#   'sitename': 'Strava',
#   'url': 'https://www.strava.com/athletes/Tangkantapon'},
#  {'img': 'F.png', 'sitename': 'F6S', 'url': 'https://www.f6s.com/Tangkantapon'},
#  {'img': 'T.png',
#   'sitename': 'TJournal',
#   'url': 'https://tjournal.ru/search/v2/subsite/relevant?query=Tangkantapon'},
#  {'img': 'P.png',
#   'sitename': 'Pixwox',
#   'url': 'https://www.pixwox.com/profile/Tangkantapon/'},
#  {'img': 'A.png', 'sitename': 'AskFM', 'url': 'https://ask.fm/Tangkantapon'},
#  {'img': 'g.png',
#   'sitename': 'giters.com',
#   'url': 'https://giters.com/Tangkantapon'},
#  {'img': 'D.png',
#   'sitename': 'DonationsAlerts',
#   'url': 'https://www.donationalerts.com/r/Tangkantapon'},
#  {'img': 'D.png',
#   'sitename': 'Dumpor',
#   'url': 'https://dumpor.com/v/Tangkantapon'},
#  {'img': 'T.png',
#   'sitename': 'TRASHBOX.RU',
#   'url': 'https://trashbox.ru/users/Tangkantapon'}])