import unittest

from Domain.entities import Book
from exceptions.exceptions import DuplicateIDException_Book, BookNotFoundExcetion
from Repository.book_repo import InMemoryRepository_Book

class TestCaseBookRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = InMemoryRepository_Book('test_repobooks.txt')
        self.repo.delete_all()

    def test_store_book(self):
        a = Book(1540, 'Dune', 'Frank Herbert')
        b = Book(3553, 'Sapiens', 'Yuval Noah Harari')
        self.repo.store_book(a)
        self.assertEqual(self.repo.size(), 1)
        self.repo.store_book(b)
        self.assertEqual(self.repo.size(), 2)
        self.assertEqual(self.repo.search_book(a.getID()), a)

        c = Book(1540, 'The Lord of the Rings', 'John Ronald Reuel Tolkien')
        self.assertRaises(DuplicateIDException_Book, self.repo.store_book, a)

    def test_remove_book(self):
        a = Book(1540, 'Dune', 'Frank Herbert')
        b = Book(3553, 'Sapiens', 'Yuval Noah Harari')
        self.repo.store_book(a)
        self.assertEqual(len(self.repo.get_all_books()), 1)
        self.repo.store_book(b)
        self.assertEqual(len(self.repo.get_all_books()), 2)
        self.assertEqual(self.repo.get_all_books()[0], a)
        self.assertEqual(self.repo.get_all_books()[1], b)
        self.repo.remove_book(3553)
        self.assertEqual(len(self.repo.get_all_books()), 1)

    def test_update_book(self):
        a = Book(1540, 'Dune', 'Frank Herbert')
        self.repo.store_book(a)

        b = Book(1540, 'Sapiens', 'Yuval Noah Harari')
        c = Book(3553, 'Dune', 'Frank Herbert')
        updated_book = self.repo.update_book(b)
        self.assertEqual(updated_book.getTitle(), 'Sapiens')
        self.assertRaises(BookNotFoundExcetion, self.repo.update_book, c)

    def tearDown(self) -> None:
        self.repo.delete_all()