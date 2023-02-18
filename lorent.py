import pygame
import sys
import random

size = w, h = 1000, 1500

screen = pygame.display.set_mode(size)
x, y, z = 0.10, 0.2, 0.10
rho = 28
sigma = 10
beta = 8 / 3
scale = 20 # scale of attractor 
time = 0.01 # time ttaken to draw 
# print(f"{sigma * (y - x)}  {x * (rho - z) - y } {x * y - beta * z}")
i = 0
while 1:
    color = [random.randint(0 , 255) , random.randint(0 , 255) , random.randint(0 , 255)  ]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
    # equations
    dx = (sigma * (y - x)) * time
    dy = (x * (rho - z) - y) * time
    dz = (x * y - beta * z) * time

    x = x + dx
    y = y + dy
    z = z + dz
    # print(f"x={x} , y={y} , z={z}")
    pygame.draw.circle(
        screen, color, (int(x * scale) + w // 2, int(y * scale) + h // 2), 1
    )
    pygame.display.update()
    i= i+1
    print(i)
