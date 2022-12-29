from datetime import date
import random
import csv

class Card: 
    def __init__(self, card = '', suit = ''):
        self.card = card
        self.suit = suit
        
    @property
    def getCard(self):
        return self.card
    @property
    def getSuit(self):
        return self.suit
    
    def __repr__(self): 
        return f"{self.card} of {self.suit}"
    
    def __str__(self):
        return self.card + ' of ' + self.suit
    
class Deck(Card):
    def __init__(self, cards = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"), 
        suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs'), values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}):
        
        self.cards = cards
        self.suits = suits
        self.values = values
        self.deck = []
    
    @property
    def getCards(self):
        return self.cards
    @property
    def getSuits(self):
        return self.suits
    @property
    def getValues(self):
        return self.values
    @property
    def getDeck(self):
        return self.deck
    
    @getDeck.setter
    def setDeck(self, deck):
        self.deck = deck
    
    @staticmethod
    def createDeck(self):
        for card in self.cards:
            for suit in self.suits:
                self.deck.append(Card(card, suit))
    @staticmethod   
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.shuffle(self)
        newCard = self.deck.pop()
        return newCard
    
class Hand(Deck):
    def __init__(self, deck, values):
        super().__init__(deck, values)
        self.name = ''
        self.value = 0
        self.aces = 0
        self.hand = []
    
    def addCard(self, card):
        self.hand.append(card)
        value = self.values[card.getCard]
        self.value += value

    def ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
class BlackJack:
    def __init__(self, name):
        self.name = name
        self.isPlaying = False
        self.startTime = date(2001, 1, 1)
        self.endTime = date(2001, 1, 1)
        
    
    @property
    def getName(self):
        return self.name
    
    @getName.setter
    def setName(self, name):
        self.name = name
    @property
    def getIsPlaying(self):
        return self.isPlaying
    @getIsPlaying.setter
    def setIsPlaying(self, isPlaying):
        self.isPlaying = isPlaying
    
    def hit(self, card, hand):
        hand.addCard(card)
        hand.ace()
     
    def hitStay(self, deck, hand):
        answer = input("Would you like to hit or stay?: ").lower()
        if (answer == "hit"):
            self.hit(deck.deal(), hand)
        elif (answer == "stay"):
                print("***************************************************************")
                print("*                     PLAYER STAYS                            *")
                print("***************************************************************")
        else: 
            answer = input("Please only enter, hit or stay: ").lower()
            if (answer == "hit"):
                self.hit(deck.deal(), hand)
            else:
                print("***************************************************************")
                print("*                     PLAYER STAYS                            *")
                print("***************************************************************")
        return answer
             
    def showCards(self, player, dealer):
        print("***************************************************************")
        print(f"*     Dealer: {dealer.hand}                       ")
        print(f"*                        Value: {dealer.value}                        ")
        print("*")
        print(f"*     Player: {player.hand}                       ")     
        print(f"*                        Value: {player.value}                        ")
        print(f"*                                                             ")   
        print("***************************************************************")
    
    def play(self):
        self.setIsPlaying = True
        name = input("Please Enter your name: ").upper()
        print(f"****************************************************************")
        print("*                                                                ")
        print("*  WELCOME TO SYCUAN CASI... OH, IT'S YOU, AGAIN!!! LAST TIME YOU ")
        print(f"*  WERE HERE, WE HAD TO DRAG YOU OUT 'CAUSE YOU JUST DON'T KNOW  ")
        print(f"*  WHEN TO STOP {name}... WHAT'S THIS YOU SAY!? YOU WANNA        ")
        print(f"*  GO DOUBLE OR NOTHIN!? AS YOU WISH, IT'S YOUR FUNERAL!!      ")     
        print(f"*                                                                ")   
        print(f"****************************************************************")
        
        while self.isPlaying:
            deck = Deck()
            deck.createDeck(deck)
            player = Hand(deck.getDeck, deck.getValues)
            player.addCard(deck.deal())
            player.addCard(deck.deal())

            dealer = Hand(deck.getDeck, deck.getValues)
            dealer.addCard(deck.deal())
            dealer.addCard(deck.deal())
            
            self.showCards(player, dealer)
            if player.value <= 16:
                while player.value < 17:
                    ans = self.hitStay(deck, player)
                    if ans == 'stay':
                        break
                    self.showCards(player, dealer)
            if dealer.value <= 21:
                while dealer.value < 17:
                    self.hit(deck.deal(), dealer)
                self.showCards(player, dealer)
            
            
            if dealer.value < player.value and player.value <= 21:
                print("***************************************************************")
                print("*                      PLAYER WINS                            *")
                print("***************************************************************")
            elif dealer.value > player.value and dealer.value <= 21:
                print("***************************************************************")
                print("*                      DEALER WINS                            *")
                print("***************************************************************")
            elif dealer.value <= 21 and player.value > 21:
                print("***************************************************************")
                print("*                      DEALER WINS                            *")
                print("***************************************************************")
            elif dealer.value >= 21 and player.value <= 21:
                print("***************************************************************")
                print("*                      PLAYER WINS                            *")
                print("***************************************************************")
            elif dealer.value > 21 and player.value > 21:
                print("***************************************************************")
                print("*                      PLAYER LOSES                           *")
                print("***************************************************************")
            else:
                print("***************************************************************")
                print("*                    GAME IS A PUSH                           *")
                print("***************************************************************")
            
            
            userInput = input("Would you like another deal, Yes or No?: ").lower()
            if userInput == "no":
                self.setIsPlaying = False
game = BlackJack("Black Jack")
game.play()