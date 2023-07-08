from Domain.entities import Client
from Domain.validators import ClientValidator
from Repository.client_repo import InMemoryRepository_Client
import random

class ClientService:
    """
    Responsabil de efectuarea operatiilor cerute de utilizator
    """
    def __init__(self, repo, validator):
        """
        Initializare service
        :param repo: obiectul de tip repo care ne ajuta sa gestionam listei de clienti
        :type repo: InMemoryRepository_Client
        :param validator: validator pentru verificarea clientilor
        :type validator: ClientValidator
        """
        self.__repo = repo
        self.__validator = validator

    def string_generator(self, size, chars):
        return ''.join(random.choice(chars) for a in range(size))

    def add_random_client(self):
        id = random.randint(1000, 9999)
        name = self.string_generator(9, 'qazwsxedcrfvtgbyhnujmikolp').capitalize() + ' ' + self.string_generator(11, 'qazwsxedcrfvtgbyhnujmikolp')
        CNP = random.randint(1000000000000, 9999999999999)

        c = Client(id, name, CNP)

        self.__repo.store_client(c)

        return c

    def add_client(self, id, name, cnp):
        """
        Adaugare client in lista
        :param id: id-ul clientului
        :type id: int
        :param name: numele clientului
        :type name: str
        :param cnp: cnp-ul clientului
        :type cnp: int
        :return: obiectul de tip Client creat
        :rtype: - ; client adaugat la repo
        :raises: ValueError daca clientul nu este valid
        """

        c = Client(id, name, cnp)

        self.__validator.validate_client(c)
        self.__repo.store_client(c)

        return c

    def delete_client(self, id_to_del):
        """
        Sterge clientul dupa id
        :param id_to_del: id-ul clientului care se sterge
        :type id_to_del: int
        :return: clientul sters
        :rtype: Client
        :raises: ValueError daca nu exista client cu id-ul dat
        """

        return self.__repo.remove_client(id_to_del)

    def get_all_clients(self):
        """
        Returneaza o lista cu toti clientii
        :return: lista de clienti
        :rtype: list of Client objects
        """
        return self.__repo.get_all_clients()

    def update_client(self, id, name, cnp):
        """
            Modificare client din lista
            :param id: id-ul clientului
            :type id: int
            :param name: numele noului client
            :type name: str
            :param cnp: cnp-ul noului client
            :type cnp: int
            :return: -
            :rtype: -
            """

        c = Client(id, name, cnp)

        self.__validator.validate_client(c)
        self.__repo.update_client(c)

        return c

    def search_client_id(self, id):
        """
        Cauta client dupa id-ul dat
        :param id: id dat
        :type id: int
        :return: clientul cu identificatorul id/None daca nu exista client
        :rtype: Client
        """
        return self.__repo.search_client(id, 0)


def test_add_client():
    repo = InMemoryRepository_Client()
    val = ClientValidator()
    test_srv = ClientService(repo, val)

    added_client = test_srv.add_client(1540, 'Deaconu Cristian', 1054373559322)
    assert (added_client.getName() == 'Deaconu Cristian')
    assert (len(test_srv.get_all_clients()) == 1)

    try:
        added_client2 = test_srv.add_client(1540, 'Cristian', 1054373559322)
        assert False
    except ValueError:
        assert True


def test_delete_client():
    repo = InMemoryRepository_Client()
    validator = ClientValidator()
    test_srv = ClientService(repo, validator)

    added_client = test_srv.add_client(1540, 'Deaconu Cristian', 1054373559322)
    added_client2 = test_srv.add_client(3553, 'Popescu Mihai', 1054373559311)

    deleted_client = test_srv.delete_client(1540)
    assert (len(test_srv.get_all_clients()) == 1)

    assert (deleted_client.getID() == 1540)
    assert (deleted_client.getName() == 'Deaconu Cristian')
    assert (deleted_client.getCNP() == 1054373559322)

    assert (test_srv.get_all_clients()[0].getName() == 'Popescu Mihai')

    try:
        deleted_client = test_srv.delete_client(5000)
        assert False

    except ValueError:
        assert True


def test_update_client():
    repo = InMemoryRepository_Client()
    validator = ClientValidator()
    test_srv = ClientService(repo, validator)

    added_client = test_srv.add_client(1540, 'Deaconu Cristian', 1054373559322)
    added_client2 = test_srv.add_client(3553, 'Popescu Mihai', 1054373559311)

    updated_client = test_srv.update_client(1540, 'Ion Pop', 9876543210681)
    assert (len(test_srv.get_all_clients()) == 2)
    assert (updated_client.getName() == 'Ion Pop')
    assert (updated_client.getCNP() == 9876543210681)

    modified_client = test_srv.search_client_id(1540)
    unchanged_client = test_srv.search_client_id(3553)

    assert (modified_client.getName() == 'Ion Pop')
    assert (modified_client.getCNP() == 9876543210681)

    assert (unchanged_client.getName() == 'Popescu Mihai')
    assert (unchanged_client.getCNP() == 1054373559311)


#test_add_client()
#test_delete_client()
#test_update_client()