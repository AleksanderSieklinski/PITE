import unittest
import os
from task import *
# This task was to write a python test for the Bank_client_system task of my friend
# I added a test.py file to check if the code works properly.
# The class checks if all essential methods work properly.
class TestTask(unittest.TestCase):
    def test_create(self):
        self.assertEqual(Client.num_of_people, 1)
    def test_cash_input(self):
        john = Client("John", "Smith")
        john.cash_input(100)
        self.assertEqual(john.balance, 100)
    def test_withdraw(self):
        john = Client("John", "Smith")
        john.cash_input(100)
        john.withdraw(50)
        self.assertEqual(john.balance, 50)
    def test_transfer_to_other_bank(self):
        client1 = Client("John", "Smith")
        client2 = Client("John", "Smithh")
        client1.bank = "ING"
        client2.bank = "PKO"
        client1.cash_input(100)
        client1.transfer(client2, 50)
        self.assertEqual(client1.balance, 40)
        self.assertEqual(client2.balance, 60)
    def test_transfer_to_same_bank(self):
        client1 = Client("John", "Smith")
        client2 = Client("John", "Smithh")
        client1.bank = "ING"
        client2.bank = "ING"
        client1.cash_input(100)
        client1.transfer(client2, 50)
        self.assertEqual(client1.balance, 50)
        self.assertEqual(client2.balance, 50)
    def test_transfer_to_other_bank_without_money(self):
        client1 = Client("John", "Smith")
        client2 = Client("John", "Smithh")
        client1.bank = "ING"
        client2.bank = "PKO"
        client1.cash_input(100)
        client1.transfer(client2, 150)
        self.assertEqual(client1.balance, 100)
        self.assertEqual(client2.balance, 0)
    def test_transfer_to_same_bank_without_money(self):
        client1 = Client("John", "Smith")
        client2 = Client("John", "Smithh")
        client1.bank = "ING"
        client2.bank = "ING"
        client1.cash_input(100)
        client1.transfer(client2, 150)
        self.assertEqual(client1.balance, 100)
        self.assertEqual(client2.balance, 0)
    def test_save_to_file(self):
        if os.path.exists("data.txt"):
            os.remove("data.txt")
        bank1 = Bank("ING")
        client1 = Client("John", "Smith")
        bank1.add_client(client1)
        client1.cash_input(100)
        bank1.save_to_file()
        with open("data.txt", "r") as f:
            self.assertEqual(f.read(), "Bank ING, Number of clients: 1\nClients:\n1. John Smith, Balance: 100\n")
    def test_delete_bank(self):
        bank1 = Bank("ING")
        client1 = Client("John", "Smith")
        bank1.add_client(client1)
        client1.cash_input(100)
        del client1
        Client.num_of_people -= 1
        del bank1
        Bank.num_of_banks -= 1
        self.assertEqual(Client.num_of_people, 1)
    def test_delete_client(self):
        bank1 = Bank("ING")
        client1 = Client("John", "Smith")
        bank1.add_client(client1)
        client1.cash_input(100)
        del client1
        Client.num_of_people -= 1
        self.assertEqual(Client.num_of_people, 1)