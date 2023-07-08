import unittest

from Domain.validators import ClientValidator
from Repository.client_repo import InMemoryRepository_Client
from service.client_service import ClientService

class TestCaseClientSrv(unittest.TestCase):
    def setUp(self) -> None:
        repo = InMemoryRepository_Client('test_clientsrv.txt')
        validator = ClientValidator()
        self.__client_srv = ClientService(repo, validator)

    def test_add_client(self):
        added_client = self.__client_srv.add_client(1540, 'Deaconu Cristian', 1054373559322)
        self.assertEqual(added_client.getName(), 'Deaconu Cristian')
        self.assertEqual(len(self.__client_srv.get_all_clients()), 1)

    def test_delete_client(self):
        added_client = self.__client_srv.add_client(1540, 'Deaconu Cristian', 1054373559322)
        added_client2 = self.__client_srv.add_client(3553, 'Popescu Mihai', 1054373559311)

        deleted_client = self.__client_srv.delete_client(1540)
        self.assertEqual(len(self.__client_srv.get_all_clients()), 1)

        self.assertEqual(deleted_client.getID(), 1540)
        self.assertEqual(deleted_client.getName(), 'Deaconu Cristian')
        self.assertEqual(deleted_client.getCNP(), 1054373559322)

        self.assertEqual(self.__client_srv.get_all_clients()[0].getName(), 'Popescu Mihai')

    def test_update_client(self):
        added_client = self.__client_srv.add_client(1540, 'Deaconu Cristian', 1054373559322)
        added_client2 = self.__client_srv.add_client(3553, 'Popescu Mihai', 1054373559311)

        updated_client = self.__client_srv.update_client(1540, 'Ion Pop', 9876543210681)
        self.assertEqual(len(self.__client_srv.get_all_clients()), 2)
        self.assertEqual(updated_client.getName(), 'Ion Pop')
        self.assertEqual(updated_client.getCNP(), 9876543210681)

        modified_client = self.__client_srv.search_client_id(1540)
        unchanged_client = self.__client_srv.search_client_id(3553)

        self.assertEqual(modified_client.getName(), 'Ion Pop')
        self.assertEqual(modified_client.getCNP(), 9876543210681)

        self.assertEqual(unchanged_client.getName(), 'Popescu Mihai')
        self.assertEqual(unchanged_client.getCNP(), 1054373559311)