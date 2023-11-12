*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pirkko  pirkko123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  sinikka  sinikka111
    Output Should Contain  User with username sinikka already exists

Register With Too Short Username And Valid Password
    Input Credentials  ak  aki123456
    Output Should Contain  Username should be at least 3 letters long

Register With Long Enough But Invald Username And Valid Password
    Input Credentials  12345  1q2w3e4r
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  birgitta  gigi123
    Output Should Contain  Password should be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  mirjami  mirkkumirkku
    Output Should Contain  Password should not contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  sinikka  sinikka123
    Input New Command
