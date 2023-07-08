from Repository.loan_repo import InMemoryRepository_Loan
from Domain.entities import Book
from Domain.entities import Client
from Domain.entities import Loan

class LoanService:
    def __init__(self, repo):
        self.__repo = repo

    def rental(self, book, client):
        """
        Inchirierea unei carti
        :param book: cartea care este inchiriata
        :type book: Book
        :param client: clientul care inchiriazaz cartea
        :type client: Client
        """
        loan = Loan(book, client)
        self.__repo.rental(loan)

    def restitution(self, book, client):
        """
            Returnarea unei carti
            :param book: cartea care este returnata
            :type book: Book
            :param client: clientul care returneaza cartea
            :type client: Client
            """
        loan = Loan(book, client)
        self.__repo.restitution(loan)

    def get_all_rentals(self):
        return self.__repo.get_all_rentals()

    def most_rented_books(self):
        return self.__repo.most_rented_books()

    def top_3(self):
        return self.__repo.top_3()

    def most_active_clients(self):
        return self.__repo.most_active_clients()


def test_rental():
    test_repo = InMemoryRepository_Loan()
    test_service = LoanService(test_repo)
    book = Book(1540, 'Dune', 'Frank Herbert')
    client = Client(1540, 'Deaconu Cristian', 1054373559322)

    try:
        test_service.rental(book, client)
        assert True
    except ValueError:
        assert False

def test_restitution():
    test_repo = InMemoryRepository_Loan()
    test_srv = LoanService(test_repo)
    book = Book(1540, 'Dune', 'Frank Herbert')
    client = Client(1540, 'Deaconu Cristian', 1054373559322)
    book2 = Book(3553, 'Sapiens', 'Yuval Noah Harari')
    client2 = Client(3553, 'Popescu Mihai', 1054373559311)

    test_srv.rental(book, client)
    test_srv.rental(book2, client2)
    test_srv.restitution(book, client)
    assert (len(test_srv.get_all_rentals()) == 1)
    try:
        test_srv.restitution(book, client)
        assert False
    except ValueError:
        assert True
    test_srv.restitution(book2, client2)
    assert (len(test_srv.get_all_rentals()) == 0)
