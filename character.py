import pygame

class Character():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/12.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image2 = pygame.image.load('images/2.png')
        self.rect2 = self.image2.get_rect()
        self.rect2.centerx = self.screen_rect.centerx
        self.rect2.centery = self.screen_rect.centery

        self.mright2 = False
        self.mleft2 = False
        self.mup2 = False
        self.mdown2 = False

        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False



    def output(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)

    def update_character(self):
            if self.mright == True and self.rect.right<self.screen_rect.right:
                self.rect.centerx += 3
            if self.mleft == True and self.rect.left>self.screen_rect.left:
                self.rect.centerx -= 3
            if self.mup == True and self.rect.top>self.screen_rect.top:
                self.rect.centery -= 3
            if self.mdown == True and self.rect.bottom<self.screen_rect.bottom:
                self.rect.centery += 3

    def update_character2(self):
        if self.mright2 == True and self.rect2.right < self.screen_rect.right:
            self.rect2.centerx += 3
        if self.mleft2 == True and self.rect2.left > self.screen_rect.left:
            self.rect2.centerx -= 3
        if self.mup2 == True and self.rect2.top > self.screen_rect.top:
            self.rect2.centery -= 3
        if self.mdown2 == True and self.rect2.bottom < self.screen_rect.bottom:
            self.rect2.centery += 3



