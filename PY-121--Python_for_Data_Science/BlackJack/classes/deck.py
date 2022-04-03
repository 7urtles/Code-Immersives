import random 
from classes.card import Card
class Deck:
    def __init__(self):
        self.cards = self.create()

    def create(self)->list:
        suits = ['Spades','Clubs','Hearts','Diamonds']
        face_cards = {'Ace':11,'King':10,'Queen':10,'Jack':10}
        # same as face_cards but with the number cards
        value_cards = {str(card):card for card in list(range(10,1,-1))}
        # combine the dictionaries
        cards = {**face_cards, **value_cards}
        final = []
        [[final.append(Card(name,suit,value)) for name,value in cards.items()] for suit in suits]
        return final

    def shuffle(self)->list:
        # add a random card to a new list 52 times
        self.cards = [self.cards[random.randint(0,len(self.cards)-1)] for _ in range(len(self.cards)-1)]
        return self.cards

    def cut(self, position:int=0)->list:
        # if a cut is requested  cut the deck at the position chosen, and re-arrage the two halves
        return self.cards[position:]+self.cards[:position]

    def deal(self,cards:int=5)->list:
        return [self.cards.pop(0) for _ in range(cards)]