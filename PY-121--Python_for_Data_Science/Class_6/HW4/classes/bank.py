from classes.tools import Tools
from classes.account import Account
from random import randint
import numpy as np

class Bank(Tools):
    def __init__(self, starting_balance:float=1_000_000) -> None:
        self.name = input('Bank Name: ')
        self.password = None
        self.set_password()
        self.accounts = np.ndarray((20,),dtype=np.object)
        self.account_counter = 0
        self.logged_in = False
        self.balance = 0
        self.routing = str([randint(0,9) for _ in range(8)])
        self.menu = {}

    def build_menu(self)->None:
        self.menu = {
            "[0] Accounts":{
                    "[0] New Account":self.create_account,
                    "[1] Account Login":{
                        f"[{num[0]}] {account.name}":account for num,account in np.ndenumerate(self.accounts)if account
                    },
                    "[2] Back":self,
                },
            "[1] Logout":0,
        }

    def create_account(self)->None:
        account_name = input('Account Name:')
        self.accounts[self.account_counter] = Account(account_name, self.routing)
        self.account_counter += 1
        print(self.accounts)

    def show_accounts(self)->list|bool:
        # if a bank exists
        if len(self.accounts) != 0:
            #have user select one
            choice = int(input('Select Account:'))
            # if selected bank exists
            if choice <= len(self.accounts):
                # return list of accounts
                return self.accounts[choice]
            else:
                # selection did not match a bank index
                print("Invalid Selection")
                return False
        print("No Accounts Created")
        return False