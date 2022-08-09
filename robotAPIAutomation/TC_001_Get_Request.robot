*** Settings ***
Library  RequestsLibrary
Library  Collections



*** Variables ***
${base_URL}  https://thetestingworldapi.com/
${student_ID}  1


*** Test Cases ***
TC_001_Get_Request
    Create Session    Get_Students_Details    ${base_URL}
    # Adding relative URL
    ${response} =  GET on Session  Get_Students_Details  ${base_URL}
    Log To Console    ${response.status_code}


TC_001_Fetch_Students_Details_By_ID
    Create Session  Fetch_Data    ${base_URL}
    ${response} =  GET On Session    Fetch_Data    api/studentsDetails/${student_ID}
    ${actual_status_code} =  Convert To String    ${response.status_code}
    Should Be Equal    ${actual_status_code}  200
    Log To Console    ${response.content}


