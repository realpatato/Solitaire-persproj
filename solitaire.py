#import libraries
import pygame 
import numpy

#anchor the pygame screen so you see it in codio.
#Click on the arrow in the upper left corner to display in a new browser tab.
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

#start the pygame module 
pygame.init() 

#variables for screen size: 
screen_width=1100 
screen_height=600 

#color code constants 
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (83, 83, 83)
YELLOW = (255, 255, 0)

#other variable initializers (fonts, text, images, etc)
currentCard='nothing'
currentFaceDownCards=21
cardBack=pygame.image.load('card back.png')
faceDownCardsX=[10, 58, 106, 106, 154, 154, 154, 202, 202, 202, 202, 250, 250, 250, 250, 250, 298, 298, 298, 298, 298, 298]
faceDownCardsY=[10, 78, 78, 88, 78, 88, 98, 78, 88, 98, 108, 78, 88, 98, 108, 118, 78, 88, 98, 108, 118, 128]

#card image loading
placeholder=pygame.image.load('transparent.png')
aceOfClubs=pygame.image.load('ace of clubs.png')
aceOfSpades=pygame.image.load('ace of spades.png')
aceOfHearts=pygame.image.load('ace of hearts.png')
aceOfDiamonds=pygame.image.load('ace of diamonds.png')
twoOfClubs=pygame.image.load('2 of clubs.png')
twoOfSpades=pygame.image.load('2 of spades.png')
twoOfHearts=pygame.image.load('2 of hearts.png')
twoOfDiamonds=pygame.image.load('2 of diamonds.png')
threeOfClubs=pygame.image.load('3 of clubs.png')
threeOfSpades=pygame.image.load('3 of spades.png')
threeOfHearts=pygame.image.load('3 of hearts.png')
threeOfDiamonds=pygame.image.load('3 of diamonds.png')
fourOfClubs=pygame.image.load('4 of clubs.png')

#card defining
cardX=[10, 58, 106, 154, 202, 250, 298, 1000, 1000, 1000, 1000, 1000, 100]
cardY=[78, 88, 98, 108, 118, 128, 138, 500, 500, 500, 500, 500, 500]
cards=[aceOfClubs, aceOfSpades, aceOfHearts, aceOfDiamonds, twoOfClubs, twoOfSpades, twoOfHearts, twoOfDiamonds, threeOfClubs, threeOfSpades, threeOfHearts, threeOfDiamonds,fourOfClubs]
cardsReset=[aceOfClubs, aceOfSpades, aceOfHearts, aceOfDiamonds, twoOfClubs, twoOfSpades, twoOfHearts, twoOfDiamonds, threeOfClubs, threeOfSpades, threeOfHearts, threeOfDiamonds,fourOfClubs]
cardsOrder=cards.reverse()
blackCards=[aceOfClubs, aceOfSpades, twoOfClubs, twoOfSpades, threeOfClubs, threeOfSpades, fourOfClubs]
redCards=[aceOfHearts, aceOfDiamonds, twoOfHearts, twoOfDiamonds, threeOfHearts, threeOfDiamonds]
mouseDown=False

#functions
def cardBackToScreen(cardNumber):
  """puts all the face down cards on the screen"""
  for i in range(cardNumber+1):
    screen.blit(cardBack, (faceDownCardsX[i], faceDownCardsY[i]))

def cardsToScreen(cardNumber):
  """puts all the face up cards on the screen"""
  for i in range(cardNumber):
    screen.blit(cards[i], (cardX[i], cardY[i]))

def cardFollow(cardNumber):
  '''lets card follow mouse'''
  for i in range(cardNumber):
    if currentCard == cards[i]:
      screen.blit(cards[i], (mouseX-19, mouseY-29))
      cards.pop(i)
      cards.insert(i,placeholder)

def mouseDownCheck(cardNumber):
  '''performs the mouse down check'''
  for i in range(cardNumber):  
    mouse_position=pygame.mouse.get_pos()
    if mouse_position[0] >= cardX[i] and mouse_position[0] <= cardX[i]+38 and mouse_position[1] >= cardY[i] and mouse_position[1] <= cardY[i]+58:
      global currentCard
      global mouseDown
      currentCard=cards[i]
      mouseDown=True

def mouseUpCheck(cardNumber):
  '''performs the mouse up check'''
  for i in range(cardNumber):
    global currentCard
    if currentCard == cards[i]:
      for s in range(cardNumber):
        if mouse_position >= cardX[s] and mouse_position[0] <= cardX[s]+38 and mouse_position[1] >= cardY[s] and mouse_position[1] <= cardY[s]+58:
          cardX[i]=cardX[s]
          cardY[i]=cardY[s]+30
          currentCard='nothing'
          break

#create a screen with dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 

#set the screen caption 
pygame.display.set_caption("Solitaire") 
#fills the screen initially with black
screen.fill((0, 0, 0))

#the clock will be used to regulate the frame rate 
clock = pygame.time.Clock() 

#variable to control the game loop 
keep_playing=True 

#Game Loop - needed to keep updating and redrawing the screen 
while keep_playing==True: 
  #iterates over the current list of events(checks for events)  
  for event in pygame.event.get(): 
    #mouse controls
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_position=pygame.mouse.get_pos()
      mouseDownCheck(13)
    if event.type == pygame.MOUSEBUTTONUP:
      mouseDown=False
      mouseUpCheck(13)

    #ends the game
    if event.type == pygame.QUIT: 
      keep_playing = False
  
  #refreshing variables
  mouse_position=pygame.mouse.get_pos()
  mouseX=mouse_position[0]
  mouseY=mouse_position[1]

  #add your key press code here
  
  #add your mouse controls here

  #all items drawn to the screen go here
  screen.fill((0,0,0))
  cardBackToScreen(currentFaceDownCards)
  if mouseDown == True:
    cardFollow(13)
    cardsToScreen(13)
    for i in range(13):
      cards.insert(i,cardsReset[i])
  if mouseDown == False:
    cardsToScreen(13)

  #This function call updates the screen
  pygame.display.update()

  #sets the frame rate
  clock.tick(60)

#quits the pygame module 
pygame.quit() 
quit() 