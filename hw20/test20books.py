import unittest
import sys
import os
from hw12.hh12 import Book, Reader

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


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
        self.assertEqual(str(e.exception), "Book 'The Hobbit' "
                                           "is reserved by another reader")
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
