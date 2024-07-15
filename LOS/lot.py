import pygame
import sys
import random

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

    def update(self, dt):
        if not self.active:
            self.activation_timer += dt / 1000.0  # Convert milliseconds to seconds
            if self.activation_timer >= self.activation_time:
                self.activate()

    def activate(self):
        self.active = True
        self.color = self.activation_color
        print(f"Circle at {self.position} activated!")

    def deactivate(self):
        self.active = False
        self.color = self.deactivation_color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.size // 2)

def main():
    # Initialize Pygame
    pygame.init()

    # Define screen dimensions
    screen_width = 800
    screen_height = 600

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Target Circle Game")

    # Set up the clock for a decent framerate
    clock = pygame.time.Clock()

    # Define player properties
    player_radius = 10
    player_color = (0, 255, 0)  # Green
    player_position = [screen_width // 2, screen_height // 2]

    # Initialize target circles
    target_positions = [
        (screen_width // 2, screen_height // 2),  # Center
        (screen_width // 2, screen_height // 4),  # Top
        (screen_width // 2, screen_height * 3 // 4),  # Bottom
        (screen_width // 4, screen_height // 2),  # Left
        (screen_width * 3 // 4, screen_height // 2)   # Right
    ]
    target_circles = []
    for pos in target_positions:
        target_circles.append(TargetCircle(pos, 50, 7))

    # Main game loop
    while True:
        dt = clock.tick(30)  # Ensure max framerate is 30 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_position[0] -= 5
        if keys[pygame.K_RIGHT]:
            player_position[0] += 5
        if keys[pygame.K_UP]:
            player_position[1] -= 5
        if keys[pygame.K_DOWN]:
            player_position[1] += 5

        # Update target circles
        for circle in target_circles:
            circle.update(dt)
        
        # Check collision with player and activate target circle
        for circle in target_circles:
            if not circle.active:
                circle_radius = circle.size // 2
                distance = ((player_position[0] - circle.position[0]) ** 2 +
                            (player_position[1] - circle.position[1]) ** 2) ** 0.5
                if distance <= player_radius + circle_radius:
                    circle.activate()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw target circles
        for circle in target_circles:
            circle.draw(screen)

        # Draw the player as a circle
        pygame.draw.circle(screen, player_color, player_position, player_radius)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
