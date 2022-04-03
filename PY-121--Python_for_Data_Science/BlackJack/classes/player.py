class Player:
    def __init__(self, name, wallet=50) -> None:
        self.name = name
        self.cards = []
        self.total = 0
        self.wallet = wallet
        self.status = 'waiting'
        self.blackjack = False
    
    def clear_hand(self):
        self.cards = []
        self.total = 0
        self.wallet = self.wallet
        self.status = 'playing'

    def draw(self,cards):
        self.cards += cards
        self.total += sum([card.value for card in cards])
        if self.total == 21: 
            self.blackjack = True
            self.tapped = True
        if self.total > 21: self.status = 'bust'
    
    def hit(self):
        choice = input('Hit?  (y/n)')
        if choice == 'y':
            return 'y'
        self.status = 'tapped'
        return 'n'
    
