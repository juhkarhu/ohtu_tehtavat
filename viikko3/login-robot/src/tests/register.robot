*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
  Input Credentials  testaaja  s4l4s4n4
  Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
  Input Credentials  kalle  s4l4s4n4
  Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
  Input Credentials  as  s4l4s4n4
  Output Should Contain  Username must be formed from letters a-z and be at least 3 characters long

Register With Valid Username And Too Short Password
  Input Credentials  kalle  p4ssu
  Output Should Contain  Password length must be at least 8

Register With Valid Username And Long Enough Password Containing Only Letters
  Input Credentials  kalle  tamaeitoimi
  Output Should Contain  Password must be contain characters and numbers

*** Keywords ***
Input New Command And Create User
    Create User  kalle  s4l41n3nsana
    Input New Command