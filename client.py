import requests

for i in range(1, 1000):
    print("initiating request")
    r = requests.get('http://127.0.0.1:5000/')
    print(r.text)