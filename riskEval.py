
import math

def calculateRisk(input:dict) -> str :
    risk=[]
    for key,value in input.items() :

        for i in value:
            temp = matrix(i['tag'],key)
            if temp != None:
                risk.append(temp)

    average = math.floor(sum(risk)/len(risk))
    print(risk)
    return average
    
    






def matrix(dmg:str,likelihood:str) ->int :

    print(dmg,'=============',likelihood)
    lowDmg = ['gaming', 'music', 'art', 'dating', 'movies', 'hobby', 'sport','forum','porn']
    medDmg =['coding', 'news', 'blog', 'shopping', 'stock','education','career','social network']
    highDmg =['trading', 'photo', 'finance','business','medicine']
    lowLikely = ['DOB','occupation','relationship','username']
    medLikely = ['education','fName','lName','fullName','familyMember','name','workPlace']
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
    

x = {'DOB': [],
 'ID': [],
 'address': [{'data': '',
              'tag': 'social network',
              'url': 'https://www.facebook.com/fubuki.tang/about'}],
 'education': [],
 'email': [],
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
 
calculateRisk(x)