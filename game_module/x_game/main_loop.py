import os
import pygame
import sys
import random

from game_controller import PlayerYController
from game_module.ui_component.text import MyText
from game_module.ui_component.button import Button
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
import pygame
import sys
import random
# Initialize Pygame
pygame.init()

# Screen dimensions for full-screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
DEVICE_WIDTH, DEVICE_HEIGHT = screen.get_size()
pygame.display.set_caption("Moving Road")

# Colors
GREEN = (0, 255, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Lane and road dimensions
MARGIN_WIDTH = DEVICE_WIDTH//5-20 
ROAD_WIDTH = DEVICE_WIDTH *0.7
LANE_WIDTH = ROAD_WIDTH //3
LINE_HEIGHT = 40
LINE_WIDTH = 10
LINE_SPACING = 20
PLAYER_CONTROLLER=PlayerYController()
# Frame rate
clock = pygame.time.Clock()
FPS = 60

# Initialize line positions
line_positions = [0, DEVICE_HEIGHT // 3, 2 * DEVICE_HEIGHT // 3]

# Font setup
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)


car_images = {
    "truck": pygame.image.load("truck.bmp"),
    "taxi": pygame.image.load("taxi.bmp"),
    "police": pygame.image.load("Police.bmp"),
    "mini_van": pygame.image.load("Mini_van.bmp"),
    "black_viper": pygame.image.load("Black_viper.bmp"),
    "car": pygame.image.load("Car.bmp")
}
class gameStatus():
    startFlag=False
    score=0
    realScore=0
    hardScore=0
    gamespeed=5
    playerDied=False
    enemies=[]
    diff=0
class Player:
    def __init__(self):
        self.width = LANE_WIDTH // 2
        self.height = 125
        self.color = (0, 0, 255)  # Blue color for the player's car
        self.x = MARGIN_WIDTH + LANE_WIDTH // 2 - self.width // 2
        self.y = DEVICE_HEIGHT - self.height -40
        self.speed = 10
        self.image=pygame.image.load("Audi.bmp")
        self.image = pygame.transform.scale(self.image, (self.width*2, self.height+25))
        self.image


    # def move_left(self):
    #     if self.x > MARGIN_WIDTH:
    #         self.x -= self.speed

    # def move_right(self):
    #     if self.x < MARGIN_WIDTH + ROAD_WIDTH - self.width:
    #         self.x += self.speed
    def updatePlayerPostion(self):
        self.x=(MARGIN_WIDTH )+(ROAD_WIDTH - self.width)*PLAYER_CONTROLLER.getPosstionX()
    def draw(self, screen):
        rect = self.get_rect()
        # pygame.draw.rect(screen, (255, 0, 0), rect, 2)  # Red color, 2 pixels wide
        screen.blit(self.image, (self.x-self.width//2, self.y-15))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class EnemyCar:
    def __init__(self,lane):
        self.width = LANE_WIDTH // 2
        self.height = 125
        self.image_name = random.choice(list(car_images.keys()))
        self.image = car_images[self.image_name]
        self.image = pygame.transform.scale(self.image, (self.width*2, self.height+25))
        self.speed = gameStatus.gamespeed
        self.lane = lane
        self.x = MARGIN_WIDTH + self.lane * LANE_WIDTH + (LANE_WIDTH - self.width) // 2
        self.y = -self.height

    def move(self):
        self.y += self.speed



    def draw(self, screen):
        rect = self.get_rect()
        # pygame.draw.rect(screen, (255, 0, 0), rect, 2)  
        screen.blit(self.image, (self.x-self.width//2, self.y-15))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

def draw_road():
    # Draw green margins
    pygame.draw.rect(screen, GREEN, (0, 0, MARGIN_WIDTH, DEVICE_HEIGHT))
    pygame.draw.rect(screen, GREEN, (DEVICE_WIDTH - MARGIN_WIDTH, 0, MARGIN_WIDTH, DEVICE_HEIGHT))
    pygame.draw.rect(screen, YELLOW, (DEVICE_WIDTH - MARGIN_WIDTH+40, 0, 20, DEVICE_HEIGHT))
    pygame.draw.rect(screen, YELLOW, (MARGIN_WIDTH-20, 0, 20, DEVICE_HEIGHT))
    
    # Draw grey road
    pygame.draw.rect(screen, GREY, (MARGIN_WIDTH, 0, ROAD_WIDTH, DEVICE_HEIGHT))
    
    # Draw lane lines
    for line_y in line_positions:
        for i in range(1, 3):  # Draw only two lines in the middle
            lane_center = MARGIN_WIDTH + i * LANE_WIDTH
            pygame.draw.rect(screen, WHITE, (lane_center - LINE_WIDTH // 2, line_y, LINE_WIDTH, LINE_HEIGHT))
def get_unique_sample():
    range_list = list(range(3))  # This creates a list [0, 1, 2]
    num_elements = 2   # Randomly decide to pick 1 or 2 elements
    sample_list = random.sample(range_list, num_elements)  # Get unique elements
    return sample_list

def move_lines():
    global line_positions
    for i in range(len(line_positions)):
        line_positions[i] += gameStatus.gamespeed
        if line_positions[i] > DEVICE_HEIGHT:
            line_positions[i] = 0

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (DEVICE_WIDTH - score_text.get_width() - 10, 10))

def check_collision(player, enemies):
    player_rect = player.get_rect()
    for enemy in enemies:
        if player_rect.colliderect(enemy.get_rect()):
            return True
    return False

def show_game_over(score):
    screen.fill(BLACK)
    game_over_text = large_font.render("Game Over", True, WHITE)
    retry_text = font.render("Press R to Retry", True, WHITE)
    final_score_text = font.render(f"Final Score: {score}", True, WHITE)
    
    screen.blit(game_over_text, ((DEVICE_WIDTH - game_over_text.get_width()) // 2, DEVICE_HEIGHT // 3))
    screen.blit(final_score_text, ((DEVICE_WIDTH - final_score_text.get_width()) // 2, DEVICE_HEIGHT // 2))
    screen.blit(retry_text, ((DEVICE_WIDTH - retry_text.get_width()) // 2, 2 * DEVICE_HEIGHT // 3))
    
    pygame.display.flip()
gameOverText=MyText(text="GAME OVER ",font=pygame.font.Font(None, 100),x=DEVICE_WIDTH/2,y=DEVICE_HEIGHT*0.2,screen=screen)
gameOverText.color=(255,0,0)
startExercizeText=MyText(text="Start Exercise ",font=pygame.font.Font(None, 100),x=DEVICE_WIDTH/2,y=DEVICE_HEIGHT*0.2,screen=screen)
startExercizeText.color=(255,0,0)
pleaseWaitText=MyText(text="Please wait ",font=pygame.font.Font(None, 100),x=DEVICE_WIDTH/2,y=DEVICE_HEIGHT*0.2,screen=screen)
pleaseWaitText.color=(255,0,0)
dontMoveText=MyText(text=" and  don't move",font=pygame.font.Font(None, 100),x=DEVICE_WIDTH/2,y=DEVICE_HEIGHT*0.4,screen=screen)
dontMoveText.color=(255,0,0)
settignCenterText=MyText(text=" Setting Center ........",font=pygame.font.Font(None, 100),x=DEVICE_WIDTH/2,y=DEVICE_HEIGHT*0.6,screen=screen)
settignCenterText.color=(255,0,0)



def reset():
    gameStatus.score = 0
    gameStatus.playerDied=False
    gameStatus.enemies=[EnemyCar(i) for i in get_unique_sample()]
    gameStatus.realScore=0
    gameStatus.gamespeed=5
    gameStatus.diff=0
    screen.fill(color=(0,0,0))
    pleaseWaitText.draw()
    dontMoveText.draw()
    settignCenterText.draw()
    pygame.display.update()  
    PLAYER_CONTROLLER.reset()
    PLAYER_CONTROLLER.setCenter()
def start():
    screen.fill(color=(0,0,0))
    pleaseWaitText.draw()
    dontMoveText.draw()
    settignCenterText.draw()
    pygame.display.update()
    PLAYER_CONTROLLER.reset()
    PLAYER_CONTROLLER.setCenter()
    gameStatus.startFlag=True

def quit():
    PLAYER_CONTROLLER.close()
    pygame.quit()
    sys.exit()
quitButton=Button(screen=screen,pygame=pygame,text='Quit',posX=DEVICE_HEIGHT*0.7,posY=DEVICE_WIDTH*0.3,do_func=quit)
restartButton=Button(screen=screen,pygame=pygame,text='Restart',posX=DEVICE_HEIGHT*0.7,posY=DEVICE_WIDTH*0.6,do_func=reset)
startButton=Button(screen=screen,pygame=pygame,text='Start',posX=DEVICE_HEIGHT*0.7,posY=DEVICE_WIDTH*0.6,do_func=start)
def game_over(score):
    scoreText=MyText(text=f"Score:{str(int(score))} ",font=pygame.font.Font(None, 100),x=DEVICE_WIDTH/2,y=DEVICE_HEIGHT*0.5,screen=screen)
    scoreText.color=(255,0,0)
    screen.fill(color=(0,0,0))
    gameOverText.draw()
    scoreText.draw()
    restartButton.draw()
    quitButton.draw()
    pygame.display.update()
def start_menu():
    screen.fill(color=(0,0,0))
    startExercizeText.draw()
    startButton.draw()
    quitButton.draw()
    pygame.display.update()
def main():

    # Initialize player
    player = Player()



    # Initialize enemies
    gameStatus.enemies = [EnemyCar(i) for i in get_unique_sample()]

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player input
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     player.move_left()
        # if keys[pygame.K_RIGHT]:
        #     player.move_right()
        if not gameStatus.startFlag:
            start_menu()
            continue


        player.updatePlayerPostion()
        if(gameStatus.playerDied):
            game_over(score=gameStatus.score)
            continue
        # Move enemies
        for enemy in gameStatus.enemies:
            enemy.move()

        # Check for collisions
        if check_collision(player, gameStatus.enemies):
            gameStatus.playerDied=True


        # Respawn enemies if necessary
        if (gameStatus.enemies[-1].y>DEVICE_HEIGHT):
            gameStatus.enemies.extend(EnemyCar(i) for i in get_unique_sample())
        if all(enemy.y > DEVICE_HEIGHT for enemy in gameStatus.enemies):
            gameStatus.enemies.pop()
            gameStatus.diff+=1
            if(gameStatus.diff>2 and gameStatus.gamespeed<20):
                gameStatus.gamespeed+=10
                print(gameStatus.gamespeed)
                gameStatus.diff=0
            #enemies = [EnemyCar() for _ in range(random.randint(1, 2))]

        screen.fill(BLACK)
        draw_road()
        move_lines()
        draw_score(gameStatus.score)
        player.draw(screen)
        for enemy in gameStatus.enemies:
            enemy.draw(screen)
        
          # Update score (example increment)
        gameStatus.realScore+=1
        gameStatus.score = int(gameStatus.realScore/10)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()