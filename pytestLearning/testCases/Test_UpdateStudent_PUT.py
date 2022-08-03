import requests
import json
import jsonpath

# pytest ./Test_UpdateStudent_PUT.py -s

def test_update_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/3398588"
    fileToOpen = open('C:/Users/pavel/PycharmProjects/Python_QA_automation_training/pytestLearning/testCases/RequestJson.json', 'r')
    json_request = json.loads(fileToOpen.read())
    response = requests.put(API_URL, json_request)
    print(response.text)