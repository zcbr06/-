import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 1000
BACKGROUND_COLOR = (150, 150, 150)  # Gray background color
CIRCLE_COLOR = (0, 255, 0)  # Green circle color
LINE_COLOR = (255, 0, 0)  # Red line color
FONT_COLOR = (0, 0, 0)  # White font color
FONT_SIZE = 25

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Green Circles with Lines and Numbers")

# Font setup
font = pygame.font.Font(None, FONT_SIZE)

# List to store information about circles (x, y, radius, order)
circles = []

# Function to check for collisions with existing circles
def check_collision(x, y, radius):
    for circle in circles:
        circle_x, circle_y, circle_radius, _ = circle
        distance = ((circle_x - x) ** 2 + (circle_y - y) ** 2) ** 0.5
        if distance < circle_radius + radius:
            return True  # Collision detected
    return False  # No collision

# Main loop
count = 1  # Variable to keep track of the order of circle creation
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add a new circle when the mouse is clicked, only if there is no collision
            x, y = pygame.mouse.get_pos()
            radius = 20  # You can adjust the radius as needed
            if not check_collision(x, y, radius):
                circles.append((x, y, radius, count))
                count += 1

    # Draw the background
    screen.fill(BACKGROUND_COLOR)

    # Draw circles
    for circle in circles:
        x, y, radius, order = circle
        pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), radius)

        # Draw number in the center of the circle
        text = font.render(str(order), True, FONT_COLOR)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    # Draw lines between circles
    for i in range(len(circles) - 1):
        start_x, start_y, _, _ = circles[i]
        end_x, end_y, _, _ = circles[i + 1]
        pygame.draw.line(screen, LINE_COLOR, (start_x, start_y), (end_x, end_y), 2)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
