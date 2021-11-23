from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K"
        ]
        self.cards = [Card(value, suit)
                      for suit in suits
                      for value in values]

    def count(self):
        return len(self.cards)

    def _deal(self, amount):
        if not len(self.cards):
            raise ValueError("All cards have been dealt")

        deal_amount = min([amount, len(self.cards)])

        dealt_cards = []
        for i in range(deal_amount):
            dealt_cards.append(self.cards.pop())

        return dealt_cards

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

    def deal_card(self):
        dealt_card = self._deal(1)[0]
        return dealt_card

    def deal_hand(self, deal_amount):
        dealt_cards = []
        for i in range(deal_amount):
            dealt_cards.append(self.deal_card())

        return dealt_cards

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
