from player import Player
from cards import Deck


dealer = Player("Dealer")
player_1 = Player("Player 1")


def another_round(player):
    ask = input("Another round?(y/n): ")
    if ask == "y":
        round(player)
    else:
        print("See you next time!")


def blackjack_start_check(player, dealer, deck):
    if dealer.hand_value() == 21 and player.hand_value() == 21:
        print("It's a draw!")
        # return False
    elif dealer.hand_value() == 21:
        print("Dealer has a blackjack! You lose")
        # player.chips -= player.bet
        # return False
    elif player.hand_value() == 21:
        print("You have a blackjack! You win")

        # player.chips += player.bet
        # return False
    """
    else:
        while True:
            # player.action(deck)
            if player.action(deck) == False:
                break
            elif player.hand_value() > 21:
                print("You have more than 21... You lose!")
                player.chips -= player.bet
                return False
    """


def blackjack_start_check_2(player, dealer, deck):
    if dealer.hand_value() == 21 and player.hand_value() == 21:
        print("It's a draw!")
        # return False
    elif dealer.hand_value() == 21:
        print("Dealer has a blackjack! You lose")
        # player.chips -= player.bet
        # return False
    elif player.hand_value() == 21:
        print("You have a blackjack! You win")

        # player.chips += player.bet
        # return False

    else:
        while True:
            # player.action(deck)
            if player.action(deck) == False:
                break
            elif player.hand_value() > 21:
                print("You have more than 21... You lose!")
                player.chips -= player.bet
                return False


def round(player=player_1, dealer=dealer):
    game_ended = False
    # win = False

    # player.enter_bet()
    blackjack_deck = Deck()
    blackjack_deck.blackjack_mode()
    blackjack_deck.shuffle_deck()
    deck = blackjack_deck.deck

    dealer.hit(deck)
    player.hit(deck)
    dealer.hit(deck)
    player.hit(deck)
    print(
        "Dealer's shown card is",
        dealer.hand[0].name,
        "of",
        dealer.hand[0].suit,
        "\nYour cards are",
        player.hand[0].name,
        "of",
        player.hand[0].suit,
        "and",
        player.hand[1].name,
        "of",
        player.hand[1].suit,
        ", your hand value is",
        player.hand_value(),
    )
    # print(dealer.hand_value())

    if blackjack_start_check(player, dealer, deck) != False:
        print("Your cards are:")
        for card in player.hand:
            print(card.__repr__())
        print("Your hand value is:", player.hand_value())
        print("Dealer cards are:")
        for card in dealer.hand:
            print(card.__repr__())
        print("Dealer's hand value is:", dealer.hand_value())

        while dealer.hand_value() < 16:
            print("Dealer hits:", end=" ")
            dealer.hit(deck)
            print(dealer.hand[-1].__repr__())

        if dealer.hand_value() > 21:
            print("Dealer busts 21! You win!")
        #    player.chips += player.bet
        else:
            print("Your hand value is:", player.hand_value())
            print("Dealer's hand value is:", dealer.hand_value())
            if dealer.hand_value() > player.hand_value():
                print("You lose!")
            # return win
            elif dealer.hand_value() < player.hand_value():
                print("You win!")
                # win = True
            #  player.chips += player.bet
            else:
                print("It's a draw! :O")

        game_ended = True
        return game_ended
    """
    if player.chips > 0:
        another_round(player)
    else:
        print("You're out of caps, sir... Thanks for playing!")
    """


round(player_1)
