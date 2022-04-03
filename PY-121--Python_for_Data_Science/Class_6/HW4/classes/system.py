from classes.tools import Tools
from classes.account import Account
from classes.bank import Bank
import numpy as np

class System(Tools):
    def __init__(self) -> None:
        self.name = 'System'
        self.password = 'sysadmin'
        self.logged_in = True
        self.banks = np.ndarray((5,),dtype=np.object)
        self.bank_counter = 0
        self.people = []
        self.selection = None
        self.menu = {}
        self.run()

    def build_menu(self)->None:
        self.menu = {
            "[0] Bank Login":{f"[{num[0]}] {bank.name}":bank for num,bank in np.ndenumerate(self.banks)if bank},
            "[1] New Bank":self.create_bank,
        }

    def create_bank(self)->None:
        self.banks[self.bank_counter] = Bank()
        self.bank_counter+=1

    def show_banks(self)->None:
        if len(self.banks) != 0:
            [print(bank.name) for bank in self.banks]
            return self.banks
        print("No Banks Created")
        return False

    def show_people(self)->None:
        if len(self.banks) != 0:
            [print(person.name) for person in self.people]
            return self.people
        print("No People Created")
        return False

    def menu_nav(self, menu_set)->Bank|Account:
        # Menu banner
        banner = '\n' + '-'*len(self.selection.name) + '\n'
        greeting = banner + self.selection.name + banner
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
            # if the chosen value is a class instance
            case System() | Bank() | Account():
                # login to return the instance
                new_session = selection if selection.logged_in else selection.login()
                # if login was successful return the instance to make it the new scope
                if new_session != False:
                    self.selection = new_session
                    return new_session
            # zero is the logout code
            case 0:
                self.selection.logout()
                self.selection = self
            # if selection is a class method, run it
            case _:
               selection()
               pass
            
    def run(self):
        self.selection = self
        while True: 
            self.selection.build_menu()
            self.menu_nav(self.selection.menu)