import pygame

def load_background():
    background = pygame.image.load("img/grass.png")
    return background


def load_character():
    char_right = [pygame.image.load("img/r1.png"),
              pygame.image.load("img/r2.png"),
              pygame.image.load("img/r3.png")]
    char_left = [pygame.image.load("img/l1.png"),
                pygame.image.load("img/l2.png"),
                pygame.image.load("img/l3.png")]
    char_up = [pygame.image.load("img/u1.png"),
                pygame.image.load("img/u2.png"),
                pygame.image.load("img/u3.png")]
    char_down = [pygame.image.load("img/d1.png"),
                pygame.image.load("img/d2.png"),
                pygame.image.load("img/d3.png")]
    return {
        "right": char_right,
        "left": char_left,
        "up": char_up,
        "down": char_down
    }