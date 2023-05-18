import pygame 
from enum import Enum
from models import *
from engine import *

pygame.init()
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("IDeclareWar")
gameEngine = GameEngine()
run = True

cardBack = pygame.image.load("images/BACK.png")
cardBack = pygame.transform.scale(cardBack,(int(238*0.8),int(332*0.8)))

def renderGame(window):
    window.fill((15,0,169))
    font = pygame.font.SysFont("comicsans", 60, True)
    window.blit(cardBack,(100,200))
    window.blit(cardBack,(700,200))
    text = font.render(str(len(gameEngine.player1.hand)) + " cards", True, (255, 255, 255))
    window.blit(text, (100, 500))
    text = font.render(str(len(gameEngine.player2.hand)) + " cards", True, (255, 255, 255))
    window.blit(text, (700, 500))
    font = pygame.font.SysFont("comicsans", 30, True)
    text = font.render("Game state is... " + str(gameEngine.state), True, (255, 255, 255))
    window.blit(text, (100, 600))

    text = font.render("current player war count... " + str(gameEngine.currentPlayer.warCount), True, (255, 255, 255))
    window.blit(text, (200, 700))
    topCard = gameEngine.pile.getLastCardPlayed()
    if topCard != None:
        if (topCard.isFaceDown):
            window.blit(cardBack, (400,200))
        else: 
            window.blit(topCard.image,(400,200))
    if gameEngine.state == GameState.WARRING:
        result = gameEngine.result
        #handle war stuff here
    if gameEngine.state == GameState.ENDED:
        result = gameEngine.result
        message = "Game Over " + result["WINNER"].playerName +" wins"
        text = font.render(message,True,(255, 255, 255))
        window.blit(text,(20,50))

while run:
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.KEYDOWN:
            key = event.key
    gameEngine.play(key)
    renderGame(window)
    pygame.display.update()



    
            









        # resolve a round
        # resolve ties (WAR)
        # counter of 1, 2, 3 for face down cards dealt in War
        # Face down cards
        # Win condition/Loss condition 