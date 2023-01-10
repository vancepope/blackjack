from unittest.mock import Mock
import sys
sys.path.insert(1, './src')
from src.blackjack import Deck, Card, BlackJack, Hand
import pytest

class TestDeck:
    cards = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
    deck = []
    directory = "src.blackjack.Deck"
    
    def test_create_deck(self):
        deck = Deck()
        deck.createDeck(self)
        assert len(self.deck) == 52
    
    def test_deal(self, mocker):
        newCard = mocker.patch(f"{self.directory}.deal", return_value=Card("Ace", "Diamonds"))
        assert type(newCard.return_value) == Card
        
class TestBlackJack:
    directory = "src.blackjack.BlackJack"

    def test_hit_stay(self, mocker):
        answer = mocker.patch(f"{self.directory}.hitStay", return_value="hit")
        assert answer.return_value == "hit"
    
    def test_set_is_playing(self):
        blackjack = BlackJack("Black Jack")    
        blackjack.setIsPlaying = True
        assert blackjack.getIsPlaying == True
        
class TestHand:
    directory = "src.blackjack.Hand"

    def test_add_card(self, mocker):
        hand = mocker.patch(f"{self.directory}.addCard", return_value=[Card("Ace", "Diamonds")])
        assert type(hand.return_value) == list
        assert len(hand.return_value) == 1
        assert type(hand.return_value[0]) == Card
        
        
    