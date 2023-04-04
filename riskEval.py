import math
from pprint import pprint
# main function of risk eval
def calculateRisk(input:dict) -> str :
    risk=[]
    datas = []
    for key,value in input.items() : # loop through each data and put into matrix function
        
        for i in value:
            temp = matrix(i['tag'],key)
            if temp != None:
                risk.append(temp)
                datas.append([i['tag'],key,i['url'],i['sitename']]) #append to datas list to use to calculate the risk

    # calculate the risk
    if len(risk) >0:
        average = math.floor(sum(risk)/len(risk))
        listHigh = findFifthHighest(risk,datas)
        sugg = sugMain(listHigh)
    else:
        average=1
        sugg = []
    return average,sugg

# find the top five heighest risk information
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
    # our risk matrix has 2 factor to consider damage and likelihood

    # damage
    lowDmg = ['gaming', 'music', 'art', 'dating', 'movies', 'hobby', 'sport','forum','porn','social network','streaming']
    medDmg =['coding', 'news', 'blog', 'shopping', 'stock','education','career','unknow']
    highDmg =['trading', 'photo', 'finance','business','medicine']
    
    # liklihood
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


# use to generate the suggestion word by using top 5 riskiest data
def suggestion(input :list):
    
    # classify the type of suggestion to be 4 type
    type1 = ['DOB','username','fName','fullName','lName','name','workPlace','occupation','education','familyMember','address']
    type2 = ['phoneNumber','email','ID']
    type3 = ['gender','relationship']
    type4 = ['picture']
    

    # rewrite the word
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

    # set the type of suggestion
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
