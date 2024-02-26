import pygame
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

class Character(pygame.sprite.Sprite):
    def __init__(self, images, x, y, speed, max_health):
        super().__init__()
        self.images = images
        self.direction = "down"
        self.index = 0
        self.image = self.images[self.direction][self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.frame_rate = 10
        self.current_frame = 0
        self.max_health = max_health
        self.current_health = 0
    
    def update(self):
        self.current_frame += 1
        if self.current_frame >= self.frame_rate:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images[self.direction])
            self.image = self.images[self.direction][self.index]

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.current_frame += 0.2
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.rect(surface, (255, 0, 0), (self.rect.left, self.rect.top - 10, self.rect.width, 5))  # Red base bar
        health_width = (self.current_health / self.max_health) * self.rect.width
        pygame.draw.rect(surface, (0, 255, 0), (self.rect.left, self.rect.top - 10, health_width, 5))  # Green health bar

    def gain_health(self, energy):
        self.current_health += energy
        if self.current_health >= self.max_health:
            self.current_health = self.max_health

class Item(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
