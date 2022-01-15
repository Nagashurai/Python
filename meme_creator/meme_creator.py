import pygame
pygame.init()

# Modify this text to display something on the image
meme_text = f"Something"


# Colors
GREEN = (0, 255, 128)
BLACK = (7, 7, 7)
WHITE = (255, 255, 255)

# Other Requirements
pygame.display.set_caption("Image")
display_image = pygame.image.load(r"images/meme.png")

# Dimensions of the window
WIDTH = display_image.get_width()
HEIGHT = display_image.get_height()
surface = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    surface.fill(BLACK)
    surface.blit(display_image, (0, 0))

    font = pygame.font.SysFont('arial', 30)
    line1 = font.render(meme_text, True, GREEN)

    # Centering the text on the screen regardless of the image size
    line1_width = WIDTH/2 - line1.get_width()/2
    line1_height = HEIGHT/2 - line1.get_height()/2

    # Populating the text on the image
    surface.blit(line1, (line1_width, line1_height))

    # Saving the image
    pygame.image.save(surface, "result.png")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
