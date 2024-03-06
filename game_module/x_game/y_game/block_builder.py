from block import Block
import pygame
import random

class BlockBuilder:
    def __init__(self,screen:pygame.Surface) -> None:
       
        self.screen=screen
        self.blocks:list[Block]=[Block(0,200,screen=self.screen)]
        self.width=screen.get_width()
        self.height=screen.get_height()
   
    def getRandom(self,position:int):
        if(position  +200  <self.height ):
            maxi=position+30
        else :
            maxi=position
        
        if((position -30) >0 ):
            mini=position-30
        else :
            mini=position
        n=random.randint(mini,maxi)
        return n
    def build(self,lastPosition):
        self.blocks.append(Block(1,self.getRandom(lastPosition),screen=self.screen))
    def run(self,dt,pygame):
        for block in self.blocks:
            block.draw(dt,pygame)
            if block.positionY > self.width+block.size:
                self.blocks.remove(block)
        if(self.blocks[-1].positionY>0):
            self.build(self.blocks[-1].gapPosition)
    def reset(self):
        self.blocks=[Block(0,200,screen=self.screen)]

        