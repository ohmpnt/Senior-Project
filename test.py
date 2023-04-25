imageUrl = "http://2.gravatar.com/avatar/287995f72c508d69c0a4ed329eb1bc2e"
if "https" in imageUrl:
    print("yes")
else:
    print("no")
print(imageUrl.rfind("https"))