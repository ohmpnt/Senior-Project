from facebook_scraper import get_profile
from pprint import pprint
from image import images

def fbScrape(x:str)->list:
    result = {
        "DOB" : [],
        "username" : [],
        "fullName" : [],
        "phoneNumber": [],
        "email": [],
        "workPlace": [],
        "education": [],
        "familyMember" : [],
        "address": [],
        "gender": [],
        "relationship": [],
        "picture" : []
    }
    linkfb = "https://www.facebook.com/"+ x +"/about" #construct the facebook url
    username = ""
    try:
        src=get_profile(x, cookies = "cookies.txt") #use facebook scrapper to get the profile data


        # find every data in src
        basic_info,contact_info,Education,Relationship,Work,Live= '','','','','',''
        if 'Basic info' in src:
            basic_info = src['Basic info']
        if 'Contact Info' in src:
            contact_info = src['Contact Info']
        
        
        # Full name
        result["fullName"].append({
                                    "sitename" : "facebook",
                                    "url" : linkfb,
                                    "data":  '' ,
                                    "tag" : "social network"
                                    }) 
        # Username
        if "Instagram" in contact_info :
            result["username"].append({
                                    "url" : linkfb,
                                    "data":  '' ,
                                    "tag" : "social network",
                                    "sitename" : "facebook"
                                    }) 
            username = contact_info["Instagram"]
        # DOB
        if "Date of birth" in basic_info:
            result["DOB"].append({
                                    "url" : linkfb,
                                    "data":  '' ,
                                    "tag" : "social network",
                                    "sitename" : "facebook"
                                    }) 
        # Gender
        if "Gender" in basic_info :
            result["gender"].append({
                                    "url" : linkfb,
                                    "data":  '' ,
                                    "tag" : "social network",
                                    "sitename" : "facebook"
                                    }) 
        # Phone number
        if "Mobile" in contact_info:
            result["phoneNumber"].append({
                                    "url" : linkfb,
                                    "data":  '' ,
                                    "tag" : "social network",
                                    "sitename" : "facebook"
                                    }) 
        # Email
        if "Email" in contact_info:
            result["email"].append({
                                    "url" : linkfb,
                                    "data":  '' ,
                                    "tag" : "social network",
                                    "sitename" : "facebook"
                                    }) 
        # work place
        if 'Work' in src:
            result["workPlace"].append({
                                    "url" : linkfb,
                                    "data":  '' ,
                                    "tag" : "social network",
                                    "sitename" : "facebook"
                                    }) 
        # Adress
        if "Places lived" in src:
            result["address"].append({
                                    "url" : linkfb,
                                    "data":  '' ,
                                    "tag" : "social network",
                                    "sitename" : "facebook"
                                    }) 
        # family member
        if "Family member" in src:
            result["familyMember"].append({
                                    "url" : linkfb,
                                    "data":  '' ,
                                    "tag" : "social network",
                                    "sitename" : "facebook"
                                    }) 
        # relationship
        if "Relationship" in src:
            result["relationship"].append({
                                    "url" : linkfb,
                                    "data":  '' ,
                                    "tag" : "social network",
                                    "sitename" : "facebook"
                                    }) 
        # picture
        if "profile_picture" in src :
            result["picture"].append({
                                    "url" : linkfb,
                                    "data":  src['profile_picture'],
                                    "tag" : "social network",
                                    "sitename" : "facebook"
                                    }) 
    except:
        print("cannot find the user's facebook") # in case cant find any facebook profile print this

    return result,username

