import unittest

from Domain.entities import Client
from Domain.validators import ClientValidator
from exceptions.exceptions import ValidationException

class TestCaseClientDom(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = ClientValidator()

    def test_create_client(self):
        client1 = Client(1540, 'Deaconu Cristian', 1054373559322)
        self.assertTrue(client1.getID() == 1540)
        self.assertTrue(client1.getName() == 'Deaconu Cristian')
        self.assertTrue(client1.getCNP() == 1054373559322)

        client1.setID(2010)
        client1.setName('Popescu Mihai')
        client1.setCNP(1054373559311)

        self.assertTrue(client1.getName() == 'Popescu Mihai')
        self.assertTrue(client1.getID() == 2010)
        self.assertTrue(client1.getCNP() == 1054373559311)

    def test_equal_clients(self):
        client1 = Client(1540, 'Deaconu Cristian', 1054373559322)
        client2 = Client(1540, 'Deaconu Cristian', 1054373559322)

        self.assertEqual(client1, client2)

        client3 = Client(3553, 'Popescu Mihai', 1054373559311)
        self.assertNotEqual(client1, client3)

    def test_ClientValidator(self):
        client1 = Client(1540, 'Deaconu Cristian', 1054373559322)
        client2 = Client(3553, 'Popescu Mihai', 1054373559311)
        self.__validator.validate_client(client1)
        self.__validator.validate_client(client2)

