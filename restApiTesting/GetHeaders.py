import requests

headerData = {'T1':"First header value", 'T2':"Second header value"}
response = requests.get('https://httpbin.org/get', headers = headerData)
print(response.text)


