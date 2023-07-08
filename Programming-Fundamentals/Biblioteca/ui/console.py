from termcolor import colored
from utils.sort import quickSort, gnomeSort, compare_book, compare_client

class Console:
    def __init__(self, srv1, srv2, srv3):
        self.__srv_book = srv1
        self.__srv_client = srv2
        self.__srv_loan = srv3

    def __show_all_books(self):
        """
        Afiseaza toate cartile
        """
        book_list = self.__srv_book.get_all_books()
        if len(book_list) == 0:
            print('Nu exista carti in lista.')
        else:
            print('Lista de carti:')
            for book in book_list:
                print(colored(book, 'cyan'))

    def __show_all_clients(self):
        """
        Afiseaza toti clientii
        """
        client_list = self.__srv_client.get_all_clients()
        if len(client_list) == 0:
            print('Nu exista clienti in lista.')
        else:
            print('Lista de clienti:')
            for client in client_list:
                print(colored(client, 'cyan'))

    def __show_all_loans(self):
        """
        Afiseaza toate inchirierile
        """
        loans_list = self.__srv_loan.get_all_rentals()
        if len(loans_list) == 0:
            print('Nu exista inchirieri.')
        else:
            print('Lista de inchirieri:')
            for loan in loans_list:
                print('Clientul: ', loan.getClient(), ' a inchiriat cartea: ', loan.getBook())

    def __add_book(self):
        """
        Adauga cartea cu datele citite
        """
        titlu = input('Titlul cartii:')
        autor = input('Autorul cartii:')
        try:
            id = int(input('ID-ul(format din 4 cifre):'))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            added_book = self.__srv_book.add_book(id, titlu, autor)
            print('Cartea cu titlul ', added_book.getTitle(), 'si autorul', added_book.getAuthor(),
                  ' s-a adaugat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __add_random_book(self):
        added_book = self.__srv_book.add_random_book()
        print('Cartea cu titlul ', added_book.getTitle(), ',autorul ', added_book.getAuthor(), 'si ID-ul ',
              added_book.getID(), ' s-a adaugat cu succes.')

    def __generate_random_books_list(self):
        for i in range(0, 9):
            self.__add_random_book()

    def __add_client(self):
        """
        Adauga client cu datele citite
        """
        nume = input('Numele clientului :')

        try:
            id = int(input('ID-ul(format din 4 cifre):'))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            cnp = int(input('CNP-ul'))
        except ValueError:
            print(colored('CNP-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            added_client = self.__srv_client.add_client(id, nume, cnp)
            print('Clientul cu numele ', added_client.getName(), ' si CNP-ul ', added_client.getCNP(),
                  ' s-a adaugat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __add_random_client(self):
        added_client = self.__srv_client.add_random_client()
        print('Clientul cu numele ', added_client.getName(), ',CNP-ul ', added_client.getCNP(), 'si ID-ul ',
              added_client.getID(), ' s-a adaugat cu succes.')

    def __generate_random_clients_list(self):
        for i in range(0, 9):
            self.__add_random_client()

    def __delete_book(self):
        """
        Sterge carte dupa id
        """
        try:
            id = int(input('ID-ul cartii care se sterge: '))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            deleted_book = self.__srv_book.delete_book(id)
            print('Cartea cu titlul', deleted_book.getTitle(), ',autorul', deleted_book.getAuthor(),
                  'si ID-ul: ', deleted_book.getID(), 's-a sters cu succes')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __delete_client(self):
        """
        Sterge client dupa id
        """
        try:
            id = int(input('ID-ul clientului care se sterge: '))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            deleted_client = self.__srv_client.delete_client(id)
            print('Clientul cu numele', deleted_client.getName(), ',CNP-ul', deleted_client.getCNP(),
                  'si ID-ul: ', deleted_client.getID(), 's-a sters cu succes')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __update_book(self):
        """
        Actualizeaza cartea cu datele citite dupa id
        """
        titlu = input('Titlul noii carti:')
        autor = input('Autorul noii carti:')
        try:
            id = int(input('ID-ul(format din 4 cifre) cartii pe care o actualizam:'))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            self.__srv_book.update_book(id, titlu, autor)
            print('Modificarea s-a efectuat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __update_client(self):
        """
        Actualizeaza client cu datele citite dupa id
        """
        nume = input('Numele noului client:')
        cnp = input('CNP-ul noului client:')
        try:
            id = int(input('ID-ul(format din 4 cifre) clientului pe care il actualizam:'))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            self.__srv_client.update_client(id, nume, cnp)
            print('Modificarea s-a efectuat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __search_book(self):
        """
        Cauta o carte dupa id
        """
        try:
            id = int(input('ID-ul(format din 4 cifre) cartii pe care o actualizam:'))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            book = self.__srv_book.search_book_id(id)
            print('Cartea cu id-ul: ', book.getID(), ' este: ', book.getTitle(), ' scrisa de: ', book.getAuthor())
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __search_client(self):
        """
        Cauta un client dupa id
        """
        try:
            id = int(input('ID-ul(format din 4 cifre) clientului pe care il actualizam:'))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            client = self.__srv_client.search_client_id(id)
            print('Clientul cu id-ul: ', client.getID(), ' este: ', client.getName(), ' cu CNP-ul: ', client.getCNP())
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __rental(self):
        """
        Inchiriaza o carte unui client
        """
        try:
            id_client = int(input('ID-ul(format din 4 cifre) clientului care doreste sa imprumute o carte:'))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            id_carte = int(input('ID-ul(format din 4 cifre) cartii care o sa fie imprumutata:'))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            book = self.__srv_book.search_book_id(id_carte)
            client = self.__srv_client.search_client_id(id_client)
            self.__srv_loan.rental(book, client)
            print("Cartea a fost inchiriata cu succes")
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __restitution(self):
        """
        Clientul returneaza o carte
        """
        try:
            id_client = int(input('ID-ul(format din 4 cifre) clientului care doreste sa returneze o carte:'))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            id_carte = int(input('ID-ul(format din 4 cifre) cartii care o sa fie returnata:'))
        except ValueError:
            print(colored('ID-ul trebuie sa fie un numar.', 'red'))
            return

        try:
            book = self.__srv_book.search_book_id(id_carte)
            client = self.__srv_client.search_client_id(id_client)
            self.__srv_loan.restitution(book, client)
            print("Cartea a fost returnata cu succes")
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __most_rented_books(self):
        for book in self.__srv_loan.most_rented_books():
            print(colored(book, 'cyan'))

    def __top_3(self):
        print(colored("Primele 3 carti sunt: ", 'green'))
        for book in self.__srv_loan.top_3():
            print(colored(book, 'cyan'))

    def __most_active_clients(self):
        print(colored("Cei mai activi clienti sunt: ", 'green'))
        for client in self.__srv_loan.most_active_clients():
            print(colored(client, 'cyan'))

    def __sort_title_author(self):
        book_list = self.__srv_book.get_all_books()
        books = quickSort(book_list, key=None, cmp=compare_book)
        for book in books:
            print(colored(book, 'cyan'))

    def __sort_name_cnp(self):
        client_list = self.__srv_client.get_all_clients()
        clients = gnomeSort(client_list, key=None, cmp=compare_client)
        for client in clients:
            print(colored(client, 'cyan'))


    def command_ui(self):
        while True:
            print(
                'Comenzi disponibile: add_book, add_random_book, generate_random_books_list, add_random_client,'
                ' generate_random_clients_list,  add_client, delete_book, delete_client, show_all_books,'
                ' show_all_clients, show_all_loans, update_book, update_client, search_book, search_client, rental,'
                ' restitution, most_rented_books, most_active_clients, top_3, sort_title_author, sort_name_cnp, exit')
            com = input('Dati comanda:')
            com = com.lower().strip()
            if com == 'add_book':
                self.__add_book()
            elif com == 'add_client':
                self.__add_client()
            elif com == 'show_all_books':
                self.__show_all_books()
            elif com == 'show_all_clients':
                self.__show_all_clients()
            elif com == 'delete_book':
                self.__delete_book()
            elif com == 'delete_client':
                self.__delete_client()
            elif com == 'update_book':
                self.__update_book()
            elif com == 'update_client':
                self.__update_client()
            elif com == 'add_random_book':
                self.__add_random_book()
            elif com == 'generate_random_books_list':
                self.__generate_random_books_list()
            elif com == 'generate_random_clients_list':
                self.__generate_random_clients_list()
            elif com == 'add_random_client':
                self.__add_random_client()
            elif com == 'search_client':
                self.__search_client()
            elif com == 'search_book':
                self.__search_book()
            elif com == 'rental':
                self.__rental()
            elif com == 'restitution':
                self.__restitution()
            elif com == 'show_all_loans':
                self.__show_all_loans()
            elif com == 'most_rented_books':
                self.__most_rented_books()
            elif com == 'most_active_clients':
                self.__most_active_clients()
            elif com == "top_3":
                self.__top_3()
            elif com == 'sort_title_author':
                self.__sort_title_author()
            elif com == 'sort_name_cnp':
                self.__sort_name_cnp()
            elif com == 'exit':
                return
            else:
                print(colored('Comanda invalida', 'red'))
