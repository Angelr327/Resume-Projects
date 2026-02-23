import requests

import http.client

conn = http.client.HTTPSConnection("tech-news3.p.rapidapi.com")

headers = {
    'Content-Type': "application/json"
}

conn.request("Get",  "/%7Bsource%7D", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))