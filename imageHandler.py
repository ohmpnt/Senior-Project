import requests
import os
from pprint import pprint

def images(input:list):
    #loop through each image and put into loadimage function
    pprint(input)
    for count,info in enumerate(input):
        imgLink= info['data']
        loadImage(count,imgLink)
   
def loadImage(num:int,src:str):
    imageUrl = src
    if "https" in imageUrl:
        url = imageUrl[imageUrl.rfind("https"):]  #start link with https incase of invalid link
    else:
        url = imageUrl[imageUrl.rfind("http"):]

    try:

        img_data = requests.get(url).content #get the image content
        curPath = os.getcwd()
        #save in folder \static\images\pic
        with open(f'{curPath}\static\images\pic{num}.jpg', 'wb') as handler:
            handler.write(img_data)

    except:
        print("error at ", num)


# images([{'data': 'https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/326348587_1291684474746045_8262627674056328296_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=109&ccb=1-7&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=3wQ2B2n7-88AX-ZL-v7&tn=BJ2reMALh13NAWEv&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfAe-Bejx2uMX06XDaNWzQamMyKKHjSRMmJXsOG3hOt2mA&oe=644C9AC2&manual_redirect=1',
#   'sitename': 'facebook',
#   'tag': 'social network',
#   'url': 'https://www.facebook.com/srisukdentalcare/about'},
#  {'data': 'https://media.licdn.com/dms/image/C4E0BAQFa3Yd2PfPzmg/company-logo_100_100/0/1519856210142?e=2147483647&v=beta&t=XlFoO9GC3HWGxQD5o8gCAA_jQm7jkpewjZqX0GTd_fQ',
#   'sitename': 'LinkedIn',
#   'tag': 'social network',
#   'url': 'https://th.linkedin.com/in/srisuk-rujisaritwong-41748619'},
#  {'data': 'https://static-cdn.jtvnw.net/user-default-pictures-uv/41780b5a-def8-11e9-94d9-784f43822e80-profile_image-150x150.png',
#   'sitename': 'Twitch',
#   'tag': 'streaming',
#   'url': 'https://www.twitch.tv/srisuk'},
#  {'data': 'https://avatars.githubusercontent.com/u/126052994?v=4',
#   'sitename': 'GitHub',
#   'tag': 'coding',
#   'url': 'https://github.com/srisuk'},
#  {'data': 'https://trello-members.s3.amazonaws.com/5de4ed855e216d690bbe513e/627a1fef80111f303ba65bf03e98ed15/170.png',
#   'sitename': 'Trello',
#   'tag': 'tasks',
#   'url': 'https://trello.com/srisuk'},
#  {'data': 'https://www.redditstatic.com/avatars/defaults/v2/avatar_default_3.png',
#   'sitename': 'Reddit',
#   'tag': 'discussion',
#   'url': 'https://www.reddit.com/user/srisuk'},
#  {'data': 'https://lastfm.freetls.fastly.net/i/u/avatar170s/818148bf682d429dc215c1705eb27b98.png',
#   'sitename': 'last.fm',
#   'tag': 'music',
#   'url': 'https://last.fm/user/srisuk'},
#  {'data': 'https://images-ssl.gotinder.com/6171f7835ceb3b0100dc1bad/original_9a5e1574-0818-4926-b15d-39ff27e0aa12.jpeg',
#   'sitename': 'Tinder',
#   'tag': 'dating',
#   'url': 'https://www.tinder.com/@srisuk'},
#  {'data': 'http://2.gravatar.com/avatar/287995f72c508d69c0a4ed329eb1bc2e',
#   'sitename': 'Gravatar',
#   'tag': 'photo',
#   'url': 'http://en.gravatar.com/srisuk'},
#  {'data': 'flex: 0 0 '
#           '80px;https://cuad.ask.fm/assets2/009/830/288/896/normal/avatar.jpg',
#   'sitename': 'AskFM',
#   'tag': 'eg',
#   'url': 'https://ask.fm/srisuk'}])

# images([{'data': 'http://2.gravatar.com/avatar/287995f72c508d69c0a4ed329eb1bc2e',
#    'sitename': 'Gravatar',
#    'tag': 'photo',
#    'url': 'http://en.gravatar.com/srisuk'}])

