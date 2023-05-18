from enum import Enum
from models import *

class GameState(Enum):
    PLAYING = 0
    WARRING = 1
    ENDED = 2

class GameEngine:
    deck = None
    player1 = None
    player2 = None
    pile = None
    state = None
    currentPlayer = None
    result = None
    playerOneWarCount = 0
    playerTwoWarCount = 0 
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player("Stephen", pygame.K_q)
        self.player2 = Player("Matt", pygame.K_o)
        self.pile = Pile()
        self.deal()
        self.currentPlayer = self.player1
        self.state = GameState.PLAYING
    def deal(self):
        halfDeck = self.deck.length() //2
        for i in range(0, halfDeck):
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)
    def switchPlayer(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1
    def roundWin(self, player: Player):
        player.hand.extend(self.pile.getAllCards())
        self.pile.clearPile()
        if self.state == GameState.WARRING:
            self.state = GameState.PLAYING
        self.currentPlayer = player
    def play(self, key):
        if key == None:
            return 
        if self.state == GameState.ENDED:
            return
        if key == self.currentPlayer.flipKey:
            playedCard = self.currentPlayer.play()
            previousCard = self.pile.getLastCardPlayed()
            if self.state == GameState.WARRING:
                if self.currentPlayer.warCount > 0: 
                    playedCard.setFaceDown()
                    self.currentPlayer.decreaseWarCount()
                
            if self.state != GameState.WARRING or (self.player1.warCount == 0 and self.player2.warCount == 0):                
                if (previousCard is not None and  playedCard.value == previousCard.value):
                    self.state = GameState.WARRING

                if previousCard is not None and playedCard.value > previousCard.value:
                    self.state = GameState.PLAYING
                    self.roundWin(self.player1)
                    self.player1.resetWarCount()
                    self.player2.resetWarCount()  
                elif previousCard is not None and playedCard.value > previousCard.value:
                    self.state = GameState.PLAYING
                    self.roundWin(self.player2)
                    self.player1.resetWarCount()
                    self.player2.resetWarCount()
                    
            self.pile.addCard(playedCard)
            self.switchPlayer()
        if len(self.player1.hand) == 0:
            self.result = {"WINNER":self.player2}
            self.state = GameState.ended
        elif len(self.player2.hand) == 0:
            self.result = {"WINNER":self.player1}
            self.state = GameState.ended