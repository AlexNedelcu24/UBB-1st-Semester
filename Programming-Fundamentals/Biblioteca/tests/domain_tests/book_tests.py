import unittest

from Domain.entities import Book
from Domain.validators import BookValidator
from exceptions.exceptions import ValidationException

class TestCaseBookDom(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = BookValidator()

    def test_create_book(self):
        book1 = Book(1540, 'Dune', 'Frank Herbert')
        self.assertTrue(book1.getID() == 1540)
        self.assertTrue(book1.getTitle() == 'Dune')
        self.assertTrue(book1.getAuthor() == 'Frank Herbert')

        book1.setID(2010)
        book1.setTitle('Altered Carbon')
        book1.setAuthor('Richard K. Morgan')

        self.assertTrue(book1.getTitle() == 'Altered Carbon')
        self.assertTrue(book1.getID() == 2010)
        self.assertTrue(book1.getAuthor() == 'Richard K. Morgan')

    def test_equal_books(self):
        book1 = Book(2010, 'Dune', 'Frank Herbert')
        book2 = Book(2010, 'Dune', 'Frank Herbert')

        self.assertEqual(book1, book2)

        book3 = Book(3553, 'Sapiens', 'Yuval Noah Harari')
        self.assertNotEqual(book1, book3)

    def test_BookValidator(self):
        book1 = Book(1540, 'Dune', 'Frank Herbert')
        book2 = Book(3553, 'Sapiens', 'Yuval Noah Harari')
        self.__validator.validate_book(book1)
        self.__validator.validate_book(book2)

        #b = Book(1547, 'Dune', 'Herbert')
        #self.assertRaises(ValidationException, self.__validator.validate_book, b)
        #b2 = Book(355, '', 'Yuval Noah Harari')
        #self.assertRaises(ValidationException, self.__validator.validate_book, b2)