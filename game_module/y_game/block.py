import pygame
class Block :
    def __init__(self,initPosition,gapPosition,screen:pygame.Surface,):
        self.screen=screen
        self.positionX =initPosition
        self.gapPosition= gapPosition
        self.gapHeight=250
        self.size=14
        self.screenHeight =screen.get_height()
        self.color=(255,0,0)
        self.speed=100
        self.positiony1 = self.gapPosition
        self.positiony2 =self.gapPosition+self.gapHeight
        self.rect1=pygame.Rect(self.positionX, self.positiony2, self.size,self.screenHeight-self.positiony2 )
        self.rect2=pygame.Rect(self.positionX, 0, self.size,self.positiony1)

    def increaseSpeed(self):
        self.speed+=10
    def run(self,dt):
        self.rect1.centerx=self.positionX
        self.rect2.centerx=self.positionX
        self.positionX+=self.speed*dt
  

    def draw(self,dt,pygame):
        
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)
        
        self.run(dt=dt)

        
