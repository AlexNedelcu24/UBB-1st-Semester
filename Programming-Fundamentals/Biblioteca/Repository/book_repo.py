from Domain.entities import Book
from exceptions.exceptions import DuplicateIDException_Book, BookNotFoundExcetion

class InMemoryRepository_Book:
    """
    Clasa creata pentru a gestiona cartile
    """

    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista cu carti
        """

        f = open(self.__filename, 'r')

        books = []
        lines = f.readlines()
        for line in lines:
            book_id, book_title, book_author = [token.strip() for token in line.split(';')]
            book = Book(int(book_id), book_title, book_author)
            books.append(book)
        f.close()
        return books

    def __save_to_file(self, books):
        """
        Salveaza cartile in fisier
        :param books: lista de carti
        :type books: list of Book
        """

        with open(self.__filename, 'w') as f:
            for book in books:
                book_str = str(book.getID()) + ';' + str(book.getTitle()) + ';' + str(book.getAuthor()) + '\n'
                f.write(book_str)

    def __find_index(self, books, id):
        """
        Gaseste index-ul in lista al cartii cu id-ul dat
        :param id: id-ul dat
        :type id: int
        :return: pozitia din lista a cartii cu id-ul dat
        :rtype: int (>=0, <repo.size()), -1 daca id nu exista
        """
        index = -1
        for i in range(len(books)):
            if books[i].getID() == id:
                index = i
        return index

    def search_book(self, id):
        """
            Cauta cartea cu id-ul dat
            :param id: id-ul dat
            :type id: int
            :return: cartea cu identificator id/None daca nu exista
            :rtype: Book
            """
        books = self.__load_from_file()
        for book in books:
            if book.getID() == id:
                return book
        return None

    def store_book(self, book):
        """
        Adauga o carte in lista
        :param book: cartea de adaugat
        :type book: Book
        :return: - ; lista de carti se modifica prin adaugarea cartii
        :rtype: -
        """
        books = self.__load_from_file()
        if book in books:
            #raise ValueError('Exista deja o carte cu id-ul dat.')
            raise DuplicateIDException_Book()
        books.append(book)
        self.__save_to_file(books)

    def get_all_books(self):
        """
        Returneaza o lista cu toate cartile din biblioteca
        :rtype: list of Book objects
        """
        return self.__load_from_file()

    def remove_book(self, id_to_del):
        """
        Elimina o carte din lista
        :param id_to_del: id-ul cartii care va fi eliminata
        :type id_to_del: int
        :return: cartea stearsa
        :rtype: Book
        :raises: ValueError daca nu exista carte cu id-ul dat
        """
        books = self.__load_from_file()
        index = self.__find_index(books, id_to_del)
        if index == -1:
            #raise ValueError('Nu exista carte cu acest id')
            raise BookNotFoundExcetion()

        del_book = books.pop(index)
        self.__save_to_file(books)
        return del_book

    def update_book(self, new_book):
        """
        Modifica o carte din lista
        :param new_book: cartea modificata
        :type new_book: Book
        :return: - ; lista de carti se modifica prin modificarea cartii
        :rtype: -
        """
        books = self.__load_from_file()
        index = self.__find_index(books, new_book.getID())
        if index == -1:
            #raise ValueError('Nu exista carte cu acest id.')
            raise BookNotFoundExcetion()
        books[index] = new_book
        self.__save_to_file(books)
        return new_book

    def size(self):
        """
        Returneaza numarul de carti in lista
        :rtype: int
        """
        books = self.__load_from_file()
        return len(books)

    def delete_all(self):
        """
        Sterge toate cartile
        """
        self.__save_to_file([])




#test_store_book()
#test_remove_book()
#test_update_book()