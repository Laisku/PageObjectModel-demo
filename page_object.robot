*** Settings ***
Library           WebDemoLibrary.py
Test Teardown     Close browser

*** Test Cases ***
Login and logout
    Open browser to login page
    Login    demo    mode
    Welcome page should be open
    Logout
    Login page should be open

Invalid login
    Open browser to login page
    Login    demo    invalid    next_page=Error
    Error page should be open
