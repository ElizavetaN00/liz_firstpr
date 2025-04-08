import unittest
import sys
import os
from hw12.hh12 import Bank, Book, Reader

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.clt_id = "0000001"
        self.bank.register_client(client_id=self.clt_id, name="Siarhei")

    def test_register_client(self):
        self.assertEqual(self.bank.clients[self.clt_id], "Siarhei")

    def test_register_same_client(self):
        with self.assertRaises(ValueError) as e:
            self.bank.register_client(client_id=self.clt_id, name="New client")
        self.assertEqual(str(e.exception), "Client was registered before")

    def test_open_deposit(self):
        self.bank.open_deposit_account(client_id=self.clt_id,
                                       start_balance=1000, years=1)
        self.assertIn(self.clt_id, self.bank.deposits)

    def test_open_deposit_not_registered_client(self):
        with self.assertRaises(ValueError) as e:
            self.bank.open_deposit_account(client_id="0000002",
                                           start_balance=1000, years=1)
        self.assertEqual(str(e.exception), "Client was not registered")

    def test_open_same_deposit(self):
        self.bank.open_deposit_account(client_id=self.clt_id,
                                       start_balance=1000, years=1)
        with self.assertRaises(ValueError) as e:
            self.bank.open_deposit_account(client_id=self.clt_id,
                                           start_balance=10000, years=3)
        self.assertEqual(str(e.exception), "Deposit was already "
                                           "opened for this client")

    def test_calc_interest_rate(self):
        self.bank.open_deposit_account(client_id=self.clt_id,
                                       start_balance=1000, years=1)
        final_balance = self.bank.calc_deposit_interest_rate(client_id=self.clt_id)
        self.assertAlmostEqual(final_balance, 1104.713067441297)

    def test_calc_interest_no_opened_deposit(self):
        with self.assertRaises(ValueError) as e:
            self.bank.calc_deposit_interest_rate(client_id="0000002")
        self.assertEqual(str(e.exception), "No deposit found for this client")

    def test_close_deposit(self):
        self.bank.open_deposit_account(client_id=self.clt_id,
                                       start_balance=1000, years=1)
        self.bank.close_deposit(client_id=self.clt_id)
        self.assertNotIn(self.clt_id, self.bank.deposits)

    def test_close_deposit_no_client_opened(self):
        with self.assertRaises(ValueError) as e:
            self.bank.close_deposit(client_id="0000002")
        self.assertEqual(str(e.exception), "There's no deposit for this client")


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book(book_name="The Hobbit", author="J.R.R. Tolkien",
                         num_pages=400, isbn="0006754023")
        self.readerV = Reader("Vasya")
        self.readerP = Reader("Petya")

    def test_reserve_book(self):
        self.readerV.reserve_book(self.book)
        self.assertTrue(self.book.is_reserved)
        self.assertEqual(self.book.reserved_by, self.readerV)

    def test_reserve_book_when_is_borrowed(self):
        self.book.is_borrowed = True
        with self.assertRaises(Exception):
            self.readerV.reserve_book(self.book)

    def test_reserve_book_when_is_reserved(self):
        self.readerV.reserve_book(self.book)
        with self.assertRaises(Exception):
            self.readerP.reserve_book(self.book)

    def test_cancel_reserve(self):
        self.readerV.reserve_book(self.book)
        self.assertTrue(self.book.is_reserved)
        self.assertEqual(self.book.reserved_by, self.readerV)
        self.readerV.cancel_reserve(self.book)
        self.assertFalse(self.book.is_reserved)
        self.assertIsNone(self.book.reserved_by)

    def test_cancel_reserve_not_reserved(self):
        self.assertFalse(self.book.is_reserved)
        self.assertIsNone(self.book.reserved_by)
        with self.assertRaises(Exception) as e:
            self.readerV.cancel_reserve(self.book)
        self.assertEqual(str(e.exception), "Book 'The Hobbit' is not reserved")

    def test_cancel_reserve_by_another_reader(self):
        self.readerV.reserve_book(self.book)
        with self.assertRaises(Exception) as e:
            self.readerP.cancel_reserve(self.book)
        self.assertEqual(str(e.exception), "Book 'The Hobbit' is "
                                           "reserved by another reader")
        self.assertTrue(self.book.is_reserved)
        self.assertEqual(self.book.reserved_by, self.readerV)

    def test_get_book(self):
        self.readerV.reserve_book(self.book)
        self.readerV.get_book(self.book)
        self.assertTrue(self.book.is_borrowed)
        self.assertEqual(self.book.borrowed_by, self.readerV)

    def test_get_book_not_reserved(self):
        with self.assertRaises(Exception) as e:
            self.readerV.get_book(self.book)
        self.assertEqual(str(e.exception), "Book 'The Hobbit' is not "
                                           "reserved. Unable to get")

    def test_return_book(self):
        self.readerV.reserve_book(self.book)
        self.readerV.get_book(self.book)
        self.readerV.return_book(self.book)
        self.assertFalse(self.book.is_borrowed)
        self.assertIsNone(self.book.borrowed_by)

    def test_return_book_not_borrowed(self):
        self.readerV.return_book(self.book)
        self.assertFalse(self.book.is_borrowed)


if __name__ == '__main__':
    unittest.main()
