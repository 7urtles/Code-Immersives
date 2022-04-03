from classes.blackjack import BlackJack

import os
names = ['Dealer', 'Charles']
def run(game):
        while game.running == True:
            #[---FIRST DEAL OF ROUND---]
            # if it is the first deal of a hand
            if game.new_hand:
                # take the bet
                game.initial_bet()
                # deal two cards to each player
                for num in range(2):
                    # subtract buy in from players wallets
                    game.players[num].wallet -= game.bet
                    # add buy in to pot
                    game.pot+=game.bet
                    # deal each player a card
                    for player in game.players:
                        player.draw(game.deck.deal(1))
                        # if a player hits blackjack end the roundy
                        if player.blackjack == True:
                            game.round_over(player)
                            continue
                game.new_hand = False

            #[---MAIN GAMEPLAY---]
            if game.active_players > 0:
                for player in game.players:
                    # clear the screen
                    os.system('clear')
                    # If player is in play
                    if player.status == 'playing':
                        # ask hit or stay
                        print(f"Dealer: {game.players[0].total}\nYou: {game.players[1].total}")
                        if player.hit() == 'y':
                            # if hit they get a card, if not they will stay for the rest of the round (handled in player Class)
                            player.draw(game.deck.deal(1))
                            os.system('clear')
                    else:
                        game.active_players -= 1
            # if all of the players have tapped or bust
            else:
                if (game.players[0].total >= game.players[1].total) and game.players[0].total <= 21:
                    game.round_over(game.players[0])
                else:
                     game.round_over(game.players[1])
                continue

game = BlackJack(names)
run(game)