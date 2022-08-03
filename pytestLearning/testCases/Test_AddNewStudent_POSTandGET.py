import requests
import json
import jsonpath


def test_add_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    fileToOpen = open('C:/Users/pavel/PycharmProjects/Python_QA_automation_training/pytestLearning/testCases/RequestJson.json', 'r')
    json_request = json.loads(fileToOpen.read())
    response = requests.post(API_URL, json_request)
    print(response.text)

def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/3398588"
    response = requests.get(API_URL)

    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print("json_response =   " + str(json_response))
    print("jsonpath.jsonpath(json_response, 'data.id')  =    " + str(id))
    assert id[0] == 3398588
    print("response = requests.get(API_URL)  =     " + str(response.text))