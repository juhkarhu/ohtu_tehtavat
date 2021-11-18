*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Home Page Should Be Open 
    Title Should Be  Ohtu Application

Register Page Should Be Open
    Title Should Be  Register

Go To Login Page
    Go To  ${LOGIN URL}

Go To Home Page
    Go To  ${HOME URL}


# Click Link
#     [Arguments]  ${login}
#     Click Link ${Login}