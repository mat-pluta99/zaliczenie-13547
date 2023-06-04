class Player:
    def __init__(self, name, chips=1000):
        self.name = name
        self.chips = chips
        self.hand = list()

    def __repr__(self):
        return "This is {name}, they have {chips} left".format(
            name=self.name, chips=self.chips
        )

    def enter_bet(self):
        while True:
            try:
                self.bet = int(
                    input(
                        "You have {chips} chips. Enter your bet: ".format(
                            chips=self.chips
                        )
                    )
                )
                break
            except ValueError:
                print("Wrong type of input!")
        if self.bet > self.chips:
            while self.bet > self.chips:
                try:
                    self.bet = int(
                        input(
                            "Enter the bet you can afford... You have {chips} chips: ".format(
                                chips=self.chips
                            )
                        )
                    )
                    break
                except ValueError:
                    print("Wrong type of input!")

    def hand_value(self):
        count = 0
        ace_check = 0
        for card in self.hand:
            count += card.value
            if card.name == "Ace":
                ace_check += 1
        if count > 21 and ace_check > 0:
            while count > 21:
                for card in self.hand:
                    if card.value == 11 and count > 21:
                        card.value = 1
                        count -= 10
        return count

    def hit(self, deck):
        dealed_card = deck.pop()
        self.hand.append(dealed_card)

    def action(self, deck):
        while True and self.hand_value() < 21:
            print("Enter your action:")
            print("1)'h' to hit a card")
            print("2)'s' to stay and check the dealer")
            action_choice = input("Your decision: ")

            if action_choice == "h":
                self.hit(deck)
                print(
                    "You get",
                    self.hand[-1].name,
                    "of",
                    self.hand[-1].suit,
                    ". Your hand value is",
                    self.hand_value(),
                )
            elif action_choice == "s":
                return False
