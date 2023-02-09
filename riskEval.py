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

    listHigh = findFifthHighest(risk,datas)
    sugg = sugMain(listHigh)
    average = math.floor(sum(risk)/len(risk))
    return average,sugg

def findFifthHighest(risk:list, datas:list):
    result = []
    for i in range(0,5):
    
        indexAt = risk.index(max(risk))
        result.append(datas.pop(indexAt))
        risk.pop(indexAt)
        
    return result

def matrix(dmg:str,likelihood:str) ->int :
    # print(dmg,'=============',likelihood)
    lowDmg = ['gaming', 'music', 'art', 'dating', 'movies', 'hobby', 'sport','forum','porn','social network','streaming']
    medDmg =['coding', 'news', 'blog', 'shopping', 'stock','education','career']
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

# x = {'DOB': [],
#  'ID': [],
#  'address': [{'data': '',
#               'tag': 'social network',
#               'url': 'https://www.facebook.com/fubuki.tang/about',
#               'sitename': 'Facebook'}],
#  'education': [],
#  'email': [],
#  'fName': [],
#  'familyMember': [],
#  'fullName': [{'data': '',
#                'tag': 'social network',
#                'url': 'https://www.facebook.com/fubuki.tang/about',
#               'sitename': 'Facebook'},
#               {'data': 'tangkantapon',
#                'sitename': 'Twitch',
#                'tag': 'streaming',
#                'url': 'https://www.twitch.tv/Tangkantapon'},
#               {'data': 'Kantapon Srigadphach',
#                'sitename': 'GitHub',
#                'tag': 'coding',
#                'url': 'https://github.com/Tangkantapon'}],
#  'gender': [{'data': '',
#              'tag': 'social network',
#              'url': 'https://www.facebook.com/fubuki.tang/about',
#               'sitename': 'Facebook'}],
#  'lName': [],
#  'name': [],
#  'occupation': [],
#  'phoneNumber': [],
#  'picture': [{'data': 'https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/290501684_5219335674825610_671348912778975975_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=104&ccb=1-7&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=wwQbyMhXm9QAX8ePY_W&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfCq0r-N4aV5ckhtVVoxq3LZOFFOGs6h_xfe0KkpaTEamg&oe=63DDC228&manual_redirect=1',
#               'tag': 'social network',
#               'url': 'https://www.facebook.com/fubuki.tang/about',
#               'sitename': 'Facebook'},
#              {'data': 'https://static-cdn.jtvnw.net/user-default-pictures-uv/ebe4cd89-b4f4-4cd9-adac-2f30151b4209-profile_image-150x150.png',
#               'sitename': 'Twitch',
#               'tag': 'streaming',
#               'url': 'https://www.twitch.tv/Tangkantapon'},
#              {'data': 'https://avatars.githubusercontent.com/u/51602945?v=4',
#               'sitename': 'GitHub',
#               'tag': 'coding',
#               'url': 'https://github.com/Tangkantapon'},
#              {'data': 'flex: 0 0 '
#                       '80px;https://cuad.ask.fm/assets2/154/971/066/880/normal/avatar.jpg',
#               'sitename': 'AskFM',
#               'tag': 'eg',
#               'url': 'https://ask.fm/Tangkantapon'}],
#  'relationship': [{'data': '',
#                    'tag': 'social network',
#                    'url': 'https://www.facebook.com/fubuki.tang/about',
#               'sitename': 'Facebook'}],
#  'username': [{'data': '',
#                'tag': 'social network',
#                'url': 'https://www.facebook.com/fubuki.tang/about',
#               'sitename': 'Facebook'},
#               {'data': 'tangkantapon',
#                'sitename': 'Twitch',
#                'tag': 'streaming',
#                'url': 'https://www.twitch.tv/Tangkantapon'}],
#  'workPlace': []}
 
# risk,sugg =calculateRisk(x)

# pprint(sugg)
