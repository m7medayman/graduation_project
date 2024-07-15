import os
import pygame
import sys
from button import Button
from game_controller import PlayerYController
from text import MyText
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
PLAYER_CONTROLLER=PlayerYController()

class TargetCircle:
    def __init__(self, position, size, activation_time):
        self.position = position  # Center position of the circle (x, y)
        self.size = size  # Diameter of the circle
        self.activation_time = activation_time  # Time in seconds for circle to activate
        self.active = False  # Activation status of the circle
        self.activation_color = (255, 0, 0)  # Red when active
        self.deactivation_color = (150, 150, 150)  # Grey when inactive
        self.color = self.deactivation_color  # Current color of the circle
        self.activation_timer = 0  # Timer for activation countdown

    def activate(self):
        self.active = True
        self.color = self.activation_color
        print(f"Circle at {self.position} activated!")

    def deactivate(self):
        self.active = False
        self.color = self.deactivation_color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.size // 2)
class Status:
    ti=False
    currentActivate = 0
    player_path = []
    # Flag to show/hide the path
    show_path = False
    finish=False
    timer_event= pygame.USEREVENT + 1
    player_position=[0,0]
    startFlag=False
DEVICE_WIDTH, DEVICE_HEIGHT = screen.get_size()
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
quitButton=Button(screen=screen,pygame=pygame,text='Quit',posX=DEVICE_HEIGHT*0.7,posY=DEVICE_WIDTH*0.3,do_func=quit,w=150)
startButton=Button(screen=screen,pygame=pygame,text='Start',posX=DEVICE_HEIGHT*0.7,posY=DEVICE_WIDTH*0.6,do_func=start)
def start():
    screen.fill(color=(0,0,0))
    pleaseWaitText.draw()
    dontMoveText.draw()
    settignCenterText.draw()
    pygame.display.update()
    PLAYER_CONTROLLER.reset()
    PLAYER_CONTROLLER.setCenter()
    Status.startFlag=True
def start_menu():
    screen.fill(color=(0,0,0))
    startExercizeText.draw()
    startButton.draw()
    quitButton.draw()
    pygame.display.update()
def main():
    # Initialize Pygame
    pygame.init()
    Status.timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(Status.timer_event, 7000)  # 7000 milliseconds = 7 seconds

    # Define screen dimensions
    screen_width = 800
    screen_height = 480

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Target Circle Game")

    # Set up the clock for a decent framerate
    clock = pygame.time.Clock()

    # Define player properties
    player_radius = 10
    player_color = (0, 255, 0)  # Green
    Status.player_position = [new_screen_width // 2, screen_height // 2]
    new_screen_width=screen_width-80
    # Initialize target circles
    target_positions = [
        (new_screen_width // 2, screen_height // 2),  # Center
        (new_screen_width // 2, screen_height // 4),  # Top
        (new_screen_width // 2, screen_height * 3 // 4),  # Bottom
        (new_screen_width // 4, screen_height // 2),  # Left
        (new_screen_width * 3 // 4, screen_height // 2)   # Right
    ]
    target_circles = []
    for pos in target_positions:
        target_circles.append(TargetCircle(pos, 50, 7))

    activationSequence = [1, 0, 2, 0, 3, 0, 4]
    Status.currentActivate = 0
    def quit():
        pygame.quit()
        sys.exit()
    Status.playr_path = []
    # Flag to show/hide the path
    Status.show_path = False
    Status.finish=False
    
    def reset():

        Status.ti=False
        Status.currentActivate = 0
        Status.player_path = []
        Status.player_position = [new_screen_width // 2, screen_height // 2]
    # Flag to show/hide the path
        Status.show_path = False
        Status.finish=False
        PLAYER_CONTROLLER.reset()
        Status.timer_event= pygame.USEREVENT + 1
        update()

        
    quitButton=Button(screen=screen,pygame=pygame,text='Quit',posX=50,posY=screen_width-200,do_func=quit,w=100)
    restartButton=Button(screen=screen,pygame=pygame,text='Restart',posX=400,posY=50,do_func=reset,w=150)
    def update():
        Status.currentActivate
        c = activationSequence[Status.currentActivate]
        target_circles[c].activate()
   


    update()

    # List to store player positions

    def DeactivateAll():
        for c in target_circles:
            c.deactivate()
    Status.ti=False
    # Main game loop
    start_ticks = pygame.time.get_ticks()
    WHITE = (255, 255, 255)
    font = pygame.font.Font(None, 74)
    
    
    while True:
        
        dt = clock.tick(30)  # Ensure max framerate is 30 FPS
        if not Status.startFlag:
            start_menu()
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == Status.timer_event:
                Status.ti=True
                print("7 seconds have passed!")
        

        # Handle player move

        Status.player_position[0]=50+PLAYER_CONTROLLER.getMeanFilterX()*400# Toggle path visibility
        Status.player_position[1]=50+PLAYER_CONTROLLER.getMeanFilterX()*200
        # Save player position
        Status.playr_path.append(tuple(Status.player_position))
        
        # Check collision with player and activate target circle
        if(not Status.finish):
              for circle in target_circles:
                    if circle.active:
                        circle_radius = circle.size // 2
                        distance = ((Status.player_position[0] - circle.position[0]) ** 2 +
                        (Status.player_position[1] - circle.position[1]) ** 2) ** 0.5
                        if (distance <= player_radius + circle_radius)or Status.ti:
                    # collision
                            pygame.time.set_timer(Status.timer_event, 7000) 
                            print("Collision")
                            start_ticks = pygame.time.get_ticks()
                            Status.currentActivate += 1
                            circle.deactivate()
                            if (Status.currentActivate >= len(activationSequence)):
                                Status.currentActivate = 0
                                Status.show_path=True
                                Status.finish=True
                            update()
                            Status.ti=False
                            if(Status.finish):
                                DeactivateAll()
        ##up date
        

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw target circles
        for circle in target_circles:
            circle.draw(screen)

        # Draw the player's path if the flag is set
        if Status.show_path:
            for pos in Status.playr_path:
                pygame.draw.circle(screen, (0, 100, 0), pos, 3)

        # Draw the player as a circle
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) / 1000

    # Render the timer
        timer_text = font.render(f"s: {int(elapsed_seconds)}", True, WHITE)
        screen.blit(timer_text, (650, 200))
        pygame.draw.circle(screen, player_color, Status.player_position, player_radius)
        quitButton.draw()
        if(Status.finish):
            restartButton.draw()
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
