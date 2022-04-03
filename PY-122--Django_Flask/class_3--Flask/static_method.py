




class Data:
    def __init__(self):
        self.some_data = 9999999
    
    @staticmethod
    def some_static():
        return 0


# wrappers
def biggie(function):

    def inner():
        x = function()
        x += " is dead."
        return  x

    return inner()


def make_hit():
    return "Tupac"

make_hit()