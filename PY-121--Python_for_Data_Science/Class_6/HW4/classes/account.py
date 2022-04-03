from classes.tools import Tools
from random import randint

class Account(Tools):
    def __init__(self, name:str, routing_number:int) -> None:
        self.name = name
        self.password = None
        self.set_password()
        self.logged_in = False
        self.wallet = 1000
        self.balance = float(input('Starting Balance: '))
        self.account_number = str([randint(0,9) for _ in range(8)])
        self.routing_number = routing_number
        self.menu = {}

    def build_menu(self)->None:
        self.menu = {
            "[0] ATM":{
                "[0] Deposit":self.deposit,
                "[1] Withdraw":self.withdraw,
                "[2] Back":self,
            },
            "[1] Logout":0,
        }
    def transaction(self, amount):
        self.wallet-=amount
        self.balance+=amount
        return True

    def deposit(self):
        if self.logged_in:
            amount = int(input(f"Account: {self.balance}\nWallet: {self.wallet}\n\nDeposit Amount: "))
            if amount <= self.wallet and amount >= 0:
                self.transaction(amount)
                return True
            else:
                print("Invalid Transaction")
                return False

    def withdraw(self):
        if self.logged_in:
            amount = -int(input(f"Account Balance: {self.balance}\nWallet: {self.wallet}\n\nWithdraw Amount: "))
            if amount <= self.balance and amount <= 0:
                self.transaction(amount)
                return True
            else:
                print("Invalid Transaction")
                return False