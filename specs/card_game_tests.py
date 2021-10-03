import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):


    def setUp(self):
        self.card1 = Card("heart", 8)
        self.card2 = Card("spade", 2)
        self.cards = (self.card1, self.card2)
        self.card_game = CardGame()
    
    def test_check_for_ace(self):
        card = Card("Spade", 1)
        self.assertEqual(True, self.card_game.check_for_ace(card))

    def test_check_for_no_ace(self):
        card = Card("Spade", 5)
        self.assertEqual(False, self.card_game.check_for_ace(card))

    def test_highest_card(self):
        card1 = Card("Heart", 4)
        card2 = Card("Heart", 3)
        self.assertEqual(card1, self.card_game.highest_card(card1, card2))

    def test_highest_card_is_card2(self):
        card1 = Card("Heart", 4)
        card2 = Card("Heart", 7)
        self.assertEqual(card2, self.card_game.highest_card(card1, card2))
    
    def test_cards_total(self):
        card1 = Card("heart", 8)
        card2 = Card("spade", 2)
        cards = self.cards
        self.assertEqual("You have a total of 10", self.card_game.cards_total(cards))