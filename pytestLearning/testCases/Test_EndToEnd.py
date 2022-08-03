import json
import jsonpath
import requests

# Adding a student https://thetestingworldapi.com/Help/Api/POST-api-studentsDetails
def test_add_new_data():
    APP_URL = "https://thetestingworldapi.com/api/studentsDetails"
    # Reading a file
    fileToOpen = open('C:/Users/pavel/PycharmProjects/Python_QA_automation_training/pytestLearning/testCases/RequestJson.json', 'r')
    # Convert to a json format
    request_json = json.loads(fileToOpen.read())
    # Creating a request
    response = requests.post(APP_URL, request_json)
    # pytest ./Test_EndToEnd.py -s
    print(response.text)
    print("-----------------------------------")
    # Fetch id
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])


    # Adding student technical details https://thetestingworldapi.com/Help/Api/POST-api-technicalskills
    TECH_APP_URL = "https://thetestingworldapi.com/api/technicalskills"
    techFileToOpen = open('C:/Users/pavel/PycharmProjects/Python_QA_automation_training/pytestLearning/testCases/TechRequestJson.json', 'r')
    request_json = json.loads(techFileToOpen.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(TECH_APP_URL, request_json)
    print(response.text)


    # Adding student address datails https://thetestingworldapi.com/Help/Api/POST-api-addresses
    ADDRESS_APP_URL = "https://thetestingworldapi.com/api/addresses"
    addressFileToOpen = open('C:/Users/pavel/PycharmProjects/Python_QA_automation_training/pytestLearning/testCases/AddressRequestJson.json', 'r')
    request_json = json.loads(addressFileToOpen.read())
    response = requests.post(ADDRESS_APP_URL, request_json)
    print(response.text)


    # Fetching completed result https://thetestingworldapi.com/Help/Api/GET-api-FinalStudentDetails-id
    FINAL_APP_URL = "https://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(FINAL_APP_URL)
    print(response.text)