import time
import requests
import json
import os

#user = str(input("enter your name"))
id= input("what your roll number?\n")
payload= {
    "id": id,
}
r = requests.get('https://fakestoreapi.com/users/1', params=payload)
#print(r)

print(r.text)
#print(r.url)
