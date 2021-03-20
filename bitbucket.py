import requests
import json 



user_name = "lanru2001"

access_token = "****************"

url = "https://api.bitbucket.org/2.0/user"

#headers = {'Content-Type':'application/json'}

r = requests.get( url, auth=( user_name , access_token)) 

#r = requests.get( url, headers = { "Authorization" : "(user_name , access_token)"})



print(r.status_code) 
print(r.content)
print(r.json())
