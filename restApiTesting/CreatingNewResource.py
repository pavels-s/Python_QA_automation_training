import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

# Read input json file
file = open('C:\\Users\\pavel\\PycharmProjects\\myPythonProject\\restApiTesting\\CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)
print("--------------------")

# Make POST request with Json body

response = requests.post(url,request_json)
print(response.content)
assert response.status_code == 201
print("--------------------")

# Fetch header from response
print(response.headers.get('Content-length'))

# Parse response to json format
response_json = json.loads(response.text)

# Pick ID using json path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])