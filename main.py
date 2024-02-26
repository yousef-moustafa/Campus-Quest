import pygame
from character import Character
from images import *
from pygame.locals import *


def main():
    pygame.init()
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 900
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('CampusQuest')

    character_images = load_character()
    character = Character(
        images=character_images,
        x=SCREEN_WIDTH // 2,
        y=SCREEN_HEIGHT// 2,
        speed=0.2,
    )

    background = load_background()
    background_x = 0
    background_y = 0

    run = True
    while run:
        screen.fill((0,0,0))
        screen.blit(background, (background_x, background_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.move(-character.speed, 0)
            background_x += character.speed
            character.direction = "left"
            character_needs_update = True
        elif keys[pygame.K_RIGHT]:
            character.move(character.speed, 0)
            background_x -= character.speed
            character.direction = "right"
            character_needs_update = True
        elif keys[pygame.K_UP]:
            character.move(0, -character.speed)
            background_y += character.speed
            character.direction = "up"
            character_needs_update = True
        elif keys[pygame.K_DOWN]:
            character.move(0, character.speed)
            background_y -= character.speed
            character.direction = "down"
            character_needs_update = True
        else:
            character_needs_update = False
        if character_needs_update:
            character.update()
        character.draw(screen)
        pygame.display.update()

pygame.quit()

if __name__ == "__main__":
    main()