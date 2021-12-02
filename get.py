import time
import requests
import json
import os

#user = str(input("enter your name"))
id= input("what your roll number?\n")
payload= {
    "id": id,
}
r = requests.get('Enter_Your_Api_Link_Here', params=payload)
#print(r)

print(r.text)
#print(r.url)
