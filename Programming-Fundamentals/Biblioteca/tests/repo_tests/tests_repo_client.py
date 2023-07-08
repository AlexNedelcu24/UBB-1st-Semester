import unittest

from Domain.entities import Client
from exceptions.exceptions import DuplicateIDException_Client, ClientNotFoundException
from Repository.client_repo import InMemoryRepository_Client

class TestCaseClientRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = InMemoryRepository_Client('test_repoclient.txt')
        self.repo.delete_all()

    def test_store_client(self):
        a = Client(1540, 'Deaconu Cristian', 1054373559322)
        b = Client(3553, 'Popescu Mihai', 1054373559311)
        self.repo.store_client(a)
        self.assertEqual(self.repo.size(), 1)
        self.repo.store_client(b)
        self.assertEqual(self.repo.size(), 2)
        self.assertEqual(self.repo.search_client(a.getID(), 0), a)

        c = Client(1540, 'Deaconu Cristian', 1054373559399)
        self.assertRaises(DuplicateIDException_Client, self.repo.store_client, a)

    def test_remove_client(self):
        a = Client(1540, 'Deaconu Cristian', 1054373559322)
        b = Client(3553, 'Popescu Mihai', 1054373559311)
        self.repo.store_client(a)
        self.assertEqual(len(self.repo.get_all_clients()), 1)
        self.repo.store_client(b)
        self.assertEqual(len(self.repo.get_all_clients()), 2)
        self.assertEqual(self.repo.get_all_clients()[0], a)
        self.assertEqual(self.repo.get_all_clients()[1], b)
        self.repo.remove_client(3553)

    def test_update_client(self):
        a = Client(1540, 'Deaconu Cristian', 1054373559322)
        self.repo.store_client(a)

        b = Client(1540, 'Popescu Mihai', 1054373559311)
        updated_client = self.repo.update_client(b)
        self.assertEqual(updated_client.getName(), 'Popescu Mihai')
        c = Client(3553, 'Deaconu Cristian', 1054373559322)
        self.assertRaises(ClientNotFoundException, self.repo.update_client, c)

    def tearDown(self) -> None:
        self.repo.delete_all()