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
    linkfb = "https://www.facebook.com/"+ x +"/about"
    username = ""
    # try:
    src=get_profile(x, cookies = "cookies.txt")
    basic_info,contact_info,Education,Relationship,Work,Live= '','','','','',''
    if 'Basic info' in src:
        basic_info = src['Basic info']
    if 'Contact Info' in src:
        contact_info = src['Contact Info']
    
    
    # Full name
    result["fullName"].append({
                                "url" : linkfb,
                                "data":  '' ,
                                "tag" : "social network"
                                }) 
    # Username
    if "Instagram" in contact_info :
        result["username"].append({
                                "url" : linkfb,
                                "data":  '' ,
                                "tag" : "social network"
                                }) 
        username = contact_info["Instagram"]
    # DOB
    if "Date of birth" in basic_info:
        result["DOB"].append({
                                "url" : linkfb,
                                "data":  '' ,
                                "tag" : "social network"
                                }) 
    # Gender
    if "Gender" in basic_info :
        result["gender"].append({
                                "url" : linkfb,
                                "data":  '' ,
                                "tag" : "social network"
                                }) 
    # Phone number
    if "Mobile" in contact_info:
        result["phoneNumber"].append({
                                "url" : linkfb,
                                "data":  '' ,
                                "tag" : "social network"
                                }) 
    # Email
    if "Email" in contact_info:
        result["email"].append({
                                "url" : linkfb,
                                "data":  '' ,
                                "tag" : "social network"
                                }) 
    # work place
    if 'Work' in src:
        result["workPlace"].append({
                                "url" : linkfb,
                                "data":  '' ,
                                "tag" : "social network"
                                }) 
    # Adress
    if "Places lived" in src:
        result["address"].append({
                                "url" : linkfb,
                                "data":  '' ,
                                "tag" : "social network"
                                }) 
    # family member
    if "Family member" in src:
        result["familyMember"].append({
                                "url" : linkfb,
                                "data":  '' ,
                                "tag" : "social network"
                                }) 
    # relationship
    if "Relationship" in src:
        result["relationship"].append({
                                "url" : linkfb,
                                "data":  '' ,
                                "tag" : "social network"
                                }) 
    # picture
    if "profile_picture" in src :
        result["picture"].append({
                                "url" : linkfb,
                                "data":  src['profile_picture'],
                                "tag" : "social network"
                                }) 
    # except:
    #     print("cannot find the user's facebook")
    # images(result["picture"])
    return result,username

# fbScrape('fubuki.tang')