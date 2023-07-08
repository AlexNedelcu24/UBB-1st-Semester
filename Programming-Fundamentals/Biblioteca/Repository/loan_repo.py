from Domain.entities import Loan
from Domain.entities import Book
from Domain.entities import Client

class InMemoryRepository_Loan:
    def __init__(self):
        self.__loans = []

    def __exist_rental(self, loan):
        """
            Verifica daca clientul a inchiriat deja cartea
            :param loan: imprumutul verificat
            :type loan: Loan
            """
        for l in self.__loans:
            if l == loan:
                return True
        return False

    def rental(self, loan):
        """
            Inchirierea unei carti
            :param loan: imprumutul
            :type loan: Loan
            """
        if self.__exist_rental(loan):
            raise ValueError("Clientul a imprumutat deja aceasta carte")
        self.__loans.append(loan)

    def restitution(self, loan):
        """
            Restituirea unei carti
            :param loan: imprumutul
            :type loan: Loan
            """
        if self.__exist_rental(loan):
            for i in range(len(self.__loans)):
                if self.__loans[i] == loan:
                    self.__loans.pop(i)
                    break
        else:
            raise ValueError("Inchirierea nu exista")

    def get_all_rentals(self):
        return self.__loans

    def most_rented_books(self):
        """
        Cauta cele mai inchiriate carti
        :return: lista cu cele mai inchiriate carti
        """
        max = 0
        most_rented_book_list = []
        rentals = []
        rented_books = []
        for loan in self.__loans:
            if loan.getBook() not in rented_books:
                rented_books.append(loan.getBook())
                rentals.append(1)
            else:
                for i in range(len(rented_books)):
                    if rented_books[i] == loan.getBook():
                        rentals[i] += 1
                        if rentals[i] > max:
                            max = rentals[i]
                        break

        for i in range(len(rented_books)):
            if rentals[i] == max:
                most_rented_book_list.append(rented_books[i])

        return most_rented_book_list

    def top_3(self):
        most_rented_book_list = []
        rentals = []
        rented_books = []
        for loan in self.__loans:
            if loan.getBook() not in rented_books:
                rented_books.append(loan.getBook())
                rentals.append(1)
            else:
                for i in range(len(rented_books)):
                    if rented_books[i] == loan.getBook():
                        rentals[i] += 1
                        break

        for i in range(len(rented_books)-1):
            for j in range(i+1, len(rented_books)):
                if rentals[i]<rentals[j]:
                    x = rentals[i]
                    rentals[i] = rentals[j]
                    rentals[j] = x
                    y = rented_books[i]
                    rented_books[i] = rented_books[j]
                    rented_books[j] = y

        for i in range(0, 3):
            most_rented_book_list.append(rented_books[i])

        return most_rented_book_list

    def most_active_clients(self):
        most_active_clients = []
        rentals = []
        avtive_clients = []
        for loan in self.__loans:
            if loan.getClient() not in avtive_clients:
                avtive_clients.append(loan.getClient())
                rentals.append(1)
            else:
                for i in range(len(avtive_clients)):
                    if avtive_clients[i] == loan.getClient():
                        rentals[i] += 1
                        break

        a = 20/100*len(avtive_clients)

        for i in range(0, a):
            most_active_clients.append(avtive_clients[i])

        return most_active_clients


def test_rental():
    test_repo = InMemoryRepository_Loan()
    book = Book(1540, 'Dune', 'Frank Herbert')
    client = Client(1540, 'Deaconu Cristian', 1054373559322)
    loan = Loan(book, client)
    test_repo.rental(loan)

    assert (len(test_repo.get_all_rentals()) == 1)

def test_restitution():
    test_repo = InMemoryRepository_Loan()
    book = Book(1540, 'Dune', 'Frank Herbert')
    client = Client(1540, 'Deaconu Cristian', 1054373559322)
    book2 = Book(3553, 'Sapiens', 'Yuval Noah Harari')
    client2 = Client(3553, 'Popescu Mihai', 1054373559311)
    loan = Loan(book, client)
    loan2 = Loan(book2, client2)
    test_repo.rental(loan)
    test_repo.rental(loan2)
    test_repo.restitution(loan)
    assert (len(test_repo.get_all_rentals()) == 1)
    try:
        test_repo.restitution(loan)
        assert False
    except ValueError:
        assert True
    test_repo.restitution(loan2)
    assert (len(test_repo.get_all_rentals()) == 0)



