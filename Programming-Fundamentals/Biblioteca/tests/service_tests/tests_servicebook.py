import unittest

from Domain.validators import BookValidator
from exceptions.exceptions import ValidationException, BookNotFoundExcetion
from Repository.book_repo import InMemoryRepository_Book
from service.book_service import BookService

class TestCaseBookSrv(unittest.TestCase):
    def setUp(self) -> None:
        repo = InMemoryRepository_Book('test_booksrv.txt')
        validator = BookValidator()
        self.__book_srv = BookService(repo, validator)

    def test_add_book(self):
        added_book = self.__book_srv.add_book(1540, 'Dune', 'Frank Herbert')
        self.assertEqual(added_book.getTitle(), 'Dune')
        self.assertEqual(len(self.__book_srv.get_all_books()), 1)

        self.assertRaises(ValidationException, self.__book_srv.add_book, 1112, 'Dune', 'hfdg')

    def test_delete_book(self):
        added_book = self.__book_srv.add_book(1540, 'Dune', 'Frank Herbert')
        added_book2 = self.__book_srv.add_book(3553, 'Sapiens', 'Yuval Noah Harari')

        deleted_book = self.__book_srv.delete_book(1540)
        self.assertEqual(len(self.__book_srv.get_all_books()), 1)

        self.assertEqual(deleted_book.getID(), 1540)
        self.assertEqual(deleted_book.getTitle(), 'Dune')
        self.assertEqual(deleted_book.getAuthor(), 'Frank Herbert')

        self.assertEqual(self.__book_srv.get_all_books()[0].getTitle(), 'Sapiens')


    def test_update_book(self):
        added_book = self.__book_srv.add_book(1540, 'Dune', 'Frank Herbert')
        added_book2 = self.__book_srv.add_book(3553, 'Sapiens', 'Yuval Noah Harari')

        updated_book = self.__book_srv.update_book(1540, 'The Shining', 'Stephen King')
        self.assertEqual(len(self.__book_srv.get_all_books()), 2)
        self.assertEqual(updated_book.getTitle(), 'The Shining')
        self.assertEqual(updated_book.getAuthor(), 'Stephen King')

        modified_book_in_list = self.__book_srv.search_book_id(1540)
        unchanged_book = self.__book_srv.search_book_id(3553)

        self.assertEqual(modified_book_in_list.getTitle(), 'The Shining')
        self.assertEqual(modified_book_in_list.getAuthor(), 'Stephen King')

        self.assertEqual(unchanged_book.getTitle(), 'Sapiens')
        self.assertEqual(unchanged_book.getAuthor(), 'Yuval Noah Harari')