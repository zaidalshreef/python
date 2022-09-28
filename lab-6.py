# from urllib.request import urlopen
# import json

# response = urlopen('https://catfact.ninja/fact')
# dic = json.loads(response.read())
# print(dic)
# print(type(dic))

import requests
import json

res = requests.get('https://catfact.ninja/fact')

res_v1=res.json()
res_v2 = res.text
print(type(res_v2))
json.loads(res_v2)
print(res_v1)
print(type(res_v1))
print(json.loads(res_v2))
print(type(json.loads(res_v2)))