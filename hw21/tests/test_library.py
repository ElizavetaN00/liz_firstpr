import pytest
from loguru import logger
from source.library import Book, Reader


@pytest.fixture
def book():
    return Book("The Hobbit", "J.R.R. Tolkien", 400, "0006754023")


@pytest.fixture
def readerV():
    return Reader("Vasya")


@pytest.fixture
def readerP():
    return Reader("Petya")


def test_reserve_book(book, readerV):
    logger.info("Testing positive book reservation")
    readerV.reserve_book(book)
    assert book.is_reserved
    assert book.reserved_by == readerV


def test_reserve_book_when_is_borrowed(book, readerV, readerP):
    logger.info("Testing reservation attempt on a borrowed book")
    readerV.reserve_book(book)
    readerV.get_book(book)

    with pytest.raises(Exception, match="is borrowed. Unable to reserve"):
        readerP.reserve_book(book)


def test_reserve_book_when_is_reserved(book, readerV, readerP):
    logger.info("Testing reservation of already reserved book")
    readerV.reserve_book(book)

    with pytest.raises(Exception):
        readerP.reserve_book(book)


def test_cancel_reserve(book, readerV):
    logger.info("Testing positive reservation cancellation")
    readerV.reserve_book(book)
    readerV.cancel_reserve(book)
    assert not book.is_reserved
    assert book.reserved_by is None


def test_cancel_reserve_not_reserved(book, readerV):
    logger.info("Testing cancel reservation when book is not reserved")

    with pytest.raises(Exception, match="is not reserved"):
        readerV.cancel_reserve(book)


def test_cancel_reserve_by_another_reader(book, readerV, readerP):
    logger.info("Testing cancel reservation by another reader")
    readerV.reserve_book(book)

    with pytest.raises(Exception, match="reserved by another reader"):
        readerP.cancel_reserve(book)


def test_get_book(book, readerV):
    logger.info("Testing positive book getting")
    readerV.reserve_book(book)
    readerV.get_book(book)
    assert book.is_borrowed
    assert book.borrowed_by == readerV
    assert not book.is_reserved


def test_get_book_not_reserved(book, readerV):
    logger.info("Testing getting book without reservation")

    with pytest.raises(Exception, match="is not reserved. Unable to get"):
        readerV.get_book(book)


def test_return_book(book, readerV):
    logger.info("Testing positive book return")
    readerV.reserve_book(book)
    readerV.get_book(book)
    readerV.return_book(book)
    assert not book.is_borrowed
    assert book.borrowed_by is None


def test_return_book_not_borrowed(book, readerV):
    logger.info("Testing return of the book that was not borrowed")
    readerV.return_book(book)
    assert not book.is_borrowed
