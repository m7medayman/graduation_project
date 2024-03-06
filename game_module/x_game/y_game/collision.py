from block import Block

def checkCollision (blocks:list[Block] , player ):
    for block in blocks :
        if (player.rect.colliderect(block.rect1)) or (player.rect.colliderect(block.rect2)):
            return True 
    

