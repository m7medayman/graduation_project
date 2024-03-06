import pygame
class Block :
    def __init__(self,initPosition,gapPosition,screen:pygame.Surface,):
        self.screen=screen
        self.positionY =initPosition
        self.gapPosition= gapPosition
        self.gapWidth=200
        self.size=50
        self.screenWidth =screen.get_width()
        self.color=(255,0,0)
        self.speed=200
        self.positiony1 =self.gapPosition+self.gapWidth
        self.firstWidth=self.gapPosition
        self.secoendWidth = self.screenWidth-self.positiony1
        self.rect1=pygame.Rect(0,0, self.firstWidth,self.size )
        self.rect2=pygame.Rect( self.positiony1,0, self.secoendWidth,self.size)

    def increaseSpeed(self):
        self.speed+=10
    def run(self,dt):
        self.rect1.centery=self.positionY
        self.rect2.centery=self.positionY
        self.positionY+=self.speed*dt
  

    def draw(self,dt,pygame):
        
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)
        
        self.run(dt=dt)

        
