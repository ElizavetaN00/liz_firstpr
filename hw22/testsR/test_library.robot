*** Settings ***
Library  OperatingSystem
Library  Collections
Library  BuiltIn
Library  ../library.py

*** Keywords ***
Create Book
    [Arguments]  ${title}  ${author}  ${pages}  ${isbn}
    ${book}=  Evaluate  library.Book("${title}", "${author}", ${pages}, "${isbn}")
    Set Test Variable  ${BOOK}  ${book}
    Should Be Equal  ${book.book_name}  ${title}
    Should Be Equal  ${book.author}  ${author}
    Should Be Equal As Numbers  ${book.num_pages}  ${pages}
    Should Be Equal  ${book.isbn}  ${isbn}

Create Reader
    [Arguments]  ${name}
    ${reader}=  Evaluate  library.Reader("${name}")
    Set Test Variable  ${READER}  ${reader}
    Should Be Equal  ${reader.name}  ${name}

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
    ${is_reserved}=  Evaluate  $BOOK.is_reserved
    Should Be True  ${is_reserved}

Reserve Already Reserved Book Fail
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    ${is_reserved}=  Evaluate  $BOOK.is_reserved
    Should Be True  ${is_reserved}
    ${reserved_by}=  Evaluate  $BOOK.reserved_by.name
    Should Be Equal  ${reserved_by}  Vasya
    Reserve Check Fail  Petya  reserved

Cancel Reservation
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Cancel Reservation
    ${is_reserved}=  Evaluate  $BOOK.is_reserved
    ${reserved_by}=  Evaluate  $BOOK.reserved_by
    Should Be True  not ${is_reserved}
    Should Be True  $reserved_by is None

Cancel Reservation By Other Reader Fail
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    ${is_reserved}=  Evaluate  $BOOK.is_reserved
    Should Be True  ${is_reserved}
    ${reserved_by}=  Evaluate  $BOOK.reserved_by.name
    Should Be Equal  ${reserved_by}  Vasya
    Cancel Reservation Check Fail  Petya  another reader

Borrow Book
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Borrow Book
    ${is_borrowed}=  Evaluate  $BOOK.is_borrowed
    Should Be True  ${is_borrowed}

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
    ${is_borrowed}=  Evaluate  $BOOK.is_borrowed
    Should Be True  not ${is_borrowed}

Borrow Without Reservation Fail
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Petya
    Borrow Check Fail  Petya  not reserved
    ${is_borrowed}=  Evaluate  $BOOK.is_borrowed
    Should Be True  not ${is_borrowed}

Borrow By Other Reader Fail
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Create Reader  Petya
    Borrow Check Fail  Petya  another reader
    ${is_borrowed}=  Evaluate  $BOOK.is_borrowed
    ${borrowed_by}=  Evaluate  $BOOK.borrowed_by.name if $BOOK.borrowed_by else None
    Should Be True  not ${is_borrowed}
    Should Be True  $borrowed_by is None

Return Book
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Reserve Book
    Borrow Book
    Return Book
    ${is_borrowed}=  Evaluate  $BOOK.is_borrowed
    Should Be True  not ${is_borrowed}

Return Book Not Borrowed
    Create Book  The Hobbit  J.R.R. Tolkien  400  0006754023
    Create Reader  Vasya
    Return Book
    ${is_borrowed}=  Evaluate  $BOOK.is_borrowed
    Should Be True  not ${is_borrowed}
