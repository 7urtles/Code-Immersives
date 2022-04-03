import numpy as np 


'''
Extension 1: add a second array stats that holds the mean, median, stdev

Extension 2: add a gift() method that donates a numpy array of a certain value to all accounts.

Extension 3: Add a second dimension to the original array (or create a brand new one) to store the inverse of the account amounts.
'''

class Account:
    def __init__(self) -> None:
        self.attrs = [
            input('Enter Name: '),
            self.set_password(),
            float(input('Starting Account Balance: ')),
            float(input('Starting Wallet Balance: ')),
        ]

    def set_password(self):
        attempt = input('New Password:\n')
        while attempt != input('Verify Password:\n'):
            attempt = input('New Password:\n')
        return attempt






class Bank:
    def __init__(self, max_accounts=5) -> None:
        self.name = 'Coin Bank'
        self.names = np.array(1)
        self.passwords = np.array(1)

        self.balances = np.array(1)
        self.wallets = np.array(1)

        self.accounts = [self.names, self.passwords, self.balances, self.wallets]
        self.stats = {
            'mean':0,
            'median':0,
            'mode:':0
        }
        self.find_stats()
        self.max_accounts = max_accounts
        self.account_counter = 0
        self.menu = {
                    "[0] New Account":self.create_account,
                    "[1] Deposit":self.deposit,
                    "[2] Withdraw":self.withdraw,
                    "[3] Gift":self.gift,
                }
    
    def gift(self):
        amount = int(input("How much should the give be"))
        self.accounts[2] += amount

    def find_stats(self):
        self.stats['mean'] = np.mean(self.accounts[2])
        self.stats['median'] = np.median(self.accounts[2])
        self.stats['mode'] = np.mode(self.accounts[2])

    def create_account(self):
        if self.account_counter >= self.max_accounts:
            print('Bank Full')
            return False
            
        for index, attr in enumerate(Account().attrs):
            np.append(self.accounts[index], attr)
        self.account_counter += 1
        return True
    
    def deposit(self):
        account = self.select_account()
        if self.check_password(account):
            amount = int(input("Deposit Amount:\n>"))
            if amount <= self.accounts[3][account] and amount > 0:
                self.accounts[2][account] += amount
                self.accounts[3][account] -= amount

    def withdraw(self):
        account = self.select_account()
        if self.check_password(account):
            amount = int(input("Deposit Amount:\n>"))
            if amount <= self.accounts[2][account] and amount > 0:
                self.accounts[2][account] -= amount
                self.accounts[3][account] += amount

    def check_password(self, account):
        print(self.accounts[1])
        return True if input('Verify Password:\n') == self.accounts[1][account] else False

    def select_account(self):
        print('Select an account:\n')
        num = 0
        for name in np.nditer(self.accounts[0]):
            if name == '': break
            print(f"[{num}] {name}")
            num += 1
        return int(input('>'))


    def menu_nav(self, menu_set):
        # Menu banner
        banner = '\n' + '-'*len(self.name) + '\n'
        greeting = banner + self.name + banner
        print(greeting)
        # Menu options
        for option in menu_set:
            print(option)
        # dictionary value of selection
        selection = list(menu_set.values())[int(input('\n>'))]
        # Recursive dictionary traversal :)
        match selection:
            # if the chosen dictionary value is a dictionary, navigate is as the new menu
            case dict():
                self.menu_nav(selection)
            case _:
               selection()
               pass
            
    def run(self):
        self.selection = self
        while True: 
            self.menu_nav(self.selection.menu)
        
bank = Bank()
bank.run()