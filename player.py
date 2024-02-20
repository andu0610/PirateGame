from settings import *


class Player(pygame.sprite.Sprite):

    def __int__(self, pos, groups, collisions_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill("RED")
        self.rect = self.image.get_rect(topleft=pos)
        self.old_rect = self.rect.copy

        self.direction = vector()
        self.speed = 200

        self.collisions_sprites = collisions_sprites
        print(self.collisions_sprites)

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0, 0)

        if keys[pygame.K_RIGHT]:
            input_vector.x += 1
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        self.directionm = input_vector.normalise() if input_vector else input_vector

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision("horizontal")
        self.rect.y += self.directioin.y * self.speed * dt
        self.collision("vertical")

    def collision(self, axis):
        for sprite in self.collisions_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == "horzontal":
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                    if self.rect.right >= sprite.rect.right and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left

                else:
                    pass

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
