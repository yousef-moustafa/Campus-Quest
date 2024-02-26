import pygame

def load_background():
    background = pygame.image.load("img/grass.png")
    return background


def load_character():
    char_right = [
    pygame.transform.scale(pygame.image.load("img/r1.png"), (32, 43)),
    pygame.transform.scale(pygame.image.load("img/r2.png"), (32, 43)),
    pygame.transform.scale(pygame.image.load("img/r3.png"), (32, 43))
    ]

    char_left = [
        pygame.transform.scale(pygame.image.load("img/l1.png"), (32, 43)),
        pygame.transform.scale(pygame.image.load("img/l2.png"), (32, 43)),
        pygame.transform.scale(pygame.image.load("img/l3.png"), (32, 43))
    ]

    char_up = [
        pygame.transform.scale(pygame.image.load("img/u1.png"), (32, 43)),
        pygame.transform.scale(pygame.image.load("img/u2.png"), (32, 43)),
        pygame.transform.scale(pygame.image.load("img/u3.png"), (32, 43))
    ]

    char_down = [
        pygame.transform.scale(pygame.image.load("img/d1.png"), (32, 43)),
        pygame.transform.scale(pygame.image.load("img/d2.png"), (32, 43)),
        pygame.transform.scale(pygame.image.load("img/d3.png"), (32, 43))
    ]
    return {
        "right": char_right,
        "left": char_left,
        "up": char_up,
        "down": char_down
    }

def load_food():
    pizza = pygame.transform.scale2x(pygame.image.load("img/pizza.png"))
    potato = pygame.transform.scale2x(pygame.image.load("img/potato.png"))
    ice_cream = pygame.transform.scale2x(pygame.image.load("img/ice-cream.png"))
    apple = pygame.transform.scale2x(pygame.image.load("img/apple.png"))
    can = pygame.transform.scale2x(pygame.image.load("img/can.png"))
    return {
        "pizza": pizza,
        "potato": potato,
        "ice_cream": ice_cream,
        "apple": apple,
        "can": can
    }