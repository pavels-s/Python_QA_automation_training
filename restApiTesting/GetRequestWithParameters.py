import requests

paramDictionary = {'name':"Name value", 'email':"Email value", 'number':"Number value"}
response = requests.get('https://httpbin.org/get', params=paramDictionary)
print(response.text)