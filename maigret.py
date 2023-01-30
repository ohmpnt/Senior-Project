
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

    showsite = ["Youtube","Facebook","Amazon","Reddit","VK","Instagram","Twitch","Ebay","Twitter","Wordpress","Pornhub","Github","Spotify","Tiktok","Xvideos","Tumblr","Printerest"]
    listOfWeb = [{'sitename' : temp['sitename'], 
                        'url' : temp['url_user'],
                        "img" : f"{firstLetter}.png"}]
    for i in input:
        
        temp = i
        sitename = temp['sitename']
        firstLetter = sitename[0:1]

        listOfWeb.append({'sitename' : temp['sitename'], 
                        'url' : temp['url_user'],
                        "img" : f"{firstLetter}.png"})

    return listOfWeb  

# maigret('ohmsnow')