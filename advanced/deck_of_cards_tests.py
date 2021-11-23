from deck_of_cards import Card, Deck
import unittest


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Hearts")

    def test_init(self):
        """Card should have a suit and a value"""
        self.assertEqual(self.card.value, "A")
        self.assertEqual(self.card.suit, "Hearts")

    def test_repr(self):
        """repr should return a string of the form 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), "A of Hearts")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """Deck should be initialized with 52 cards"""
        self.assertEqual(self.deck.count(), 52)

    def test_repr(self):
        """repr should indicate the number of cards in the deck"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")
        self.deck.deal_hand(20)
        self.assertEqual(repr(self.deck), "Deck of 32 cards")

    def test_count(self):
        """count should return the number of cards in the deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.deal_hand(20)
        self.assertEqual(self.deck.count(), 32)

    def test_deal_card(self):
        """deal_card should return a card and subtract it from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertIsInstance(dealt_card, Card)
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_card_empty(self):
        """deal_card should raise a ValueError if the deck is empty"""
        self.deck.deal_hand(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck.deal_card()

    def test_deal_hand(self):
        """deal_hand should return the specified number of cards and subtract those cards from the deck"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_deal_hand_insufficient_cards(self):
        """deal_hand should raise a ValueError if it attempts to deal more cards than are left in the deck"""
        with self.assertRaises(ValueError):
            self.deck.deal_hand(self.deck.count() + 1)

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full, without subtracting any cards"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        """shuffle should raise a ValueError if the deck is not full"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()


if __name__ == "__main__":
    unittest.main()
