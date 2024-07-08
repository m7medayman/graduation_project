import pygame
import sys

from game_module.game_controller import PlayerYController

class PlayerModule:
    def __init__(self,screen:pygame.Surface,pygme:pygame) -> None:
        self.color=(0,0,255)
        self.size=40
        self.screen=screen
        self.screenHeight=screen.get_height()
        self.startPosition=screen.get_height()/2
        self.PositionX= screen.get_width()*3/4
        self.PositionY=self.startPosition
        self.playerPostionController=PlayerYController()
        self.pygame=pygame
        self.rect=pygame.Rect(self.PositionX, self.PositionY, self.size,self.size)
    def getPlayerPosition(self):
        value=self.playerPostionController.getPosstionX()
        playerPosition=self.screenHeight*value
        return playerPosition

    def run (self):
        self.pygame.draw.rect(self.screen, self.color, self.rect)
        self.rect.centery=self.getPlayerPosition()
    def reset(self):
         self.PositionY=self.startPosition
         self.playerPostionController.reset()


