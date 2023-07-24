import pygame

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))

# Цвета
BLACK = (0, 0, 0)
WHITE = (0, 255, 0)

# Переменные для рисования
drawing = False
last_pos = None

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка событий мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos
                pygame.draw.line(screen, WHITE, last_pos, current_pos, 2)
                last_pos = current_pos

    # Отображение обновленного кадра
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()