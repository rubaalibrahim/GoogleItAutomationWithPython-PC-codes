import os
import requests


source = "/data/feedback/"
files = os.listdir(source)
IP = "<website's IP address>"
for f in files:
    fb = open(source+f)
    data = fb.read().split("\n")
    dic = {"title": data[0], "name": data[1], "data": data[2], "feedback": data[3]}
    response = requests.post("http://{}/feedback".format(IP), json=dic)
    print(response.status_code)