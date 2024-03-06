import pygame
import sys
sys.path.append('/home/pi/body balance seeker/game_module/shared_component')
from sensor_input.module import SensorInput
class PlayerModule:
    def __init__(self,screen:pygame.Surface,pygme:pygame) -> None:
        self.color=(0,0,255)
        self.size=40
        self.screen=screen
        self.sensorInput= SensorInput()
        self.screenWidth=screen.get_width()
        self.startPosition=screen.get_height()*3/4
        self.PositionX= screen.get_width()/2
        self.PositionY=self.startPosition
        self.pygame=pygame
        self.rect=pygame.Rect(self.PositionX, self.PositionY, self.size,self.size)
    def getPlayerPosition(self):
        value=self.sensorInput.getVlaue()
        playerPosition=self.screenWidth*value
        return playerPosition

    def run (self):
        self.pygame.draw.rect(self.screen, self.color, self.rect)
        self.rect.centery=self.getPlayerPosition()
    def reset(self):
         self.PositionY=self.startPosition

