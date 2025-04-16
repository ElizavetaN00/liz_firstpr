import unittest
import sys
import os
from hw12.hh12 import Bank

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.clt_id = "0000001"
        self.bank.register_client(client_id=self.clt_id, name="Siarhei")

    def test_register_client(self):
        self.assertEqual(self.bank.clients[self.clt_id], "Siarhei")

    def test_register_same_client(self):
        with self.assertRaises(ValueError) as e:
            self.bank.register_client(client_id=self.clt_id, name="New client")
        self.assertEqual(str(e.exception), "Client was registered before")

    def test_open_deposit(self):
        self.bank.open_deposit_account(client_id=self.clt_id,
                                       start_balance=1000, years=1)
        self.assertIn(self.clt_id, self.bank.deposits)

    def test_open_deposit_not_registered_client(self):
        with self.assertRaises(ValueError) as e:
            self.bank.open_deposit_account(client_id="0000002",
                                           start_balance=1000, years=1)
        self.assertEqual(str(e.exception), "Client was not registered")

    def test_open_same_deposit(self):
        self.bank.open_deposit_account(client_id=self.clt_id,
                                       start_balance=1000, years=1)
        with self.assertRaises(ValueError) as e:
            self.bank.open_deposit_account(client_id=self.clt_id,
                                           start_balance=10000, years=3)
        self.assertEqual(str(e.exception), "Deposit was already "
                                           "opened for this client")

    def test_calc_interest_rate(self):
        self.bank.open_deposit_account(client_id=self.clt_id,
                                       start_balance=1000, years=1)
        final_balance = self.bank.calc_deposit_interest_rate(client_id=self.clt_id)
        self.assertAlmostEqual(final_balance, 1104.713067441297)

    def test_calc_interest_no_opened_deposit(self):
        with self.assertRaises(ValueError) as e:
            self.bank.calc_deposit_interest_rate(client_id="0000002")
        self.assertEqual(str(e.exception), "No deposit found for this client")

    def test_close_deposit(self):
        self.bank.open_deposit_account(client_id=self.clt_id,
                                       start_balance=1000, years=1)
        self.bank.close_deposit(client_id=self.clt_id)
        self.assertNotIn(self.clt_id, self.bank.deposits)

    def test_close_deposit_no_client_opened(self):
        with self.assertRaises(ValueError) as e:
            self.bank.close_deposit(client_id="0000002")
        self.assertEqual(str(e.exception), "There's no deposit for this client")


if __name__ == '__main__':
    unittest.main()
