*** Settings ***
Library  OperatingSystem
Library  Collections
Library  ../bank.py

*** Keywords ***
Create Bank
    ${bank}=  Evaluate  bank.Bank()
    Set Test Variable  ${BANK}  ${bank}

Register Client
    [Arguments]  ${client_id}  ${name}
    Call Method  ${BANK}  register_client  ${client_id}  ${name}

Client Check Exist
    [Arguments]  ${client_id}
    Dictionary Should Contain Key  ${BANK.clients}  ${client_id}

Register Check Fail
    [Arguments]  ${client_id}  ${name}  ${error}
    Run Keyword And Expect Error
    ...    *${error}*
    ...    Call Method  ${BANK}  register_client  ${client_id}  ${name}

Open Deposit
    [Arguments]  ${client_id}  ${amount}  ${years}
    ${amount}=  Convert To Number  ${amount}
    ${years}=  Convert To Integer  ${years}
    Call Method  ${BANK}  open_deposit_account  ${client_id}  ${amount}  ${years}

Deposit Check Exist
    [Arguments]  ${client_id}
    Dictionary Should Contain Key  ${BANK.deposits}  ${client_id}

Open Deposit Check Fail
    [Arguments]  ${client_id}  ${amount}  ${years}  ${error}
    Run Keyword And Expect Error
    ...  *${error}*
    ...  Call Method  ${BANK}  open_deposit_account  ${client_id}  ${amount}  ${years}

Calculate Interest Rate
    [Arguments]  ${client_id}
    ${result}=  Call Method  ${BANK}  calc_deposit_interest_rate  ${client_id}
    [Return]  ${result}

Calculate Interest Rate Fail
    [Arguments]  ${client_id}  ${error}
    Run Keyword And Expect Error
    ...  *${error}*
    ...  Call Method  ${BANK}  calc_deposit_interest_rate  ${client_id}

Close Deposit
    [Arguments]  ${client_id}
    Call Method  ${BANK}  close_deposit  ${client_id}

Deposit Check Not Exist
    [Arguments]  ${client_id}
    Dictionary Should Not Contain Key  ${BANK.deposits}  ${client_id}


*** Test Cases ***
Register New Client
    Create Bank
    Register Client  0000001  Elizaveta
    Client Check Exist  0000001
    Should Be Equal  ${BANK.clients['0000001']}  Elizaveta

Register Existing Client Fail
    Create Bank
    Register Client  0000001  Elizaveta
    Register Check Fail  0000001  Mike  Client was registered before

Open Deposit For Registered Client
    Create Bank
    Register Client  0000001  Elizaveta
    Open Deposit  0000001  1000  1
    Deposit Check Exist  0000001
    ${deposit}=  Evaluate  $BANK.deposits["0000001"]
    Should Be Equal As Numbers  ${deposit['start_balance']}  1000
    Should Be Equal As Numbers  ${deposit['years']}  1
    Should Be Equal As Numbers  ${deposit['current_balance']}  1000

Open Deposit For Unregistered Client Fail
    Create Bank
    Open Deposit Check Fail  0000001  1000  1  Client was not registered

Open Same Deposit Fail
    Create Bank
    Register Client  0000001  Elizaveta
    Open Deposit  0000001  1000  1
    Open Deposit Check Fail  0000001  2000  1  Deposit was already opened

Calculate Deposit Interest Rate
    Create Bank
    Register Client  0000001  Elizaveta
    Open Deposit  0000001  1000  1
    ${result}=  Calculate Interest Rate  0000001
    Should Be Equal As Numbers  ${result}  1104.713067441297  precision=0.0001

Calculate Interest Without Deposit Fail
    Create Bank
    Register Client  0000001  Elizaveta
    Calculate Interest Rate Fail  0000001  No deposit found for this client

Close Deposit Account
    Create Bank
    Register Client  0000001  Elizaveta
    Open Deposit  0000001  1000  1
    Close Deposit  0000001
    Deposit Check Not Exist  0000001
    Calculate Interest Rate Fail  0000001  No deposit found for this client
