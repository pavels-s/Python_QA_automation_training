import json
import requests
import jsonpath

def test_oauth_api():
    token_url = "https://thetestingworldapi.com/Token"
    data = {'grant_type':'password', 'username':'admin','password':'pass'}
    response1 = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(response1.json(), 'access_token')

    auth = {'Authorization':'Bearer '+token_value[0]}
    API_URL = "https://thetestingworldapi.com/api/stDetails/1104"
    response = requests.get(API_URL, headers=auth)
    print(response.text)