from Domain.entities import Client
from exceptions.exceptions import DuplicateIDException_Client, ClientNotFoundException

class InMemoryRepository_Client:
    """
    Clasa creata pentru a gestiona clientii
    """

    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista cu clienti
        """

        f = open(self.__filename, 'r')

        clients = []
        lines = f.readlines()
        for line in lines:
            client_id, client_name, client_CNP = [token.strip() for token in line.split(';')]
            client = Client(int(client_id), client_name, int(client_CNP))
            clients.append(client)
        f.close()
        return clients

    def __save_to_file(self, clients):
        """
        Salveaza clientii in fisier
        :param clients: lista de clienti
        :type clients: list of Client
        """

        with open(self.__filename, 'w') as f:
            for client in clients:
                client_str = str(client.getID()) + ';' + str(client.getName()) + ';' + str(client.getCNP()) + '\n'
                f.write(client_str)

    def __exist_id(self, id):
        """
            Verifica daca exista un client cu id-ul dat in lista
            :param id: id-ul dat
            :type id: int
            :return: True daca exista client cu id-ul dat, False altfel
            :rtype: bool
            """
        clients = self.__load_from_file()
        for client in clients:
            if client.getID() == id:
                return True
        return False

    def __find_index(self, clients, id):
        """
        Gaseste index-ul in lista al clientului cu id-ul dat
        :param id: id-ul dat
        :type id: int
        :return: pozitia din lista a clientului cu id-ul dat
        :rtype: int (>=0, <repo.size()), -1 daca id nu exista
        """
        index = -1
        for i in range(len(clients)):
            if clients[i].getID() == id:
                index = i
        return index

    def search_client(self, id, crt):
        """
            Cauta clientul cu id-ul dat
            :param id: id-ul dat
            :type id: int
            :return: clientul cu identificator id/None daca nu exista
            :rtype: Client
            """
        clients = self.__load_from_file()
        if clients[crt].getID() == id:
            return clients[crt]
        if crt < (len(clients)-1):
            return self.search_client(id, crt+1)
        else:
            raise ValueError('Nu exista client cu acest id.')

    def search_client2(self, id):
        """
            Cauta clientul cu id-ul dat
            :param id: id-ul dat
            :type id: int
            :return: clientul cu identificator id/None daca nu exista
            :rtype: Client

            Complexitate:
            caz favorabil:clientul este primul - T(n)=θ(n)=n
            caz defavorabil:clientul este ultimul - T(n)=θ(n)=n
            caz mediu:clientul se afla pe orice pozitie - T(n)= n*(n+1)/2*n = (n+1)/2

            Complexitatea este liniara O(n)=n

            """
        clients = self.__load_from_file()
        for client in clients:
            if client.getID() == id:
                return client
        return None

    def remove_client(self, id_to_del):
        """
        Elimina un client din lista
        :param id_to_del: id-ul clientului care va fi eliminata
        :type id_to_del: int
        :return: clientul sters
        :rtype: Client
        :raises: ValueError daca nu exista client cu id-ul dat
        """
        clients = self.__load_from_file()
        index = self.__find_index(clients, id_to_del)
        if index == -1:
            raise ClientNotFoundException()

        client1 = self.search_client2(id_to_del)
        ok = True
        while ok:
            ok = False
            for client in clients:
                if client.getID() == id_to_del:
                    clients.remove(client)
                    ok = True
        return client1

    def store_client(self, client):
        """
        Adauga un client in lista
        :param client: clientul de adaugat
        :type client: Client
        :return: - ; lista de clienti se modifica prin adaugarea clientului
        :rtype: -
        """
        clients = self.__load_from_file()
        if client in clients:
            raise DuplicateIDException_Client()
        clients.append(client)
        self.__save_to_file(clients)

    def get_all_clients(self):
        """
        Returneaza o lista cu toti clientii
        :rtype: list of Client objects
        """
        return self.__load_from_file()

    def update_client(self, new_client):
        """
        Modifica un client din lista
        :param client: clientul modificat
        :type client: Client
        :return: - ; lista de clienti se modifica prin modificarea clientului
        :rtype: -
        """
        clients = self.__load_from_file()
        index = self.__find_index(clients, new_client.getID())
        if index == -1:
            raise ClientNotFoundException()
        clients[index] = new_client
        self.__save_to_file(clients)
        return new_client

    def size(self):
        """
        Returneaza numarul de clienti din lista
        :rtype: int
        """
        clients = self.__load_from_file()
        return len(clients)

    def delete_all(self):
        """
        Sterge toti clientii
        """
        self.__save_to_file([])


def test_store_client():
    test_repo = InMemoryRepository_Client()
    a = Client(1540, 'Deaconu Cristian', 1054373559322)
    b = Client(3553, 'Popescu Mihai', 1054373559311)
    test_repo.store_client(a)

    assert (test_repo.size() == 1)

    test_repo.store_client(b)
    assert (test_repo.size() == 2)
    assert (test_repo.search_client(a.getID()) == a)

    c = Client(1540, 'Deaconu Cristian', 1054373559399)

    try:
        test_repo.store_client(c)
        assert False
    except ValueError:
        assert True


def test_remove_client():
    test_repo = InMemoryRepository_Client()
    a = Client(1540, 'Deaconu Cristian', 1054373559322)
    b = Client(3553, 'Popescu Mihai', 1054373559311)
    test_repo.store_client(a)
    test_repo.store_client(b)

    deleted_client = test_repo.remove_client(1540)
    assert (test_repo.size() == 1)
    assert (deleted_client.getID() == 1540)
    assert (deleted_client.getName() == 'Deaconu Cristian')
    assert (deleted_client.getCNP() == 1054373559322)

    try:
        deleted_client = test_repo.remove_client(6000)
        assert False
    except ValueError:
        assert True


def test_update_client():
    test_repo = InMemoryRepository_Client()
    a = Client(1540, 'Deaconu Cristian', 1054373559322)
    test_repo.store_client(a)

    b = Client(1540, 'Popescu Mihai', 1054373559311)
    updated_client = test_repo.update_client(b)
    assert (updated_client.getName() == 'Popescu Mihai')
    assert (updated_client.getCNP() == 1054373559311)

    c = Client(154, 'Deaconu Cristian', 1054373559322)
    try:
        updated_client = test_repo.update_client(c)
        assert False
    except ValueError:
        assert True