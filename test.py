import re
# x = {
#     "ID" : "123123",
#     "lol" : "123522"
# }

# x.get
# temp = x["image"]
# print (temp)

# x= ["birth_date","DOB"]
# print(x[1])
email = ['\n\t\t\t\t\t\t\t\t\t   ict@mahidol.ac.th\t\t\t\t\t\t\t\t\t   ','\n\t\t\t\t\t\t\t\t\t   ict@mahidol.ac.th\t\t\t\t\t\t\t\t\t   ','\n\t\t\t\t\t\t\t\t\t   ict@mahidol.ac.th\t\t\t\t\t\t\t\t\t   ']
for count,data in enumerate(email): 
    data = re.sub('\s+', '', data)
    email[count]=data

print(email)