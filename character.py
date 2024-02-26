import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, images, x, y, speed):
        super().__init__()
        self.images = images
        self.direction = "down"
        self.index = 0
        self.image = self.images[self.direction][self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
    
    def update(self):
        self.index = (self.index + 1) % len(self.images[self.direction])
        self.image = self.images[self.direction][self.index]

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)