import math
from pprint import pprint

def calculateRisk(input:dict) -> str :
    risk=[]
    datas = []
    for key,value in input.items() :
        
        for i in value:
            temp = matrix(i['tag'],key)
            if temp != None:
                risk.append(temp)
                datas.append([i['tag'],key,i['url'],i['sitename']])
    if len(risk) >0:
        average = math.floor(sum(risk)/len(risk))
        listHigh = findFifthHighest(risk,datas)
        sugg = sugMain(listHigh)
    else:
        average=1
        sugg = []
    return average,sugg

def findFifthHighest(risk:list, datas:list):
    print(risk,datas)
    result = []
    for i in range(0,5):
        try:
            indexAt = risk.index(max(risk))
            result.append(datas.pop(indexAt))
            risk.pop(indexAt)
        except:
            break
    return result

def matrix(dmg:str,likelihood:str) ->int :
    # print(dmg,'=============',likelihood)
    lowDmg = ['gaming', 'music', 'art', 'dating', 'movies', 'hobby', 'sport','forum','porn','social network','streaming']
    medDmg =['coding', 'news', 'blog', 'shopping', 'stock','education','career','unknow']
    highDmg =['trading', 'photo', 'finance','business','medicine']
    lowLikely = ['DOB','occupation','relationship','username','fName','lName','gender']
    medLikely = ['education','fullName','familyMember','name','workPlace']
    highLikely =['ID','address','email','phoneNumber','picture']

    if likelihood in lowLikely and dmg in lowDmg :
        return 1
    elif likelihood in lowLikely and dmg in medDmg :
        return 2
    elif likelihood in lowLikely and dmg in highDmg :
        return 3
    elif likelihood in medLikely and dmg in lowDmg :
        return 2
    elif likelihood in medLikely and dmg in medDmg :
        return 3
    elif likelihood in medLikely and dmg in highDmg :
        return 4
    elif likelihood in highLikely and dmg in lowDmg :
        return 3
    elif likelihood in highLikely and dmg in medDmg :
        return 4
    elif likelihood in highLikely and dmg in highDmg :
        return 5

def sugMain (input:list):
    result = []

    for i in input:
        result.append(suggestion(i))
    return result

def suggestion(input :list):
    
    type1 = ['DOB','username','fName','fullName','lName','name','workPlace','occupation','education','familyMember','address']
    type2 = ['phoneNumber','email','ID']
    type3 = ['gender','relationship']
    type4 = ['picture']
    
    if input[1] == 'DOB':
        word = 'date of birth'
    elif input[1] == 'username':
        word = 'username'
    elif input[1] == 'fName':
        word = 'first name'
    elif input[1] == 'fullName':
        word = 'full name'
    elif input[1] == 'lName':
        word = 'last name'
    elif input[1] == 'name':
        word = 'nickname'
    elif input[1] == 'phoneNumber':
        word = 'phone number'
    elif input[1] == 'email':
        word = 'email'
    elif input[1] == 'ID':
        word = 'identification number'
    elif input[1] == 'workPlace':
        word = 'work place'
    elif input[1] == 'occupation':
        word = 'occupation'
    elif input[1] == 'picture':
        word = 'photo'
    elif input[1] == 'education':
        word = 'education'
    elif input[1] == 'familyMember':
        word = 'family member'
    elif input[1] == 'address':
        word = 'address'
    elif input[1] == 'gender':
        word = 'gender'
    elif input[1] == 'relationship':
        word = 'relationship'

    # result = f"there is information about your {word} on {input[3]} website"
    # names = ['● Observe on your account and may consider changing the privacy settings', f'● Be careful when filling in {word} information in unreliable sources']
    # nl = '\n'
    # text = f"Winners are:{nl}{nl.join(names)}"

    if input[1] in type1:
        detail = ['● Observe on your account and may consider changing the privacy settings', f'● Be careful when filling in {word} information in unreliable sources']
    elif input[1] in type2:
        detail = ['● Observe on your account and may consider changing the privacy settings', f'● Be careful when filling in {word} information in unreliable sources', f'● Enable for two-factor authentication']
    elif input[1] in type3:
        detail = ['● Observe on your account and may consider changing the privacy settings']
    elif input[1] in type4:
        detail = ['● Observe on your account and may consider changing the privacy settings', f'● Be careful when uploading a {word} in unreliable sources']
        

    out = [word,input[3],detail,input[2]]

    return out

# x = {'DOB': [{'data': '',
#           'sitename': 'facebook',
#           'tag': 'social network',
#           'url': 'https://www.facebook.com/135221053181397/about'}],
#  'ID': [],
#  'address': [],
#  'education': [],
#  'email': [],
#  'fName': [],
#  'familyMember': [],
#  'fullName': [{'data': '',
#                'sitename': 'facebook',
#                'tag': 'social network',
#                'url': 'https://www.facebook.com/135221053181397/about'}],
#  'gender': [],
#  'lName': [],
#  'name': [],
#  'occupation': [],
#  'phoneNumber': [],
#  'picture': [],
#  'relationship': [],
#  'username': [],
#  'workPlace': []}
# {'DOB': [{'data': '',
#           'sitename': 'facebook',
#           'tag': 'social network',
#           'url': 'https://www.facebook.com/135221053181397/about'}],
#  'ID': [],
#  'address': [],
#  'education': [],
#  'email': [],
#  'fName': [],
#  'familyMember': [],
#  'fullName': [{'data': '',
#                'sitename': 'facebook',
#                'tag': 'social network',
#                'url': 'https://www.facebook.com/135221053181397/about'}],
#  'gender': [],
#  'lName': [],
#  'name': [],
#  'occupation': [],
#  'phoneNumber': [],
#  'picture': [],
#  'relationship': [],
#  'username': [],
#  'workPlace': []}
# [{'img': 'Pinterest.png',
#   'name': ['SudsanguanNgamsuriyaroj'],
#   'sitename': 'Pinterest',
#   'url': ['https://www.pinterest.com/SudsanguanNgamsuriyaroj/']},
#  {'img': 'A.png',
#   'name': ['SudsanguanNgamsuriyaroj'],
#   'sitename': 'Academia.edu',
#   'url': ['https://independent.academia.edu/SudsanguanNgamsuriyaroj']},
#  {'img': 'S.png',
#   'name': ['SudsanguanNgamsuriyaroj'],
#   'sitename': 'Strava',
#   'url': ['https://www.strava.com/athletes/SudsanguanNgamsuriyaroj']},
#  {'img': 'P.png',
#   'name': ['SudsanguanNgamsuriyaroj'],
#   'sitename': 'Picuki',
#   'url': ['https://www.picuki.com/profile/SudsanguanNgamsuriyaroj']},
#  {'img': 'P.png',
#   'name': ['SudsanguanNgamsuriyaroj'],
#   'sitename': 'Pixwox',
#   'url': ['https://www.pixwox.com/profile/SudsanguanNgamsuriyaroj/']},
#  {'img': 'D.png',
#   'name': ['SudsanguanNgamsuriyaroj'],
#   'sitename': 'DonationsAlerts',
#   'url': ['https://www.donationalerts.com/r/SudsanguanNgamsuriyaroj']},
#  {'img': 'D.png',
#   'name': ['SudsanguanNgamsuriyaroj'],
#   'sitename': 'Dumpor',
#   'url': ['https://dumpor.com/v/SudsanguanNgamsuriyaroj']}]
 
# risk,sugg =calculateRisk(x)

# pprint(sugg)
