import pygame

pygame.init()

width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooter")

clock = pygame.time.Clock()
game_over = False

background = pygame.transform.scale(pygame.image.load("galaxy.jpg"), (width, height))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, size, speed):
        self.image = pygame.transform.scale(pygame.image.load(image), (size, size))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x =+ self.speed

    def fire(self):
        pass


ship = Player("rocket.png", 400, 500, 80, 10)




while not game_over:
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    ship.update()
    ship.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()