class Book:
    def __init__(self, id, title, author):
        """
        Creeaza o noua carte cu id-ul id, titlul cartii titlu si autorul cartii autor
        :param id: id-ul cartii
        :type id: int
        :param title: titlul cartii
        :type title: str
        :param author: autorul cartii
        :type author: str
        """
        self.__id = id
        self.__title = title
        self.__author = author

    def getID(self):
        return self.__id

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def setID(self, new_id):
        self.__id = new_id

    def setTitle(self, new_title):
        self.__title = new_title

    def setAutor(self, new_author):
        self.__author = new_author

    def __eq__(self, other):
        """
            Verifica egalitatea carte1==carte2
            :param other: cartea cu care se compara
            :type other: Book
            :return: True daca cartea curenta este egala cu cartea other (daca au acelasi titlu si autor), False altfel
            :rtype: bool
            """
        if self.__title == other.getTitle() and self.__author == other.getAuthor() and self.__id == other.getID():
            return True
        return False

    def __str__(self):
        return "ID-ul: " + str(self.getID()) + "; Titlul: " + self.getTitle() + '; Autor: ' + self.getAuthor()


class Client:
    def __init__(self, id, name, CNP):
        """
        Creeaza un nou client cu id-ul id, numele nume si cnp-ul CNP
        :param id: id-ul clientului
        :type id: int
        :param name: numele clientului
        :type name: str
        :param CNP: cnp-ul clientului
        :type CNP: int
        """
        self.__id = id
        self.__name = name
        self.__CNP = CNP

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getCNP(self):
        return self.__CNP

    def setID(self, new_id):
        self.__id = new_id

    def setName(self, new_name):
        self.__name = new_name

    def setCNP(self, new_cnp):
        self.__CNP = new_cnp

    def __eq__(self, other):
        """
            Verifica egalitatea client1==client2
            :param other: clientul cu care se compara
            :type other: Client
            :return: True daca clientul curent este egal cu clientul other (daca au acelasi nume si CNP), False altfel
            :rtype: bool
            """
        if self.__name == other.getName() and self.__CNP == other.getCNP():
            return True
        return False

    def __str__(self):
        return "ID: " + str(self.getID()) + "; Numele: " + self.getName() + '; CNP: ' + str(self.getCNP())


class Loan:
    def __init__(self, Book, Client):
        """
        Creeaza un imprumut
        :param Book: cartea inchiriata
        :type Book: Book
        :param Client: clientul care imprumuta cartea
        :type Client: Client
        """
        self.__book = Book
        self.__client = Client

    def getBook(self):
        return self.__book

    def getClient(self):
        return self.__client

    def __eq__(self, other):
        if self.__book == other.getBook() and self.__client == other.getClient():
            return True

def test_create_loan():
    book = Book(1540, 'Dune', 'Frank Herbert')
    client = Client(1540, 'Deaconu Cristian', 1054373559322)

    test = Loan(book, client)
    assert (test.getBook() == book)
    assert (test.getClient() == client)


def test_equal_loan():
    book = Book(1540, 'Dune', 'Frank Herbert')
    client = Client(1540, 'Deaconu Cristian', 1054373559322)
    book2 = Book(3553, 'Sapiens', 'Yuval Noah Harari')
    client2 = Client(3553, 'Popescu Mihai', 1054373559311)

    test = Loan(book, client)
    test2 = Loan(book2, client2)
    test3 = Loan(book, client)

    assert (test == test3)
    assert (test != test2)


test_equal_loan()
test_create_loan()