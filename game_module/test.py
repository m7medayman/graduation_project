import os
import pygame
import sys
import random
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

# Lane and road dimensions
MARGIN_WIDTH = DEVICE_WIDTH//5 
ROAD_WIDTH = DEVICE_WIDTH *0.7
LANE_WIDTH = ROAD_WIDTH //3
LINE_HEIGHT = 40
LINE_WIDTH = 10
LINE_SPACING = 20

# Frame rate
clock = pygame.time.Clock()
FPS = 60

# Initialize line positions
line_positions = [0, DEVICE_HEIGHT // 3, 2 * DEVICE_HEIGHT // 3]

# Font setup
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)
score = 0

car_images = {
    "truck": pygame.image.load("truck.bmp"),
    "taxi": pygame.image.load("taxi.bmp"),
    "police": pygame.image.load("Police.bmp"),
    "mini_van": pygame.image.load("Mini_van.bmp"),
    "black_viper": pygame.image.load("Black_viper.bmp"),
    "car": pygame.image.load("Car.bmp")
}

class Player:
    def __init__(self):
        self.width = LANE_WIDTH // 2
        self.height = 100
        self.color = (0, 0, 255)  # Blue color for the player's car
        self.x = MARGIN_WIDTH + LANE_WIDTH // 2 - self.width // 2
        self.y = DEVICE_HEIGHT - self.height - 20
        self.speed = 10

    def move_left(self):
        if self.x > MARGIN_WIDTH:
            self.x -= self.speed

    def move_right(self):
        if self.x < MARGIN_WIDTH + ROAD_WIDTH - self.width:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class EnemyCar:
    def __init__(self,lane):
        self.width = LANE_WIDTH // 1
        self.height = 150
        self.image_name = random.choice(list(car_images.keys()))
        self.image = car_images[self.image_name]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speed = 10
        self.lane = lane
        self.x = MARGIN_WIDTH + self.lane * LANE_WIDTH + (LANE_WIDTH - self.width) // 2
        self.y = -self.height

    def move(self):
        self.y += self.speed



    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x + (self.width - 40) // 2, self.y + 5, 40, self.height - 10)

def draw_road():
    # Draw green margins
    pygame.draw.rect(screen, GREEN, (0, 0, MARGIN_WIDTH, DEVICE_HEIGHT))
    pygame.draw.rect(screen, GREEN, (DEVICE_WIDTH - MARGIN_WIDTH, 0, MARGIN_WIDTH, DEVICE_HEIGHT))
    
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
        line_positions[i] += 10
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

def main():
    global score

    # Initialize player
    player = Player()

    # Initialize enemies
    enemies = [EnemyCar(i) for i in get_unique_sample()]

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()

        # Move enemies
        for enemy in enemies:
            enemy.move()

        # Check for collisions
        if check_collision(player, enemies):
            show_game_over(score)
            retry = False
            while not retry:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        retry = True
                        score = 0
                        main()
                        return

        # Respawn enemies if necessary
        if (enemies[-1].y>DEVICE_HEIGHT):
            enemies.extend(EnemyCar(i) for i in get_unique_sample())
        if all(enemy.y > DEVICE_HEIGHT for enemy in enemies):
            enemies.pop()
            #enemies = [EnemyCar() for _ in range(random.randint(1, 2))]

        screen.fill(BLACK)
        draw_road()
        move_lines()
        draw_score(score)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        
        score += 1  # Update score (example increment)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()