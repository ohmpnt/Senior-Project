


def calculateRisk(input:dict) -> str :
    risk=[]
    for key,value in input.items() :

        for i in value:
            risk.append(matrix(i['tag'],key))


    return max(risk)
    






def matrix(dmg:str,likelihood:str) ->int :
    lowDmg = []
    medDmg =[]
    highDmg =[]
    lowLikely = []
    medLikely = []
    highLikely =[]


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
    

# {'DOB': [],
#  'ID': [],
#  'address': [{'data': '',
#               'tag': 'social network',
#               'url': 'https://www.facebook.com/Songpon.te/about'}],
#  'education': [],
#  'email': [{'data': '*ct@mahidol.ac.th (not breach)',
#             'tag': 'unknow',
#             'url': 'https://www.ict.mahidol.ac.th/people/staff-contact/songpon-teerakanok/'}],
#  'fName': [],
#  'familyMember': [],
#  'fullName': [{'data': '',
#                'tag': 'social network',
#                'url': 'https://www.facebook.com/Songpon.te/about'}],
#  'gender': [{'data': '',
#              'tag': 'social network',
#              'url': 'https://www.facebook.com/Songpon.te/about'}],
#  'lName': [],
#  'name': [],
#  'occupation': [],
#  'phoneNumber': [],
#  'picture': [{'data': 'https://scontent.fbkk28-1.fna.fbcdn.net/v/t39.30808-6/299835346_10222653853429438_238771487539892262_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=100&ccb=1-7&_nc_sid=85a577&efg=eyJpIjoidCJ9&_nc_ohc=CcGPeRZCb-wAX9NN1sP&tn=-DFwpzWxTywRKSgz&_nc_ht=scontent.fbkk28-1.fna&oh=00_AfBQPBi4-vrrHCHsqR_XpxAH7bgto_INBVg0Mu-zdTpNaA&oe=63D30FE5&manual_redirect=1',
#               'tag': 'social network',
#               'url': 'https://www.facebook.com/Songpon.te/about'}],
#  'relationship': [],
#  'username': [],
#  'workPlace': [{'data': '',
#                 'tag': 'social network',
#                 'url': 'https://www.facebook.com/Songpon.te/about'}]}