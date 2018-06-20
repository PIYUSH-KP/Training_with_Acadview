# Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
print('__'*40)
print("An access token is a credential that is used by an application to access an API")

#Reading Consumer key and secret from consumerKeys File
consumerKey = "bPFGvkfhqAOELn07ZIsqcfVRu"
consumerSecret = "9WgvaFV2hllLeY4JQ2ZxIAhISVh7w89SZMoeFcqMV23YsUQB95"

#authenticating twitter consumer key
auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.secure=True
authUrl = auth.get_authorization_url()

#go to this url
print("Please Visit This link and authorize the app ==> ",authUrl)

#writing access tokes to file
pin =input("Enter The Authorization PIN:").strip()
token = auth.get_access_token(verifier=pin)
accessTokenFile = open("accessTokens","w")
accessTokenFile.write(token[0]+'\n')
accessTokenFile.write(token[1]+'\n')

print('__'*40)

# Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.
print("IP ADDRESS OF www.google.com --> 216.58.203.164")
print("IP ADDRESS OF www.facebook.com --> 31.13.75.38")
print("IP ADDRESS OF www.acadview.com --> 54.69.196.196")

import socket
print("google: ",socket.gethostbyname('www.google.com'))

print("Facebook: ",socket.gethostbyname('www.facebook.com'))

print("Acadview: ",socket.gethostbyname('www.acadview.com'))



# Q.4- What is a difference between library and API . Figure it out with examples.

'''An architect (read application developer) wanted to build a house(read application), so he prepared for all its aspects including structure,
plumbing, wiring, decors etc(read different libraries).
He cant do all of the stuff himself so he took help from various experts in those fields, who are really good at doing what they do.
But he needed to communicate his needs and requirements face to face or via mail (read invoking API )so that they can cater to his need and provide the asked service.
After some time a fellow Architect came and wanted to accomplish a similar task but with a few add on features like swimming pool (a new library).
He can conveniently use the framework provided by our architect and add new features invoking any new service.'''\



'''API is a part of library which defines how an application communicates with external code. API can be written in any language.
Library is written in same language which is a collection of all the functionalities required for the use case.
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large
collection of high-level mathematical functions to operate on these arrays'''\

'''eg- Angular js- a JS framework may use many libraries like iniline editing of text using an exposed API of that library.'''

