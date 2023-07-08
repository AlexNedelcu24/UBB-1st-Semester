from Domain.entities import Book
from Domain.entities import Client


class BookValidator:
    """
    clasa pentru validarea cartilor
    """

    def validate_book(self, book):
        errors = []
        if len(book.getAuthor().split()) < 2:
            errors.append('Numele autorului trebuie sa aiba cel putin 2 cuvinte.')
        if book.getID() < 1000 or book.getID() > 9999:
            errors.append('ID-ul trebuie sa fie un numar intre 1000 si 9999.')

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)


class ClientValidator:
    """
        clasa pentru validarea clientilor
        """
    def validate_client(self, client):
        errors = []
        if len(client.getName().split()) < 2:
            errors.append('Numele clientului trebuie sa aiba cel putin 2 cuvinte.')
        if client.getID() < 1000 or client.getID() > 9999:
            errors.append('ID-ul trebuie sa fie un numar intre 1000 si 9999.')
        if client.getCNP() < 1000000000000 or client.getCNP() > 9999999999999:
            errors.append('CNP-ul trebuie sa aiba 13 cifre.')

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)



def test_BookValidator():
    validator = BookValidator()
    book1 = Book(1540, 'Dune', 'Frank Herbert')
    book2 = Book(3553, 'Sapiens', 'Yuval Noah Harari')
    validator.validate_book(book1)
    validator.validate_book(book2)

    try:
        book3 = Book(1540, 'Dune', 'Frank')
        validator.validate_book(book3)
        assert False
    except ValueError:
        assert True


    try:
        book4 = Book(15406, 'Dune', 'Frank Herbert')
        validator.validate_book(book4)
        assert False
    except ValueError:
        assert True


def test_ClientValidator():
    validator = ClientValidator()
    client1 = Client(1540, 'Deaconu Cristian', 1054373559322)
    client2 = Client(3553, 'Popescu Mihai', 1054373559311)
    validator.validate_client(client1)
    validator.validate_client(client2)

    try:
        client3 = Client(3553, 'Mihai', 105437359311)
        validator.validate_client(client3)
        assert False
    except ValueError:
        assert True


    try:
        client4 = Client(3553, 'Popescu Mihai', 105439311)
        validator.validate_client(client4)
        assert False
    except ValueError:
        assert True


test_BookValidator()
test_ClientValidator()