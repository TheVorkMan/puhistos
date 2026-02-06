import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 10

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Инициализация Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

# Класс змейки
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.direction = "RIGHT"
        self.body = [self.rect]

    def update(self):
        x, y = self.rect.x, self.rect.y

        if self.direction == "UP":
            y -= 10
        elif self.direction == "DOWN":
            y += 10
        elif self.direction == "LEFT":
            x -= 10
        elif self.direction == "RIGHT":
            x += 10

        self.rect = pygame.Rect(x, y, self.rect.width, self.rect.height)
        self.body.insert(0, self.rect.copy())

        if pygame.sprite.collide_rect(snake, food):
            food.rect.x = random.randrange(WIDTH - food.rect.width)
            food.rect.y = random.randrange(HEIGHT - food.rect.height)
            self.grow()

        if len(self.body) > 1:
            self.body.pop()

    def grow(self):
        new_segment = self.body[-1].copy()
        self.body.append(new_segment)

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, segment)

# Класс еды
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)

    def update(self):
        pass

# Инициализация змейки и еды
all_sprites = pygame.sprite.Group()
snake = Snake()
food = Food()
all_sprites.add(snake, food)

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"

    all_sprites.update()

    if pygame.sprite.collide_rect(snake, food):
        food.rect.x = random.randrange(WIDTH - food.rect.width)
        food.rect.y = random.randrange(HEIGHT - food.rect.height)
        snake.grow()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()