import pygame
import random
import threading
from block import Block

class BlockBuilder:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.blocks = [Block(-50, 200, screen=self.screen)]
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.build_thread = threading.Thread(target=self.build_blocks_thread, daemon=True)
        self.build_thread.start()

    def getRandom(self, position: int):
        if position + 200 < self.width:
            maxi = self.width
        else:
            maxi = position

        if (position - 30) > 0:
            mini = 0
        else:
            mini = position
        n = random.randint(mini, maxi)
        return n

    def build_blocks_thread(self):
        while True:
            if self.blocks[-1].positionY > self.width * 3 / 4:
                self.build(self.blocks[-1].gapPosition)
            for block in self.blocks:
                if block.positionY > self.width:
                    self.blocks.remove(block)


    def build(self, lastPosition):
        self.blocks.append(Block(-50, self.getRandom(lastPosition), screen=self.screen))
        

    def run(self, dt, pygame):
        for block in self.blocks:
            block.draw(dt, pygame)

    def reset(self):
        self.blocks = [Block(0, 200, screen=self.screen)]
