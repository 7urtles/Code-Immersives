from classes.player import Player
from classes.deck import Deck
class BlackJack:
    def __init__(self, names:list[str]) -> None:
        self.running = True
        self.discard = []
        # initialize deck
        self.deck = Deck()
        # shuffle deck
        self.deck.shuffle()
        # initialize players
        self.players = tuple(Player(name) for name in names)
        # tracker for end of a round
        self.active_players = len(self.players)
        # signal to deal a fresh hand to the players
        self.new_hand = True
        # player buy in cost
        self.bet = 5
        #initialize pot
        self.pot = 0

    def initial_bet(self)->None:
        # take the min bet from every player
        for player in self.players:
            player.wallet -= self.bet
            # and add it to the pot
            self.pot += self.bet     

    def round_over(self, winner:Player)->None:
        winner.wallet += self.pot
        self.pot = 0
        if input(f"{winner.name} won!\n{self.players[0].name}: {self.players[0].total}  {self.players[1].name}: {self.players[1].total}\nPlay again?\n(y/n) :") != 'y': 
            # if they dont say yes end the script
            self.running = False
        for player in self.players:
            # put players cards in the discard pile
            self.discard += player.cards
            # set flag to signify begenning of a new round
            self.new_hand = True
            # reset active player counter
            self.active_players = len(self.players)
            player.clear_hand()
