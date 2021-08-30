import pygame
import time
import random
from pygame.locals import *

SIZE = 40
BACKGROUND_COLOR = (50, 16, 168)


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24)*SIZE
        self.y = random.randint(1, 19)*SIZE


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_up(self):
        # Allows movement in all directions with no limitations at length = 1
        if self.length == 1:
            self.direction = 'up'
        # Do not change direction if that would collide with itself
        elif self.direction != 'down' and self.length >= 2:
            self.direction = 'up'
        else:
            pass

    def move_down(self):
        # Allows movement in all directions with no limitations at length = 1
        if self.length == 1:
            self.direction = 'down'
        # Do not change direction if that would collide with itself
        elif self.direction != 'up' and self.length >= 2:
            self.direction = 'down'
        else:
            pass

    def move_left(self):
        # Allows movement in all directions with no limitations at length = 1
        if self.length == 1:
            self.direction = 'left'
        # Do not change direction if that would collide with itself
        elif self.direction != 'right' and self.length >= 2:
            self.direction = 'left'
        else:
            pass

    def move_right(self):
        # Allows movement in all directions with no limitations at length = 1
        if self.length == 1:
            self.direction = 'right'
        # Do not change direction if that would collide with itself
        elif self.direction != 'left' and self.length >= 2:
            self.direction = 'right'
        else:
            pass

    def walk(self):
        # update body
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOR)

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        pygame.mixer.init()
        self.play_background_music()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def play_background_music(self):
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(-1, 0)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Apple Collision
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # Self Collision
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over"

        # Right to left teleport
        for i in range(0, self.snake.length):
            if self.snake.x[i] > 24 * SIZE:
                self.snake.x[i] = 0

        # Left to right teleport
        for i in range(0, self.snake.length):
            if self.snake.x[0] < 0:
                self.snake.x[i] = 25 * SIZE

        # bottom to top teleport
        for i in range(0, self.snake.length):
            if self.snake.y[0] > 19 * SIZE:
                self.snake.y[i] = 0

        # top to bottom teleport
        for i in range(0, self.snake.length):
            if self.snake.y[0] < 0:
                self.snake.y[i] = 20 * SIZE

    def display_score(self):
        with open("high_score.txt", 'r') as f:
            high_score = int(f.read())
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length * 10}", True, (200, 200, 200))
        self.surface.blit(score, (400, 10))
        if (self.snake.length * 10) > high_score:
            game_score = self.snake.length * 10
            high_score_display = font.render(f"Score: {game_score}", True, (200, 200, 200))
            self.surface.blit(high_score_display, (600, 10))
        else:
            game_score = high_score
            high_score_display = font.render(f"Score: {game_score}", True, (200, 200, 200))
            self.surface.blit(high_score_display, (600, 10))
            return high_score

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game Over! Your Score: {self.snake.length * 10}", True, (200, 200, 200))
        self.surface.blit(line1, (300, 300))
        line2 = font.render(f"To play again press Enter.", True, (200, 200, 200))
        self.surface.blit(line2, (300, 350))
        line3 = font.render(f"To exit press Escape.", True, (200, 200, 200))
        self.surface.blit(line3, (300, 400))
        pygame.display.flip()

        snake_game_score = self.snake.length * 10
        with open("high_score.txt", 'w') as f:
            try:
                self.high_score = int(f.read())
            except:
                self.high_score = 0
            if self.high_score >= snake_game_score:
                pass
            else:
                f.write(str(snake_game_score))

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)


if __name__ == '__main__':
    game = Game()
    game.run()
