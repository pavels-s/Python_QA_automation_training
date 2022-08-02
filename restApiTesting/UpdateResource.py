import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

# Read input json file
file = open('C:\\Users\\pavel\\PycharmProjects\\myPythonProject\\restApiTesting\\CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)

# Make PUT request
response = requests.put(url, request_json)

# Validating response code
assert response.status_code == 200

# Parse response content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])