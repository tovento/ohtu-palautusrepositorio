*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  iivari
    Set Password  iivari123
    Confirm Password  iivari123
    Submit Credentials
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set Username  li
    Set Password  li123456
    Confirm Password  li123456
    Submit Credentials
    Registering Should Fail With Message  Username should be at least 3 letters long

Register With Valid Username And Invalid Password
    Set Username  martina
    Set Password  martinajee
    Confirm Password  martinajee
    Submit Credentials
    Registering Should Fail With Message  Password should not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  pentti
    Set Password  pentti123
    Confirm Password  pentti456
    Submit Credentials
    Registering Should Fail With Message  Passwords don't match

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
