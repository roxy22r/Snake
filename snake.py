import pygame
import sys
import numpy as np

squareSize = 25
snake = [[13, 13], [13, 14]]
appleCoordinates = []
direction = 0

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([700, 700])


def draw():
    screen.fill((0, 102, 0))
    for a in appleCoordinates:
        coordinate = [a[0] * squareSize, a[1] + squareSize]
        pygame.draw.rect(screen, (255, 0, 0), (coordinate[0], coordinate[1], squareSize, squareSize), 0)
    head = True
    for x in snake:
        coordinate = [x[0] * squareSize, x[1] * squareSize]
        if head:
            pygame.draw.rect(screen, (0, 0, 0), (coordinate[0], coordinate[1], squareSize, squareSize), 0)
            head = False
        else:
            pygame.draw.rect(screen, (47, 79, 79), (coordinate[0], coordinate[1], squareSize, squareSize), 0)


def appleCoordinantionGen():
    notOK = True
    while notOK:
        coordinate = [np.random.randint(0, 28), np.random.randint(0, 28)]
        change = False
        for x in snake:
            if coordinate == x:
                change = True
        for x in appleCoordinates:
            if coordinate == x:
                change = True
        if not change:
            return coordinate


appleCoordinates.append(appleCoordinantionGen())

go = True
addElement = None
appleind = -1
end = False
score = 0

while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 2:
                direction = 0
            if event.key == pygame.K_RIGHT and direction != 3:
                direction = 1
            if event.key == pygame.K_DOWN and direction != 0:
                direction = 2
            if event.key == pygame.K_LEFT and direction != 1:
                direction = 3

    if addElement is not None:
        snake.append(addElement.copy())
        addElement = None
        appleCoordinates.pop(appleind)
    number = len(snake) - 1
    for i in range(1, len(snake)):
        snake[number] = snake[number - 1].copy()
        number -= 1

    if direction == 0:
        snake[0][1] -= 1
    if direction == 1:
        snake[0][0] += 1
    if direction == 2:
        snake[0][1] += 1
    if direction == 3:
        snake[0][0] -= 1

    for x in range(0, len(appleCoordinates)):
        if appleCoordinates[x] == snake[0]:
            addElement = snake[-1].copy()
            appleind = x
            score += 10

    randomNumber = np.random.randint(0, 100)
    if randomNumber <= 1 and len(appleCoordinates) < 4 or len(appleCoordinates) == 0:
        appleCoordinates.append(appleCoordinantionGen())
    if not end:
        draw()
        pygame.display.update()
    else:
        print("Du hast" + str(score) + "Punkt erreicht")
        sys.exit()
    clock.tick(10)
