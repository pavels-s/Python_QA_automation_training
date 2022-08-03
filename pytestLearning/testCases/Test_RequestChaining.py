import json
import jsonpath
import requests

# pytest ./Test_RequestChaining.py -s
def test_add_new_student():
    global id
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    fileToOpen = open("C:/Users/pavel/PycharmProjects/Python_QA_automation_training/pytestLearning/testCases/RequestChaining_AddStudent.json", 'r')
    json_request = json.loads(fileToOpen.read())
    response = requests.post(api_url, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

def test_get_details():
    details_url = "https://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(details_url)
    print(response.text)