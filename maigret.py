
import os
import json
from pprint import pprint



def maigrets(input: list):
    # input = list of usernames
    newOut = {}
    listWebOut = []
    # loop through each username and put into maigret function
    for i in input:
        temp,listWeb =profileSearch(i) # put into maigret function
        newOut = merge(newOut,temp) #merge with new data
        listWebOut= listMerge(listWebOut,listWeb) #merge with new listweb
    listWebOut = sortIcon(listWebOut) #sort the icon
    listWebOut = removeTrash(listWebOut) #remove the unessesary website
    return newOut,listWebOut


# use to merge list
def listMerge (list1:list,list2:list) ->list :
    result = list1
    for i in range(len(result)):
        temp = result[i]
        for j in list2:
            if temp['sitename'] == j['sitename']:
                url = j['url']
                name = j['name']
                temp['url'].append(url[0])
                temp['name'].append(name[0])
                list2.pop(list2.index(j))

    result = result+list2

    return result


# maigret function
def profileSearch(input:str):

    print(input)
    curPath = os.getcwd()
    os.system(f'python "{curPath}/maigret/maigret.py" {input} --json ndjson --timeout 8 ') #call maigret tool

    try : 
        file = open(f'reports/report_{input}_ndjson.json') #open the report files
        datas = file.readlines()
        output= []
        for data in datas:
            output.append(json.loads(data)) #put the file into json format
        file.close()
    
        data = pageData(output) # call the page data to gather info onwebsite page
        weblist = listWeb(output,input) # use to construct list web to display in web app
        return data,weblist
    except :
        print('something worng!')
    



def pageData (input:list):

    #the target name of information we want to get
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

    #loop through each element and add infomation to data list in json format
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


# use to merge data list
def merge (dict_1:dict, dict_2:dict):
    for key, value in dict_2.items():
        if key in dict_1:
            if value:
                for i in value:
                    dict_1[key].append(i)  
        else:
            dict_1[key] = value

    return dict_1



def listWeb (input:list,name:str):
    #list of special icon sites
    showsite = ["Youtube","Facebook","Amazon","Reddit","VK","Instagram","Twitch","Ebay","Twitter","Wordpress","Pornhub","GitHub","Spotify",
                "TikTok","Xvideos","Tumblr","Pinterest","Patreon","9gag","Academia","Adobe","Baidu","Figma","Freepik","Googlemap","Googleplus",
                "Imgur","Medium","OracleCommunity","Playstore","Quora","Researchgate","Roblox","Shutterstock","Slack","Slideshare","Soundcloud",
                "Stackoverflow","Steam","Telegram","TradingView","Trello","TripAdvisor","Vimeo","Weibo","Wikipedia","Xhamster","VSCO"] 
    listOfWeb = []

    for i in input:
        
        temp = i
        sitename = temp['sitename']
        firstLetter = sitename[0:1]
        if sitename in showsite: #if site name in showsite we will use special icon

            listOfWeb.append({'sitename' : temp['sitename'], 
                            'url' : [temp['url_user']],
                            "img" : f"{sitename}.png",
                            "name" : [f"{name}"]})
        else:
            listOfWeb.append({'sitename' : temp['sitename'], 
                            'url' : [temp['url_user']],
                            "img" : f"{firstLetter}.png",
                            "name" : [f"{name}"]})

    return listOfWeb  

#sort the icon by showsite first
def sortIcon(input:list):
    showsite = ["Youtube","Facebook","Amazon","Reddit","VK","Instagram","Twitch","Ebay","Twitter","Wordpress","Pornhub","GitHub","Spotify",
                "TikTok","Xvideos","Tumblr","Pinterest","Patreon","9gag","Academia","Adobe","Baidu","Figma","Freepik","Googlemap","Googleplus",
                "Imgur","Medium","OracleCommunity","Playstore","Quora","Researchgate","Roblox","Shutterstock","Slack","Slideshare","Soundcloud",
                "Stackoverflow","Steam","Telegram","TradingView","Trello","TripAdvisor","Vimeo","Weibo","Wikipedia","Xhamster","VSCO"] 
    for i in input:
        if i['sitename'] in showsite:
            input.insert(0, input.pop(input.index(i)))
    return input

# remove the unnessary website from listweb
def removeTrash(input:list):
    trash = ['F6S','TJournal','Pixwox','TRASHBOX.RU', 'Strava', 'DonationsAlerts','forums.imore.com',"banki.ru"]
    temp = input.copy()
    for i in input:
        if i['sitename'] in trash:
            temp.pop(temp.index(i))
    return temp





