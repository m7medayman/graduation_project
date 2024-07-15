import pygame 
class MyText :
    def __init__(self,text,font,x,y,screen:pygame.Surface) -> None:
        self.text=text
        self.font=font 
        self.color = (0,0,0)
        self.x=x
        self.y=y
        self.screen=screen


    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x, self.y)
        self.screen.blit(text_surface, text_rect)