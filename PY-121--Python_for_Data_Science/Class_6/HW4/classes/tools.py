import os

class Tools:
    def set_password(self)->None:
        password,password1 = True,False
        while password != password1:
            password = input('Create Password: ')
            password1 = input('Verify Password: ')
        self.password = password
        return True

    def check_password(self)->bool:
        print(self.password)
        if input('Enter Password: ') == self.password:
            print('Logged In')
            return True
        return False

    def change_password(self)->bool:
        if self.check_password():
            return self.set_password()
        return False

    def check_name(self)->str:
        return self.name

    def check_balance(self):
        if self.check_password():
            return self.balance
        return False

    def login(self):
        if not self.logged_in:
            if self.check_password():
                self.logged_in = True
                return self
            return False 
        return self

    def logout(self):
        self.logged_in = False 
        return True

    def clear(self)->None:
        os.system('cls' if os.name == 'nt' else 'clear')