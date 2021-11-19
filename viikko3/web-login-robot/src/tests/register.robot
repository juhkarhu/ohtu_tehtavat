*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Register With Valid Username And Password
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  kalevi
    Set Password  kalle123
    Set Password_Confirmation  kalle123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  aa
    Set Password  kalle123
    Set Password_Confirmation  kalle123
    Submit Registration
    Register Should Fail With Message  Username must be formed from letters a-z and be at least 3 characters long

Register With Valid Username And Too Short Password
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  pekka
    Set Password  kle23
    Set Password_Confirmation  kle23
    Submit Registration
    Register Should Fail With Message  Password length must be at least 8

Register With Nonmatching Password And Password Confirmation
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  uolevi
    Set Password  kalle123
    Set Password_Confirmation  kalle23
    Submit Registration
    Register Should Fail With Message  Passwords didn't match

Login After Successful Registration
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  pekkarinen
    Set Password  kalle123
    Set Password_Confirmation  kalle123
    Submit Registration
    Register Should Succeed
    Go To Login Page
    Set Username  pekkarinen
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  pekka
    Set Password  kle23
    Set Password_Confirmation  kle23
    Submit Registration
    Register Should Fail With Message  Password length must be at least 8
    Go To Login Page
    Set Username  pekkarinen
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed


*** Keywords ***
Set Password_Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${Password confirmation}

Submit Registration
    Click Button  Register

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Go To Main Page
    Go To Home Page