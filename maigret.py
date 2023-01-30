
import os
import json
from pprint import pprint



def maigrets(input: list):
    newOut = {}
    listWebOut = []
    for i in input:
        temp,listWeb =profileSearch(i)
        newOut = merge(newOut,temp)
        listWebOut= listWebOut+listWeb

    return newOut,listWebOut



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

    showsite = ["Youtube","Facebook","Amazon","Reddit","VK","Instagram","Twitch","Ebay","Twitter","Wordpress","Pornhub","Github","Spotify","Tiktok","Xvideos","Tumblr","Pinterest","Patreon"]
    # listOfWeb = [{'sitename' : temp['sitename'], 
    #                     'url' : temp['url_user'],
    #                     "img" : f"{firstLetter}.png"}]
    listOfWeb=[{'sitename' : "Youtube", 
                       'url' : '',
                        "img" : "Youtube_grey.png"},
                {'sitename' : "Facebook", 
                       'url' : '',
                        "img" : "Facebook_grey.png"},
                {'sitename' : "Amazon", 
                       'url' : '',
                        "img" : "Amazon_grey.png"},
                {'sitename' : "Reddit", 
                       'url' : '',
                        "img" : "Reddit_grey.png"},
                {'sitename' : "VK", 
                       'url' : '',
                        "img" : "VK_grey.png"},
                {'sitename' : "Instagram", 
                       'url' : '',
                        "img" : "Instagram_grey.png"},
                {'sitename' : "Twitch", 
                       'url' : '',
                        "img" : "Twitch_grey.png"},
                {'sitename' : "Ebay", 
                       'url' : '',
                        "img" : "Ebay_grey.png"},
                {'sitename' : "Twitter", 
                       'url' : '',
                        "img" : "Twitter_grey.png"},
                {'sitename' : "Wordpress", 
                       'url' : '',
                        "img" : "Wordpress_grey.png"},
                {'sitename' : "Pornhub", 
                       'url' : '',
                        "img" : "Pornhub_grey.png"},
                {'sitename' : "Github", 
                       'url' : '',
                        "img" : "Github_grey.png"},
                {'sitename' : "Spotify", 
                       'url' : '',
                        "img" : "Spotify_grey.png"},
                {'sitename' : "Tiktok", 
                       'url' : '',
                        "img" : "Tiktok_grey.png"},
                {'sitename' : "Xvideos", 
                       'url' : '',
                        "img" : "Xvideos_grey.png"},
                {'sitename' : "Tumblr", 
                       'url' : '',
                        "img" : "Tumblr_grey.png"},
                {'sitename' : "Pinterest", 
                       'url' : '',
                        "img" : "Pinterest_grey.png"},
                {'sitename' : "Patreon", 
                       'url' : '',
                        "img" : "Patreon_grey.png"}]
    for i in input:
        
        temp = i
        sitename = temp['sitename']
        firstLetter = sitename[0:1]
        if sitename in showsite:
            index = checkdupe(listOfWeb,sitename)
            listOfWeb[index]={'sitename' : temp['sitename'], 
                            'url' : temp['url_user'],
                            "img" : f"{sitename}.png"}
        else:
            listOfWeb.append({'sitename' : temp['sitename'], 
                            'url' : temp['url_user'],
                            "img" : f"{firstLetter}.png"})

    return listOfWeb  


def checkdupe(input :list ,sitename:str):

    for count,data in enumerate(input):
        if sitename == data['sitename']:
            return count


# maigret('ohmsnow')