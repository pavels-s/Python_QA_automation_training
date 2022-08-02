import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

# Send Get request
response = requests.get(url)
print(response.content)
print("---------")

# Parse respond to Json format
json_response = json.loads(response.text)
print(json_response)
print("---------")

# Fetch value using Json path
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])
assert pages[0] == 2
print("---------")

first_name = jsonpath.jsonpath(json_response,'data[3].first_name')
print(first_name[0])
print("---------")

for i in range(0,3):
    last_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].last_name')
    print(last_name[0])
