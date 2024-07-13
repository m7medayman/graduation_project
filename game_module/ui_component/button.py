import pygame

from game_module.ui_component.text import MyText
class Button :
   
    def __init__(self,screen:pygame.Surface,pygame:pygame,text,posX,posY,do_func) -> None:
        self.screen =screen
        width=screen.get_width()
        height=screen.get_height()
        self.rect=pygame.Rect(posY, posX, 150, 50)
        self.buttonColor=(0,255,0)
        self.do_func=do_func
        self.pygame=pygame
        self.font=pygame.font.Font(None, 64)
        self.textColor=(255,255,255)
        self.text=MyText(text,font=self.font,screen=self.screen,x=self.rect.centerx,y=self.rect.centery)

        
    
    def draw(self):
        self.pygame.draw.rect(self.screen, self.buttonColor, self.rect)
        self.text.draw()
        mouse_x, mouse_y = self.pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y ):
            print("clicked")
            self.pygame.mouse.set_pos(0, 0)
            self.do_func()
        


                    
