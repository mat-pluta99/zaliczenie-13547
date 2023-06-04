import random


class Card:
    def __init__(self, value, suit):
        self.name = value
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "The {name} of {suit}".format(name=self.name, suit=self.suit)


class Deck:
    card_values = list(range(2, 15))
    card_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    high_card_names = ["Jack", "Queen", "King", "Ace"]

    deck = list()

    for value in card_values:
        for suit in card_suits:
            deck.append(Card(value, suit))

    for card in deck:
        if card.value == 11:
            card.name = "Jack"
        elif card.value == 12:
            card.name = "Queen"
        elif card.value == 13:
            card.name = "King"
        elif card.value == 14:
            card.name = "Ace"

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def blackjack_mode(self):
        for card in self.deck:
            if card.value > 10 and card.name != "Ace":
                card.value = 10
            if card.name == "Ace":
                card.value = 11
