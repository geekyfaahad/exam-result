import time
import requests
import json
import os
name = str(input("enter your name?\n"))
marks = int(input("enter your marks?\n"))
#print(name,marks)
payload = {
    "Name": name,
    "Marks": marks,
    }
jsonobject = json.dumps(payload, indent = 6)
with open("sample.json", "a") as outfile:
    outfile.write(""+jsonobject+"\n")
r = requests.post("Enter_Your_Api_Here", json=payload)
time.sleep(1.5)
print ("Thanks for submitting the request")
