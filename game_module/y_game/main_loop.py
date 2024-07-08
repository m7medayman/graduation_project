
import pygame
import os
from block_builder import BlockBuilder
from collision import checkCollision
from player import PlayerModule
from game_status import GameStatus
import sys
sys.path.append('/home/pi/body balance seeker/game_module/shared_component')
from ui_component.text import MyText
from ui_component.button import Button

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


pygame.init()

gameStatus=GameStatus()
width,height = 800, 450
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((width,height),flags)
pygame.display.set_caption("Y game")
BLACK = (0, 0, 0)
blockBuilder=BlockBuilder( screen= screen )
blockBuilder
player=PlayerModule(screen=screen,pygme=pygame)
clock = pygame.time.Clock()
running = True
collision=False
def game_over():
        scoreText=MyText(text=f"Score:{str(int(gameStatus.getScore()))} ",font=pygame.font.Font(None, 100),x=width/2,y=height*0.5,screen=screen)
        scoreText.color=(255,0,0)
        screen.fill(color=(0,0,0))
        gameOverText.draw()
        scoreText.draw()
        restartButton.draw()
        quitButton.draw()
        pygame.display.update()
def reset():
     player.reset()
     blockBuilder.reset()
     gameStatus.reset()
def quit():
     gameStatus.isRunning=False

quitButton=Button(screen=screen,pygame=pygame,text='Quit',posX=height*0.7,posY=width*0.3,do_func=quit)
restartButton=Button(screen=screen,pygame=pygame,text='restart',posX=height*0.7,posY=width*0.6,do_func=reset)
gameOverText=MyText(text="game over ",font=pygame.font.Font(None, 100),x=width/2,y=height*0.2,screen=screen)
gameOverText.color=(255,0,0)
while  gameStatus.isRunning:
    screen.fill(BLACK)
        # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameStatus.isRunning = False
            # Get the time since the last frame
    dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
            # Move the object
    if(gameStatus.playerDied):
         game_over()
         continue

    gameStatus.playerDied= checkCollision(player=player,blocks=blockBuilder.blocks)
    gameStatus.increase()
    blockBuilder.run(dt=dt,pygame=pygame)
    player.run()       # Update the display
    pygame.display.update()
            # Check if the object has reached the end of the screen
  # Reset object position

pygame.quit()
