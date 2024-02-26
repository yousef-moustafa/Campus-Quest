import pygame
from character import *
from images import *
from pygame.locals import *
import random

def main():
    pygame.init()
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 640
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('CampusQuest')

    background = load_background()
    background_x = 0
    background_y = 0
    clock = pygame.time.Clock()
    character_images = load_character()
    character = Character(
        images=character_images,
        x=SCREEN_WIDTH // 2,
        y=SCREEN_HEIGHT// 2,
        speed=3,
        max_health=100
    )

    food_images = load_food()
    food_items = []
    for food_name, food_image in food_images.items():
        food_item = Item(food_image, random.randint(0, SCREEN_WIDTH - 1), random.randint(0, SCREEN_HEIGHT - 1))
        food_items.append(food_item)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.move(-character.speed, 0)
            character.direction = "left"
            character_needs_update = True
        elif keys[pygame.K_RIGHT]:
            character.move(character.speed, 0)
            character.direction = "right"
            character_needs_update = True
        elif keys[pygame.K_UP]:
            character.move(0, -character.speed)
            character.direction = "up"
            character_needs_update = True
        elif keys[pygame.K_DOWN]:
            character.move(0, character.speed)
            character.direction = "down"
            character_needs_update = True
        else:
            character_needs_update = False
        if character_needs_update:
            clock.tick(30)
            character.update()
        collision_index = character.rect.collidelist([food_item.rect for food_item in food_items])
        if collision_index != -1:
            character.gain_health(0.005)
        screen.fill((0,0,0))
        screen.blit(background, (background_x, background_y))
        character.draw(screen)
        for food_item in food_items:
            food_item.draw(screen)
        pygame.display.update()
pygame.quit()

if __name__ == "__main__":
    main()