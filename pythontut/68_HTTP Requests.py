'''
google search
status code
request http for hummans

free api

https://httpbin.org
https://financialmodelingprep.com/developer/docs/

'''

import requests

# get requests
# get request general kobhai url ko lekar aayege
req = requests.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=9e0bb9dce3ec9552bc5533246f6af640")
print(req.text)


print(req.status_code)

# post request me end point hota hai aor uske sath data
# send karana padata hai (post request send url with some data )
# example : password is  pass to post request

# url = "www.something.com"
# data = {
#     "p1" : 4,
#     "p2" : 8
# }
# req2 = requests.post(url=url, data=data)

# post request
pload = {'username':'Olivia','password':'123'}
req = requests.post("https://httpbin.org/post",pload)
print(req.text)



