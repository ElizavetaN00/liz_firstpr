*** Settings ***
Library  OperatingSystem
Library  Collections
Library  ../library.py

*** Keywords ***
Create Book
    [Arguments]  ${title}  ${author}  ${pages}  ${isbn}
    ${book}=  Evaluate  library.Book("${title}", "${author}", ${pages}, "${isbn}")
    Set Test Variable  ${BOOK}  ${book}

Create Reader
    [Arguments]  ${name}
    ${reader}=  Evaluate  library.Reader("${name}")
    Set Test Variable  ${READER}  ${reader}

Reserve Book
    Call Method  ${READER}  reserve_book  ${BOOK}

Reserve Check Fail
    [Arguments]  ${reader_name}  ${error}
    ${other}=  Evaluate  library.Reader("${reader_name}")
    Run Keyword And Expect Error  *${error}*  Call Method  ${other}  reserve_book  ${BOOK}

Cancel Reservation
    Call Method  ${READER}  cancel_reserve  ${BOOK}

Cancel Reservation Check Fail
    [Arguments]  ${reader_name}  ${error}
    ${other}=  Evaluate  library.Reader("${reader_name}")
    Run Keyword And Expect Error  *${error}*  Call Method  ${other}  cancel_reserve  ${BOOK}

Borrow Book
    Call Method  ${READER}  get_book  ${BOOK}

Borrow Check Fail
    [Arguments]  ${reader_name}  ${error}
    ${other}=  Evaluate  library.Reader("${reader_name}")
    Run Keyword And Expect Error  *${error}*  Call Method  ${other}  get_book  ${BOOK}

Return Book
    Call Method  ${READER}  return_book  ${BOOK}

*** Test Cases ***
Reserve Book
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book

Reserve Already Reserved Book Fail
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Reserve Check Fail  Petya  reserved

Cancel Reservation
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Cancel Reservation

Cancel Reservation By Other Reader Fail
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Cancel Reservation Check Fail  Petya  another reader

Borrow Book
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Borrow Book

Get Book After Reservation
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Call Method  ${BOOK}  get_book  ${READER}
    ${is_borrowed}=  Evaluate  $BOOK.is_borrowed
    ${borrowed_by}=  Evaluate  $BOOK.borrowed_by
    ${borrowed_by_name}=  Evaluate  $borrowed_by.name if $borrowed_by else None
    Should Be True  ${is_borrowed}
    Should Be Equal  ${borrowed_by_name}  Vasya

Get Book Without Reservation Fail
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Run Keyword And Expect Error  *not reserved*  Call Method  ${BOOK}  get_book  ${READER}

Borrow Without Reservation Fail
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Petya
    Borrow Check Fail  Petya  not reserved

Borrow By Other Reader Fail
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Create Reader  Petya
    Borrow Check Fail  Petya  another reader

Return Book
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Borrow Book
    Return Book

Return Book Not Borrowed
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Return Book
