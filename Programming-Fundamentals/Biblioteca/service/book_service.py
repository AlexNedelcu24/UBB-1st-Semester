from Domain.entities import Book
from Domain.validators import BookValidator
from Repository.book_repo import InMemoryRepository_Book
import random

class BookService:
    """
    Responsabil de efectuarea operatiilor cerute de utilizator
    """
    def __init__(self, repo, validator):
        """
        Initializare service
        :param repo: obiectul de tip repo care ne ajuta sa gestionam listei de carti
        :type repo: InMemoryRepository_Book
        :param validator: validator pentru verificarea cartilor
        :type validator: BookValidator
        """
        self.__repo = repo
        self.__validator = validator

    def string_generator(self, size, chars):
        return ''.join(random.choice(chars) for a in range(size))

    def add_random_book(self):
        id = random.randint(1000, 9999)
        author = self.string_generator(9, 'qazwsxedcrfvtgbyhnujmikolp').capitalize() + ' ' + self.string_generator(11, 'qazwsxedcrfvtgbyhnujmikolp')
        title = self.string_generator(10, 'qazwsxedcrfvtgbyhnujmikolp').capitalize()

        b = Book(id, title, author)

        self.__repo.store_book(b)

        return b

    def add_book(self, id, title, author):
        """
        Adaugare carte in lista
        :param id: id-ul cartii
        :type id: int
        :param title: titlul cartii
        :type title: str
        :param author: autorul cartii
        :type author: str
        :return: obiectul de tip Book creat
        :rtype: - ; carte adaugata la repo
        :raises: ValueError daca cartea nu este valida
        """

        b = Book(id, title, author)

        self.__validator.validate_book(b)
        self.__repo.store_book(b)

        return b

    def delete_book(self, id_to_del):
        """
        Sterge cartea dupa id
        :param id_to_del: id-ul cartii care se sterge
        :type id_to_del: int
        :return: cartea stearsa
        :rtype: Book
        :raises: ValueError daca nu exista carte cu id-ul dat
        """

        return self.__repo.remove_book(id_to_del)

    def update_book(self, id, title, author):
        """
            Modificare carte din lista
            :param id: id-ul cartii
            :type id: int
            :param title: titlul noii carti
            :type title: str
            :param author: autorul noii carti
            :type author: str
            :return: -
            :rtype: -
            """

        b = Book(id, title, author)

        self.__validator.validate_book(b)
        self.__repo.update_book(b)

        return b

    def get_all_books(self):
        """
        Returneaza o lista cu toate cartile
        :return: lista de carti
        :rtype: list of Book objects
        """
        return self.__repo.get_all_books()

    def search_book_id(self, id):
        """
        Cauta carte dupa id-ul dat
        :param id: id dat
        :type id: int
        :return: cartea cu identificatorul id/None daca nu exista cartea
        :rtype: Book
        """
        return self.__repo.search_book(id)


def test_add_book():
    repo = InMemoryRepository_Book()
    val = BookValidator()
    test_srv = BookService(repo, val)

    added_book = test_srv.add_book(1540, 'Dune', 'Frank Herbert')
    assert (added_book.getTitle() == 'Dune')
    assert (len(test_srv.get_all_books()) == 1)

    try:
        added_book2 = test_srv.add_book(15402, 'Dune', 'Frank Herbert')
        assert False
    except ValueError:
        assert True


def test_delete_book():
    repo = InMemoryRepository_Book()
    validator = BookValidator()
    test_srv = BookService(repo, validator)

    added_book = test_srv.add_book(1540, 'Dune', 'Frank Herbert')
    added_book2 = test_srv.add_book(3553, 'Sapiens', 'Yuval Noah Harari')

    deleted_book = test_srv.delete_book(1540)
    assert (len(test_srv.get_all_books()) == 1)

    assert (deleted_book.getID() == 1540)
    assert (deleted_book.getTitle() == 'Dune')
    assert (deleted_book.getAuthor() == 'Frank Herbert')

    assert (test_srv.get_all_books()[0].getTitle() == 'Sapiens')

    try:
        deleted_book = test_srv.delete_book(5000)
        assert False

    except ValueError:
        assert True


def test_update_book():
    repo = InMemoryRepository_Book()
    validator = BookValidator()
    test_srv = BookService(repo, validator)

    added_book = test_srv.add_book(1540, 'Dune', 'Frank Herbert')
    added_book2 = test_srv.add_book(3553, 'Sapiens', 'Yuval Noah Harari')

    updated_book = test_srv.update_book(1540, 'The Shining', 'Stephen King')
    assert (len(test_srv.get_all_books()) == 2)
    assert (updated_book.getTitle() == 'The Shining')
    assert (updated_book.getAuthor() == 'Stephen King')

    modified_book_in_list = test_srv.search_book_id(1540)
    unchanged_book = test_srv.search_book_id(3553)

    assert (modified_book_in_list.getTitle() == 'The Shining')
    assert (modified_book_in_list.getAuthor() == 'Stephen King')

    assert (unchanged_book.getTitle() == 'Sapiens')
    assert (unchanged_book.getAuthor() == 'Yuval Noah Harari')


#test_add_book()
#test_delete_book()
#test_update_book()