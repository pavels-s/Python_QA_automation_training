*** Settings ***
Documentation  This is some documentation in settings
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
Product searching
    [Documentation]  This is some documentation in test cases
    [Tags]  Smoke
    Open Browser  http://www.amazon.com  chrome
    Wait Until Page Contains  Hello, Sign in
    Input Text    id=twotabsearchtextbox    Ferrari 458
    Click Button    xpath=//*[@id='nav-search-submit-button']
    Wait Until Page Contains  results for "Ferrari 458"
    Click Link    xpath=//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/h2/a
    Wait Until Page Contains    Back to results
    Close Browser

*** Keywords ***
