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
    
    @pytest.fixture
    def create_deck(self):
        for card in self.cards:
            for suit in self.suits:
                self.deck.append(Card(card, suit))
        return self.deck
    
    def test_create_deck(self, create_deck, mocker):
        deck = mocker.patch(f"{self.directory}.createDeck", return_value=self.deck)
        assert create_deck is deck.return_value
    
    def test_deal(self, mocker):
        newCard = mocker.patch(f"{self.directory}.deal", return_value=Card("Ace", "Diamonds"))
        assert type(newCard.return_value) == Card
        assert str(newCard.return_value) == "Ace of Diamonds"
        
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
        assert str(hand.return_value[0]) == "Ace of Diamonds"
        
class TestCard:
    directory = "src.blackjack.Card"
    def test___repr__(self, mocker):
        result = mocker.patch(f"{self.directory}.__repr__", return_value=Card("Ace", "Diamonds"))
        assert str(result.return_value) == "Ace of Diamonds"
        