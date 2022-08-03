import requests
import json
import jsonpath

def test_delete_student():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/3398588"
    response = requests.delete(API_URL)
    print(response.text)

def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/3398588"
    response = requests.get(API_URL)
    json_response = response.json()
    print("json_response =   " + str(json_response))
    print("jsonpath.jsonpath(json_response, 'data.id')  =    " + str(id))
    assert id[0] == 3398588
    print("response = requests.get(API_URL)  =     " + str(response.text))