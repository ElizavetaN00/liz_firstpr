class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = False
        self.is_borrowed = False
        self.reserved_by = None
        self.borrowed_by = None

    def reserve(self, reader):
        if self.is_borrowed:
            raise Exception(f"Book '{self.book_name}' is borrowed. Unable to reserve")
        elif self.is_reserved:
            raise Exception(f"Book '{self.book_name}' is reserved. Unable to reserve")
        else:
            self.is_reserved = True
            self.reserved_by = reader
            print(f"Book '{self.book_name}' reserved by {reader.name}")

    def cancel_reserve(self, reader):
        if not self.is_reserved:
            raise Exception(f"Book '{self.book_name}' is not reserved")
        elif self.reserved_by != reader:
            raise Exception(f"Book '{self.book_name}' is reserved by another reader")
        else:
            self.is_reserved = False
            self.reserved_by = None
            print(f"Reservation of book '{self.book_name}' canceled by {reader.name}")

    def get_book(self, reader):
        if self.is_borrowed:
            raise Exception(f"Book '{self.book_name}' is borrowed. Unable to get")
        elif not self.is_reserved:
            raise Exception(f"Book '{self.book_name}' is not reserved. Unable to get")
        elif self.reserved_by != reader:
            raise Exception(f"Book '{self.book_name}' is reserved by another reader. "
                  f"Unable to get")
        else:
            self.is_borrowed = True
            self.borrowed_by = reader
            self.is_reserved = False
            self.reserved_by = None
            print(f"Book '{self.book_name}' was handed to reader {reader.name}")

    def return_book(self, reader):
        if not self.is_borrowed:
            print(f"Book '{self.book_name}' is not borrowed. "
                  f"Cannot return")
        elif self.borrowed_by != reader:
            print(f"Book '{self.book_name}' is borrowed by another reader. "
                  f"Cannot return")
        else:
            self.is_borrowed = False
            self.borrowed_by = None
            print(f"Book '{self.book_name}' returned by {reader.name}")


class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        book.reserve(self)

    def cancel_reserve(self, book):
        book.cancel_reserve(self)

    def get_book(self, book):
        book.get_book(self)

    def return_book(self, book):
        book.return_book(self)
