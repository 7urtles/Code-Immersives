# What am I solving again?
class Solving_Problems():

    # I have no idea what this is for yet
    def first_function_of_class():
        print("Welp here we are!")

    # Cake run rutine
    def cake_maker():
        instructions = {0:"Bake the cake.", 1:"Mix it up."}
        count = 0
        while count < len(instructions):
            print(instructions[count])
            count += 1


class Cereal_Maker():
    def __init__(self, bowl):
        self.bowl = {"milk":0, "cereal":0,
            "spoon":False, "spilling":True, "space":10}
        
    def pour_cereal(self):
        while self.bowl["space"] > 0:
            self.bowl["cereal"] += 1
            self.bowl["space"] -= 1
            print("Bowl Space Left: {}".format(self.bowl["space"]))
            print("Cereal Level: {}".format(self.bowl["cereal"]))
            print("\n")
    
    def pour_milk(self):
        while self.bowl["space"] > 0:
            self.bowl["milk"] += 1
            self.bowl["space"] -= 1
            print("Bowl Space Left: {}".format(self.bowl["space"]))
            print("Milk Level: {}".format(self.bowl["milk"]))
            print("\n")
    
    def take_bite(self):
        if self.bowl["cereal"]  > 0:
            self.bowl["cereal"] -= 2
            self.bowl["space"] += 2


Cereal = Cereal_Maker("Cookie_Crisps").pour_cereal()

# Solving_Problems.cake_maker()

