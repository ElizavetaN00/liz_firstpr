class Bank:
    def __init__(self, clients=None, deposits=None):
        self.clients = clients if clients is not None else {}
        self.deposits = deposits if deposits is not None else {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            raise ValueError("Client was registered before")
        self.clients[client_id] = name

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            raise ValueError("Client was not registered")
        if client_id in self.deposits:
            raise ValueError("Deposit was already opened for this client")
        self.deposits[client_id] = {
            'start_balance': start_balance,
            'years': years,
            'current_balance': start_balance
        }

    def calc_deposit_interest_rate(self, client_id):
        if client_id not in self.deposits:
            raise ValueError("No deposit found for this client")
        deposit = self.deposits[client_id]
        start_balance = deposit['start_balance']
        years = deposit['years']
        monthly_rate = 0.10 / 12
        months = years * 12
        current_balance = start_balance
        for i in range(months):
            current_balance *= (1 + monthly_rate)
        final_balance = current_balance
        deposit['current_balance'] = final_balance
        return final_balance

    def close_deposit(self, client_id):
        if client_id not in self.deposits:
            raise ValueError("There's no deposit for this client")
        del self.deposits[client_id]


client_id = "0000001"

bank = Bank()
bank.register_client(client_id=client_id, name="Siarhei")
print(bank.clients)
bank.open_deposit_account(client_id=client_id, start_balance=1000, years=1)
print(bank.deposits)
# assert bank.calc_interest_rate(client_id = client_id) == 1104.71, "<Error message>"
print(f"Client: {bank.clients["0000001"]}, Final balance: {bank.calc_deposit_interest_rate(client_id="0000001")} rub")
bank.close_deposit(client_id=client_id)
print(bank.deposits)


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
            print(f"Book '{self.book_name}' is borrowed. Unable to reserve")
        elif self.is_reserved:
            print(f"Book '{self.book_name}' is reserved. Unable to reserve")
        else:
            self.is_reserved = True
            self.reserved_by = reader
            print(f"Book '{self.book_name}' reserved by {reader.name}")

    def cancel_reserve(self, reader):
        if not self.is_reserved:
            print(f"Book '{self.book_name}' is not reserved")
        elif self.reserved_by != reader:
            print(f"Book '{self.book_name}' is reserved by another reader")
        else:
            self.is_reserved = False
            self.reserved_by = None
            print(f"Reservation of book '{self.book_name}' canceled by {reader.name}")

    def get_book(self, reader):
        if self.is_borrowed:
            print(f"Book '{self.book_name}' is borrowed. Unable to get")
        elif not self.is_reserved:
            print(f"Book '{self.book_name}' is not reserved. Unable to get")
        elif self.reserved_by != reader:
            print(f"Book '{self.book_name}' is reserved by another reader. "
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


book = Book(book_name = "The Hobbit", author = "J.R.R. Tolkien",
            num_pages = 400, isbn = "0006754023")
vasya = Reader("Vasya")
petya = Reader("Petya")

vasya.reserve_book(book)
petya.reserve_book(book)
vasya.cancel_reserve(book)

petya.reserve_book(book)
vasya.get_book(book)
petya.get_book(book)
vasya.return_book(book)
petya.return_book(book)
vasya.get_book(book)
