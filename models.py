from enum import Enum
import pygame
import random

class Suits(Enum):
  CLUB = 0
  SPADE = 1
  HEART = 2
  DIAMOND = 3

class Card:
  suit = None
  value = None
  image = None
  isFaceDown = False
  def __init__(self, suit, value):
      self.suit = suit
      self.value = value
      self.image = pygame.image.load('images/' + self.suit.name + '-' + str(self.value) + '.svg')
      self.isFaceDown = False
  def setFaceDown(self):
      self.isFaceDown = True
    

class Deck:
    cards = None
    def __init__(self):
        self.cards = []
        for suit in Suits:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        return self.cards.pop()
    def length(self):
        return len(self.cards)

class Pile:
    cards = None
    def __init__(self):
        self.cards = []
    def addCard(self, card):
        self.cards.append(card)
    def getLastCardPlayed(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else: 
            return None
    def getAllCards(self):
        return self.cards
    def clearPile(self):
        self.cards = []
    def isWar(self):
        if len(self.cards) > 1:
            if self.cards[-1].value == self.cards[-2].value:
                return True
            else:
                return False

class Player:
    hand = None
    playerName = None
    flipKey = None
    warCount= None
    def __init__(self, playerName, flipKey):
        self.playerName = playerName
        self.hand = []
        self.flipKey = flipKey
        self.warCount = 3
    def decreaseWarCount(self):
        self.warCount = self.warCount - 1 
    def resetWarCount(self):
        self.warCount = 3
    def draw(self, deck):
        self.hand.append(deck.deal())
    def play(self):
        return self.hand.pop(0)
    

        





